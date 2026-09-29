import gradio as gr
import pandas as pd
import ollama as ol
import os
import requests

class RegistroLicencias:
    def __init__(self, db_file="registro_licencias.csv", modelo_ollama="llama3"):
        self.db_file = db_file
        self.modelo_ollama = modelo_ollama
        
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
            df,)
    def ia(self, prompt_user):
        respuesta = ol.chat(
            model=self.modelo_ollama,
            messages=[{"role": "user", "content": prompt_user}],
        )
        return respuesta["message"]["content"]
        
#--------Interfaz-----------
    def InterfazGradio(self):
        with gr.Blocks(theme=gr.Theme.from_hub("Ruby-NewLeaf/MaybeRedsLikeRoses-Theme")) as demo:
            gr.Markdown("# Sistema de Gestión de Licencias")

            with gr.Tab("Registrar y ver licencias"):
                with gr.Row():
                    with gr.Column():
                        gr.Markdown("### Datos de la licencia")
                        in_id = gr.Textbox(
                  label="ID de Licencia", placeholder="Ejemplo: LIC-KAZ2Y5"
                )
                        in_titular = gr.Textbox(
                  label="Titular / Empresa", placeholder="Ingrese su titular aca"
                )
                        in_tipo = gr.Dropdown(
                  ["Comercial", "Educativa", "Prueba", "Enterprise"],
                  label="Tipo de Licencia",
                  value="Comercial",
                )
                        in_emision = gr.Textbox(
                  label="Fecha de Emisión de la licencia", placeholder="YYYY-MM-DD"
                )
                        in_expiracion = gr.Textbox(
                  label="Fecha de Expiración de la licencia", placeholder="YYYY-MM-DD"
                )
                        in_estado = gr.Radio(
                  ["Activa", "Suspendida", "Expirada"],
                  label="Estado",
                  value="Activa",
                )
                        btn_guardar = gr.Button("Guardar Licencia", variant="primary")

                    with gr.Column():
                        gr.Markdown("### Base de Datos Actual")
                        out_mensaje = gr.Textbox(
                  label="Estado de la Operación", interactive=False
              )
                        tabla_licencias = gr.DataFrame(
                  value=self.obtener_info(), interactive=False
                ) 
                        btn_guardar.click(
                fn=self.guardar_licencia,
                inputs=[
                  in_id,
                  in_titular,
                  in_tipo,
                  in_emision,
                  in_expiracion,
                  in_estado,
              ],
                outputs=[out_mensaje, tabla_licencias],
          )
            return demo


if __name__ == "__main__":
  app = RegistroLicencias()
  demo = app.InterfazGradio()
  demo.launch()