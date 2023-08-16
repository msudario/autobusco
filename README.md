# Welcome to autobusco 
autobusco is a python script to run BUSCO to all files in a folder and autoplot them.
Simple run in your terminal: <code>python path/to/script.py</code>     with the options and go grab a coffe <p>
  
options:<p>
  -h, --help       show this help message and exit<p>
  -l , --lineage   Valid BUSCO lineage i.e: enterobacterales_odb10<p>
  -i , --input     path to the fasta files i.e: <code>home/usr/Desktop/folder_with_your_files or ~/Desktop/folder_with_your_files</code><p>
  -m , --mode      BUSCO mode (genome, transcriptome or proteins)<p>
  -c , --cpu       CPU thread usage (OPTIONAL)<p>
 
 
Exemple of running it: <code>python ~/Desktop/scripts/autobusco/autobusco.py -l enterobacterales_odb10 -i ~/Desktop/myfiles -m genome </code>

After running Busco analyses, you will be asked whether you want to plot the results as a single graph to check for missing genes. Type 'y' if you want to autoplot the results or 'n' to exit.
    
#
* Must run it in terminal/enviroment with busco installed.
* If you want to autoplot them, you must have an internet connection to download the script from BUSCO.
* You must have R installed to plot with BUSCO's script.

