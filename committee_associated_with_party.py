import gzip

def main():
    #checks which committee is associated with a specific party
    fout = open("committee_party.txt", "w", newline = "\n")
    with gzip.open("candidate20.gz", "rt") as f:
        content = f.read()
        lines = content.split('\n')
        for line in lines:
            fields = line.split("|")
            if len(fields) > 9:   #checks if its not empty
                committee = fields[9]
                party = fields[2]
                if committee and party:
                    print(committee + "|" + party)
                    fout.write(committee + "|" + party + "\n")
        
main()
