import streamlit as st
from projects import project1
from pathlib import Path

st.set_page_config(
    page_title="Data Science Portfolio",
    page_icon="📊",
    # layout="wide"
)

# menu = st.sidebar.radio(
#     "Navegación",
#     ["Inicio", "Proyectos", "Sobre mí", "Contacto"]
# )

# if menu == "Inicio":

st.title("Feliciano Rodríguez López")
st.subheader("Data Scientist")

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
# st.write("""
# Bienvenido a mi portafolio de Data Science.

# Aquí presento proyectos donde aplico análisis de datos,
# modelado predictivo y herramientas del ecosistema de
# ciencia de datos para resolver problemas reales.
# """)

st.write("### Habilidades principales")

# st.write("- 🐍 Python")
# st.write("- 🗄 SQL")
assets_images = Path(__file__).parent / "assets" / "images"

skills = [
    ("Python", assets_images / "python-svgrepo-com.svg"),
    ("SQL", assets_images / "sql-database-generic-svgrepo-com.svg"),
]

for skill_name, skill_icon in skills:
    col_icon, col_name = st.columns([1, 14])
    with col_icon:
        st.image(str(skill_icon), width=26)
    with col_name:
        st.write(skill_name)

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.write("🐍 Python")

# with col2:
#     st.write("🗄 SQL")

# with col3:
#     st.write("📊 Data Analysis")


# elif menu == "Proyectos":

st.title("Proyectos")

# project_option = st.selectbox(
#     "Selecciona un proyecto",
#     [
#         "Análisis de preferencias de pasajeros (Zuber)",
#     ]
# )

# if project_option == "Análisis de preferencias de pasajeros (Zuber)":
#     project1.show()
projects = [
    {
        "title": "Análisis de preferencias de pasajeros (Zuber)",
        "summary": "Análisis de datos de una empresa de viajes compartidos para identificar patrones de comportamiento de pasajeros.",
        "tags": ["Python", "SQL", "Pandas"],
        "module": project1,
    },
    # añade más proyectos aquí
]

for project in projects:
    with st.container(border=True):
        st.subheader(project["title"])
        st.write(project["summary"])
        st.write(" ".join([f"`{t}`" for t in project["tags"]]))
        with st.expander("Ver detalles"):
            project["module"].show()


# elif menu == "Sobre mí":


# elif menu == "Contacto":

st.title("Contacto")

st.write("Puedes encontrarme en:")

st.markdown("[LinkedIn](https://www.linkedin.com/in/feliciano-rodriguez/)")
st.markdown("[GitHub](https://github.com/FelicianoRodriguez)")
st.markdown("📧 felicianorodriguezlp@gmail.com")
