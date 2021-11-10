import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output



def Tfunc(n_row,n_col):
    T=np.zeros([n_row,n_col])
    for x_i in range(n_row):
        for y_j in range(n_col):

            if y_j==0:
                T[x_i,y_j] = T[x_i,y_j+1]

            elif y_j==n_col-1:
                T[x_i,y_j] = T[x_i,y_j-1]

            if x_i==0:
                T[x_i,y_j]=0

            if x_i==n_row-1:
                T[x_i,y_j]=1
    return (T)

def Tmap(T,iters,Errors):
    fig1 = plt.figure(1)
    ax1 = fig1.add_subplot(121)
    ax2 = fig1.add_subplot(122)
    
    clear_output(wait=True)
    
    ax1.clear()
    heatmap = ax1.pcolor(T, cmap=plt.cm.gist_heat)
    plt.colorbar(heatmap,ax=ax1)
    ax1.set_xlabel('$Y_{j}$')
    ax1.set_ylabel('$X_{i}$')
    ax1.set_title("Temperature profile")
    
    ticks=[round(i/mesh,2) for i in ax1.get_xticks()]
    
    ax1.set_xticklabels(ticks)
    ax1.set_yticklabels(ticks)

   
    ax2.clear()
    ax2.plot(iters,Errors)
    ax2.set_xlabel('Iteration')
    ax2.set_ylabel('Error')
    ax2.set_title("Convergence History")
    
    plt.show()
    

def FiniteDiff(Temp,mesh,method,w):
    
    n_col = mesh
    n_row = mesh
    
    dy=(1/n_col)
    dx=(1/n_row)

    a=(dx**2)
    b=(dy**2)
    
    
    T=Temp.copy()
    
    if method == 'Jacobi':
        Tbuffer=T.copy()
 
    else:
        Tbuffer=T
           
        
    Tnew=T.copy()
        
    for x_i in range(1,n_row-1):

        for y_j in range(1,n_col-1):

            Tbuffer[x_i,y_j]=((100*a*b-b*(T[x_i+1,y_j]+T[x_i-1,y_j])-a*(T[x_i,y_j+1]+T[x_i,y_j-1]))/(-2*(a+b)))
            if method =='SOR':
                Tbuffer[x_i,y_j]=Tnew[x_i,y_j]+w*(Tbuffer[x_i,y_j]-Tnew[x_i,y_j])
            else:
                continue
    
    T=Tnew.copy()
    Tnew=Tbuffer.copy()
    


    for x_i in range(n_row):
        for y_j in range(n_col):

            if y_j==0:
                Tnew[x_i,y_j] = Tnew[x_i,y_j+1]

            elif y_j==n_col-1:
                Tnew[x_i,y_j] = Tnew[x_i,y_j-1]

            if x_i==0:
                Tnew[x_i,y_j]=0

            if x_i==n_row-1:
                Tnew[x_i,y_j]=1

    
    A=abs(Tnew-T)
    
    maxError=np.amax(A)
    
    return (Tnew,A,maxError)
  

  
def Temp_Profile(mesh,method,w=1):
    
    n_col = mesh
    n_row = mesh

    dy=(1/n_col)
    dx=(1/n_row)

    a=(dx**2)
    b=(dy**2)

    tolerance=0.001

    iterations=[]
    Errors=[]
    
    iteration=1
    

    y=[j*dy for j in range(n_col)]
    x=[i*dx for i in range(n_row)]

    Temp=Tfunc(n_row,n_col)
    
    Tmap(Temp,iterations,Errors)

    
    T_Jacobi,A,Error=FiniteDiff(Temp,mesh,method,w)
    
    Errors.append(Error)
    iterations.append(iteration)
    
    Tmap(T_Jacobi,iterations,Errors)

    print('Initial Error = ', Error,'\n\n')
    
    while Error>tolerance:
    
        T_Jacobi,A,Error=FiniteDiff(T_Jacobi,mesh,method,w)
        
        iteration+=1
        
        Errors.append(Error)
        iterations.append(iteration)
        
        Tmap(T_Jacobi,iterations,Errors)
        
        
        print('iter = ',iteration,'\tError = ',Error)
        

        
#testing
'''

Meshes=[9,17,33]
Methods=['Jacobi','Gauss','SOR']

for mesh in Meshes:
    for method in Methods:
        print('**********mesh = ',mesh,'\tmethod = ',method,'**********\n\n')
        if method=='SOR':
            for w in [0.5,1.5,2]:
                print('***W = ',w,' ***')
                Temp_Profile(mesh,method,w)
        else:
            Temp_Profile(mesh,method)

'''
