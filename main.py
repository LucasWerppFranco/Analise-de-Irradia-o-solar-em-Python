import pandas as pd
import matplotlib.pyplot as plt

# Carregamento dos dados
df = pd.read_csv("dados_radiacao.csv")

# Conversão para datetime
df["Datetime"] = pd.to_datetime({
    "year": 2023,  # ou o ano que você quiser
    "month": df["Month"],
    "day": df["Day"],
    "hour": df["Hour"]
})

# Organizar pelo tempo
df = df.sort_values("Datetime")

# Análise básica
print("Resumo estatístico:\n")
print(df[[
    "Beam Irradiance (W/m2)",
    "Diffuse Irradiance (W/m2)",
    "Plane of Array Irradiance (W/m2)",
    "DC Array Output (W)",
    "AC System Output (W)"
]].describe())

# Gráfico da irradiância no tempo
plt.figure(figsize=(12, 6))
plt.plot(df["Datetime"], df["Plane of Array Irradiance (W/m2)"], label="POA Irradiance")
plt.plot(df["Datetime"], df["DC Array Output (W)"], label="DC Output")
plt.plot(df["Datetime"], df["AC System Output (W)"], label="AC Output")
plt.title("Irradiância e Produção de Energia")
plt.xlabel("Data e Hora")
plt.ylabel("W/m² ou W")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

