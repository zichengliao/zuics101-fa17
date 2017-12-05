import numpy as np
import matplotlib.pyplot as plt
import itertools

n = 10
items   = list( range( n ) )
weights = np.random.uniform( size=(n,) ) * 50
values  = np.random.uniform( size=(n,) ) * 100

def f( wts, vals ):
    total_weight = 0
    total_value = 0

    for i in range( len( wts ) ):
        total_weight += wts[ i ]
        total_value  += vals[ i ]

    if total_weight >= 50:
        return 0
    else:
        return total_value

max_value = 0.0
max_set = None
lists = []
for i in range(n):
    for set in itertools.combinations( items,i ):
        wts  = []
        vals = []
        for item in set:
            wts.append( weights[ item ] )
            vals.append( values[ item ] )
        value = f( wts,vals )
        lists.append( ( wts, value ) )
        if value > 0:
            print( value, wts )
        if value > max_value:
            max_value = value
            max_set = set

array = np.array( lists )
plt.plot( array[:,1], 'b.' )
plt.xlim( ( 0, len(lists) ) )
plt.show()

max_value = 0.0
max_set = None
for i in range(n):
    for set in itertools.combinations( items,i ):
        wts  = []
        vals = []
        for item in set:
            wts.append( weights[ item ] )
            vals.append( values[ item ] )
        value = f( wts,vals )
        if value > max_value:
            max_value = value
            max_set = set
