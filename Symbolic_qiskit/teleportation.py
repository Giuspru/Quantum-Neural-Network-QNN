import qiskit 
import qiskit_symb
from numpy import pi

from qiskit import QuantumCircuit
from qiskit.circuit import Parameter, ParameterVector
from qiskit_symb.quantum_info import Statevector

'''
    We want to implent the circuit used in trained pennylane circuit:
    0: ──RX(y)──RY(p[0])──RZ(p[1])──RX([2])─┤  <Z>
'''
r1 = Parameter('r1')
r2 = Parameter('r2')


# Build a quantum circuit
circuit = QuantumCircuit(3)
circuit.h(1)
circuit.cx(1,2)
#circuit.barrier(0,1,2)

circuit.cx(0,1)
circuit.h(0)
#circuit.barrier(0,1,2)

circuit.crx(pi, 1, 2 )
circuit.crz(pi , 0, 2)


print("\n-Circuit:\n", circuit)
psi = Statevector(circuit)
formula = psi.to_sympy()
print(formula)


 

