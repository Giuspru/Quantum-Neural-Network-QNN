import pennylane as qml 
from pennylane import numpy as np 
import matplotlib.pyplot as plt 
import random


n_qubits = 2 
dev = dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev)


#implemntation of a circuit with 2 qubits
def circuit(x , weights):

    #Encoding input --> encoding classical information in quantum circuit
    qml.RX(x, wires=0)

    #Parametrized rotation first layer
    qml.RY(weights[0], wires=0)
    qml.RZ(weights[1], wires=0)
    qml.RX(weights[2], wires=0)
    
    #Entangling 
    qml.CNOT(wires=[0,1])


    #Parametrized secind layer:
    qml.RY(weights[3], wires=1)
    qml.RZ(weights[4], wires=1)
    qml.RX(weights[5], wires=1)

    return qml.expval(qml.PauliZ(1))

def target_function(x):
    return x**2

def scale_output(outuput):
    return((outuput+1))

def cost(weights, X, Y_true):
    Y_pred = np.array([scale_output(circuit(x,weights)) for x in X])
    return np.mean((Y_pred - Y_true)**2)


#Initial weights
weights = np.random.normal(0, 2*np.pi, 6, requires_grad=True)
#weights = np.array([-4.96308144, -0.03660885, 1.58028067, -5.06214749, 1.57076047, -8.20368752], requires_grad=True)
print("\nWeights:")
print(weights)

print("\n")
print(qml.draw(circuit)(0.5, weights), "\n")

X_train = np.linspace(0,1,50)
#np.random.shuffle(X_train)
print("X_train:\n", X_train)

Y_train = target_function(X_train)
print("\nY_train:" , Y_train)


# ran = abs(np.random.normal(0, 0.5, 10))
# print("\nrandom:", ran)


opt = qml.AdamOptimizer(0.2)
epochs = 50

for i in range(epochs):
    weights = opt.step(lambda w: cost(w, X_train, Y_train), weights)
    if i % 10 == 0:
        loss = cost(weights, X_train, Y_train)
        print(f"Epoch {i} - Loss: {loss:.4f}")
        print(f"Weights: {weights}")


# Testing
X_test = np.linspace(0, 1, 50)
Y_pred = np.array([scale_output(circuit(x, weights)) for x in X_test])
Y_true = target_function(X_test)


plt.plot(X_test, Y_true, label="Target:  3x", linewidth=2)
plt.plot(X_test, Y_pred, label="Quantum Approximation", linestyle="--")
plt.title("Quantum circuit fitting 3x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()


