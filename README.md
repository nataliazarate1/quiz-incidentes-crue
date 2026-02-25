# Análisis Temporal de Incidentes CRUE

## Descripción del Proyecto

Este proyecto realiza un análisis estadístico y temporal sobre un conjunto de datos de incidentes reportados por el sistema CRUE.

El archivo `incidentes_crue_diarios.txt` contiene:

- Fecha del incidente
- Número total de incidentes por día
- Total de registros: 730
- Período analizado: Enero 2022 - Diciembre 2023

El objetivo del proyecto es calcular las estadísticas descriptivas y analizar el comportamiento temporal de los incidentes reportados.

---

## Colaboradores

| Nombre              | GitHub |
|---------------------|--------|
| Natalia Zárate      | https://github.com/nataliazarate1 |
| Josue Pedraza | https://github.com/josuepedraza |

---

## Hallazgos Principales

| Estadística | Resultado |
|-------------|------------|
| Media general | 1717.47 incidentes diarios |
| Desviación estándar | 256.31 |
| Día con más incidentes | 2022-12-25 (3275) |
| Día con menos incidentes | 2022-04-15 (935) |
| Q1 | 1337 |
| Q3 | 1508.5 |


---

## Análisis Temporal

### Promedio por año
- 2022: 1667.1
- 2023: 1767.85
- Diferencia: 100.75

### Día con mayor promedio de incidentes
- El domingo es el día con mayor incidentes reportados, con un  promedio de 1880.04. 

### Mes con mayor promedio
- Diciembres es el mes con mayor promedio de incidentes reportados, con una cifra de 1881.02.

---

## ¿Se puede predecir?

Sí, dado que el comportamiento de los incidentes muestra patrones temporales que podrían modelarse usando técnicas de series de tiempo. Si se cuenta con datos históricos de varios años, sería posible aplicar modelos predictivos como regresión o ARIMA para estimar tendencias futuras. 

---
