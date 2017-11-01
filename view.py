from flask import Flask, render_template, request, redirect,jsonify, url_for, flash
app = Flask(__name__)

import project


@app.route('/')
def main():
  return render_template('main.html')

@app.route('/article', methods=['POST', 'GET'])
def viewArticle():
    return render_template('view_article.html', articles=project.getArticles())

@app.route('/author', methods=['POST', 'GET'])
def viewAuthor():
    return render_template('view_author.html', authors=project.getAuthors())

@app.route('/error', methods=['POST', 'GET'])
def viewError(): 
    return render_template('view_error.html', errors=project.getErrors())

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True, port=8000)

