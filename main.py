from sympy import *
from sympy.abc import x
from re import sub

inp = input("equation: ")
# inp = "f''(x) - 2f'(x) + 3f(x) + cos(2x) + 8x^4"
inp = inp.replace("^", "**")

f = Function('f')
if "f" in inp:
	inp = sub("f('+)\(x\)", lambda m: "diff(f(x), x, %s)" %len(m[1]), inp)
	inp = sub("([0-9])([a-zA-Z])", r"\1*\2", inp)
	print(inp)
	eq = eval(inp)
	sol = dsolve(eq, f(x))
else:
	eq = eval(inp)
	sol = solve(eq)
print(sol)

# f''(x) - 2f'(x) + 3f(x) + cos(2x) + 8x^4
