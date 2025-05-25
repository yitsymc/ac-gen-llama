# ac-gen-llama
**ac-gen-llama** es una aplicación interactiva desarrollada con Streamlit que sugiere **criterios de aceptación** para historias de usuario ágiles. Utiliza el modelo **Llama3.2** ejecutado localmente a través de [Ollama](https://ollama.com/) para generar criterios en formatos estructurados como **Gherkin** o en formato de **lista con viñetas**.

---

## Función

Dado un resumen o descripción de una historia de usuario, sugiere criterios de aceptación automáticamente, ayudando a equipos de desarrollo a mejorar la claridad y definición de sus tareas.

---

## Estructura
**app.py**: Proporciona una interfaz sencilla en la que el usuario introduce una descripción, elige el rango de criterios y el formato deseado.

**ollama_interaction.py**: Genera el prompt dinámicamente y utiliza ChatPromptTemplate junto con el modelo llama3.2 de Ollama para obtener los criterios de aceptación en el formato solictado:
* Gherkin: Estructura tipo Given/When/Then (https://karaleise.com/writing-user-stories-in-gherkin-format).
* Listado: Lista clara de criterios con viñetas.


## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener:

1. **Python 3.11 o superior**
2. **[Ollama](https://ollama.com) instalado** en tu máquina
3. El modelo **Llama3.2** descargado y corriendo localmente (https://ollama.com/library/llama3.2):

```bash
ollama run llama3.2
```

## Ejecución
1. Clona el repositorio.
2. Instala las dependencias:
```bash
pip install -r requirements.txt
```
3. Inicia el servidor de Streamlit.

## Licencia
MIT
