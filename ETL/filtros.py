import pandas as pd   

df = pd.read_csv("C:\\Users\\mwlm1\\Downloads\\dados_covid_sp\\dados_covid_sp.csv",delimiter=';')

def filter_dataframe(df,column, value):
  return df[df[column] != value]

def salve_to_csv(df, filename):
  return df.to_csv(filename, index=False)



colunas_desejadas_casos = ['nome_munic','datahora', 'casos','casos_novos']
colunas_desejadas_obitos = ['nome_munic','datahora', 'obitos','obitos_novos']

exclusao_ignorados = filter_dataframe(df, 'nome_munic', 'Ignorado')

casos = exclusao_ignorados[colunas_desejadas_casos]
salvar_casos = salve_to_csv(casos,'casos.csv')

mortes = exclusao_ignorados[colunas_desejadas_obitos]
salvar_mortes = salve_to_csv(mortes,'mortes.csv')