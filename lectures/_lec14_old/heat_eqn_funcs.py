import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt

def calc_params( nx,nt,alpha,length,tmax ):
    '''
    Compute mesh spacing and time step.
    nx - number of grid points in x
    nt - number of time steps in t
    alpha - thermal diffusivity
    length - of bar, m
    tmax - maximum time value, s
    '''
    dx = length / (nx-1)  # m
    dt = tmax / (nt-1)    # s
    return (dx, dt)

def create_arrays( nx,nt,length,tmax ):
    '''
    Create arrays to save data in process.
    nx - number of grid points in x
    nt - number of time steps in t
    length - of bar, m
    tmax - maximum time value, s
    '''
    x = np.linspace(0, length+1e-15, nx)  # m
    t = np.linspace(0, tmax+1e-15, nt)    # s
    u = np.zeros( [nx,nt] )               # deg C
    return ( x,t,u )

def set_ic( u,x,length ):
    '''
    Set initial and boundary conditions.
    u - heat values in grid of x and t, deg C
    x - grid of x values
    length - of bar, m
    '''
    u[:, 0] = np.sin(np.pi*x/length)**2   # deg C
    #boundaries are implicitly set by this initial condition
    return u

def plot_results( u,x ):
    '''
    Plot the results (initial and final conditions).
    u - heat values in grid of x and t, deg C
    x - grid of x values
    '''
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
    # Set default values for simulation parameters.
    nt = 100      # number of time steps in t
    nx = 20       # number of grid points in x
    alpha = 0.1   # thermal diffusivity
    length = 1.0  # length of bar, m
    tmax = 0.5    # maximum time value, s
    
    # Set up grid and system of equations.
    dx,dt = calc_params( nx,nt,alpha,length,tmax )
    x,t,u = create_arrays( nx,nt,length,tmax )
    u = set_ic( u,x,length )
    A = gen_matrix( nx,alpha,dt,dx )

    # Loop through each time step.
    for n in range( 1,nt ):
        u[ :,n ] = A.dot( u[ :,n-1 ] )

    # Plot results of initial and final temperature.
    plot_results( u,x )

if __name__=='__main__':
    main()
