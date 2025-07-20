#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    button_python = None
    button_telegram = None
    button_html = None
    button_db = None  # Добавляем инициализацию button_db

    if request.method == 'POST':
        button_python = request.form.get('button_python')
        button_telegram = request.form.get('button_telegram')
        button_html = request.form.get('button_html')
        button_db = request.form.get('button_db')  # Получаем значение button_db

    return render_template(
        'index.html',
        button_python=button_python,
        button_telegram=button_telegram,
        button_html=button_html,
        button_db=button_db  # Передаём button_db в шаблон
    )


if __name__ == "__main__":
    app.run(debug=True)


