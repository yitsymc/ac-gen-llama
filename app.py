import streamlit as st
from ollama_interaction import generate_acceptance_criteria

st.title("Sugerencia de Criterios de Aceptación")
st.write(
    "Completa los siguientes campos para sugerir criterios de aceptación a partir de una descripción."
)

with st.form("criteria_form"):
    description = st.text_area(
        "Historia de usuario o descripción de la Tarea:", height=150
    )
    min_criteria = st.number_input(
        "Cantidad mínima de criterios:", min_value=1, max_value=10, value=3
    )
    max_criteria = st.number_input(
        "Cantidad máxima de criterios:", min_value=min_criteria, max_value=10, value=5
    )
    formatting = st.selectbox("Formato de salida:", ["Listado", "Gherkin"])
    submitted = st.form_submit_button("Sugerir criterios")

if submitted:
    with st.spinner("Generando sugerencias..."):
        output_format = "bullet" if formatting == "Listado" else "gherkin"
        output = generate_acceptance_criteria(
            min_criteria, max_criteria, output_format, description
        )
    st.subheader("Criterios sugeridos:")
    st.markdown(output)
