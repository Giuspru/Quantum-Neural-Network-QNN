import qiskit 
import qiskit_symb

from qiskit import QuantumCircuit
from qiskit.circuit import Parameter, ParameterVector

x = Parameter('x')

# Build a quantum circuit
circuit = QuantumCircuit(1)
circuit.rx(x, 0)
circuit.ry(1.47,0)
circuit.rz(-0.21,0)
circuit.rx(1.00,0)
#circuit.measure(range(2), range(2))

print(circuit)

from qiskit_symb.quantum_info import Statevector

psi = Statevector(circuit)
formula = psi.to_sympy()
print("\nThe symbolical form of the circuit:  " , formula)




