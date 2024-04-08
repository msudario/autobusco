import subprocess
list = ['gene="PelA"', 'gene="PelB"', 'gene="PelC"', 'gene="PelD"', 'gene="PelE"', 'gene="PelI"', 'gene="PelL"', 'gene="PelN"', 'gene="PelZ"','gene="PelX"','gene="PelW"','gene="PehV"', 'gene="PehW"', 'gene="PehX"', 'gene="PehK"', 'gene="PehN"','gene="PemA"','gene="PemB"', 'gene="PaeX"', 'gene="PaeY"']

 
for i in list:
   command = ['grep', '-i', f'{i}', 'CCRMP144.gbk','CCRMP250.gbk']
   subprocess.call(command)