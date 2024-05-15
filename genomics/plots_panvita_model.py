import pandas as pd
import matplotlib.pyplot as plt

# Carrega os arquivos CSV em DataFrames do Pandas
df = pd.read_csv('/home/mateus/Documents/ARTIGO1_dadantii/8_panvita/Results_vfdb_23-05-2023_14-52-31/vfdb_mechanisms.csv', sep=';')

# Set the 'Mechanism' column as the index
df.set_index('Virulence Mechanism', inplace=True)

# Plot the stacked bar plot
ax = df.plot(kind='bar', stacked=True, figsize=(10, 7))

# Step 4: Customize the plot
plt.title('Pan Virulome Bar Chart')
plt.xlabel('Mechanism')
plt.ylabel('Genes')
plt.legend(title='Types')

# Add the values on top of each bar
for container in ax.containers:
    
    ax.bar_label(container, labels=[f'{v:.0f}' if v > 0 else '' for v in container.datavalues], label_type='center', fontsize=6)

#Show the plot
plt.tight_layout()

# Save the plot with 400 DPI - uncomment to save
# plt.savefig('stacked_bar_plot.png', dpi=400)

plt.show()