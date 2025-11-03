import qiskit 
import qiskit_symb
from sympy import Symbol, I 

from qiskit import QuantumCircuit
from qiskit.circuit import Parameter, ParameterVector

'''
    We want to implent the circuit used in trained pennylane circuit:
    0: ──RX(y)──RY(p[0])──RZ(p[1])──RX([2])─┤  <Z>
'''
x = Parameter('x')
print("\n- This is the classical value encoded into the parameter circuit: ", x)
p1 = Parameter('p1')
p2 = Parameter('p2')
p3 = Parameter('p3')
p4 = Parameter('p4')
p5 = Parameter('p5')
p6 = Parameter('p6')
print("\n- These are the circuit's parameteres (angles): " ,p1,p2,p3)

# Build a quantum circuit
circuit = QuantumCircuit(2)
circuit.h(0)
circuit.h(1)
circuit.rx(x, 0)
circuit.ry(p1,0)
circuit.cx(0,1)
circuit.rz(p2,0)
circuit.rx(p3,0)
circuit.cx(0,1)
circuit.ry(p4,1)
circuit.rz(p5,1)
circuit.cx(1,0)
circuit.rx(p6,1)
#circuit.measure(range(2), range(2))

print("\n-Circuit:\n", circuit)

from qiskit_symb.quantum_info import Statevector

psi = Statevector(circuit)
formula = psi.to_sympy()
print("\n- The symbolical form of the circuit:  " , formula ,"\n")


#Insert some data: 

new_psi = psi.subs({ 
    p1 : 1.47,
    p2 : -0.21,
    p3 : 1.00,
    p4 : 1.23,
    p5 : -0.21,
    p6 : -1.00
})
new_formula = new_psi.to_sympy()
print("\n- The new symbolical form of the circuit:  " , new_formula ,"\n")

print("\n######################################################")
print("\nTYPE: ", type(new_formula))
print("\nElement0:", new_formula[0] )
print("\nLength: ", len(new_formula))
print("\nElement1:", new_formula[1])
print("\n######################################################")

result = []
result.append(new_formula[0].evalf())
result.append(new_formula[1].evalf())


print("\nEvaluation: " , result)







 