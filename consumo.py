import pandas as pd
import numpy as np

# Carregar o arquivo Excel
file_path = 'dados_radiacao.xlsx'  # Ajuste o caminho se necessário
dados = pd.read_excel(file_path)

# Selecionar duas variáveis para análise univariada
var1 = dados['Beam Irradiance (W/m2)']
var2 = dados['Ambient Temperature (C)']

# Função para calcular as medidas estatísticas
def analise_univariada(serie):
    medidas = {}
    # Medidas de Tendência Central
    medidas['média'] = serie.mean()
    medidas['mediana'] = serie.median()
    medidas['moda'] = serie.mode().values.tolist()

    # Medidas de Dispersão
    medidas['amplitude'] = serie.max() - serie.min()
    medidas['variância'] = serie.var()
    medidas['desvio padrão'] = serie.std()
    medidas['coeficiente de variação (%)'] = (serie.std() / serie.mean()) * 100 if serie.mean() != 0 else np.nan

    # Medidas Separatrizes
    medidas['quartil 1 (Q1)'] = serie.quantile(0.25)
    medidas['quartil 2 (Q2 - mediana)'] = serie.quantile(0.5)
    medidas['quartil 3 (Q3)'] = serie.quantile(0.75)
    medidas['mínimo'] = serie.min()
    medidas['máximo'] = serie.max()

    return medidas

# Realizar análises
analise_var1 = analise_univariada(var1)
analise_var2 = analise_univariada(var2)

# Exibir resultados
print("Análise - Beam Irradiance (W/m²):")
for k, v in analise_var1.items():
    print(f"{k}: {v}")

print("\nAnálise - Ambient Temperature (°C):")
for k, v in analise_var2.items():
    print(f"{k}: {v}")

# Interpretação
print("\n# A análise da variável 'Beam Irradiance' evidencia que a maioria das observações possui valor igual a zero,")
print("# refletido na mediana e moda nulas. Contudo, a média está acima de 200 W/m², indicando a presença de valores")
print("# extremos que elevam esta medida, confirmada também pela ampla dispersão (desvio padrão elevado e coeficiente")
print("# de variação superior a 100%). A amplitude máxima de 1053 W/m² reforça esta variabilidade. Por outro lado,")
print("# a variável 'Ambient Temperature' apresenta distribuição mais concentrada, com média e mediana próximas e")
print("# coeficiente de variação abaixo de 25%, sugerindo estabilidade nos valores ao longo do tempo. A amplitude de")
print("# cerca de 32 °C, embora expressiva, não compromete a homogeneidade dos dados, como demonstrado pelo baixo")
print("# desvio padrão.")
