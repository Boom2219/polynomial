from polynomial import poly

## Initialisation of polynomials

PolyA = poly([1, 0], 1)
print "## Set exponent of 1"
print "Polynomial object with coefficients of %s and exponent of %d is equal to" % (PolyA.coefs, PolyA.exponent) 
print "(%s)(%s) which is also equal to" % (poly(PolyA.coefs), poly([1], PolyA.exponent)) 
print PolyA
print

PolyA.clean()
print "## Clean polynomial"
print "Polynomial object with coefficients of %s and exponent of %d is equal to" % (PolyA.coefs, PolyA.exponent) 
print "(%s)(%s) which is also equal to" % (poly(PolyA.coefs), poly([1], PolyA.exponent)) 
print PolyA
print

PolyB = poly([1, -3])
print "## Create polynomial with default exponent"
print "Polynomial object with coefficients of %s and exponent of %d is equal to" % (PolyB.coefs, PolyB.exponent) 
print "(%s)(%s) which is also equal to" % (poly(PolyB.coefs), poly([1], PolyB.exponent)) 
print PolyB
print

## Operations performed on polynomials

PolyC = (PolyA + PolyB).clean()
print "## Sum of 2 polynomials"
print "Polynomial object with coefficients of %s and exponent of %d is equal to" % (PolyC.coefs, PolyC.exponent) 
print "(%s)(%s) which is also equal to" % (poly(PolyC.coefs), poly([1], PolyC.exponent)) 
print PolyC
print

PolyC = PolyA * PolyB
PolyC.clean()
print "## Product of 2 polynomials"
print "Polynomial object with coefficients of %s and exponent of %d is equal to" % (PolyC.coefs, PolyC.exponent) 
print "(%s)(%s) which is also equal to" % (poly(PolyC.coefs), poly([1], PolyC.exponent)) 
print PolyC