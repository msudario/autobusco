import Bio.SeqIO
import subprocess
import os

# Carregue as sequências do arquivo FASTA
seq1 = Bio.SeqIO.read("/home/mateus/Desktop/teste/seq1.fasta", "fasta")
seq2 = Bio.SeqIO.read("/home/mateus/Desktop/teste/seq2.fasta", "fasta")
seq3 = Bio.SeqIO.read("/home/mateus/Desktop/teste/seq3.fasta", "fasta")

# para mostrar pro BLAST a sequencia de referencia no alignment multiplo
sequencia_de_referencia = '/home/mateus/Desktop/teste/seq1.fasta'

def rodando_blast():
    # Crie um arquivo temporário para armazenar as sequências
    temp_file = "/home/mateus/Desktop/teste/temp.fasta"
    Bio.SeqIO.write([seq1, seq2, seq3], temp_file, "fasta")

    # Crie um arquivo temporário para armazenar o resultado do BLAST
    temp_file2 = "/home/mateus/Desktop/teste/alinhamento"

    # Comando para executar o BLAST local (lembrar que o subject é um arquivo separado de referencia)
    blast_command = f'blastn -query {temp_file} -subject {sequencia_de_referencia} -out {temp_file2} -outfmt "6 qseq sseq"'

    # Execute o comando usando um subprocesso
    try:
        subprocess.run(blast_command, shell=True, check=True)
        print("BLAST local concluído com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o BLAST: {e}")

""" gerando a imagem """

import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import numpy as np

# Sequências de consulta (Query) e sequência alvo (Sbjct)
query_sequence = 'ACACTTGCTTCTGACACAACCGTGTTCACTAGCAACTACACAAACAGACACCATG--------------------------CTGACTGCTGAGGAGAAGGCTGCCGTCACCGCCTTTTGGGGCAAGGTGAAAGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGTAGGTATCCCACTTACAAGGCAGGTTTAAGGAGAGTGAAATGCACCTGGGCGTGTGAGGACAGAGCCGTCCC-TGAGATTCAGAGAGCTGCTGGCTTCCTCTGACCT-T-GTGCTGTTTTCTCCCCC-TAGGCTGCTGGTTGTCTACCCCTGGACTCAGAGGTTCTTTGAGTCCTTTGGGGACTTGTCCACTGCTGATGCTGTTATGAACAACCCTAAGGTGAAGGCCCATGGCAAGAAGGTGCTAGATTCCTTTAGTAATGGCATGAAGCATCTCGATGACCTCAAGGGCACCTTTGCTGCGCTGAGTGAGCTGCACTGTGATAAGCTGCATGTGGATCCTGAGAACTTCAAGGTGAGTTTGTGGAATCCTCAGTGTTCTCCTTC---TTCTTTT-TATGGTCAAGCTCATGTCAT-G-A-GGAGA-AAGCTGAATGGCAGGACACAGTTTAGAATGGAGAA'
sbjct_sequence = 'ACATTTGCTTCTGACACAACTGTGTTCACTAGCAAC--CTCAAACAGACACCATG--------------------------TGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATA-GAAACTGGGCATGTGGAGACAGAGAAGACTCTTGGGTTTCTGATAGGCACTGACTCTCTCTG-CCTATTGGTCTATTTTCCCACCCTTAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGGTGAGTCTATGGGACGCTTGATGTTTTCTTTCCCCTTCTTTTCTATGGTTAAGTTCATGTCATAGGAAGGGGATAAG-T-AA---CAGGGTACAGTTTAGAATGG-GAA'


# Configurações para o gráfico
fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Raio interno e externo dos anéis
inner_radius = 0.4
outer_radius = 0.5

# Função para desenhar os anéis
def draw_ring(sequence, radius, ax, color):
    angle = 360 / len(sequence)
    for i, base in enumerate(sequence):
        if base == "-":
            # Desalinhamento (espaço em branco)
            continue
        start_angle = i * angle
        end_angle = (i + 1) * angle
        arc = Wedge(center=(0, 0), r=radius, theta1=start_angle, theta2=end_angle, width=0.05, fill=True, color=color)
        ax.add_patch(arc)
        x = (radius + 0.075) * np.cos(np.deg2rad((start_angle + end_angle) / 2))
        y = (radius + 0.075) * np.sin(np.deg2rad((start_angle + end_angle) / 2))
        

# Desenha os anéis para Query e Sbjct
draw_ring(query_sequence, inner_radius, ax, 'blue')
draw_ring(sbjct_sequence, outer_radius, ax, 'red')

# Configurações adicionais do gráfico
ax.axis('off')
# plt.gca().set_aspect('equal', adjustable='box')
# plt.tight_layout()

# Exibe o gráfico
plt.show()
