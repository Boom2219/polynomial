from polynomial import poly

PolyA = poly([1, 0, 16])
## x^2 + 16

PolyB = poly([1, -4])
## x - 4

quotient = PolyA / PolyB # x + 4
remainder = PolyA % PolyB # 32

print "%s divided by %s equals\n%s with remainder %s" % (PolyA, PolyB, quotient, remainder)