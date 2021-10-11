import math

def trapezoid(a,b,n,f):
    '''
    Parameters
    ----------
    a : int 
        the lower limit of the integral
        
    b : int
        the upper limit of the integral
        
    n : int
        number of subdivisions
        
    f: function

    Returns
    -------
    The approximate integral of f from a to b with n subdivisions.

    '''
    internal=0
    h=(b-a)/n
    for i in range(1,n):
        internal += f(a+i*h)
    return (h/2 *(f(a)+2*internal+f(b)))
   
    #test
    f= lambda x: math.exp(-x**3)
    
    trapezoid(0,1,2,f)
