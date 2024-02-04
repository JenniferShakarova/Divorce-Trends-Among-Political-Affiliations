import matplotlib.pyplot as plt
import numpy as np


data_same = {}

with open("years_party.txt") as f:
    content = f.read()
    lines = content.split("\n")
    for line in lines:
        fields = line.split("|")
        if len(fields) == 2:
            years = int(fields[0])
            party = fields[1]
            if party == 'SAME':
                if years in data_same:
                    data_same[years] = data_same[years] + 1
                else:
                    data_same[years] = 1
                    
dict_keys = list(data_same.keys())
dict_keys.sort()
sorted_data = {i: data_same[i] for i in dict_keys}

years = list(sorted_data.keys())
count = list(sorted_data.values())

fig = plt.figure(figsize = (10,5))

#creating the bar plot
plt.bar(years, count, color='maroon')

plt.xlabel("Years Married before Divorce")
plt.ylabel("Number of Couples")
plt.title("Years Married for Couples with Same Party Affiliation")

fig.savefig("graph.pdf")
