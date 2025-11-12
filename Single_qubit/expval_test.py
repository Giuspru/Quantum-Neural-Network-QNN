import numpy as np
import matplotlib.pyplot as plt
import pennylane as qml 
import math

import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt

import qiskit 
import qiskit_symb
from sympy import Symbol, I 

from qiskit import QuantumCircuit
from qiskit.circuit import Parameter, ParameterVector


dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def circuit():
    #qml.RZ(x, wires=0)
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])
    pauli = qml.PauliZ(0)
    return [qml.expval(pauli), qml.state()]

print(circuit()[0])

print('################')


print(circuit()[1])


