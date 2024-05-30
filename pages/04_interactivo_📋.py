import streamlit as st
import pandas as pd

# Cargar los archivos CSV en DataFrames
consumibles_df = pd.read_csv('consumibles-miseq.csv')
equipamiento_df = pd.read_csv('equipamiento-miseq.csv')

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
    
    # Utilizar HTML y JavaScript para crear checkboxes dinámicamente
    for index, row in consumibles_df.iterrows():
        checkbox_id = f'checkbox_{index}'
        st.markdown(f'<input type="checkbox" id="{checkbox_id}" /> {row.to_string(index=False)}', unsafe_allow_html=True)

    # Obtener las filas seleccionadas mediante JavaScript
    selected_rows = st.button("Obtener filas seleccionadas")

    if selected_rows:
        selected_rows = st.execute_script(
            """
            var checkboxes = document.querySelectorAll('input[type="checkbox"]');
            var selectedRows = [];
            checkboxes.forEach(function(checkbox, index){
                if (checkbox.checked) {
                    selectedRows.push(index);
                }
            });
            return selectedRows;
            """
        )
        st.write(f'Se han seleccionado las siguientes filas:')
        for index in selected_rows:
            st.write(consumibles_df.iloc[index].to_frame().T)
        
    st.download_button(
        label="Descargar Consumibles MiSeq",
        data=consumibles_df.to_csv().encode('utf-8'),
        file_name='consumibles_miseq.csv',
        key='consumibles_download'
    )
