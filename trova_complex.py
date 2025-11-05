from sympy import *

x = Symbol('x', real=True)
y = Symbol('y', real=False)

f_1 = exp(x)
f_2 = exp(y)
f_3 = exp(4*I)
esponente_1 = f_1.exp
esponente_2 = f_2.exp
esponente_3 = f_3.exp


print("Esponente: " , esponente_1,\
      "\nReale --> ", esponente_1.is_real, \
      "\nComplesso --> ", esponente_1.is_complex, \
      "\nImmaginario --> ", esponente_1.is_imaginary )

print("\nEsponente: " , esponente_2,\
      "\nReale --> ", esponente_2.is_real, \
      "\nComplesso --> ", esponente_2.is_complex, \
      "\nImmaginario --> ", esponente_2.is_imaginary )


print("\nEsponente: " , esponente_3,\
      "\nReale --> ", esponente_3.is_real, \
      "\nComplesso --> ", esponente_3.is_complex, \
      "\nImmaginario --> ", esponente_3.is_imaginary, \
      "\nNatural --> ", esponente_3.is_natural )

