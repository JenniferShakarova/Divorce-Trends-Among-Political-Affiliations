all: graph.pdf graph2.pdf
	echo "everything has been built"

#run make 
clean:
	rm committee_party.txt texasRecords.txt fips_to_zip.txt change_zips_to_fips.txt number_of_donations.txt couples.txt mixed_or_same.txt years_party.txt

#step A
committee_party.txt: candidate20.gz stepA.py
	python3 stepA.py > committee_party.txt

#stepB
texasRecords.txt: committee_party.txt indiv20.gz stepB.py
	python3 stepB.py > texasRecords.txt

#converting
fips_to_zip.txt: zipcounty.txt step1.py 
	python3 step1.py > fips_to_zip.txt

#stepC
change_zips_to_fips.txt: fips_to_zip.txt texasRecords.txt stepC.py
	python3 stepC.py > change_zips_to_fips.txt

#stepD
number_of_donations.txt: change_zips_to_fips.txt stepD.py
	python3 stepD.py > number_of_donations.txt

#stepE
couples.txt: AllDivorces.gz stepE.py
	python3 stepE.py > couples.txt

#stepF
mixed_or_same.txt: couples.txt number_of_donations.txt stepF.py
	python3 stepF.py > mixed_or_same.txt

#stepG
years_party.txt: mixed_or_same.txt stepG.py
	python3 stepG.py > years_party.txt

graph.pdf: years_party.txt graph.py
	python3 graph.py

graph2.pdf: years_party.txt graph2.py
	python3 graph2.py
