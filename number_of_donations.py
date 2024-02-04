import re
import pyspark

def main(line):   
        fields = line.split("|")
        name = fields[0]
        fips = fields[1]
        party = fields[2]
        return (name + "|" + fips + "|" + party)

def new(x):
        original_key = x[0]
        count = x[1]
        fields = original_key.split("|")
        name = fields[0]
        fips = fields[1]
        party = fields[2]
        return (name + "|" + fips, party, count)
        

sc = pyspark.SparkContext()
lines = sc.textFile('change_zips_to_fips.txt')

a = lines.map(main) 
b = a.filter(lambda x: x.split("|")[2] == "DEM" or  x.split("|")[2] == "REP")
c = b.map(lambda x: (x, 1))
d = c.reduceByKey(lambda x,y: x+y) 
e = d.map(new) 
f = e.collect()


my_dict = {}
for entry in f:
        key = entry[0]
        party = entry[1]
        count = entry[2]
        if key in my_dict:
                my_dict[key][party] = count
        else:
                my_dict[key] = {party: count}

fout = open("number_of_donations.txt", "w")

#checks if REP and DEM key exists in dict 
for key in my_dict:
        
        dem_donations = int(my_dict[key]["DEM"]) if "DEM" in my_dict[key] else 0
        rep_donations = int(my_dict[key]["REP"]) if "REP" in my_dict[key] else 0
        party = ""
        if dem_donations > rep_donations:
                party = 'DEM'
        elif rep_donations > dem_donations:
                party = 'REP'
        else: # they are equal
                party = ""
        name, fips = key.split("|")
        if party:
                fout.write(name + "|" + fips + "|" + party + "\n")
