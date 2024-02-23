import pandas as pd   
df = pd.read_csv("C:\\Users\\mwlm1\\OneDrive\\Área de Trabalho\\Projeto_final_Impacta\\Datasets\\Dados_SP\\dados_covid_sp.csv\\dados_covid_sp.csv",delimiter=';')
colunas_desejandas_casos = ['nome_munic', 'dia', 'mes', 'datahora', 'casos','casos_novos']
filtro = df[colunas_desejandas_casos]
casos = filtro.copy()
salvar = r'E:\cursos\casos_covid_sp.csv'
casos.to_csv(salvar, index=False, sep=',')