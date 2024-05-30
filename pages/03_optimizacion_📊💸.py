import streamlit as st

# Título de la aplicación
st.title("Optimizacion de Paneles")

texto = """
Dado un conjunto de paneles genómicos, cada uno con un costo asociado y una lista de enfermedades genéticas detectables, y un presupuesto limitado, el objetivo es determinar la combinación óptima de paneles para secuenciar de manera que se maximice la detección de enfermedades genéticas sin exceder el presupuesto disponible.

Las variables en este problema son:

- n: número de paneles genómicos disponibles.
- w_i: costo del panel genómico i.
- v_i: lista de enfermedades genéticas detectables por el panel i.
- W: presupuesto máximo disponible.

El problema ahora se convierte en seleccionar un conjunto de paneles genómicos de manera que el costo total no supere el presupuesto W y se maximice la detección de enfermedades genéticas. Esta formulación es análoga al problema de la mochila, donde en lugar de maximizar el valor, se busca maximizar la detección de enfermedades genéticas.

Esta representación puede ayudar a abordar decisiones sobre qué paneles secuenciar para maximizar la información genética relevante dentro de un presupuesto determinado en el contexto de la secuenciación genómica.
"""

st.write(texto)

st.title("Ejemplo FRIENDLY")

import streamlit as st
import pandas as pd
import numpy as np

def optimizar_paneles(n, costos, enfermedades, presupuesto_maximo):
    dp = np.zeros((n + 1, presupuesto_maximo + 1), dtype=int)

    for i in range(1, n + 1):
        for j in range(presupuesto_maximo + 1):
            if costos[i - 1] <= j:
                dp[i, j] = max(dp[i - 1, j], len(set(enfermedades[i - 1].split(','))) + dp[i - 1, j - costos[i - 1]])
            else:
                dp[i, j] = dp[i - 1, j]

    combinacion_optima = []
    i, j = n, presupuesto_maximo
    while i > 0 and j > 0:
        if dp[i, j] != dp[i - 1, j]:
            combinacion_optima.append(i - 1)
            j -= costos[i - 1]
        i -= 1

    return combinacion_optima

# Datos de ejemplo
paneles = ['Panel A', 'Panel B', 'Panel C']
costos = [10, 15, 20]
enfermedades = ['Enf1, Enf2', 'Enf2, Enf3', 'Enf1, Enf3']

# Crear DataFrame para mostrar la información de los paneles
df_paneles = pd.DataFrame({'Panel': paneles, 'Costo': costos, 'Enfermedades': enfermedades})

# Mostrar tabla en Streamlit
st.write("Información de los Paneles:")
st.write(df_paneles)

# Widget para ajustar el presupuesto máximo
presupuesto_maximo = st.slider("Presupuesto Máximo", min_value=0, max_value=100, value=30)
n = len(paneles)

combinacion_optima = optimizar_paneles(n, costos, enfermedades, presupuesto_maximo)

# Mostrar resultado en Streamlit
st.write(f"\nPresupuesto Máximo: {presupuesto_maximo}")
st.write(f"Combinación Óptima de Paneles: {[paneles[i] for i in combinacion_optima]}")
