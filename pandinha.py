import pandas as pd

df = pd.read_csv('/home/mateus/Documentos/Dickeya/ARTIGO1_dadantii/8_panvita/Results_bacmet_23-05-2023_14-52-36/bacmet_gene_count.csv', sep = ';')

count = df['Presence Number'].value_counts()

def core_genome(df):
    core_genes = df[df['Presence Number'] == 11]
    genes = core_genes['Genes']
    
    #printando cada core    
    lista_core = []
    for i in genes:
        lista_core.append(i), ','
    print('a lista de genes core é: ', ','.join(lista_core))

   #contando os genes core
    contador_core = 0
    for i in lista_core:
        contador_core += 1
    print('total de genes core = ', contador_core)
    
def acessory_genome(df):
    acessory_genes = df[(df['Presence Number'] != 11) & (df['Presence Number'] != 1)]
    genes = acessory_genes['Genes']
    
    #printando cada acessory    
    lista_acessory = []
    for i in genes:
        lista_acessory.append(i), ','
    print('a lista de genes acessory é: ', ','.join(lista_acessory))

   #contando os genes acessorios
    contador_acessory = 0
    for i in lista_acessory:
        contador_acessory += 1
    print('total de genes acessory = ', contador_acessory)
       
def exclusive_genome(df):
    exclusive_genes = df[df['Presence Number'] == 1]   
    genes = exclusive_genes['Genes']
    
    #printando cada exclusive
    lista_exclusive = []
    for i in genes:
        lista_exclusive.append(i), ','
    print('a lista de genes exclusive é: ', ','.join(lista_exclusive))
    
    #contando os genes exclusivos
    contador_exclusive = 0
    for i in lista_exclusive:
        contador_exclusive += 1
    print('total de genes exclusive = ', contador_exclusive)
    
    #procurando os genes no DB do panvita    
    for cada_item in lista_exclusive:
        print(cada_item)
    
exclusive_genome(df)

# def pan_analysis(df):
#     core_genome(df)
#     acessory_genome(df)
#     exclusive_genome(df)    
    
# if __name__ == '__main__':
#     pan_analysis(df)




