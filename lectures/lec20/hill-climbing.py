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

max_wt = 50.0

wts_orig  = wts[ : ]
vals_orig = vals[ : ]

best_vals = [ ]
best_wts  = [ ]
best_vals.append( max( vals ) )
best_wts.append( wts[ vals.index( max( vals ) ) ] )
wts.remove( wts[ vals.index( max( vals ) ) ] )
vals.remove( max( vals ) )

while sum( best_wts ) + wts[ vals.index( max( vals ) ) ] \
        < max_wt:
    best_vals.append( max( vals ) )
    best_wts.append( wts[ vals.index( max( vals ) ) ] )
    wts.remove( wts[ vals.index( max( vals ) ) ] )
    vals.remove( max( vals ) )

wts  = wts_orig[ : ]
vals = vals_orig[ : ]
