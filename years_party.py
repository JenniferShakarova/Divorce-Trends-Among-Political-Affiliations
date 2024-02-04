import re

def main():
    fout = open("years_party.txt", "w")
    with open("mixed_or_same.txt") as f:
        content = f.read()
        lines = content.split("\n")
        for line in lines:
            fields = line.split("|")
            if len(fields) == 2:
                days = fields[0]
                party = fields[1]

                #changes days to years then rounds
                time = int(days)/365
                years = round(time)
                

                fout.write(str(years) + "|" + party +"\n")

main()
