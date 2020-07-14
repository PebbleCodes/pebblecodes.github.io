from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('partymode.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['p']
    mode = request.form['activate']
    first_color = request.form['first']
    second_color = request.form['second']
    third_color = request.form['third']
    fourth_color = request.form['fourth']

    print(text)
    print(mode)
    print(first_color)
    print(second_color)
    print(third_color)
    print(fourth_color)
    return text

if __name__ == "__main__":
    app.run()
    app.my_form_post()