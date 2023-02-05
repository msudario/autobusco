# autobusco is a python script to run BUSCO to all files in a folder (I've not tried running with Gene models in GTF or GFF3 format but probrably it would work)
### INSTRUCTIONS####

# 1) join the folder where your files are via terminal (busco must be installed)
# 2) run the script with the arguments:
-f [for the format file that BUSCO accepts, i.e: fasta, fna...] -l [for the BUSCO lineage, i.e: enterobacterales_odb10] -m [for BUSCO mode, i.e: genome] -i [the directory of the files]
# 3) type 'y' if you want to autoplot or 'n' to exit.
