from flask import Flask, request, jsonify, render_template, json
from journo import *


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/suggestions')
def suggestions():
    print("APP QUESTIONS")
    text = request.args.get('jsdata')
    text_1 = generate_interview_question(paragraph=text)
    questions_list = text_1
    return render_template('suggestions.html', suggestions=questions_list)


@app.route('/suggestions_1')
def suggestions_1():
    print("APP HEADLINE")
    text = request.args.get('jsdata')
    text_1 = generate_headline(paragraph=text)
    headline = text_1
    return render_template('suggestions_1.html', suggestions=headline)


@app.route('/suggestions_2')
def suggestions_2():
    print("APP OUTLINE")
    text = request.args.get('jsdata')
    text_1 = generate_article_outline(paragraph=text)
    outlines = text_1
    return render_template('suggestions_2.html', suggestions=outlines)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
