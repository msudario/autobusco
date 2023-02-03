import os
import glob
import subprocess
import shutil
import argparse


parser = argparse.ArgumentParser(
    description='running autobusco')
parser.add_argument('-f', '--format', metavar='', type=str, required=True,
                    help='a valid BUSCO format i.e: fasta, fna')
parser.add_argument('-l', '--lineage', metavar='', type=str, required=True,
                    help='a valid BUSCO lineage i.e: hypocreales_odb10')
parser.add_argument('-i', '--imput', metavar='', type=str, required=True,
                    help='an imput folder')
parser.add_argument('-m', '--mode', metavar='', type=str, required=True,
                    help='BUSCO mode (genome, transcriptome or proteins')

args = parser.parse_args()

folder_imput = f'{args.imput}'

# entrar na pasta e trabalhar com todos elementos ali dentro
for i in glob.glob(os.path.join(folder_imput, f'*.{args.format}')):
    if args.format == 'fna' or 'faa' or 'fasta':

        command_line = [
            'busco', '-i', i, '-l', f'{args.lineage}',  '-o', f'{i}'.split(
                "/")[-1].replace(f'.{args.format}', ''), '-m', f'{args.mode}', '-c', '5'
        ]

    # executando a commandline
        subprocess.call(command_line)
    else:
        print('Please enter a valid format (faa, fasta, fna)')
######################### SEPARANDO OS RESULTADOS #######################

x = True
while x == True:
    # perguntando ao usuario se deseja autoplotar
    auto_plot = input('Would you like to plot the files?: (y/n)? \n')
    if auto_plot == "y":

        # acessando o imput
        os.chdir(folder_imput)
        # criando uma pasta para armazenar os resultados
        if 'results_autobusco' not in os.listdir():
            os.mkdir('results_autobusco')
        # separando apenas as pastas dentro do imput
        for file in os.listdir(folder_imput):
            d = os.path.join(folder_imput, file)
            if os.path.isdir(d):
                os.chdir(d)
                # movendo os apenas os .txt dentro da pasta para a pasta results_autobusco
                txts = [f for f in os.listdir() if '.txt' in f.lower()]
                for files in txts:
                    new_path = folder_imput + '/results_autobusco/' + files
                    shutil.move(files, new_path)

        ##### rodando o comando do busco para plotagem #####
        new_path2 = folder_imput + '/results_autobusco/'
        command_line = [
            'python', '/home/mateus/anaconda3/pkgs/busco-5.4.2-pyhdfd78af_0/python-scripts/generate_plot.py', '-wd', f'{new_path2}'
        ]

        # executando a commandline
        subprocess.call(command_line)
        print('Thank You!')
        break

    elif auto_plot == 'n':
        print('Thank you!')
        break

    else:
        print("Would you like to plot busco results? Please type 'y' for yes or 'n' for no")
