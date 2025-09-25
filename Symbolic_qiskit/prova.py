from qiskit import QuantumCircuit
from qiskit.circuit import Parameter, ParameterVector

y = Parameter('y')
p = ParameterVector('p', length=2)

pqc = QuantumCircuit(2)
pqc.ry(y, 0)
pqc.cx(0, 1)
pqc.u(p[0], 0, p[1], 1)

print(pqc)

from qiskit_symb.quantum_info import Statevector

psi = Statevector(pqc)
a = psi.to_sympy()
print(a)
