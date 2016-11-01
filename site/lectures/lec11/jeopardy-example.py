myfile = open('jeopardy.csv')
lines = myfile.readlines()
d = {}
for line in lines:
    cat = line.split(',')[3]
    if cat in d:
        d[cat] += 1
    else:
        d[cat] = 1

# d now contains as keys all categories and as values the number of occurrences of each category
# but dicts don't have order so we have to be a little clever

l = list(d.values())
l.sort()  # now l is a sorted list of category counts
hi_val = l[-1]  # the most frequent category value
for key in d:
    if d[key] == hi_val:
        print(key)
# we have to do this because while it's easy to get a value given a key, it's a bit convoluted to get a key given a value (since the same value can be shared by multiple keys)
# anyway, this is an illustrative example rather than something I'll rigorously test
