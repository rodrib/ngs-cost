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
