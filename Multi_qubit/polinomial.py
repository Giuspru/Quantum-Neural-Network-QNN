import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt

n_qubits = 3
dev = qml.device("default.qubit", wires=n_qubits)


@qml.qnode(dev)
def circuit(x, weights):
    
    for i in range(n_qubits):
        qml.RX(x, wires=i)

    # Parametrized layer
    for i in range(n_qubits):
        qml.RY(weights[i, 0], wires=i)
        qml.RZ(weights[i, 1], wires=i)
    
    # Entanglement (catena lineare + chiusura)
    for i in range(n_qubits - 1):
        qml.CNOT(wires=[i, i + 1])
    qml.CNOT(wires=[n_qubits - 1, 0])  
    
    # Measurement
    # return sum([qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]) / n_qubits
    # q1 = qml.expval(qml.PauliZ(0))
    # q2 = qml.expval(qml.PauliZ(1))
    # q3 = qml.expval(qml.PauliZ(2))
    # return q1, q2, q3

    return qml.expval(qml.PauliZ(0))

# Funzione target
def target_function(x):
    return 3 * x + 2 * x**2

# Scaling output: da [-1, +1] → [0, 5]
def scale_output(output):
    return (output + 1) * 2.5

def inverse_scale_output(y):
    return (y / 2.5) - 1

# Cost function (MSE tra prediction e target)
def cost(weights, X, Y_true):
    Y_pred = np.array([scale_output(circuit(x, weights)) for x in X])
    return np.mean((Y_pred - Y_true) ** 2)

# Dataset
X_train = np.linspace(0, 1, 30)
Y_train = target_function(X_train)



# Inizializzazione pesi (per ogni qubit: 2 angoli RY, RZ)
weights = np.random.normal(0, 1, size=(n_qubits, 2), requires_grad=True)

# Print circuit
print(qml.draw(circuit)(0.5, weights))

# Ottimizzatore
opt = qml.GradientDescentOptimizer(stepsize=0.2)
epochs = 100

for i in range(epochs):
    weights = opt.step(lambda w: cost(w, X_train, Y_train), weights)
    if i % 10 == 0:
        print(f"Epoch {i} - Loss: {cost(weights, X_train, Y_train):.4f}")

# Testing
X_test = np.linspace(0, 1, 100)
Y_pred = np.array([scale_output(circuit(x, weights)) for x in X_test])
Y_true = target_function(X_test)

# Plot
plt.plot(X_test, Y_true, label="Target: 3x + 2x²", linewidth=2)
plt.plot(X_test, Y_pred, label="Quantum Approximation (3 qubits)", linestyle="--")
plt.title("VQC a 3 qubit per approssimare 3x + 2x²")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
