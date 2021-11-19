from flask import Flask, request, jsonify, render_template, json
from journo import *

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/suggestions')
def suggestions():
    text = request.args.get('jsdata')
    print("TEXT: ", text)
    text_1 = generate_interview_question(paragraph=text)
    print("TEXT : ", text_1)
    questions_list = text_1
    return render_template('suggestions.html', suggestions=questions_list)


@app.route('/suggestions_1')
def suggestions_1():
    text = request.args.get('jsdata')
    text_1 = generate_headline(paragraph=text)
    print("HEADLINE TEXT 1", text_1)
    questions_list = text_1
    return render_template('suggestions_1.html', suggestions=questions_list)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
