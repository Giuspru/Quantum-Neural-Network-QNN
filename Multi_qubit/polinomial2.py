import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt


n_qubits = 3
dev = qml.device("default.qubit", wires=n_qubits)


def feature_map(x):
    for i in range(n_qubits):
        qml.RX(x, wires=i)


def variational_layer(weights):
    for i in range(n_qubits):
        qml.RY(weights[i][0], wires=i)
        qml.RZ(weights[i][1], wires=i)
    # entanglement a catena
    for i in range(n_qubits - 1):
        qml.CNOT(wires=[i, i + 1])



@qml.qnode(dev)
def circuit(x, weights):
    feature_map(x)
    variational_layer(weights)
    return qml.expval(qml.PauliZ(0))


def qnn_model(x, weights):
    return circuit(x, weights)


X = np.linspace(-1, 1, 50)
Y = X ** 3  # target da approssimare


#np.random.seed(42)
weights_init = 0.01 * np.random.randn(n_qubits, 2, requires_grad=True)


def cost(weights):
    preds = [qnn_model(x, weights) for x in X]
    return np.mean((preds - Y) ** 2)




opt = qml.GradientDescentOptimizer(stepsize=0.2)
weights = weights_init
epochs = 100

for epoch in range(epochs):
    weights = opt.step(lambda w: cost(w), weights)
    if epoch % 10 == 0:
        loss = cost(weights)
        print(f"Epoch {epoch}: Loss = {loss:.4f}")



# Valutazione del modello
preds = [qnn_model(x, weights) for x in X]

# Plot del risultato
plt.figure(figsize=(10, 6))
plt.plot(X, Y, label="Target f(x) = x^3", color='black')
plt.plot(X, preds, label="QNN output", linestyle='--', color='blue')
plt.title("Quantum Neural Network Functional Learning")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()
