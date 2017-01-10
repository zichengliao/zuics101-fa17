import requests
import os

def grab_website_data():
    '''Get raw data as HTML string from the NOAA website.'''
    
    page_file = ".stations.txt"
    if not os.path.isfile(page_file):
        url = 'http://www.nws.noaa.gov/mdl/gfslamp/docs/stations_info.shtml'
        
        ## YOUR CODE HERE
        
        f = open(page_file,'w')
        f.write(page.text)
        f.close()
        return page.text
    else:
        f = open(page_file,'r')
        data = f.read()
        f.close()
        return data

def extract_section(text):
    '''Find Illinois data segment (in a PRE tag).
    We know (from examination) that inside of the PRE block containing ' IL '
    (with whitespace and case matching) we can find the IL station data.
    This solution isn't robust, but it's good enough for practical cases.'''
    
    il_start  = text.find(' IL ')
    tag_start = text.rfind('PRE', il_start-200, il_start) # look backwards
    tag_end   = text.find('PRE', il_start)
    data = text[tag_start+4:tag_end-2]
    lines = data.splitlines()
    lines = lines[2:-1]
    return lines

def parse_station_line(line):
    '''Extract latitude and longitude of stations. We know the columns are fixed
    (which is both inconvenient and convenient). In this case, we will simply
    set the limits of the relevant columns by counting the number of columns
    over we need to go.'''
    
    # YOUR CODE HERE
    
    return stn, lon, lat
    


text = grab_website_data()
lines = extract_section(text)
for line in lines:
    try:
        stn, lon, lat = parse_station_line(line)
        print('%s\t%f\t%f'%(stn,lon,lat))
    except:
        print('Could not parse line\n\t%s'%line)
