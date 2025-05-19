import pandas as pd

df = pd.read_csv("dados_radiacao.csv")

frequencia_discreta = df['Hour'].value_counts().sort_index()
tabela_discreta = pd.DataFrame({
    'Hora': frequencia_discreta.index,
    'Frequência Absoluta (fi)': frequencia_discreta.values
})
tabela_discreta['Frequência Relativa (%)'] = (tabela_discreta['Frequência Absoluta (fi)'] / tabela_discreta['Frequência Absoluta (fi)'].sum()) * 100

print("Tabela de Distribuição de Frequência - Variável Discreta (Hora):")
print(tabela_discreta)

hora_mais_frequente = tabela_discreta.loc[tabela_discreta['Frequência Absoluta (fi)'].idxmax(), 'Hora']
print(f"\n# A hora mais frequente registrada foi: {hora_mais_frequente}h.")

quantidade_madrugada = tabela_discreta[tabela_discreta['Hora'] < 6]['Frequência Absoluta (fi)'].sum()
print(f"# Houve {quantidade_madrugada} registros entre 0h e 5h, período de baixa incidência solar.")

variavel_continua = df["Beam Irradiance (W/m2)"]

n = len(variavel_continua)
k = int(1 + 3.322 * (n ** 0.5)) 
tabela_continua = pd.DataFrame()

classes = pd.cut(variavel_continua, bins=k)

frequencia_continua = classes.value_counts().sort_index()
tabela_continua['Classe'] = frequencia_continua.index.astype(str)
tabela_continua['Frequência Absoluta (fi)'] = frequencia_continua.values
tabela_continua['Frequência Relativa (%)'] = (frequencia_continua.values / frequencia_continua.values.sum()) * 100

print("\nTabela de Distribuição de Frequência - Variável Contínua (Beam Irradiance):")
print(tabela_continua)

classe_maior_freq = tabela_continua.loc[tabela_continua['Frequência Absoluta (fi)'].idxmax(), 'Classe']
print(f"\n# A faixa de irradiância com mais ocorrências foi: {classe_maior_freq}.")

percentual_irradiancia_alta = tabela_continua[tabela_continua['Classe'].str.contains('\(.*,\s*2000.0\]')]['Frequência Relativa (%)'].sum()
print(f"# Aproximadamente {percentual_irradiancia_alta:.2f}% dos dados estão em faixas de alta irradiância (>1500 W/m2).")

with pd.ExcelWriter("tabelas_frequencia.xlsx") as writer:
    tabela_discreta.to_excel(writer, sheet_name="Hora (Discreta)", index=False)
    tabela_continua.to_excel(writer, sheet_name="Irradiancia (Contínua)", index=False)

print("\n# As tabelas foram salvas no arquivo 'tabelas_frequencia.xlsx'.")

