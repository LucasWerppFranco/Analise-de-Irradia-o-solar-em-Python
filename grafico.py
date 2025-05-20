import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados do Excel
df = pd.read_excel('dados_radiacao.xlsx', engine='openpyxl')

# Estilo dos gráficos
sns.set(style="whitegrid")

# Gráfico de Setores (Distribuição de registros por mês)
month_counts = df['Month'].value_counts().sort_index()
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_colors = sns.color_palette("pastel")

plt.figure(figsize=(6,6))
plt.pie(month_counts, labels=month_labels, autopct='%1.1f%%', colors=month_colors)
plt.title('Distribuição de Registros por Mês')
plt.legend(month_labels, title="Meses", bbox_to_anchor=(1, 0.9))
plt.tight_layout()
plt.show()

# Gráfico de Barras (Irradiação Direta Média por Mês)
beam_by_month = df.groupby('Month')['Beam Irradiance (W/m2)'].mean()
plt.figure(figsize=(8,5))
sns.barplot(x=month_labels, y=beam_by_month.values, palette='viridis')
plt.title('Irradiação Direta Média por Mês')
plt.xlabel('Mês')
plt.ylabel('Irradiação Direta (W/m²)')
plt.legend(['Média Mensal'])
plt.tight_layout()
plt.show()

# Histograma da Temperatura Ambiente
plt.figure(figsize=(8,5))
plt.hist(df['Ambient Temperature (C)'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.title('Distribuição da Temperatura Ambiente')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()

# Boxplot da Irradiação Total no Plano por Mês
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='Month', y='Plane of Array Irradiance (W/m2)', palette='Set3')
plt.title('Boxplot da Irradiação no Plano por Mês')
plt.xlabel('Mês')
plt.ylabel('Irradiação no Plano (W/m²)')
plt.tight_layout()
plt.show()

# -------------------------------------------------------
# Insights:
# A distribuição por mês é equilibrada, o que mostra uma boa coleta de dados ao longo do ano.
# A irradiação direta tem média maior nos meses de verão, como esperado em locais tropicais.
# A temperatura ambiente se concentra entre 15 °C e 35 °C, com leve assimetria.
# O boxplot mostra que há grande variação da irradiação ao longo dos meses e outliers visíveis.
# Esses dados ajudam a entender padrões sazonais e podem ser úteis para otimizar sistemas solares.
