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
	
    def index(self):
        if request.method == "POST":
            titulo = request.form["titulo"]
            keywords = request.form["keywords"]
            input_text = titulo + "." + keywords
            response = openai.ChatCompletion.create(
                model=self.id_Fine_Tune1,
                messages=[{"role": "user", "content": input_text}],
                temperature=1,
                max_tokens=300,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            result = response.choices[0].message.content
            return redirect(url_for("index", result=result))

        result = request.args.get("result")
        return render_template("index.html", result=result)



if __name__ == '__main__':
    app = ChatApp()
    app.app.run()
