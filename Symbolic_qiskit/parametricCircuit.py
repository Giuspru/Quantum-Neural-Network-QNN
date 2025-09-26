import qiskit 
import qiskit_symb

from qiskit import QuantumCircuit
from qiskit.circuit import Parameter, ParameterVector

'''
    We want to implent the circuit used in trained pennylane circuit:
    0: ──RX(y)──RY(p[0])──RZ(p[1])──RX([2])─┤  <Z>
'''
y = Parameter('y')
print("\n- This is the classical value encoded into the parameter circuit: ", y)
p = ParameterVector('p', length=3)
print("\n- These are the circuit's parameteres (angles): " , p)

# Build a quantum circuit
circuit = QuantumCircuit(1)
circuit.rx(y, 0)
circuit.ry(p[0],0)
circuit.rz(p[1],0)
circuit.rx(p[2],0)
#circuit.measure(range(2), range(2))

print("\n-Circuit:\n", circuit)

from qiskit_symb.quantum_info import Statevector

psi = Statevector(circuit)
formula = psi.to_sympy()
print("\n- The symbolical form of the circuit:  " , formula ,"\n")


#Insert some data: 

new_psi = psi.subs({
    y : 1 , 
    p : [2,3,4]
})
new_formula = new_psi.to_sympy()
print("\n- The new symbolical form of the circuit:  " , new_formula ,"\n")
 