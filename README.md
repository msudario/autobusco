# Welcome to autobusco
Autobusco is a script that automatically runs Busco and also plots it.

options:
  -h, --help       show this help message and exit<p>
  -l , --lineage   Valid BUSCO lineage i.e: enterobacterales_odb10<p>
  -i , --input     input folder with the files<p>
  -m , --mode      BUSCO mode (genome, transcriptome or proteins<p>
  -c , --cpu       CPU thread usage (OPTIONAL)<p>

Exemple of running it: <code>python ~/Desktop/scripts/autobusco.py -l enterobacterales_odb10 -i ~/Desktop/myfiles -m genome</code>
#
* Must have R installed to plot 
