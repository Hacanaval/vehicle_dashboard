import streamlit as st
import pandas as pd
import plotly.express as px

# Cargamos el dataset
car_data = pd.read_csv('vehicles_us.csv')

# Creamos un encabezado en Streamlit
st.header('Dashboard de Anuncios de Autos')

# Casilla de verificación para el histograma
build_histogram = st.checkbox('Mostrar histograma del kilometraje')

if build_histogram:  
    st.write('Histograma del kilometraje de los autos')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig)

# Casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Mostrar gráfico de dispersión')

if build_scatter:  
    st.write('Gráfico de dispersión para la relación entre odómetro y precio')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Relación entre odómetro y precio")
    st.plotly_chart(fig_scatter, use_container_width=True)
