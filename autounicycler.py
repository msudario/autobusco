import os
import argparse
import subprocess


parser = argparse.ArgumentParser(
    description='running autounicycler')

parser.add_argument('-i', '--input', metavar='', type=str, required=True,
                    help='Path to the files i.e: home/usr/Desktop/myfiles')
parser.add_argument('-t', '--thread', metavar='', type=str, required=False,
                    help='[OPTIONAL] Number of threads i.e: 8')

args = parser.parse_args()

diretorio = os.path.expanduser(f'{args.input}') 
extensoes = ['.fastq', '.fq']

def validate_input_directory(diretorio):
    if not os.path.isdir(diretorio):
        raise ValueError("Invalid input directory")

def function(diretorio):
    lista = []
    if 'results_autounicycler' not in os.listdir(diretorio):
        os.mkdir(os.path.join(f'{diretorio}','results_autounicycler'))
    
    for arquivos in os.listdir(args.input):
        for extensao in extensoes:
            if arquivos.endswith(extensao):   
                lista.append(arquivos)
                lista.sort()
                break

    for cada_item_da_lista in range(0, len(lista), 2):
        lista2 = lista[cada_item_da_lista:cada_item_da_lista+2]   
        
        nome_do_diretorio = os.path.splitext(lista2[0])[0]
         
        os.mkdir(os.path.join(f'{diretorio}', 'results_autounicycler', f'{nome_do_diretorio}'))
        caminho = os.path.join(f'{diretorio}', 'results_autounicycler', f'{nome_do_diretorio}')
        
        if args.thread:
            command_line = ['unicycler', '-1', os.path.join(f'{diretorio}', f'{lista2[0]}'), '-2', os.path.join(f'{diretorio}', f'{lista2[1]}'), '-o', f'{caminho}', '-t', args.thread, '--min_fasta_length',	'200']
            subprocess.call(command_line)
            
        else:
            command_line = ['unicycler', '-1', os.path.join(f'{diretorio}', f'{lista2[0]}'), '-2', os.path.join(f'{diretorio}', f'{lista2[1]}'), '-o', f'{caminho}', '--min_fasta_length',	'200']
            subprocess.call(command_line)
            
if __name__ == '__main__':
    validate_input_directory(diretorio)
    function(diretorio)