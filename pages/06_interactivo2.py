import pandas as pd
import streamlit as st

# Cargar el archivo CSV en un DataFrame
consumibles_df = pd.read_csv('consumibles-miseq.csv')

# Título para el costo parcial
st.title('Modulo de NGS')

# Resumen de la justificación
resumen_texto = """
**Proyecto**
... (tu texto aquí)
"""
# Mostrar el resumen en la aplicación
st.title("Justificación de los Equipos Pedidos")
st.markdown(resumen_texto)

# Cargar imagen desde un archivo local
imagen_local = "ngs-pasos.jpg"
imagen = st.image(imagen_local, caption="Pasos en NGS", use_column_width=True)

# Cargar imagen desde un archivo local
imagen_renis = "Renis.jpeg"
imagen = st.image(imagen_renis, caption="RENIS", use_column_width=True)

# Título para el costo parcial
st.title('Consumibles Miseq')
# Crear botones para mostrar y descargar los DataFrames
if st.button('Mostrar y Descargar Consumibles MiSeq'):
    st.title('Consumibles MiSeq')
    st.write('Datos de consumibles:')

    # Formulario para seleccionar columnas y opciones
    with st.form('form'):
        sel_column = st.multiselect('Seleccionar columnas', consumibles_df.columns,
                                    help='Selecciona columnas para formar un nuevo dataframe. Presiona enviar cuando hayas terminado.')
        sel_rows = st.multiselect('Seleccionar filas', consumibles_df.index.tolist(),
                                  help='Selecciona filas para formar un nuevo dataframe. Presiona enviar cuando hayas terminado.')
        drop_na = st.checkbox('Eliminar filas con valores faltantes', value=True)
        submitted = st.form_submit_button("Enviar")

    # Crear el nuevo dataframe basado en las selecciones
    if submitted:
        consumibles_new_df = consumibles_df.loc[sel_rows, sel_column] if sel_rows else consumibles_df[sel_column]
        if drop_na:
            consumibles_new_df = consumibles_new_df.dropna()

        st.write('Nuevo dataframe')
        consumibles_new_style = consumibles_new_df.style.format(precision=2, na_rep='MISSING', thousands=",", formatter={('A'): "{:.0f}"})
        st.dataframe(consumibles_new_style)

        st.download_button(
            label="Descargar Consumibles Seleccionados",
            data=consumibles_new_df.to_csv().encode('utf-8'),
            file_name='consumibles_seleccionados.csv',
            key='consumibles_selected_download'
        )
