def Simpson3rd(a,b,n,f):
    '''
    Parameters
    ----------
    a : int 
        the lower limit of the integral
        
    b : int
        the upper limit of the integral
        
    n : int
        number of subdivisions
        
    f: lambda function

    Returns
    -------
    The approximate integral of f from a to b with n subdivisions.

    '''
    internal1=0
    internal2=0
    
    h=(b-a)/n
    for i in range(1,n//2+1):
        internal1 += f(a+(2*i-1)*h)
        
    for i in range(1,n//2):
        internal2 += f(a+(2*i)*h)
        
    In = h/3 *(f(a) + 4*internal1 + 2*internal2 + f(b))
    return(In)
  
  
  '''
  Test
  
 Checking integration rule of $\int_0^1 xf(x)dx$ for $f(x)=x^2+2x$
  '''
f= lambda x: x*(x**2+(2*x))
print(Simpson3rd(0,1,2,f))
