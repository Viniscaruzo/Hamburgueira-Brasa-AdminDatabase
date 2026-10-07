import streamlit as st 
import pandas as pd
import re

from sqlalchemy import create_engine, text 
from urllib.parse import quote_plus

SERVIDOR = r"D18S22-1252889\VINI_BANCO"
BANCO = "HamburgueriaBrasa"
DRIVE = "ODBC Driver 18 for SQL Server"

#Outro metodo de Login
Usuario = "sa"
Senha= "Senai@134"



def conectar():
    # AAutenticação via windows utilizando ODBC

    odbc = (
        f"DRIVER={{{DRIVE}}};SERVER={SERVIDOR};DATABASE={BANCO};"
        f"UID={Usuario};PWD={Senha};" 
        "TrustServerCertificate=yes"
    )

    return create_engine("mssql+pyodbc:///?odbc_connect="+ quote_plus (odbc))

def consultar(sql):
    """ Executa a consulta no sql server e devolve o resultado como tabela"""
    with conectar().connect() as conexao:
        return pd.read_sql(text(sql), conexao)


def mensagem_erro(erro):
    """Tira só a mensagem do SQL Server do meio do texto do erro."""
    achou = re.search(r"\[SQL Server\](.+?)\s*\(\d+\)", str(erro))
    return achou.group(1) if achou else str(erro)