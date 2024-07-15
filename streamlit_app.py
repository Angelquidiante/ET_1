import streamlit as st
import pandas as pd

# Título de la aplicación
st.title('Análisis y Visualización de Datos CSV con Streamlit')

# Cargar archivo CSV
archivo_csv = st.file_uploader("Cargar archivo CSV", type=['csv'])

if archivo_csv is not None:
    # Leer archivo CSV
    df = pd.read_csv(archivo_csv)

    # Mostrar DataFrame en Streamlit
    st.subheader("Vista Previa de los Datos:")
    st.write(df.head())

    # Mostrar resumen estadístico interactivo
    st.subheader("Resumen Estadístico:")
    st.write(df.describe())

    # Gráfico interactivo: Histograma
    st.subheader("Histograma de una Columna:")
    column_for_histogram = st.selectbox('Selecciona una columna para el histograma:', df.columns)
    st.bar_chart(df[column_for_histogram])

    # Gráfico interactivo: Gráfico de dispersión
    st.subheader("Gráfico de Dispersión:")
    x_column = st.selectbox('Selecciona una columna para el eje X:', df.columns)
    y_column = st.selectbox('Selecciona una columna para el eje Y:', df.columns)
    st.line_chart(df[[x_column, y_column]])


    # Gráfico interactivo: Gráfico de barras
    st.subheader("Gráfico de Barras:")
    column_for_bars = st.selectbox('Selecciona una columna para el gráfico de barras:', df.columns)
    st.bar_chart(df[column_for_bars].value_counts())
