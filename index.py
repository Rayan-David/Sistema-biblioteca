import streamlit as st
import random

st.title("Sistema de biblioteca")

#Criar lista de livros
if "livros" not in st.session_state:
    st.session_state.livros = []
    
#Cadastrar livro
st.header("Cadastrar Livro")
nome_livro = st.text_input("Nome do Livro")
autor = st.text_input("Autor")

#Botão cadastrar
if st.button("Cadastrar Livro"):

    if nome_livro != "" and autor != "":
        livro = {
            "nome": nome_livro,
            "Autor": autor,
            "Emprestado": False
        }
        st.session_state.livros.append(livro)
        st.success("Livro cadastrado com sucesso!")      
