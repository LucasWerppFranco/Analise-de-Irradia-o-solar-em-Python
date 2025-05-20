import pandas as pd
import math

# Leitura correta do arquivo Excel
df = pd.read_excel("dados_radiacao.xlsx")

# Garantir que 'Hour' e 'Beam Irradiance (W/m2)' sejam numéricos
df['Hour'] = pd.to_numeric(df['Hour'], errors='coerce')
df['Beam Irradiance (W/m2)'] = pd.to_numeric(df['Beam Irradiance (W/m2)'], errors='coerce')

# Remover registros com valores ausentes
df = df.dropna(subset=['Hour', 'Beam Irradiance (W/m2)'])

# ---------------------------
# VARIÁVEL DISCRETA: HORA
# ---------------------------
frequencia_discreta = df['Hour'].value_counts().sort_index()
tabela_discreta = pd.DataFrame({
    'Hora': frequencia_discreta.index.astype(int),
    'Frequência Absoluta (fi)': frequencia_discreta.values
})
tabela_discreta['Frequência Relativa (%)'] = (
    tabela_discreta['Frequência Absoluta (fi)'] / tabela_discreta['Frequência Absoluta (fi)'].sum()
) * 100

print("Tabela de Distribuição de Frequência - Variável Discreta (Hora):")
print(tabela_discreta)

# Hora mais frequente
hora_mais_frequente = tabela_discreta.loc[
    tabela_discreta['Frequência Absoluta (fi)'].idxmax(), 'Hora'
]
print(f"\n# A hora mais frequente registrada foi: {hora_mais_frequente}h.")

# Quantidade entre 0h e 5h
quantidade_madrugada = tabela_discreta[tabela_discreta['Hora'] < 6]['Frequência Absoluta (fi)'].sum()
print(f"# Houve {quantidade_madrugada} registros entre 0h e 5h, período de baixa incidência solar.")

# ---------------------------
# VARIÁVEL CONTÍNUA: IRRADIÂNCIA
# ---------------------------
irradiancia = df["Beam Irradiance (W/m2)"]
n = len(irradiancia)
k = int(1 + 3.322 * math.log10(n))  # Fórmula de Sturges

# Definição das classes
classes = pd.cut(irradiancia, bins=k)

frequencia_continua = classes.value_counts().sort_index()
tabela_continua = pd.DataFrame({
    'Classe': frequencia_continua.index.astype(str),
    'Frequência Absoluta (fi)': frequencia_continua.values
})
tabela_continua['Frequência Relativa (%)'] = (
    tabela_continua['Frequência Absoluta (fi)'] / tabela_continua['Frequência Absoluta (fi)'].sum()
) * 100

print("\nTabela de Distribuição de Frequência - Variável Contínua (Beam Irradiance):")
print(tabela_continua)

# Classe mais frequente
classe_maior_freq = tabela_continua.loc[
    tabela_continua['Frequência Absoluta (fi)'].idxmax(), 'Classe'
]
print(f"\n# A faixa de irradiância com mais ocorrências foi: {classe_maior_freq}.")

# Percentual de irradiância alta (> 1500 W/m2)
percentual_irradiancia_alta = (
    irradiancia[irradiancia > 1500].count() / n
) * 100
print(f"# Aproximadamente {percentual_irradiancia_alta:.2f}% dos dados estão em faixas de alta irradiância (>1500 W/m2).")

# ---------------------------
# Exportar para Excel
# ---------------------------
with pd.ExcelWriter("tabelas_frequencia.xlsx") as writer:
    tabela_discreta.to_excel(writer, sheet_name="Hora (Discreta)", index=False)
    tabela_continua.to_excel(writer, sheet_name="Irradiancia (Contínua)", index=False)

print("\n# As tabelas foram salvas no arquivo 'tabelas_frequencia.xlsx'.")

