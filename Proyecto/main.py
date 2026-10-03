import gradio as gr
import pandas as pd
import ollama as ol
import os
import requests

class RegistroLicencias:
    def __init__(self, db_file="registro_licencias.csv", modelo_ollama="llama3.2"):
        self.db_file = db_file
        self.modelo_ollama = modelo_ollama
        self.datos_licencias()
        
    def datos_licencias(self):
        if not os.path.exists(self.db_file):
            df_licencia = pd.DataFrame(
                columns=[
                    "ID_Licencia",
                    "Titular",
                    "Tipo",
                    "Fecha_Emision",
                    "Fecha_Expiracion",
                    "Estado",
                ]
            )
            df_licencia.to_csv(self.db_file, index=False)
     
    def obtener_info(self):
        if os.path.exists(self.db_file):
            return pd.read_csv(self.db_file)
        return pd.DataFrame()
    
    def guardar_licencia(self, id_lic, titular, tipo, f_emision, f_expiracion, estado):
        df = self.obtener_info()
        if str(id_lic) in df["ID_Licencia"].astype(str).values:
            return (
                f"La licencia con ID {id_lic} ya está registrada.",
                df,
            )
        fila_nueva = pd.DataFrame([{
            "ID_Licencia": id_lic,
            "Titular": titular,
            "Tipo": tipo,
            "Fecha_Emision": f_emision,
            "Fecha_Expiracion": f_expiracion,
            "Estado": estado,
        }])
        df = pd.concat([df, fila_nueva], ignore_index=True)
        df.to_csv(self.db_file, index=False)
        return (
            f"Licencia: {id_lic} registrada para {titular}!",
            df,
        )

    def preguntar_ia(self, mensaje, historial):
        if mensaje is None or not str(mensaje).strip():
            yield "Escribe una pregunta válida para la IA."
            return

        yield "Consultando a la IA y analizando las licencias..."

        df = self.obtener_info()
        contexto_bd = df.to_string(index=False) if not df.empty else "No hay licencias registradas aún en el sistema."

        contexto = f"""
        Eres un analista de datos especializado en licencias.
        Estos son los datos disponibles en el sistema:
        {contexto_bd}

        Instrucciones obligatorias:
        - Responde solo con la información que exista en los datos.
        - Si no hay datos, di claramente que no hay licencias registradas.
        - No inventes IDs, nombres, fechas ni tipos de licencias.
        - Responde de forma breve, clara y amable.
        - Si el usuario pide contar, filtrar o comparar, hazlo solo con la información real del CSV.
        """

        mensajes = [{"role": "system", "content": contexto}]
        historial = historial or []

        for item in historial:
            if isinstance(item, tuple) and len(item) >= 2:
                human, assistant = item
                mensajes.append({"role": "user", "content": str(human)})
                mensajes.append({"role": "assistant", "content": str(assistant)})

        mensajes.append({"role": "user", "content": str(mensaje).strip()})

        try:
            respuesta = ol.chat(
                model=self.modelo_ollama,
                messages=mensajes,
                options={"temperature": 0.1}
            )
            yield respuesta["message"]["content"]
        except Exception as e:
            yield f"Error al conectar con Ollama. Asegúrate de tenerlo abierto y que el modelo '{self.modelo_ollama}' exista. Detalle: {e}"

    # -------- Interfaz Gráfica ----------- :P
    def InterfazGradio(self):
        with gr.Blocks(theme=gr.themes.Soft()) as demo:
            gr.Markdown("# Sistema de Gestión de Licencias")

            with gr.Tabs():
                with gr.Tab("Registrar y ver licencias"):
                    with gr.Row():
                        with gr.Column():
                            gr.Markdown("### Datos de la licencia")
                            in_id = gr.Textbox(label="ID de Licencia", placeholder="Ejemplo: LIC-KAZ2Y5")
                            in_titular = gr.Textbox(label="Titular / Empresa", placeholder="Ingrese su titular aca")
                            in_tipo = gr.Dropdown(["Comercial", "Prueba", "Enterprise"], label="Tipo de Licencia", value="Comercial")
                            in_emision = gr.Textbox(label="Fecha de Emisión de la licencia", placeholder="YYYY-MM-DD")
                            in_expiracion = gr.Textbox(label="Fecha de Expiración", placeholder="YYYY-MM-DD")
                            in_estado = gr.Radio(["Activa", "Expirada"], label="Estado", value="Activa")
                            btn_guardar = gr.Button("Guardar Licencia", variant="primary")

                        with gr.Column():
                            gr.Markdown("### Base de Datos Actual")
                            out_mensaje = gr.Textbox(label="Registro", interactive=False)
                            tabla_licencias = gr.DataFrame(value=self.obtener_info(), interactive=False) 

                            btn_guardar.click(
                                fn=self.guardar_licencia,
                                inputs=[in_id, in_titular, in_tipo, in_emision, in_expiracion, in_estado],
                                outputs=[out_mensaje, tabla_licencias],
                            )
                with gr.Tab("Preguntar a la IA"):
                    gr.ChatInterface(
                        fn=self.preguntar_ia,
                        title=None,
                        description="### Asistente de datos\nEscribe tu pregunta en relación a las licencias registradas en el sistema.",
                        textbox=gr.Textbox(placeholder="Escribe tu pregunta acá :p...", container=False, scale=7),
                        submit_btn="Enviar",
                        chatbot=gr.Chatbot(label="", show_label=False)
                    )
        return demo

if __name__ == "__main__":
    app = RegistroLicencias()
    demo = app.InterfazGradio()
    demo.launch()