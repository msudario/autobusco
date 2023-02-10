#!/usr/bin/env python3

import os
import glob
import subprocess
import shutil
import argparse


parser = argparse.ArgumentParser(
    description='running autobusco')
parser.add_argument('-f', '--format', metavar='', type=str, required=True,
                    help='Valid BUSCO format i.e: fasta, fna')
parser.add_argument('-l', '--lineage', metavar='', type=str, required=True,
                    help='Valid BUSCO lineage i.e: enterobacterales_odb10')
parser.add_argument('-i', '--input', metavar='', type=str, required=True,
                    help='input folder with the files')
parser.add_argument('-m', '--mode', metavar='', type=str, required=True,
                    help='BUSCO mode (genome, transcriptome or proteins')

args = parser.parse_args()

folder_input = f'{args.input}'

for i in glob.glob(os.path.join(folder_input, f'*.{args.format}')):
    if args.format == 'fna' or 'faa' or 'fasta':

        command_line = [
            'busco', '-i', i, '-l', f'{args.lineage}',  '-o', f'{i}'.split(
                "/")[-1].replace(f'.{args.format}', ''), '-m', f'{args.mode}', '-c', '5'
        ]

        subprocess.call(command_line)
    else:
        print('Please enter a valid format (faa, fasta, fna)')


######################### SEPARANDO OS RESULTADOS #######################

while True:
    auto_plot = input('Would you like to plot the files? (y/n): ')
    if auto_plot == "y":
        path_to_generatepy = input(
            'Select the path to BUSCO "generate_plot.py":')
        if not os.path.exists(os.path.join(path_to_generatepy, "generate_plot.py")):
            print(
                f'Error: autobusco could not find "generate_plot.py" in {path_to_generatepy}')
        else:
            os.chdir(folder_input)
            if 'results_autobusco' not in os.listdir():
                os.mkdir('results_autobusco')
            for file in os.listdir(folder_input):
                d = os.path.join(folder_input, file)
                if os.path.isdir(d):
                    os.chdir(d)
                txts = [f for f in os.listdir() if '.txt' in f.lower()]
                for files in txts:
                    new_path = folder_input + '/results_autobusco/' + files
                    shutil.move(files, new_path)
            new_path2 = folder_input + '/results_autobusco/'
            command_line = [
                'python', f'{path_to_generatepy}/generate_plot.py', '-wd', f'{new_path2}'
            ]
            subprocess.call(command_line)
            print('Thank You!')
            break
    elif auto_plot == 'n':
        print('Thank you!')
        break
    else:
        print("Would you like to plot busco results? Please type 'y' for yes or 'n' for no")
