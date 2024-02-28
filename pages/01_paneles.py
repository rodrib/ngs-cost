import pandas as pd
import streamlit as st
import os

df = pd.read_csv('Paneles-3.csv')

#df = pd.read_csv('Paneles-1.csv')


# Título de la aplicación
st.title("Visualizador de Paneles")

st.markdown("""
Adicionalmente, te ofrecemos la posibilidad de comparar dos paneles genómicos. Al seleccionar esta opción, podrás elegir dos paneles distintos y visualizar de manera clara:
- Los genes que ambos paneles comparten.
- Los genes específicos del primer panel.
- Los genes específicos del segundo panel.

Esta herramienta facilita la identificación de similitudes y diferencias entre paneles, brindándote una visión detallada de los genes asociados a cada uno.
""")

# Botones para seleccionar el panel
panel_seleccionado = st.radio("Selecciona un Panel:", ["Panel de Cáncer", "Panel de Desorden Metabólico"])



# Espacio en blanco para mostrar las columnas seleccionadas
espacio_columnas = st.empty()

# Mostrar las columnas solo si se hizo clic en un panel
if st.button("Mostrar Paneles"):
    # Filtrar y mostrar las filas según la selección
    if panel_seleccionado == "Panel de Cáncer":
        valores_a_mostrar = ["HC_38", "HC_55", "HC_117", "HC_144","Cancer_Manlab","SOPHiA_DDMTM_HCS v2.0","Devyser_HBOC_RUO_7","Devyser_BRCA"]
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

    # Calcular los genes exclusivos en el Panel 1
    genes_exclusivos_panel_1 = genes_panel_1 - genes_comunes

    # Calcular los genes exclusivos en el Panel 2
    genes_exclusivos_panel_2 = genes_panel_2 - genes_comunes

    # Calcular el porcentaje de genes comunes
    porcentaje_genes_comunes = (len(genes_comunes) / len(genes_panel_1.union(genes_panel_2))) * 100

    # Mostrar los resultados
    st.write(f"Genes comunes entre {panel_1} y {panel_2}: {genes_comunes}")
    st.write(f"Porcentaje de genes comunes: {porcentaje_genes_comunes:.2f}%")

    st.write("Genes exclusivos en el Panel 1:")
    st.write(genes_exclusivos_panel_1)
    st.write("Genes exclusivos en el Panel 2:")
    st.write(genes_exclusivos_panel_2)


resumen_panel = """En mas informacion se encuentra los detalles de los paneles """

st.markdown(resumen_panel)

# Enlace como un botón
url = "https://drive.google.com/file/d/1hRjufv3_1fKGw7aKqCKPEh6oOaXW3U1N/view?usp=drive_link"
url1 = "https://drive.google.com/file/d/1ONYZCDzC0shZuMgV0Nwj_Da358YXl6ZG/view?usp=sharing"
url2 = "https://drive.google.com/file/d/1_qeljdBflXvuSV8_YwRG4A0lmONEi_V-/view?usp=sharing"

if st.button("Más Información"):
    st.markdown(f"[Paneles de Sophia]({url})", unsafe_allow_html=True)
    st.markdown(f"[HCS v2.0]({url1})", unsafe_allow_html=True)
    st.markdown(f"[Protocolo elegido]({url2})", unsafe_allow_html=True)




####
