def line_equation(a, b, x):
    y = a * x + b
    return y

def equations(a, b, x):
    y1 = a * x + b
    y2 = a * x
    return y1, y2

def conversion_C_F(temp_c):
    '''Function to convert temperatures in C (integer or float) to F'''
    temp_f = temp_c * 9/5 + 32
    return temp_f

def circle(r):
    """Function to compute the perimeter and area of a circle given the radius (r)"""
    import numpy as np
    print('perimeter:', 2*np.pi*r)
    print('area:', np.pi*r**2)

def rectangle(l, h):
    """Function to compute the perimeter, area, and diagonal of a rectangle given two sides (l, h)"""
    import numpy as np
    print('perimeter:', 2*(l+h))
    print('area:', l*h)
    print('diagonal:', np.sqrt(l**2 + h**2))

def cylinder(r, h):
    """Function to compute the area and volume of a cylinder given the radius end the height (r, h)"""
    import numpy as np
    print('area:', 2*np.pi*r*h + 2*np.pi*r**2)
    print('volume:', np.pi*r**2*h)