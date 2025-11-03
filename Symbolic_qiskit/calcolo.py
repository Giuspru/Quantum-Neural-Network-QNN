import qiskit 
import qiskit_symb
import numpy as np
from sympy import Symbol, I , sin, cos, exp
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter, ParameterVector

values = np.arange(-5.0, 5.5, 0.5)

for i in values:
    x = i 
    part1 = 0.479425538604203*I*(1.22311487210696*(-0.706208954520116*I*sin(x/2) + 0.706208954520116*cos(x/2))*exp(-0.105*I) - 0.668190699997*I*(-0.0356217988822122*I*sin(x/2) + 0.0356217988822122*cos(x/2))*exp(0.105*I))*exp(-0.105*I) + 0.877582561890373*(-0.114973399399077*I*(-0.706208954520116*I*sin(x/2) + 0.706208954520116*cos(x/2))*exp(-0.105*I) + 0.210457395923552*(-0.0356217988822122*I*sin(x/2) + 0.0356217988822122*cos(x/2))*exp(0.105*I))*exp(0.105*I)
    part2 = 0.877582561890373*(0.210457395923552*(-0.706208954520116*I*sin(x/2) + 0.706208954520116*cos(x/2))*exp(-0.105*I) - 0.114973399399077*I*(-0.0356217988822122*I*sin(x/2) + 0.0356217988822122*cos(x/2))*exp(0.105*I))*exp(0.105*I) + 0.479425538604203*I*(-0.668190699997*I*(-0.706208954520116*I*sin(x/2) + 0.706208954520116*cos(x/2))*exp(-0.105*I) + 1.22311487210696*(-0.0356217988822122*I*sin(x/2) + 0.0356217988822122*cos(x/2))*exp(0.105*I))*exp(-0.105*I)
    print("\n", x)
    print("\nPrima parte -->  " , part1.evalf() )
    print("\nSeconda parte --> " , part2.evalf())
    print("\n","\n")


