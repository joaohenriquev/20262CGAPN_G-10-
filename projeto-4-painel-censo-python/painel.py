# Painel do Censo Escolar 2024 - Projeto 4
# Grupo: João Henrique Viana, Gustavo Del Gilgio e João Vitor Arantes

# carregar o pandas e o streamlit
import pandas as pd
import streamlit as st


### Função ###
# classificar o porte da escola pelo número de matrículas
def classificar_porte(total):
    if total <= 200:
        return "Pequena"
    elif total <= 400:
        return "Média"
    else:
        return "Grande"


### Carregamento dos dados ###
censo = pd.read_csv("escolas_sp_regioes_2024_geo.csv")

# criar a coluna de porte a partir das matrículas
censo["porte"] = censo["matriculas"].apply(classificar_porte)


### Montagem do painel ###
st.set_page_config(page_title="Painel do Censo Escolar 2024", layout="wide")
st.title("Painel de Escolas de Regiões de SP")
st.caption("Adaptado do Censo Escolar 2024 (INEP) - escolas em atividade de 30 municípios")

## Filtros (ficam na barra lateral e vêm antes de tudo)
st.sidebar.header("Filtros")

# filtro 1: região
regiao = st.sidebar.selectbox(
    "Região",
    ["Todas", "Região Metropolitana de SP", "Baixada Santista", "Litoral Norte", "Vale do Ribeira"],
)
if regiao != "Todas":
    censo = censo[censo["regiao"] == regiao]

# filtro 2: dependência administrativa
dependencia = st.sidebar.selectbox(
    "Dependência administrativa",
    ["Todas", "Municipal", "Estadual", "Federal", "Privada"],
)
if dependencia != "Todas":
    censo = censo[censo["dependencia"] == dependencia]

# filtro 3: município (mostra só os municípios que sobraram depois dos filtros acima)
municipios = ["Todos"] + sorted(censo["municipio"].unique())
municipio = st.sidebar.selectbox("Município", municipios)
if municipio != "Todos":
    censo = censo[censo["municipio"] == municipio]

## Indicadores (big numbers)
col1, col2 = st.columns(2)
col1.metric("Total de escolas", f"{len(censo):,}".replace(",", "."))
col2.metric("Total de matrículas", f"{int(censo['matriculas'].sum()):,}".replace(",", "."))

if len(censo) == 0:
    st.warning("Nenhuma escola atende a essa combinação de filtros.")
    st.stop()

## Gráficos de características
st.header("Características das escolas")
col3, col4 = st.columns(2)

col3.subheader("Escolas por porte")
col3.bar_chart(censo["porte"].value_counts())

col4.subheader("Escolas por localização")
col4.bar_chart(censo["localizacao"].value_counts())

## Gráficos de infraestrutura
st.header("Infraestrutura")
col5, col6 = st.columns(2)

col5.subheader("Escolas por abastecimento de água")
col5.bar_chart(censo["agua"].value_counts())

col6.subheader("Escolas por esgotamento sanitário")
col6.bar_chart(censo["esgoto"].value_counts())

## Mapa das escolas
st.header("Mapa das escolas")
st.map(censo[["latitude", "longitude"]].dropna())

## Lista das escolas
st.header("Lista das escolas")
st.dataframe(
    censo[["municipio", "escola", "dependencia", "localizacao", "matriculas", "porte"]],
    hide_index=True,
)
