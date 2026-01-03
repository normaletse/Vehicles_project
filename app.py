import plotly.express as px
import pandas as pd
import streamlit as st

st.title('Análisis de vehículos usados')

# cargar datos
df = pd.read_csv('vehicles_us.csv')
df = df.dropna(subset=['price', 'model_year', 'type'])

df['price'] = df['price'].astype(int)
df['model_year'] = df['model_year'].astype(int)

df = df[
    (df['price'] > 0) &
    (df['price'] < 100000) &
    (df['model_year'] >= 1980)
]

st.subheader('Datos después de la limpieza')
st.write('Filas restantes', df.shape[0])


st.sidebar.header('Filtros')

conditions = df['condition'].dropna().unique()
selected_condition = st.sidebar.selectbox(
    'Selecciona la condición',
    conditions
) 

# Filtro por vehiculos
vehicle_types = df['type'].unique()
selected_type = st.sidebar.selectbox(
    'Selecciona el tipo de vehiculo', vehicle_types)

# Filtro por año y modelo
min_year = int(df['model_year'].min())
max_year = int(df['model_year'].max()
               )
selected_year = st.sidebar.slider('Selecciona el año del modelo',
                                  min_year,
                                  max_year,
                                  (min_year, max_year)
                                  )

# Aplicar filtros
filtered_df = df[
    (df['type'] == selected_type) &
    (df['condition'] == selected_condition)&
    (df['model_year'] >= selected_year[0]) &
    (df['model_year'] <= selected_year[1])
]

st. subheader('vista previa del dataset')
st.dataframe(df.head())

st.subheader('Información general del dataset')
st.write('Número de filas:', df.shape[0])
st.write('Número de columnas:', df.shape[1])

st.subheader('Columnas y tipos de datos')
st.write(df.dtypes)

st.subheader('Valores faltantes por columna')
st.write(df.isna().sum())


st.subheader("Precio promedio por tipo de vehículo")

# Calcular precio promedio por tipo
avg_price_by_type = filtered_df.groupby("type")["price"].mean().reset_index()

# Crear gráfica
fig = px.bar(
    avg_price_by_type,
    x="type",
    y="price",
    labels={"type": "Tipo de vehículo", "price": "Precio promedio"},
    title="Precio promedio por tipo de vehículo"
)

# Mostrar gráfica
st.plotly_chart(fig)
