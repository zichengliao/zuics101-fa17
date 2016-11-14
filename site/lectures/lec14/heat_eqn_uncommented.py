import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt

def calc_params( nx,nt,alpha,length,tmax ):
    dx = length / (nx-1)
    dt = tmax / (nt-1)
    return (dx, dt)

def create_arrays( nx,nt,length,tmax ):
    x = np.linspace(0, length+1e-15, nx)
    t = np.linspace(0, tmax+1e-15, nt)
    u = np.zeros( [nx,nt] )
    return ( x,t,u )

def set_ic( u,x,length ):
    u[:, 0] = np.sin(np.pi*x/length)**2
    return u

def plot_results( u,x ):
    mpl.rcParams['figure.figsize']=[15,3]
    plt.plot(x, u[:,0], 'k-', lw=2)
    plt.plot(x, u[:,-1],  'b-', lw=2)
    
    plt.ylim((0,1))
    plt.xlim((0,1))
    plt.show()

def gen_matrix( nx,alpha,dt,dx ):
    r  = alpha * dt / (dx*dx)
    s  = 1 - 2*r
    A = np.zeros( ( nx,nx ), dtype=np.float128 )
    i,j = np.indices( A.shape )
    A[ i==j   ] = s
    A[ i==j-1 ] = r
    A[ i==j+1 ] = r
    A[ 0,0 ]    = 1
    A[ 0,1 ]    = 0
    A[ 1,0 ]    = 0
    A[ nx-1,nx-1 ] = 1
    A[ nx-1,nx-2 ] = 0
    A[ nx-2,nx-1 ] = 0
    return A

def main():
    nt = 100
    nx = 20
    alpha = 0.1
    length = 1.0
    tmax = 0.5
    
    dx,dt = calc_params( nx,nt,alpha,length,tmax )
    x,t,u = create_arrays( nx,nt,length,tmax )
    u = set_ic( u,x,length )
    A = gen_matrix( nx,alpha,dt,dx )

    for n in range( 1,nt ):
        u[ :,n ] = A.dot( u[ :,n-1 ] )

    plot_results( u,x )

if __name__=='__main__':
    main()
