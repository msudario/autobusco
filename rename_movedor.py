import os
import shutil

# folder_input = os.path.join('/home/mateus/Desktop/undicola/results_autoprokka')

# def files_rename(folder_input):
#     os.chdir(folder_input)
#     for i in os.listdir():
#         strain = i.split('_')[1]
#         especie = i.split('_')[0]
#         primeiras_3_letras = especie[0] + especie[1] + especie[2]
#         os.chdir(os.path.join(folder_input, i))
#         for j in os.listdir():
#             caminho_antigo = os.path.join(folder_input,i,  j)
#             nome_novo = f'{primeiras_3_letras}_{strain}'
#             caminho, ext = os.path.splitext(caminho_antigo)
#             caminho_novo = os.path.join(folder_input,i, nome_novo) + f'{ext}'
#             os.rename(caminho_antigo, caminho_novo)
    


diretorio = '/home/mateus/Documentos/Dickeya/9_orthofinder/anotadas_184/oryzae'
new_dir = '/home/mateus/Documentos/Dickeya/ARTIGO2_zeae/7_panvita'




for root, dirs, files in os.walk(diretorio):
    for i in files:
        if i.endswith('.gbk'):
            old_path = os.path.join(root, i)
            new_path = os.path.join(new_dir, i) 
            shutil.copy(old_path, new_path)  
            print(f'Movido: {old_path} -------> {new_path}')           

