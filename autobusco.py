import os
import glob
import subprocess
import shutil

# priro mudar o folder_imput
# esse script tem que ser ativado dentro do conda no ambiente em que o busco foi instalado
# você tem que estar dentro da pasta na qual esta trabalhando dentro do terminal e chamar o script

folder_imput = '/home/mateus/Desktop/Dickeya/7_brig/zeae_all_ncbistrains'

# entrar na pasta e trabalhar com todos elementos ali dentro
for i in glob.glob(os.path.join(folder_imput, '*.fna')):

    #     # rodar um busco para cada elemento ali dentro

    command_line = [
        'busco', '-i', i, '-l', 'enterobacterales_odb10',  '-o', f'{i}'.split(
            "/")[-1].replace('.fna', ''), '-m', 'genome'
    ]

    # executando a commandline
    subprocess.call(command_line)

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
