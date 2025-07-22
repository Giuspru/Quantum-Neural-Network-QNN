import numpy as np
import matplotlib.pyplot as plt
import pennylane as qml 
import math

import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt



#Setting the divice where implementing the circut
dev = qml.device("default.qubit", wires=1)


#Node
@qml.qnode(dev)

#implementation of a QNN circuit, very basic it's a test.
def circuit(x, weights):
    # Encode input --> encoding classical information in quantum circuit as input. 
    qml.RX(x, wires=0)
    
    # Parametrized rotation
    qml.RY(weights[0], wires=0)
    qml.RZ(weights[1], wires=0)
    qml.RX(weights[2], wires=0)
    
    return qml.expval(qml.PauliZ(0))  #Expval on z axis is between -1 and 1

# Cost function, easy mean squared error between predictions done by the quantum circuit and the target values.
def cost(weights, X, Y):
    preds = np.array([circuit(x, weights) for x in X])
    # print("\nPreds:")
    # print(preds)
    # print("\nY:")
    # print(Y)
    # print("\nCost:")
    return np.mean((preds - Y) ** 2)

# Dati di training
X_train = np.linspace(0, 2 * np.pi, 20)
Y_train = np.sin(X_train)  #Target function
print("\nX:")
print(X_train)
print("\nY:")
print(Y_train)



#Initial weights
weights = np.random.normal(0, 1, 3, requires_grad=True)
print("\nWeights:")
print(weights)

print(qml.draw(circuit)(X_train[0], weights))





#Ottimization:


opt = qml.GradientDescentOptimizer(stepsize=0.1)
epochs = 5

print("\nInizio ottimizzazione:\n")
for i in range(epochs):
    print("weights:\n")
    print(weights)
    weights = opt.step(lambda w: cost(w, X_train, Y_train), weights)
    if i % 2 == 0:
        print(f"Epoch {i} - Cost: {cost(weights, X_train, Y_train):.4f}")

# Validation
X_test = np.linspace(0, 2*np.pi, 100) #--> metterli random compresi tra [0,1]
Y_pred = np.array([circuit(x, weights) for x in X_test])

plt.plot(X_test, np.sin(X_test), label="Target sin(x)")
plt.plot(X_test, Y_pred, label="Quantum Approximation")
plt.legend()
plt.title("Quantum circuit fitting sin(x)")
plt.show()

#plotting error curve:
print("\nXtest:\n")
print(X_test)
print("\nYpred:\n")
print(Y_pred)

print(type(X_test[0]))
print(type(Y_pred[0]))
    
print(X_test[0] - Y_pred[0])
print(abs(X_test[0] - Y_pred[0]))

err = []
for i in range(len(X_test)):
    err.append(float(abs(X_test[i] - Y_pred[i])))
    
    


