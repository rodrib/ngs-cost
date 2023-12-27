import pandas as pd
import streamlit as st
import os

df = pd.read_csv('Paneles.csv')




# Título de la aplicación
st.title("Visualizador de Paneles")

# Botones para seleccionar el panel
panel_seleccionado = st.radio("Selecciona un Panel:", ["Panel de Cáncer", "Panel de Desorden Metabólico"])



# Espacio en blanco para mostrar las columnas seleccionadas
espacio_columnas = st.empty()

# Mostrar las columnas solo si se hizo clic en un panel
if st.button("Mostrar Paneles"):
    # Filtrar y mostrar las filas según la selección
    if panel_seleccionado == "Panel de Cáncer":
        valores_a_mostrar = ["HC_38", "HC_55", "HC_117", "HC_144"]
    elif panel_seleccionado == "Panel de Desorden Metabólico":
        valores_a_mostrar = ["MD_40", "MD_50", "MD_9", "MD_70"]
    else:
        # Agrega aquí la lógica para otros paneles si es necesario
        valores_a_mostrar = []

    # Filtrar el DataFrame para mostrar solo las filas correspondientes a los valores seleccionados
    df_filtrado = df[df['Panel'].isin(valores_a_mostrar)]

    # Seleccionar las columnas relevantes
    columnas_mostrar = ["Panel", "Genes-Panel"] + [col for col in df.columns if any(valor in col for valor in valores_a_mostrar)]

    # Llenar el espacio en blanco con las filas y columnas seleccionadas
    espacio_columnas.write("Filas y Columnas Seleccionadas:")
    espacio_columnas.write(df_filtrado[columnas_mostrar])


# Seleccionar los paneles a comparar
panel_1 = st.selectbox("Selecciona el primer panel:", df['Panel'].unique(), key='panel_1')
panel_2 = st.selectbox("Selecciona el segundo panel:", df['Panel'].unique(), key='panel_2')

# Botón para comparar paneles
if st.button("Comparar Paneles"):
    # Obtener los genes de ambos paneles
    genes_panel_1 = set(df[df['Panel'] == panel_1]['Genes-Panel'].str.split(',').explode().str.strip())
    genes_panel_2 = set(df[df['Panel'] == panel_2]['Genes-Panel'].str.split(',').explode().str.strip())

    # Calcular los genes comunes
    genes_comunes = genes_panel_1.intersection(genes_panel_2)

    # Calcular el porcentaje de genes comunes
    porcentaje_genes_comunes = (len(genes_comunes) / len(genes_panel_1.union(genes_panel_2))) * 100

    # Mostrar los resultados
    st.write(f"Genes comunes entre {panel_1} y {panel_2}: {genes_comunes}")
    st.write(f"Porcentaje de genes comunes: {porcentaje_genes_comunes:.2f}%")


# Enlace como un botón
url = "https://drive.google.com/file/d/1hRjufv3_1fKGw7aKqCKPEh6oOaXW3U1N/view?usp=drive_link"
if st.button("Más Información"):
    st.markdown(f"[Más Información]({url})", unsafe_allow_html=True)


####
