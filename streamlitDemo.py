import streamlit as st
import pandas as pd
import plotly.express as px

# Configurar la página para hacerla más amigable en móviles
st.set_page_config(page_title="Precio del Oro", layout="wide")

# Título de la aplicación
st.title("Visualización de Series Temporales: Precios del Oro")

# Cargar el archivo CSV
@st.cache
def load_data():
    data = pd.read_csv('gold_price_history.csv', parse_dates=['Date'])
    data.set_index('Date', inplace=True)
    return data

# Cargar los datos
data = load_data()

# Mostrar los datos cargados
st.write("Datos cargados (muestra de 5 filas):")
st.dataframe(data.head())

# Crear un gráfico interactivo con Plotly
st.subheader("Gráfico de Serie Temporal del Precio del Oro (Cierre Ajustado)")
fig = px.line(data, x=data.index, y='Adj Close', title='Precio de Cierre Ajustado del Oro')
fig.update_layout(
    xaxis_title="Fecha",
    yaxis_title="Precio de Cierre Ajustado",
    margin=dict(l=0, r=0, t=50, b=50),  # Márgenes optimizados para dispositivos móviles
    height=600  # Altura del gráfico
)
st.plotly_chart(fig, use_container_width=True)

# Opción para descargar los datos filtrados
csv_data = data.to_csv().encode('utf-8')
st.download_button("Descargar CSV", csv_data, 'gold_price_history.csv', "text/csv")