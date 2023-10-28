import os
import openai
from flask import Flask, redirect, render_template, request, url_for

class ChatApp:
    def __init__(self):
        self.app = Flask(__name__)
        openai.api_key = "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"
        self.id_Fine_Tune1 = "ft:gpt-3.5-turbo-0613:personal::85HQ9luZ"
        self.id_Fine_Tune2 = "ft:gpt-3.5-turbo-0613:personal::867x2rfm"
        self.id_Fine_Tune3 = "ft:gpt-3.5-turbo-0613:personal::86YIZOge"
        self.app.route("/", methods=("GET", "POST"))(self.index)
   
    def procesar_Formulario(id_Fine_Tune, input_Text):
        response = openai.ChatCompletion.create(
                model=id_Fine_Tune,
                messages=[{"role": "user", "content": input_Text}],
                temperature=1,
                max_tokens=300,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
        return response.choices[0].message.content


    def index(self):
        result = None
        if request.method == "POST":

            if reques.form["formularioResumen"]:
                titulo = request.form["tema"]
                keywords = request.form["keywords"]
                input_text = tema + "." + keywords
                
                result = self.procesar_Formulario(self.id_Fine_Tune2, input_text)

            elif reques.form["formularioKeyword"]:
                titulo = request.form["tema"]
                keywords = request.form["resumen"]
                input_text = titulo + "." + keywords

                result = self.procesar_Formulario(self.id_Fine_Tune2, input_text)

            elif reques.form["formularioTema"]:
                titulo = request.form["resumen"]
                keywords = request.form["keywords"]
                input_text = titulo + "." + keywords

                result = self.procesar_Formulario(self.id_Fine_Tune2, input_text)

            elif:
                result = 'sin resultados'

        return render_template("index.html", result=result)

app_Class  = ChatApp()  # Definir la aplicación Flask globalmente
app = app_Class.app
if __name__ == '__main__':
    app.run()
