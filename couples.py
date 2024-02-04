import re
import gzip
from datetime import datetime


def main():
    couples = []
    fout = open("couples.txt", "w")
    with gzip.open('AllDivorces.gz', 'rt') as f:
        content = f.read()
        lines = content.split('\n')
        for line in lines:
            #checked for invalid data
            pattern = r'(?:VOID)'
            match = re.search(pattern, line)
            if not match:
                fields = line.split('|')
                #makes sure fields is not empty by using len
                marriage_date = fields[6] if len(fields) >=7 else None
                divorce_date = fields[7] if len(fields) >=7 else None
              
                if marriage_date and divorce_date:
                    year = marriage_date.split("/")[-1]

                    #looking for newer data 2000+ and breaking up date
                    if year.isnumeric(): #and int(year) >= 2000:
                        month, day, year = marriage_date.split('/')
                     
                        #calculating date time 
                        try:
                            start = datetime(year = int(year), month = int(month), day = int(day))
                        except:
                            start = None
                        month, day, year = divorce_date.split("/")
                        try:
                            end = datetime(year = int(year), month = int(month), day = int(day))
                        except:
                            end = None
                        if start and end:
                            delta = (end - start).days
                        else:
                            continue
                       
                        texas_county_code = fields[8] if len(fields) >= 9 else None
                        if texas_county_code and texas_county_code.isnumeric():
                            #converting 
                            fips = int(texas_county_code) * 2 - 1 + 48000

                            # check if spouse2 has a last name
                            spouse2 = fields[3].split(' ')
                            last_name = fields[1].split(' ')[0]
                            if len(spouse2) == 1:
                                spouse2 = last_name + " " + spouse2[0]
                            elif len(spouse2) == 2:
                                second_name = spouse2[1]
                                if len(second_name) == 1: # this is a middle initial
                                    spouse2 = last_name + " " + " ".join(spouse2)
                                
                                else:
                                    spouse2 = fields[3]
                            else:
                                spouse2 = fields[3]
                        
                            fout.write(fields[1] + "|" + spouse2 + "|" + str(fips) + "|" + str(delta) + "\n")


main()
