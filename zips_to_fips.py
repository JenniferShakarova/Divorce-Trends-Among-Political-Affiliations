import re

def main():
    fout = open("change_zips_to_fips.txt", "w")
    with open("fips_to_zip.txt") as fzf:
        zips_fips_dict = {}
        fz_content = fzf.read()
        lines = fz_content.split("\n")
        for line in lines:
            if len(line) >= 2:  #checks if not empty
                fields = line.split("|")
                zips = fields[1]
                fips = fields[0]

                zips_fips_dict[zips] = fips
            
    
    with open('texasRecords.txt') as f:
        content = f.read()
        lines = content.split('\n')
        for line in lines:
            if len(line) >= 3:
                fields = line.split("|")
                name = fields[0]
                zips = fields[1]
                party = fields[2]
                #checks if zips exists as key
                if zips:
                    fips = zips_fips_dict[zips] if zips in zips_fips_dict else None
                    if fips:
                        fout.write(name + "|" + fips + "|" + party + "\n")
                        
        

            

main()
