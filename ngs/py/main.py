import pandas as pd
import streamlit as st

# Cargar los archivos CSV en DataFrames
consumibles_df = pd.read_csv('consumibles-miseq.csv')
equipamiento_df = pd.read_csv('equipamiento-miseq.csv')

# Título para el costo parcial
st.title('Modulo de NGS')



# Resumen de la justificación
resumen_texto = """
**Proyecto**

El proyecto "Aplicación de un panel multigénico para la búsqueda de variantes genéticas de riesgo en cáncer de mama/ovario hereditario desde el ámbito de la Salud Pública" del Instituto de Genética Humana de Misiones (IGeHM) está en desarrollo. Bajo la dirección de la Dra. Roxana Cerrtini, Jefa del Cenagen, el proyecto tiene dos objetivos principales.

Primero, busca ofrecer asesoramiento genético temprano para pacientes y sus familias, permitiendo la implementación de una clínica personalizada mediante la detección de variantes genéticas en genes asociados al cáncer hereditario. Segundo, busca evaluar la frecuencia y distribución de las variantes de riesgo, proporcionando conocimiento sobre la epidemiología de diferentes genes de susceptibilidad al cáncer hereditario.

El diagnóstico molecular de cáncer de mama/cáncer de ovario es posible a través de la identificación de variantes genéticas utilizando técnicas de secuenciación masiva (NGS). Este proyecto es destacado por ser pionero en el ámbito de la Salud Pública en Argentina, ya que propone la aplicación de un panel multigénico más extenso y preciso a un costo significativamente menor, asegurando la igualdad de acceso para la población en riesgo.
"""

# Mostrar el resumen en la aplicación
st.title("Justificación de los Equipos Pedidos")
st.markdown(resumen_texto)

# ... (más código de tu aplicación)


# Título para el costo parcial
st.title('Consumibles Miseq')
# Crear botones para mostrar y descargar los DataFrames
if st.button('Mostrar y Descargar Consumibles MiSeq'):
    st.title('Consumibles MiSeq')
    st.write('Datos de consumibles:')
    st.write(consumibles_df)
    st.download_button(
        label="Descargar Consumibles MiSeq",
        data=consumibles_df.to_csv().encode('utf-8'),
        file_name='consumibles_miseq.csv',
        key='consumibles_download'
    )

# Título para el costo parcial
st.title('Equipamientos Miseq')
if st.button('Mostrar y Descargar Equipamiento MiSeq'):
    st.title('Equipamiento MiSeq')
    st.write('Datos de equipamiento:')
    st.write(equipamiento_df)
    st.download_button(
        label="Descargar Equipamiento MiSeq",
        data=equipamiento_df.to_csv().encode('utf-8'),
        file_name='equipamiento_miseq.csv',
        key='equipamiento_download'
    )

# Título para el costo parcial
st.title('Costo Parcial')

# Solicitar al usuario el costo de análisis de NGS
costo_analisis_ngs = st.number_input('Ingrese el costo de análisis de NGS (en USD)')

# Calcular la suma total de equipamiento MiSeq
suma_total_equipamiento = equipamiento_df['Precio en USD'].sum() + costo_analisis_ngs

# Obtener el número de pacientes
num_pacientes = st.number_input('Ingrese el número de pacientes')

# Calcular el costo por paciente
costo_por_paciente = suma_total_equipamiento / num_pacientes

# Mostrar la suma total de equipamiento y el costo por paciente
st.write(f'Suma total de equipamiento MiSeq: {suma_total_equipamiento} USD')
st.write(f'Costo por paciente: {costo_por_paciente} USD')