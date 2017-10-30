# open a csv file traditionally (open + readlines)
plankton = open( 'plankton.csv' )
plankdata = plankton.readlines()

planksizes = {}
plankfreqs = {}
for line in plankdata[2:]: # look out for the header lines!
    data = line.strip().split(',')		# split by ','
    planksizes[ data[0] ] = float(data[1])
    plankfreqs[ data[0] ] = max(float(line[2]), float(line[3]), float(line[4]), float(line[5]))

# now find the key (species name) with the largest value in planksizes and plankfreqs 

# open the file using DictReader
from csv import DictReader
reader = DictReader( open( 'plankton.csv' ) )
for row in reader:
    print( row['Species'], row['Size'] )

