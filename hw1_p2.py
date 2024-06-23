Force = int(input(" Input the force : "))
Mass1 = int(input(" Input the mass of m1 : "))
Distance = int(input(" Input the distance : "))

G = 6.67*10**-11
C = 299792458

Mass2 = (Force*Distance**2) / (G * Mass1)
Energy = Mass2*C**2

print("The mass of m2 =", Mass2)
print("The energy of m2 =", Energy)