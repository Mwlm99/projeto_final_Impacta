import pandas as pd   

df = pd.read_csv("C:\\Users\\mwlm1\\Downloads\\dados_covid_sp\\dados_covid_sp.csv",delimiter=';')

def filter_dataframe(df,column, value):
    """
    Remove linhas do DataFrame onde a coluna especificada tem o valor fornecido.
    
    Parâmetros:
        df (DataFrame): O DataFrame de entrada.
        coluna (str): O nome da coluna para filtrar.
        valor: O valor a ser removido.
        
    Retorna:
        DataFrame: Um novo DataFrame com as linhas removidas.
    """
    return df[df[column] != value]

def salve_to_csv(df, filename):
     """
    Salva o DataFrame em um arquivo CSV.
    
    Parâmetros:
        df (DataFrame): O DataFrame a ser salvo.
        nome_arquivo (str): O nome do arquivo CSV.
    """
     return df.to_csv(filename, index=False)


# Definir colunas de interesse
colunas_desejadas_casos = ['nome_munic','datahora', 'casos','casos_novos']
colunas_desejadas_obitos = ['nome_munic','datahora', 'obitos','obitos_novos']

# Filtrar linhas com 'Ignorado' na coluna 'nome_munic'
exclusao_ignorados = filter_dataframe(df, 'nome_munic', 'Ignorado')

# Extrair colunas desejadas para casos e salvar em CSV
casos = exclusao_ignorados[colunas_desejadas_casos]
salvar_casos = salve_to_csv(casos,'casos.csv')

# Extrair colunas desejadas para óbitos e salvar em CSV
mortes = exclusao_ignorados[colunas_desejadas_obitos]
salvar_mortes = salve_to_csv(mortes,'mortes.csv')