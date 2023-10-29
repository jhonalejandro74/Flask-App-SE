import openai
from flask import Flask, render_template, request
from openAI_MODELS import models

class ChatApp:
    def __init__(self):
        self.app = Flask(__name__)
        openai.api_key = "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"
        self.id_Fine_Tune_Resumen = models.resumen_model
        self.id_Fine_Tune_Keywords = models.keywords_model
        self.id_Fine_Tune_Tema = models.tema_model
        self.app.route("/", methods=("GET", "POST"))(self.index)
   
    def procesar_Formulario(self,id_Fine_Tune, input_Text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system","content": id_Fine_Tune['system']},
                {"role": "user","content": id_Fine_Tune['user']},
                {"role": "assistant","content": id_Fine_Tune['assistant']},
                {"role": "user","content": input_Text}
                ],
            
            temperature=1,
            max_tokens=300,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0)
        return response.choices[0].message.content


    def index(self):
        result = None
        if request.method == "POST":
            if request.form.get("formularioResumen"):
                tema = request.form["tema"]
                keywords = request.form["keywords"]
                input_text = tema + " - " + keywords
                
                result = self.procesar_Formulario(self.id_Fine_Tune_Resumen, input_text)

            elif request.form.get("formularioKeyword"):
                titulo = request.form["tema"]
                keywords = request.form["resumen"]
                input_text = titulo + " - " + keywords

                result = self.procesar_Formulario(self.id_Fine_Tune_Keywords, input_text)

            elif request.form.get("formularioTema"):
                titulo = request.form["resumen"]
                keywords = request.form["keywords"]
                input_text = titulo + " - " + keywords

                result = self.procesar_Formulario(self.id_Fine_Tune_Tema, input_text)

            else:
                result = 'sin resultados'

        return render_template("index.html", result=result)

app_Class  = ChatApp()  # Definir la aplicación Flask globalmente
app = app_Class.app
if __name__ == '__main__':
    app.run()
