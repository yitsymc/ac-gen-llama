from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

GHERKIN_FORMAT_ES: str = """
    Usa el formato **Gherkin: Given / When / Then** para cada criterio. \n
    
    Ejemplo de entrada: \n
    Historia de usuario: *Como comprador en línea, quiero poder filtrar productos por precio, 
    para encontrar opciones dentro de mi presupuesto.* \n
    
    Ejemplo de salida:
    1. **Dado** que el usuario está en la página de resultados, **Cuando** selecciona un rango de precios, **Entonces** solo se deben mostrar los productos dentro de ese rango.  
    2. **Dado** que el usuario elimina los filtros de precio, **Cuando** se actualiza la página, **Entonces** todos los productos deben ser visibles nuevamente.  
    3. **Dado** que el usuario establece un filtro con un valor mínimo mayor al máximo, **Cuando** aplica el filtro, **Entonces** debe mostrarse un mensaje de error claro. 
"""

BULLET_POINT_FORMAT_ES = """
    Genera una lista clara y precisa de criterios de aceptación como una lista de requisitos simples (bullet points), 
    NO en formato Gherkin. \n
    Formato de salida:
        - [criterio 1]
        - [criterio 2]
        - [criterio 3]
        - ...
"""

PROMPT_TEMPLATE_AC_GENERATOR_ES = """
    Actúa como un generador experto de *Acceptance Criteria* (criterios de aceptación) 
    para historias de usuario. \n
    Toma como entrada una historia de usuario o una descripción funcional 
    y genera entre %s y %s criterios de aceptación siguiendo estas mejores prácticas:
    - Sé **específico y medible**: define claramente qué se debe lograr y cómo se verifica.
    - Usa **lenguaje claro y sin ambigüedades**.
    - Enfócate en el **valor para el usuario**.
    - Asegúrate de que los criterios sean **comprobables mediante pruebas**.
    - Imagina que los criterios fueron definidos **en colaboración con stakeholders** 
    (product owner, desarrolladores, QA).
    
    No incluyas explicaciones, solamente devuelve los criterios en el formato especificado.
    ---
    Historia de usuario o funcionalidad: %s.

"""


def generate_acceptance_criteria(
    min_criteria: int, max_criteria: int, formatting: str, description: str
):
    """
    Generates a list of acceptance criteria based on a given description using an LLM-powered prompt chain.

    :param min_criteria: Minimum number of acceptance criteria to generate.
    :param max_criteria: Maximum number of acceptance criteria to generate.
    :param formatting: Desired formatting style for the output. Supported values are:
                       'gherkin' for Gherkin syntax or 'bullet' for bullet-point list.
    :param description: A textual description of the user story or feature to generate acceptance criteria for.
    :return: A string containing the generated acceptance criteria formatted according to the specified style.
    """
    format_template_map = {
        "gherkin": GHERKIN_FORMAT_ES,
        "bullet": BULLET_POINT_FORMAT_ES,
    }
    template = PROMPT_TEMPLATE_AC_GENERATOR_ES % (
        min_criteria,
        max_criteria,
        description,
    )
    if formatting in format_template_map:
        template += f"\n {format_template_map[formatting]}"

    prompt_template = ChatPromptTemplate.from_template(template)

    ollama_model = OllamaLLM(model="llama3.2")
    chain = prompt_template | ollama_model
    response = chain.invoke({"question": description})
    return response
