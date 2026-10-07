import streamlit  as st 


st.set_page_config(page_title="Brasa & Pão - Painel SLQ", layout="wide")

st.navigation([
    st.Page("Paginas/inicio.py", title="Inicio", default=True),
    st.Page("Paginas/nivel_1.py", title= "Nivel 1 - Aquecimento"),
    st.Page("Paginas/nivel_2.py", title="Nivel 2 - Join"),
    st.Page("Paginas/nivel_3.py", title= "Nivel 3 - Desafio")

    
]).run() 
