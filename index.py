import streamlit as st
import random

st.title("Sistema de biblioteca")

#Criar lista de livros
if "livros" not in st.session_state:
    st.session_state.livros = []
    
#Cadastrar livro
st.header("Cadastrar Livro")