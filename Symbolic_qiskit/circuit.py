import qiskit 
import qiskit_symb

from qiskit import QuantumCircuit
from qiskit.circuit import Parameter, ParameterVector

'''
    We want to implent the circuit used in trained pennylane circuit:
    0: ──RX(0.00)──RY(1.47)──RZ(-0.21)──RX(1.00)─┤  <Z>
'''
y = Parameter('y')
print(y)
p = ParameterVector('p', length=3)
print(p)

# Build a quantum circuit
circuit = QuantumCircuit(1)
circuit.rx(0, 0)
circuit.ry(1.47,0)
circuit.rz(-0.21,0)
circuit.rx(1.00,0)
#circuit.measure(range(2), range(2))

print(circuit)

from qiskit_symb.quantum_info import Statevector

psi = Statevector(circuit)
formula = psi.to_sympy()
print("\nThe symbolical form of the circuit:  " , formula)




