import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = "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"

id_Fine_Tune1 = "ft:gpt-3.5-turbo-0613:personal::85HQ9luZ"
id_Fine_Tune2 = "ft:gpt-3.5-turbo-0613:personal::867x2rfm"
id_Fine_Tune3 = "ft:gpt-3.5-turbo-0613:personal::86YIZOge"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        titulo = request.form["titulo"]
        keywords = request.form["keywords"]
        input = titulo + "." + keywords
        print("hola mundo")
        response = openai.ChatCompletion.create(
            model=id_Fine_Tune1,
            messages=[{"role": "user", "content": input}],
            temperature=1,
            max_tokens=300,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        print(response.choices[0].message.content)
        return redirect(url_for("index", result=response.choices[0].message.content))

    result = request.args.get("result")
    return render_template("index.html", result=result)
