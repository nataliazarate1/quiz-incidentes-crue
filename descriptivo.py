import pandas as pd
import numpy as np

# Leer archivo (separado por tabulaciones)
df = pd.read_csv("incidentes_crue_diarios.txt", sep="\t")

# Convertir fecha a formato datetime
df["fecha"] = pd.to_datetime(df["fecha"])

# Serie de incidentes
incidentes = df["incidentes"]

# ===============================
# MEDIDAS DE TENDENCIA CENTRAL
# ===============================
media = incidentes.mean()
mediana = incidentes.median()
moda = incidentes.mode()

# ===============================
# MEDIDAS DE DISPERSIÓN
# ===============================
desv_std = incidentes.std()          # muestral
varianza = incidentes.var()          # muestral
cv = (desv_std / media) * 100
rango = incidentes.max() - incidentes.min()

# ===============================
# CUARTILES Y PERCENTILES
# ===============================
q1 = incidentes.quantile(0.25)
q2 = incidentes.quantile(0.50)
q3 = incidentes.quantile(0.75)
iqr = q3 - q1
p95 = incidentes.quantile(0.95)

# ===============================
# VALORES EXTREMOS
# ===============================
max_val = incidentes.max()
min_val = incidentes.min()

dia_max = df.loc[incidentes.idxmax(), "fecha"]
dia_min = df.loc[incidentes.idxmin(), "fecha"]

# ===============================
# RESULTADOS
# ===============================
print("MEDIDAS DE TENDENCIA CENTRAL")
print("Media:", round(media, 2))
print("Mediana:", mediana)
print("Moda:", moda.values if not moda.empty else "No hay moda")

print("\nMEDIDAS DE DISPERSIÓN")
print("Desviación estándar:", round(desv_std, 2))
print("Varianza:", round(varianza, 2))
print("Coeficiente de variación (%):", round(cv, 2))
print("Rango:", rango)

print("\nCUARTILES Y PERCENTILES")
print("Q1:", q1)
print("Q2 (Mediana):", q2)
print("Q3:", q3)
print("IQR:", iqr)
print("Percentil 95:", p95)

print("\nVALORES EXTREMOS")
print("Día con MÁS incidentes:", dia_max.date(), "-", max_val)
print("Día con MENOS incidentes:", dia_min.date(), "-", min_val)