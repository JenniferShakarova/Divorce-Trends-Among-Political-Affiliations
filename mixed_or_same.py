import re

def main():
    fout = open("mixed_or_same.txt", "w")
    with open("number_of_donations.txt") as f:
        donation_records = {}
    
        content = f.read()
        lines = content.split("\n")
        for line in lines:
            fields = line.split("|")
            if len(fields) == 3:
                name = "".join(fields[0].split(","))
                fips = fields[1]
                party = fields[2]
                key = name + "|" + fips
            
                donation_records[key] = party

    with open("couples.txt") as cf:
        spouse_party ={}
        cf_content = cf.read()
        cf_lines = cf_content.split("\n")
        for line in cf_lines:
            fields = line.split("|")
            if len(fields) == 4:
                spouse1 = fields[0]
                spouse2 = fields[1]
                fips = fields[2]
                days = fields[3]
                key1 = spouse1 + "|" + fips
                key2 = spouse2 + "|" + fips
            
                #checks if key is in data
                spouse1party = donation_records[key1] if key1 in donation_records else None 
                spouse2party = donation_records[key2] if key2 in donation_records else None
                #checks is spouse has mixed or same party
                if spouse1party and spouse2party:
                    is_same = "MIXED"

                    if spouse1party == spouse2party:
                        is_same = "SAME"

                    fout.write(days + "|" + is_same + "\n") 
        
            
main()
