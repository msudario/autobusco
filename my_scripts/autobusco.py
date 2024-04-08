#!/usr/bin/env python3
# coding: utf-8

import os
import subprocess
import shutil
import argparse

parser = argparse.ArgumentParser(
    description='Welcome to autoBUSCO')

parser.add_argument('-l', '--lineage', metavar='', type=str, required=True,
                    help='Valid BUSCO lineage i.e: enterobacterales_odb10')
parser.add_argument('-i', '--input', metavar='', type=str, required=True,
                    help='input folder with the files')
parser.add_argument('-m', '--mode', metavar='', type=str, required=True,
                    help='BUSCO mode (genome, transcriptome or proteins')
parser.add_argument('-c', '--cpu', metavar='', type=str, required=False,
                    help='CPU thread usage (OPTIONAL)')

args = parser.parse_args()

folder_input = os.path.expanduser(f'{args.input}')
extensoes = ['.fasta', '.fna', '.fa']


def run_busco(folder_input):
    os.chdir(folder_input)
    if 'results_autobusco' not in os.listdir(folder_input):
                    os.mkdir('results_autobusco')
                   
    if args.cpu:
        os.chdir(os.path.join(folder_input, 'results_autobusco'))
        for arquivos in os.listdir(folder_input):
            for extensao in extensoes:
                if arquivos.endswith(extensao): 
                    with open(os.path.join(folder_input, arquivos), "r") as file:
                        output = arquivos.replace('.fna', '').replace('.fasta', '').replace('.fa', '')
                        command_line = ['busco', '-i', os.path.join(folder_input, f'{arquivos}'), '-l', f'{args.lineage}',  '-o', f'{output}' , '-m', f'{args.mode}', '-c', f'{args.cpu}']

                        subprocess.call(command_line)

    else:
        os.chdir(os.path.join(folder_input, 'results_autobusco'))
        for arquivos in os.listdir(folder_input):
            for extensao in extensoes:
                if arquivos.endswith(extensao): 
                    with open(os.path.join(folder_input, arquivos), "r") as file: 
                        output = arquivos.replace('.fna', '').replace('.fasta', '').replace('.fa', '')
                        command_line = ['busco', '-i', os.path.join(folder_input, f'{arquivos}'), '-l', f'{args.lineage}',  '-o', f'{output}', '-m', f'{args.mode}']

                        subprocess.call(command_line)
                        

                        
            
            

def plot_results(folder_input):
    while True:
        auto_plot = input('Would you like to plot the files? (y/n): ')
        if auto_plot == "y":
            caminho_autobusco = os.path.join(folder_input, 'results_autobusco')
            path_to_generatepy = os.path.join(caminho_autobusco,'busco_downloads', 'generate_plot.py')

            if not os.path.exists(path_to_generatepy):
                os.chdir(os.path.join(caminho_autobusco, 'busco_downloads'))
                os.system('wget "https://gitlab.com/ezlab/busco/-/raw/master/scripts/generate_plot.py?inline=false" -O generate_plot.py')
                
                for file in os.listdir(caminho_autobusco):
                    d = os.path.join(caminho_autobusco, file)
                    if os.path.isdir(d):
                        os.chdir(d)
                    txts = [f for f in os.listdir() if '.txt' in f.lower()]
                    for files in txts:
                        new_path = os.path.join(caminho_autobusco, files)
                        shutil.copy(files, new_path)
                
                command_line = [
                    'python3', f'{path_to_generatepy}', '-wd', f'{caminho_autobusco}'
                    ]
                subprocess.call(command_line)
                break

            elif os.path.exists(path_to_generatepy):
                for file in os.listdir(caminho_autobusco):
                    d = os.path.join(caminho_autobusco, file)
                    if os.path.isdir(d):
                        os.chdir(d)
                    txts = [f for f in os.listdir() if '.txt' in f.lower()]
                    for files in txts:
                        new_path = os.path.join(caminho_autobusco, files)
                        shutil.copy(files, new_path)
                
                command_line = [
                    'python3', f'{path_to_generatepy}', '-wd', f'{caminho_autobusco}'
                    ]
                subprocess.call(command_line)
                break

            else:
                print(f'Error: autobusco could not find "generate_plot.py" in {folder_input}')

        elif auto_plot == 'n':
            print('Thank you!')
            break
        else:
            print("Would you like to plot busco results? Please type 'y' for yes or 'n' for no")

def process_files(folder_input):
    run_busco(folder_input)
    plot_results(folder_input)

if __name__ == '__main__':
    process_files(folder_input)
#testing