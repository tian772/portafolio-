# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_HTML = request.form.get('button_HTML')
    button_BD = request.form.get('button_BD')
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_HTML=button_HTML, button_BD=button_BD)


if __name__ == "__main__":
    app.run(debug=True)
