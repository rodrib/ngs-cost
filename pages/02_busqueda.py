####
import streamlit as st
import pandas as pd

# Cargar el DataFrame desde el archivo CSV
df = pd.read_csv('Paneles-3.csv')

# Título de la aplicación
st.title("Busqueda de Genes")

# Texto explicativo
st.markdown("""
En esta sección, tendrás la opción de seleccionar un panel genómico específico. Al hacerlo, se mostrarán los genes asociados a ese panel. 
Además, cada gen se presenta como un enlace interactivo. Al hacer clic en el nombre de un gen, se abrirá una nueva pestaña con su página correspondiente en GeneCards, 
donde podrás obtener información detallada sobre su función y relevancia.
""")

# Botones para seleccionar el panel
panel_seleccionado = st.radio("Selecciona un Panel:", ["HC_38", "HC_55", "HC_117", "HC_144","Cancer_Manlab","SOPHiA_DDMTM_HCS v2.0","Devyser_HBOC_RUO_7","Devyser_BRCA","MD_40", "MD_50","MD_9", "MD_70"])



# Espacio en blanco para mostrar las columnas seleccionadas
espacio_columnas = st.empty()

# # Mostrar las columnas solo si se hizo clic en un panel
# if st.button("Mostrar Genes del Panel"):
#     # Filtrar el DataFrame para mostrar solo las filas correspondientes al panel seleccionado
#     df_filtrado = df[df['Panel'] == panel_seleccionado]

#     # Llenar el espacio en blanco con las filas y columnas seleccionadas
#     espacio_columnas.write("Filas y Columnas Seleccionadas:")
    
#     # Mostrar panel y genes como enlaces y abrir GeneCards al hacer clic
#     for index, row in df_filtrado.iterrows():
#         panel = row["Panel"]
#         genes = row["Genes-Panel"].split(", ")  # Separar los genes por comas
#         espacio_columnas.write(f"Panel: {panel}")
#         for gene_name in genes:
#             gene_link = f"<a href='https://www.genecards.org/cgi-bin/carddisp.pl?gene={gene_name}&keywords={gene_name}'>{gene_name}</a>"
#             st.markdown(gene_link, unsafe_allow_html=True)

# Mostrar las columnas solo si se hizo clic en un panel
if st.button("Mostrar Genes del Panel"):
    # Filtrar el DataFrame para mostrar solo las filas correspondientes al panel seleccionado
    df_filtrado = df[df['Panel'] == panel_seleccionado]

    # Crear una lista de genes
    genes = []
    for _, row in df_filtrado.iterrows():
        genes.extend(row["Genes-Panel"].split(", "))

    # Crear una lista de enlaces de genes a GeneCards con formato HTML
    enlaces_genes = []
    for gene in genes:
        gene_link = f"<a href='https://www.genecards.org/cgi-bin/carddisp.pl?gene={gene.replace(' ', '%20')}&keywords={gene.replace(' ', '%20')}' target='_blank'>{gene}</a>"
        enlaces_genes.append(gene_link)

    # Mostrar la lista de enlaces en formato HTML
    espacio_columnas.write("Genes del Panel:")
    espacio_columnas.markdown(", ".join(enlaces_genes), unsafe_allow_html=True)
