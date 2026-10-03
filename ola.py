import gradio as gr
import ollama as ol

class AsistenteLibreria:
    def __init__(self, modelo_ollama="llama3.2"):
        self.modelo_ollama = modelo_ollama

    def recomendar_libros(self, tema):
        if not tema.strip():
            return "Por favor, escribe un tema o género válido."
            
        system_prompt = (
            "Eres el asistente virtual experto de una librería. "
            "Tus reglas son: 1. Responde siempre en español. "
            "2. Recomienda exactamente dos libros relacionados con el tema solicitado por el usuario."
        )
        
        user_prompt = f"Quiero que me recomiendes libros sobre el siguiente tema o género: {tema}"

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
            return f"Error al conectar con Ollama. Asegúrate de tenerlo abierto. Detalle: {e}"

    def InterfazGradio(self):
        with gr.Blocks() as demo:
            gr.Markdown("# Asistente Virtual para Librería")

            with gr.Row():
                with gr.Column():
                    in_tema = gr.Textbox(
                        label="Tema o género de interés",
                        placeholder="Ejemplo: misterio, historia, ciencia ficción..."
                    )
                    btn_recomendar = gr.Button("Recomendar", variant="primary")

                with gr.Column():
                    out_recomendacion = gr.Textbox(
                        label="Recomendación de la librería",
                        interactive=False
                    )

                    btn_recomendar.click(
                        fn=self.recomendar_libros,
                        inputs=[in_tema],
                        outputs=[out_recomendacion]
                    )

        return demo

if __name__ == "__main__":
    app = AsistenteLibreria()
    demo = app.InterfazGradio()
    demo.launch()