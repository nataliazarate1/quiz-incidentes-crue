import pandas as pd

# ==============================
# CARGAR DATOS
# ==============================
df = pd.read_csv("incidentes_crue_diarios.txt", sep="\t")
df["fecha"] = pd.to_datetime(df["fecha"])

# Crear columnas auxiliares
df["año"] = df["fecha"].dt.year
df["mes"] = df["fecha"].dt.month
df["dia_semana"] = df["fecha"].dt.day_name()

# ==============================
# PROMEDIO POR AÑO
# ==============================
promedio_anual = df.groupby("año")["incidentes"].mean()

prom_2022 = promedio_anual.get(2022, 0)
prom_2023 = promedio_anual.get(2023, 0)
diferencia = prom_2023 - prom_2022

print("PROMEDIO POR AÑO")
print("Promedio 2022:", round(prom_2022, 2))
print("Promedio 2023:", round(prom_2023, 2))
print("Diferencia (2023-2022):", round(diferencia, 2))

# ==============================
# PROMEDIO POR DÍA DE LA SEMANA
# ==============================
orden_dias = ["Monday", "Tuesday", "Wednesday", "Thursday",
              "Friday", "Saturday", "Sunday"]

promedio_dia = df.groupby("dia_semana")["incidentes"].mean()

print("\nPROMEDIO POR DÍA DE LA SEMANA")

for dia in orden_dias:
    valor = promedio_dia.get(dia, 0)
    print(dia + ":", round(valor, 2))

dia_mayor = promedio_dia.idxmax()
print("Día con MÁS incidentes:", dia_mayor)

# ==============================
# PROMEDIO POR MES
# ==============================
promedio_mes = df.groupby("mes")["incidentes"].mean()
promedio_mes_ordenado = promedio_mes.sort_values(ascending=False)

print("\nPROMEDIO POR MES")

print("Mes #1 (más alto):", promedio_mes_ordenado.index[0],
      "-", round(promedio_mes_ordenado.iloc[0], 2))

print("Mes #2:", promedio_mes_ordenado.index[1],
      "-", round(promedio_mes_ordenado.iloc[1], 2))

print("Mes #3:", promedio_mes_ordenado.index[2],
      "-", round(promedio_mes_ordenado.iloc[2], 2))

mes_mas_bajo = promedio_mes.idxmin()
print("Mes más BAJO:", mes_mas_bajo,
      "-", round(promedio_mes.min(), 2))