from math import sin, cos, pi

def deriv2(x):
    return cos(2*x), -2*sin(2*x), -4*cos(2*x)

f, df, d2f = deriv2(x=pi)
print(' F=%d,dF=%d,D2F=%d'%(f, df, d2f))
