import streamlit as st
import requests
import json

def buscar_restaurantes(tipo_comida, presupuesto, ubicacion):
    api_key = "TU_API_KEY"  # Sustituye con tu API Key de Google Places
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    
    params = {
        "query": f"{tipo_comida} restaurants in {ubicacion} within {presupuesto} budget",
        "key": api_key,
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        resultados = data.get("results", [])[:5]  # Tomamos los primeros 5 resultados
        return [(r["name"], r.get("formatted_address", "Dirección no disponible")) for r in resultados]
    else:
        return ["No se pudieron obtener resultados."]

# Configuración de la aplicación
st.title("Recomendador de Restaurantes con IA")
st.write("Encuentra el mejor lugar para comer según tu presupuesto y preferencias.")

# Entradas del usuario
tipo_comida = st.text_input("¿Qué tipo de comida prefieres? (Ej. Sushi, Mexicana, China)")
presupuesto = st.number_input("Presupuesto por persona (USD):", min_value=1, step=1)
ubicacion = st.text_input("Ubicación (Ciudad o Distrito):")

# Botón de búsqueda
if st.button("Buscar Restaurantes"):
    if tipo_comida and presupuesto and ubicacion:
        resultados = buscar_restaurantes(tipo_comida, presupuesto, ubicacion)
        st.write("### Restaurantes recomendados:")
        for nombre, direccion in resultados:
            st.write(f"- **{nombre}** - {direccion}")
    else:
        st.warning("Por favor, completa todos los campos.")

# Sección de cómo funciona
st.header("¿Cómo funciona?")
st.write("""
1. Ingresa el tipo de comida que deseas.
2. Especifica tu presupuesto por persona.
3. Indica la ciudad o distrito donde buscas restaurantes.
4. Presiona el botón "Buscar Restaurantes".
5. Recibirás una lista con las mejores opciones disponibles.
""")
