import matplotlib.pyplot as plt
import numpy as np

data_mixed = {}
with open("years_party.txt") as f:
    content = f.read()
    lines = content.split("\n")
    for line in lines:
        fields = line.split("|")
        if len(fields) == 2:
            years = int(fields[0])
            party = fields[1]
            if party == 'MIXED':
                if years in data_mixed:
                    data_mixed[years] = data_mixed[years] + 1
                else:
                    data_mixed[years] = 1

mixed_dict_keys = list(data_mixed.keys())
mixed_dict_keys.sort()
mixed_sorted_data = {i: data_mixed[i] for i in mixed_dict_keys}
mixed_years =list(mixed_sorted_data.keys())
mixed_count = list(mixed_sorted_data.values())


fig = plt.figure(figsize = (10,5))

#creating the bar plot
plt.bar(mixed_years, mixed_count, color= 'blue')

plt.xlabel("Years Married before Divorce")
plt.ylabel("Number of Couples")
plt.title("Years Married for Couples with Mixed Party Affiliation")


fig.savefig("graph2.pdf")

