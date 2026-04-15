import streamlit as st
from projects import project1

st.set_page_config(
    page_title="Data Science Portfolio",
    page_icon="📊",
    layout="wide"
)

menu = st.sidebar.radio(
    "Navegación",
    ["Inicio", "Proyectos", "Sobre mí", "Contacto"]
)

if menu == "Inicio":

    st.title("Feliciano Rodríguez López")
    st.subheader("Data Scientist")

    st.write("""
    Bienvenido a mi portafolio de Data Science.

    Aquí presento proyectos donde aplico análisis de datos,
    modelado predictivo y herramientas del ecosistema de
    ciencia de datos para resolver problemas reales.
    """)

    st.write("### Habilidades principales")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("🐍 Python")

    with col2:
        st.write("🗄 SQL")

    with col3:
        st.write("📊 Data Analysis")


elif menu == "Proyectos":

    st.title("Proyectos")

    project_option = st.selectbox(
        "Selecciona un proyecto",
        [
            "Análisis de preferencias de pasajeros (Zuber)",
        ]
    )

    if project_option == "Análisis de preferencias de pasajeros (Zuber)":
        project1.show()


elif menu == "Sobre mí":

    st.title("Sobre mí")

    st.write("""
    Soy Data Scientist en formación con background en ingeniería
    de software. Me especializo en el análisis de datos con Python
    y SQL para descubrir patrones, generar insights y apoyar la
    toma de decisiones basadas en datos.

    Actualmente desarrollo proyectos de análisis y machine learning
    trabajando con datasets reales y herramientas del ecosistema
    de Data Science.
    """)


elif menu == "Contacto":

    st.title("Contacto")

    st.write("Puedes encontrarme en:")

    st.markdown("[LinkedIn](https://linkedin.com)")
    st.markdown("[GitHub](https://github.com)")
    st.markdown("📧 felixidf@gmail.com")
