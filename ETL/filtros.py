import pandas as pd   

df = pd.read_csv("C:\\Users\\mwlm1\\OneDrive\\Área de Trabalho\\Projeto_final_Impacta\\Datasets\\Dados_SP\\dados_covid_sp.csv\\dados_covid_sp.csv",delimiter=';')
df2 = pd.read_csv("E:\\cursos\\casos_covid_sp.csv")
df3 = pd.read_csv("C:\\Users\\mwlm1\\OneDrive\\Área de Trabalho\\Projeto_final_Impacta\\Datasets\\ETL\\mortes_covid_sp.csv")

colunas_desejandas_casos = ['nome_munic', 'dia', 'mes', 'datahora', 'casos','casos_novos']
colunas_desejandas_mortes = ['nome_munic', 'dia', 'mes', 'datahora','obitos','obitos_novos']
# Casos
filtro_casos = df[colunas_desejandas_casos]
'''print(filtro_casos) '''

casos = filtro_casos.copy()
salvar_casos = r'C:\Users\mwlm1\OneDrive\Área de Trabalho\Projeto_final_Impacta\Datasets\ETL\casos_covid_sp.csv'
casos.to_csv(salvar_casos, index=False, sep=',') 


filtro_ignorado_casos = df2.loc[df2['nome_munic'] == 'Ignorado']
'''print(filtro_ignorado_casos)'''

Ignorado_casos = filtro_ignorado_casos.copy()
salvar_ignorados_casos = r'C:\Users\mwlm1\OneDrive\Área de Trabalho\Projeto_final_Impacta\Datasets\ETL\ignorado_casos_covid_sp.csv'
Ignorado_casos.to_csv(salvar_ignorados_casos, index=False, sep=',') 

# Mortes
filtro_mortes = df[colunas_desejandas_mortes]
'''print(filtro_mortes)'''

mortes  = filtro_mortes.copy()
salvar_mortes = r'C:\Users\mwlm1\OneDrive\Área de Trabalho\Projeto_final_Impacta\Datasets\ETL\mortes_covid_sp.csv'
mortes.to_csv(salvar_mortes, index=False, sep=',')

filtro_ignorado_morte = df3.loc[df3['nome_munic'] == 'Ignorado']
'''print(filtro_ignorado_morte)'''

Ignorado_mortes = filtro_ignorado_morte.copy()
salvar_ignorados_mortes = r'C:\Users\mwlm1\OneDrive\Área de Trabalho\Projeto_final_Impacta\Datasets\ETL\ignorado_mortes_covid.csv'
Ignorado_mortes.to_csv(salvar_ignorados_mortes, index=False, sep=',')

# Vacinação
