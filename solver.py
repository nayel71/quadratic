print("*******************************")
print("   Solving X^2 - P*X + Q = 0   ")
print("*******************************")
P = input("Enter the value of P: ")
Q = input("Enter the value of Q: ")

from fractions import Fraction

# convert to fractions
P = Fraction(P)
Q = Fraction(Q)

midpoint = Fraction(P, 2)
distance = f"sqrt({midpoint * midpoint - Q})"
R1 = f"{midpoint} - {distance}"
R2 = f"{midpoint} + {distance}"

print(f"Roots: {R1}, {R2}")
