import streamlit as st
import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
	host='localhost',
	user=st.secrets["db_username"],
	password=st.secrets["db_password"],
	database=st.secrets["db_name"]
)

def carregarVagas():
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM Vaga")
	v = cursor.fetchall()
	colunas = [desc[0] for desc in cursor.description]
	v = pd.DataFrame(v, columns=colunas)
	return v

df= carregarVagas()
st.dataframe(df)

with st.sidebar:
	st.title("Configurações")
	st.selectbox("Escolha uma cidade: ", ['Rio Claro', 'São Paulo'])

with st.form("Cadastro"):
	st.title("Cadastro de usuários")
	nome = st.text_input("Nome: ")
	senha = st.text_input("Senha: ", type="password")
	num = st.slider("Escolha um número: ", 1, 10)
	color = st.selectbox("Escoha uma cor:", ['vermelho', 'laranja', 'azul', 'verde'])
	tipo_contrato = st.multiselect("Cidade", df['tipo_contratacao'].unique())
	submit = st.form_submit_button("Enviar")

st.write(nome)

st.write(st.secrets["db_name"])



