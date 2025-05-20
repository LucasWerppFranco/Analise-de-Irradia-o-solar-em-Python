def bubble_sort_prioridade(dispositivos):
    n = len(dispositivos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if dispositivos[j]['prioridade'] < dispositivos[j + 1]['prioridade']:
                dispositivos[j], dispositivos[j + 1] = dispositivos[j + 1], dispositivos[j]
    return dispositivos

def simular_consumo(dispositivos, energia_disponivel):
    # Ordenar por prioridade (maior para menor)
    dispositivos_ordenados = bubble_sort_prioridade(dispositivos.copy())

    consumo_total = 0
    ativados = []
    desligados = []

    for d in dispositivos_ordenados:
        if consumo_total + d['consumo'] <= energia_disponivel:
            ativados.append(d['nome'])
            consumo_total += d['consumo']
        else:
            desligados.append(d['nome'])

    # Exibir resultados
    print("=== Simulação de Consumo de Energia ===")
    print(f"→ Energia disponível: {energia_disponivel} kWh\n")
    print("Dispositivos ligados (em ordem de prioridade):")
    for nome in ativados:
        print(f"✔ {nome}")
    print("\nDispositivos desligados:")
    for nome in desligados:
        print(f"✘ {nome}")
    print(f"\nConsumo total: {consumo_total:.2f} kWh")


# Exemplo de uso
if __name__ == "__main__":
    dispositivos = [
        {'nome': 'Geladeira', 'consumo': 1.2, 'prioridade': 5},
        {'nome': 'Ar Condicionado', 'consumo': 3.5, 'prioridade': 3},
        {'nome': 'Lâmpadas', 'consumo': 0.6, 'prioridade': 4},
        {'nome': 'Máquina de Lavar', 'consumo': 2.0, 'prioridade': 2},
        {'nome': 'TV', 'consumo': 0.8, 'prioridade': 1}
    ]

    energia_disponivel = 4.0  # kWh
    simular_consumo(dispositivos, energia_disponivel)
