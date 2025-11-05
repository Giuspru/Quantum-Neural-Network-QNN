import qiskit 
import qiskit_symb
import numpy as np
from sympy import Symbol, I , sin, cos, exp
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter, ParameterVector

values = np.arange(-5.0, 5.5, 0.5)

for i in values:
    x = i 
    part1 = (1.0*I*sin(1)*sin(x/2)*cos(2)**2 + cos(1)*cos(2)**2*cos(x/2))*exp(-1.5*I)
    part2 = (-1.0*I*sin(x/2)*cos(1)*cos(2)**2 + sin(1)*cos(2)**2*cos(x/2))*exp(1.5*I)
    print("\n", x)
    print("\nPrima parte -->  " , part1.evalf() )
    print("\nSeconda parte --> " , part2.evalf())
    print("\n","\n")


