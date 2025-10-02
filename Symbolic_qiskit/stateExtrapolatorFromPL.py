import pennylane as qml 
from pennylane import numpy as np
import matplotlib.pyplot as plt
import qiskit 
import qiskit_symb

from qiskit import QuantumCircuit
from qiskit.circuit import Parameter, ParameterVector


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

    return qml.state()

cImp = 1
params = [2,3,4]

a = circuit(cImp, params)
print(a)

