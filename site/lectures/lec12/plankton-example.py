# open the file traditionally (open + split)
plankton = open( 'plankton.csv' )
plankdata = plankton.readlines()
datasizes = {}
for line in plankdata:
    data = line.strip().split(',')
    datasizes[ data[0] ] = float(data[1])
# fails because of header lines!
datasizes = {}
for line in plankdata[2:]:
    data = line.strip().split(',')
    datasizes[ data[0] ] = float(data[1])

# open the file using DictReader
from csv import DictReader
reader = DictReader( open( 'plankton.csv' ) )
for row in reader:
    print( row['Species'], row['Size'] )

