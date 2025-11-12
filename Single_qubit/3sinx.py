import numpy as np
import matplotlib.pyplot as plt
import pennylane as qml 
import math

import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt
from qiskit.quantum_info import Statevector
from qiskit.quantum_info import Pauli

#Setting the divice where implementing the circut
dev = qml.device("default.qubit", wires=1)


#Node
@qml.qnode(dev)


#implementation of a QNN circuit, very basic it's a test.
def circuit(x, weights):
    print("xxxxxxxxx")
    print(x)
    print(weights)
    print("xxxxxxxxx")
    # Encode input --> encoding classical information in quantum circuit as input. 
    qml.RX(x, wires=0)
    
    # Parametrized rotation
    qml.RY(weights[0], wires=0)
    qml.RZ(weights[1], wires=0)
    qml.RX(weights[2], wires=0)
    
    return qml.expval(qml.PauliZ(0))  #Expval on z axis is between -1 and 1

#implementation of a QNN circuit, very basic it's a test.
def circuit_fpga(x, weights):
    # chiamata a fpga con x e weights

    state_list = [] # output che mi ritorna fpga

    # Create a Statevector object
    state_vector = Statevector(state_list)

    # The Statevector will automatically normalize it
    print(state_vector)

    pauli_z_0 = Pauli('ZI')  # Z on qubit 0, I on qubit 1
    expval = state_vector.expectation_value(pauli_z_0).real

    print("Expectation value of Z on qubit 0:", expval)
    print("State vector:", state_vector)
    
    return expval

def target_function(x):
    return 3*np.sin(x) # <-- riscala a [-1,1]

def scale_output(output):
    # Scaling [-1, 1] → [-3,3]
    return output * 3


# Cost function, easy mean squared error between predictions done by the quantum circuit and the target values.
def cost(weights, X, Y):

    for x in X:
        test = (circuit(x, weights))
        print("==========")
        print(type(test))
        print(test)
        print("==========")
        input()


    preds = np.array([scale_output(circuit(x, weights)) for x in X])
    # print("\nPreds:")
    # print(preds)
    # print("\nY:")
    # print(Y)
    # print("\nCost:")
    return np.sqrt(np.mean((preds - Y) ** 2))

def cost_fpga(weights, X, Y):
    # Step 1: Create an empty list to store the intermediate results
    results = []

    # Step 2: Loop through each element x in X
    for x in X:
        # Step 3: Compute the raw output of the circuit for this x
        circuit_output = circuit_fpga(x, weights)
        
        # Step 4: Apply the scaling function to that output
        scaled_output = scale_output(circuit_output)
        
        # Step 5: Append the result to the list
        results.append(scaled_output)

    # Step 6: Convert the list into a NumPy array
    preds = np.array(results)

    return np.sqrt(np.mean((preds - Y) ** 2))



# Dati di training
X_train = np.linspace(0, 2 * np.pi, 100)
Y_train = target_function(X_train)
solo_seno = np.sin(X_train)  #Target function
print("\nX:")
print(solo_seno)
print("\nX train:")
print(X_train)
print("\nY:")
print(Y_train)


#Initial weights
weights = np.random.normal(0, 1, 3, requires_grad=True)
print("\nWeights:")
print(weights)


print(qml.draw(circuit)(X_train[0], weights))


#Ottimization:
opt = qml.GradientDescentOptimizer(stepsize=0.01)
epochs = 20


print("\nInizio ottimizzazione:\n")
for i in range(epochs):
    #print("weights:\n")
    #print(weights)
    weights = opt.step(lambda w: cost(w, X_train, Y_train), weights)
    # if i % 50 == 0:
    #     #print(f"Epoch {i} - Cost: {cost(weights, X_train, Y_train):.4f}")
    #     print(weights)
    # elif i % 199 == 0:
    #     #print(f"Epoch {i} - Cost: {cost(weights, X_train, Y_train):.4f}")
    #     print(weights)


# Validation
X_test = np.linspace(0, 2*np.pi, 100) #--> metterli random compresi tra [0,1]
Y_pred = np.array([scale_output(circuit(x, weights)) for x in X_test])


plt.plot(X_test, target_function(X_test), label="Target 3sin(x)")
plt.plot(X_test, Y_pred, label="Quantum Approximation")
plt.legend()
plt.title("Quantum circuit fitting sin(x)")
plt.show()