import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt

#1 qubit circuit:
dev = qml.device("default.qubit", wires=1)


@qml.qnode(dev)
def circuit(x, weights):
    # Input Encoding --> bring classical information into the quantum circuit
    qml.RX(x, wires=0)
    
    # Parametrized layer
    qml.RY(weights[0], wires=0)
    qml.RZ(weights[1], wires=0)
    qml.RX(weights[2], wires=0)
    qml.RY(weights[3], wires=0)
    qml.RZ(weights[4], wires=0)
    qml.RX(weights[5], wires=0)
    qml.RY(weights[6], wires=0)
    qml.RZ(weights[7], wires=0)
    qml.RX(weights[8], wires=0)
    qml.RY(weights[9], wires=0)
    qml.RZ(weights[10], wires=0)
    qml.RX(weights[11], wires=0)
    
    return qml.expval(qml.PauliZ(0))  # output ∈ [-1, 1]

#Target function:
def target_function(x):
    return 3 * x + 2 * x**2  # <-- riscala a [-1,1]

# Output is mapped in [-1,1] → f(x) ∈ [0, 5] eve if x ∈ [0, 1]

def scale_output(output):
    # Scaling [-1, 1] → [0, 5]
    return (output + 1) * 2.5

# Rescaling for comparision: 
def inverse_scale_output(y):
    return (y / 2.5) - 1

# Funzione di costo (errore quadratico medio tra target e predizione scalata)
def cost(weights, X, Y_true):
    Y_pred = np.array([scale_output(circuit(x, weights)) for x in X])
    #return np.sqrt(np.mean((Y_pred - Y_true) ** 2))
    return np.mean((Y_pred - Y_true) ** 2)

#Data:
X_train = np.linspace(0, 1, 600)
Y_train = target_function(X_train)

#Initial weights:
weights = np.random.normal(0, 1, 12, requires_grad=True)

# Ottimizzatore
#opt = qml.GradientDescentOptimizer(stepsize=0.01)
opt = qml.AdamOptimizer(0.1)
epochs = 100

for i in range(epochs):
    weights = opt.step(lambda w: cost(w, X_train, Y_train), weights)
    if i % 10 == 0:
        loss = cost(weights, X_train, Y_train)
        print(f"Epoch {i} - Loss: {loss:.4f}")
        print(f"Weights: {weights}")

# Testing
X_test = np.linspace(0, 1, 100)
Y_pred = np.array([scale_output(circuit(x, weights)) for x in X_test])
Y_true = target_function(X_test)

# Plot
plt.plot(X_test, Y_true, label="Target: 3x + 2x^2", linewidth=2)
plt.plot(X_test, Y_pred, label="Quantum Approximation", linestyle="--")
plt.title("Quantum circuit fitting 3x + 2x²")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
