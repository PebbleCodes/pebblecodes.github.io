#!/usr/bin/python

from flask import Flask, request, render_template
import array as arr

password = 'Pebble'
user_pw = ''
mode = ''
first_color = ''
second_color = ''
third_color = ''
fourth_color = ''
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('config.html')

@app.route('/', methods=['POST'])
def clubPebble():
    user_pw = request.form['p']
    mode = request.form['activate']
    first_color = request.form['first']
    second_color = request.form['second']
    third_color = request.form['third']
    fourth_color = request.form['fourth']
    colors = [first_color, second_color, third_color, fourth_color]
    partyColors = colors
    print(user_pw)
    print(mode)
    for i in partyColors:
        print(i)
    return render_template('dnd.html')



if __name__ == "__main__":
    app.run()