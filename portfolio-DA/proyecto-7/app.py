import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Proyecto 7 - Herramientas de Desarrollo de Software')


hist_button = 
('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón

# escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches puede ver la base de datos en mi Git Hub https://github.com/lozaner/notebooks/tree/main')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)