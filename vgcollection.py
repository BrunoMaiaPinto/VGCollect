import pandas as pd
import csv

df = pd.read_csv('collection-2025-03-05.csv')

lista=[]

for i in range(len(df)):
  print(f'{i+1:0>3} | {df['Name'][i]} ({df['Platform'][i]})')
  lista.append([i+1, df['Name'][i], df['Platform'][i]])

with open('cvsCollection.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Index', 'Jogo', 'Consola'])
    writer.writerows(lista)

df_export = pd.DataFrame(lista, columns=['Index', 'Jogo', 'Consola'])

with pd.ExcelWriter('excelVgCollection.xlsx', engine='xlsxwriter') as writer:
    df_export.to_excel(writer, sheet_name='Colecção', index=False)