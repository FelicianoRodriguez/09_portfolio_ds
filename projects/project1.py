import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path


def show():

    st.header("Análisis de preferencias de pasajeros")

    st.subheader("Descripción del proyecto")

    st.write("""
    Este proyecto analiza datos de viajes de una empresa ficticia
    de transporte compartido llamada Zuber en Chicago.

    El objetivo fue identificar patrones en la información de
    viajes para comprender las preferencias de los pasajeros y
    analizar cómo factores externos pueden influir en la demanda
    del servicio.

    Durante el proyecto realicé análisis exploratorio de datos,
    limpieza del dataset y visualización de patrones relevantes
    que ayudan a entender el comportamiento de los usuarios.
    """)

    st.subheader("Tecnologías utilizadas")

    st.write("""
             - SQL
    - Python
    - Pandas
    - NumPy
    - Matplotlib
    - Seaborn
    - Jupyter Notebook
    """)

    # st.subheader("Evidencias visuales")

    # st.image("assets/images/project1_eda.png")
    # st.image("assets/images/project1_model.png")
    # Vamos a estudíar el dataset

    # df_01 = pd.read_csv('data/project_sql_result_01.csv')
    # df_04 = pd.read_csv('data/project_sql_result_04.csv')

    st.subheader("Viajes totales de las compañias de taxi de Chicago")

    data_dir = Path(__file__).resolve().parent.parent / "data"
    df_01 = pd.read_csv(data_dir / "project_sql_result_01.csv")

    # Si quieres Top 10, ordena y toma 10
    top_10 = df_01.sort_values("trips_amount", ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(data=top_10, x="company_name", y="trips_amount", ax=ax)

    ax.set_title("Viajes totales por empresa")
    ax.set_xlabel("Compañías de taxi")
    ax.set_ylabel("Número de viajes")
    ax.tick_params(axis="x", rotation=90)

    st.pyplot(fig)
    plt.close(fig)

    st.subheader(
        "Top 10 principales barrios en terminos de finalización de recorrido")

    data_dir_2 = Path(__file__).resolve().parent.parent / "data"
    df_04 = pd.read_csv(data_dir_2 / "project_sql_result_04.csv")

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(data=df_04.head(10),
                x='dropoff_location_name', y='average_trips')
    ax.set_title("Promedio de viajes con finalización en los barrios")
    ax.set_xlabel("Barrios de Chicago")
    ax.set_ylabel("Promedio de barrios")
    ax.tick_params(axis="x", rotation=90)

    st.pyplot(fig)
    plt.close(fig)

    st.subheader("Código fuente")

    st.markdown(
        "[Ver proyecto en GitHub](https://github.com/FelicianoRodriguez/tripleten-projects/tree/main/08_zeros)")
