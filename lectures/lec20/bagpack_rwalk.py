def f(wts, vals):
    total_weight = 0
    total_value = 0
    
    for i in range(len(wts)):
        total_weight += wts[i]
        total_value += vals[i]

    if total_weight >= 50:
        return 0
    else:
        return total_value


import numpy as np
n = 10
items = list(range(n))
weights = np.random.uniform(size=(n,))*20
values = np.random.uniform(size=(n,))*100

selected = np.zeros(n)
current_wts = weights[np.where(selected==1)]
current_vals = values[np.where(selected==1)]

for t in range(1000):
    selected_bk = selected[:]
    if np.random.randint(2) == 0:  #adding an item
        zero_idxs = np.where(selected==0)[0]
        if len(zero_idxs) > 0:
            selected[np.random.choice(zero_idxs)] = 1
    else: #swapping (take one out, take another in) 
        zero_idxs = np.where(selected==0)[0]
        one_idxs = np.where(selected==1)[0]
        if len(zero_idxs) > 0 and len(one_idxs) > 0:
            selected[np.random.choice(zero_idxs)] = 1
            selected[np.random.choice(one_idxs)] = 0

    trial_wts = weights[np.where(selected==1)]
    trial_vals = values[np.where(selected==1)]
    new_value = f(trial_wts, trial_vals)
    current_value = f(current_wts, current_vals)
    if new_value > current_value:
        current_wts,current_vals =  trial_wts, trial_vals 
        print('up-hilling: %.3f'%new_value)
    else:   #accept with a probability
        if new_value > 0.75*current_value and np.random.uniform() < 0.5:
            current_wts,current_vals =  trial_wts, trial_vals
            print('down-hilling: %.3f'%new_value)
        else:
            selected = selected_bk[:]

print('\nFinal value: %.3f'%current_value)
print(current_wts, current_vals)

