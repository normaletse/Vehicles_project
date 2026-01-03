import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Limpieza básica
car_data = car_data.dropna(subset=['odometer', 'price', 'model_year'])
car_data['model_year'] = car_data['model_year'].astype(int)

# Encabezado
st.header('Análisis de anuncios de venta de vehículos')

st.write(
    'Esta aplicación web permite analizar anuncios de venta de vehículos '
    'utilizando gráficos interactivos.'
)

# Botón para histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el odómetro de los vehículos')

    fig_hist = px.histogram(
        car_data,
        x='odometer',
        title='Distribución del odómetro'
    )

    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión: precio vs año del modelo')

    fig_scatter = px.scatter(
        car_data,
        x='model_year',
        y='price',
        title='Precio según el año del modelo'
    )

    st.plotly_chart(fig_scatter, use_container_width=True)

