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

# try a configuration at random
best_set = [ np.random.choice( len( wts ) ) ]
trial_set = best_set[ : ]

# alter it at random with small likelihood of getting worse
for t in range( 1000 ):
    next_set = trial_set[ : ]
    # two possible moves:  adding or removing
    trial = np.random.uniform()
    if trial < 0.5:
        # avoid infinite loop
        if len( trial_set ) >= len( wts ):
            continue
        # add a value
        trial_index = np.random.choice( len( wts ) )
        while trial_index in trial_set:
            trial_index = np.random.choice( len( wts ) )
        next_set.append( trial_index )
    else:
        # avoid infinite loop
        if len( trial_set ) < 1:
            continue
        # remove a value
        trial_index = np.random.choice( len( wts ) )
        while trial_index not in trial_set:
            trial_index = np.random.choice( len( wts ) )
        del next_set[ trial_set.index( trial_index ) ]

    # convert list of indices to wts/vals
    trial_wts =  [ ]
    trial_vals = [ ]
    next_wts =   [ ]
    next_vals =  [ ]
    best_wts =   [ ]
    best_vals =  [ ]
    for index in trial_set:
        trial_wts.append(  wts[ index ] )
        trial_vals.append( vals[ index ] )
    for index in next_set:
        next_wts.append(  wts[ index ] )
        next_vals.append( vals[ index ] )
    print( sum( next_vals ),next_set )
    for index in best_set:
        best_wts.append(  wts[ index ] )
        best_vals.append( vals[ index ] )
    print( sum( best_vals ),best_set )

    if f( next_wts,next_vals ) > f( trial_wts,trial_vals ):
        # if improvement, accept the change
        trial_set = next_set[ : ]
        print( 'accepted better case' )
    else:
        # if no improvement, *maybe* accept the change
        if np.random.uniform() < 0.20:
            trial_set = next_set[ : ]
            print( 'accepted worse case' )

    # if all-time best, track it
    #print( f( next_wts,next_vals ), f( best_wts,best_vals ) )
    if f( next_wts,next_vals ) > f( best_wts,best_vals ):
        best_set = next_set[ : ]
        print( 'new best found' )

print( 'best case is ', str( best_set ) )
print( 'with value %f' % sum( best_vals ) )
