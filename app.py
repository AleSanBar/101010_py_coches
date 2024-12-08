import streamlit as st
import pandas as pd
import plotly.express as px

# leer los datos
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

# título de la aplicación
st.title('Análisis de Datos de Vehículos Usados')

# Descripci[on
st.write('Esta aplicación permite visualizar datos de vehículos usados mediante histográmas y gráficos de dispersión.')

# Crear casillas de verificación para seleccionar el ripo de gráfico
show_histogram = st.checkbox('Mostrar Histograma')
show_scatter = st.checkbox('Mostrar Gráfico de Dispersión')

# Mostrar histograma si el checkbox está seleccionado
if show_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
    
# Mostrar gráfico de dispersión si el checkbox está seleccionado
if show_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

