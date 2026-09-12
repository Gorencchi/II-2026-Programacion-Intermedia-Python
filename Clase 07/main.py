import gradio as gr#Gradio para la construcción de la interfaz
import pandas as pd#Pandas para manejar datos
from Estudiante import Estudiante#Import de la clase Estudiante

estudiantes = []

# Función para agregar un estudiante a la lista y actualizar la tabla y correlación
def agregar_estudiante(nombre, edad, estatura, horas_estudio, calificacion):
    estudiante = Estudiante(
        nombre,
        edad,
        estatura,
        horas_estudio,
        calificacion
    )
    estudiantes.append(estudiante)
    return obtener_estudiantes(), calcular_correlacion(), obtener_estudiantes()

# Función para obtener los estudiantes en un DataFrame
def obtener_estudiantes():
    df = []
    for estudiante in estudiantes:
        df.append(estudiante.__dict__)
    return pd.DataFrame(df)

# Función para calcular la correlación entre las variables numéricas de los estudiantes
def calcular_correlacion():
    if len(estudiantes) < 2:
        return None
    df = obtener_estudiantes()
    correlacion = df.corr(numeric_only=True)
    correlacion.insert(
        0,
        "Variable",
        correlacion.index
    )
    return correlacion.reset_index(drop=True)
# Construcción de la interfaz con Gradio
with gr.Blocks() as app:
    gr.Markdown("<h1 style='text-align: center;'>Sistema de Estudiantes</h1>")
    with gr.Row():
        with gr.Column():
            gr.Markdown("## Agregar Estudiante")
            nombre = gr.Textbox(label="Nombre")
            edad = gr.Number(label="Edad")
            estatura = gr.Number(label="Estatura")
            horas_estudio = gr.Number(label="Horas de Estudio")
            calificacion = gr.Number(label="Calificación")
            boton = gr.Button("Agregar estudiante", variant="primary")
        with gr.Column():
            gr.Markdown("## Lista de Estudiantes")
            tabla = gr.DataFrame(value=obtener_estudiantes())
    with gr.Row():
        with gr.Column():
            # Correlacion
            gr.Markdown("## Correlaciones")
            correlacion = gr.DataFrame(
                value=calcular_correlacion()
            )

        # Grafico de correlaciones
        with gr.Column():
            gr.Markdown("### Gráfico de dispersión")
            scatter_plot = gr.ScatterPlot(
                value=obtener_estudiantes(),
                x="horas_estudio",
                y="calificacion",
                x_lim = [0, 20],
                y_lim = [0, 100],
            )
    boton.click(
        fn=agregar_estudiante,
        inputs=[
            nombre,
            edad,
            estatura,
            horas_estudio,
            calificacion
        ],
        outputs=[tabla, correlacion, scatter_plot]
    )

app.launch()