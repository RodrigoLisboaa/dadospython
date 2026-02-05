import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path.cwd()
if ROOT.name == "notebooks":
    ROOT = ROOT.parent

DATA = ROOT  
FIGS = ROOT / "reports" / "figures"
FIGS.mkdir(parents=True, exist_ok=True)

df = pd.read_excel('2021/ideb_2021_anos_finais.xlsx', sheet_name='estados')

df_redes = df[df['dependencia_id'].isin([4, 5])]
df_redes = df_redes.sort_values(by='ibge_id')

siglas_estados = {
    11: 'RO', 12: 'AC', 13: 'AM', 14: 'RR', 15: 'PA', 16: 'AP', 17: 'TO',
    21: 'MA', 22: 'PI', 23: 'CE', 24: 'RN', 25: 'PB', 26: 'PE', 27: 'AL', 28: 'SE', 29: 'BA',
    31: 'MG', 32: 'ES', 33: 'RJ', 35: 'SP',
    41: 'PR', 42: 'SC', 43: 'RS',
    50: 'MS', 51: 'MT', 52: 'GO', 53: 'DF'
}

df_redes['sigla'] = df_redes['ibge_id'].map(siglas_estados)

plt.figure(figsize=(12, 6))

for rede_id, label in zip([4, 5], ['Privada', 'Publica']):
    dados_rede = df_redes[df_redes['dependencia_id'] == rede_id]
    plt.plot(dados_rede['sigla'], dados_rede['ideb'], marker='o', label=label)

plt.title('IDEB 2021 - Anos Finais: Comparação entre redes Pública e Privada')
plt.xlabel('Estado')
plt.ylabel('IDEB')
plt.legend()
plt.tight_layout()
plt.show()
