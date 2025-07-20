from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
def save_feedback(email, message):
    with open('feedback.txt', 'a', encoding='utf-8') as f:
        f.write(f"Email: {email}\nMessage: {message}\n{'='*30}\n")
@app.route('/', methods=['GET', 'POST'])
def index():
    button_python = None
    button_telegram = None
    button_html = None
    button_db = None
    if request.method == 'POST':
        if 'email' in request.form:
            # Обработка формы обратной связи
            email = request.form['email']
            message = request.form['text']
            save_feedback(email, message)
            return redirect(url_for('index', _anchor='feedback'))
        else:
            button_python = request.form.get('button_python')
            button_telegram = request.form.get('button_telegram')
            button_html = request.form.get('button_html')
            button_db = request.form.get('button_db')
    return render_template(
        'index.html',
        button_python=button_python,
        button_telegram=button_telegram,
        button_html=button_html,
        button_db=button_db
    )
if __name__ == "__main__":
    app.run(debug=True)


