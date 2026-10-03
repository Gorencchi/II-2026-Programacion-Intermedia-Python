import gradio as gr
import ollama as ol

class Asistente_videojuegos():
    def __init__(self, modelo_ollama="llama3.2"):
        self.modelo_ollama = modelo_ollama.strip().replace(" ", "")

    def recomendaciones_videojuegos(self, tema):
        if not tema or not tema.strip():
            return "Escriba un genero o tipo de videojuegos valido"

        system_prompt = (
            "Eres una asistente virtual llamada Miku destinada a recomendar videjuegos relacionados a las preferencias del usuario, responde de manera coherente. "
            "Tus reglas son: 1. Recomienda unicamente 3 videojuegos al usuario segun sus preferencias. 2. Recomienda videojuegos en Español o que tengan traduccion al Español. 3. No respondas de forma extensa, responde brevemente."
        )
        user_prompt = f"Quiero que me recomiendes videojuegos sobre el siguiente tema: {tema.strip()}"

        try:
            respuesta = ol.chat(
                model=self.modelo_ollama,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )
            return respuesta["message"]["content"]
        except Exception as e:
            return f"Error al conectar con Ollama: {e}"

    def interfazgradio(self):
        with gr.Blocks(theme=gr.Theme.from_hub("mkill33/HALO")) as demo:
            gr.Markdown("## Asistente Miku, recomendación de videojuegos")

            with gr.Column():
                in_tema = gr.Textbox(
                    label="Escribe acá tu género de videojuegos",
                    placeholder="Ejemplo: [Terror, Shooter, RPG...]",
                )

            boton = gr.Button("Recomendar", variant="primary")
            recomendacion = gr.Textbox(
                label="Recomendaciones dadas por Miku",
                interactive=False,
            )
            boton.click(
                fn=self.recomendaciones_videojuegos,
                inputs=[in_tema],
                outputs=[recomendacion],
            )
        return demo

if __name__ == "__main__":
    app = Asistente_videojuegos()
    demo = app.interfazgradio()
    demo.launch()