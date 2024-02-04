import re

def main():
  # process zipcounty
  fips_to_zip_map = {}

  # write output to fips_to_zip.txt
  fout = open("fips_to_zip.txt", "w")
  
  with open('zipcounty.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    for line in lines:
      result = re.split(r'\t+', line)
      zip = result[0]
      fips = result[1]
      county_name = result[2]
      state = result[3]
      #makes sure to get info from TX
      if state == 'TX':
        fips_to_zip_map[fips] = zip
        fout.write(fips + "|" + zip+"\n")

main()
