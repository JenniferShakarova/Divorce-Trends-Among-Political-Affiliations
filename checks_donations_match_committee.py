import gzip

def main():
    with open("committee_party.txt") as cpf:
        committee_party_dict = {}
        cpf_content = cpf.read()
        cpf_lines = cpf_content.split('\n')
        for line in cpf_lines:
            fields = line.split("|")
            if len(fields) >= 2:
                committee = fields[0]
                party = fields[1]

                committee_party_dict[committee] = party

            

    #checks if candidate committee matches individuals who donated to that committee
    fout = open("texasRecords.txt", "w")
    with gzip.open('indiv20.gz', 'rt') as f:
        content = f.read()
        lines = content.split('\n')
        for line in lines:
            if len(line) > 15:
                fields = line.split("|")
                committee = fields[0]
                zips = fields[10][:5]
                state = fields[9]
                name = fields[7]
                donation = int(fields[14])
                #checks if committee exists as key
                party = committee_party_dict[committee] if committee in committee_party_dict else None
                if state == "TX" and donation > 0 and party:
                    fout.write(name + "|" + zips + "|" + party + '\n')

main()
