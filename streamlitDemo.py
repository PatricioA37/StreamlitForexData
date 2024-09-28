import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Definir los pares de divisas
currency_pairs = {
    'EUR/USD': 'EURUSD=X',
    'GBP/USD': 'GBPUSD=X',
    'USD/JPY': 'USDJPY=X',
    'USD/CHF': 'USDCHF=X',
    'AUD/USD': 'AUDUSD=X'
}

# Configurar la página para hacerla más amigable en móviles
st.set_page_config(page_title="Precio de Divisas", layout="wide")

# Crear una lista desplegable para seleccionar la divisa
selected_currency = st.selectbox("Selecciona un par de divisas:", list(currency_pairs.keys()))

# Crear una lista desplegable para seleccionar el tipo de datos a visualizar
data_type = st.selectbox("Selecciona el tipo de datos:", ["Datos Originales", "Datos con Indicadores"])

# Generar el nombre del archivo CSV correspondiente basado en la selección
if data_type == "Datos Originales":
    csv_filename = f"{currency_pairs[selected_currency].replace('=', '_').lower()}.csv"
else:
    csv_filename = f"{currency_pairs[selected_currency].replace('=', '_').lower()}_with_indicators.csv"

# Verificar si el archivo CSV existe
if os.path.exists(csv_filename):
    # Cargar los datos del archivo CSV
    data = pd.read_csv(csv_filename)

    # Mostrar los datos en la aplicación
    st.write(f"Datos para {selected_currency} ({data_type}):")
    st.dataframe(data)

    # Ejemplo de visualización con Plotly (ejemplo para 'Close')
    fig = px.line(data, x=data.index, y='Close', title=f'Precio de Cierre de {selected_currency}')
    st.plotly_chart(fig)

    # Si se seleccionaron indicadores, agregar gráficos para los indicadores
    if data_type == "Datos con Indicadores":
        # Graficar RSI
        if 'RSI' in data.columns:
            fig_rsi = px.line(data, x=data.index, y='RSI', title=f'RSI de {selected_currency}')
            st.plotly_chart(fig_rsi)

        # Graficar MACD
        if 'MACD' in data.columns:
            fig_macd = px.line(data, x=data.index, y='MACD', title=f'MACD de {selected_currency}')
            st.plotly_chart(fig_macd)

        # Graficar Bollinger Bands
        if 'Upper_BB' in data.columns and 'Lower_BB' in data.columns:
            fig_bb = px.line(data, x=data.index, y=['Upper_BB', 'Lower_BB'], title=f'Bollinger Bands de {selected_currency}')
            st.plotly_chart(fig_bb)

else:
    st.error(f"No se encontró el archivo CSV para {selected_currency}. Asegúrate de que los datos se hayan descargado correctamente.")
