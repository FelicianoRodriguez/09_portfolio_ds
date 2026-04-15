import streamlit as st


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
    - Python
    - Pandas
    - NumPy
    - Matplotlib
    - Seaborn
    - Jupyter Notebook
    """)

    st.subheader("Evidencias visuales")

    # st.image("assets/images/project1_eda.png")
    # st.image("assets/images/project1_model.png")

    st.subheader("Código fuente")

    st.markdown("[Ver proyecto en GitHub](https://github.com/tu-repo)")
