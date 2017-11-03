from flask import Flask, render_template, request, url_for
import project
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/article', methods=['POST', 'GET'])
def view_article():
    return render_template('view_article.html', articles=project.get_articles())


@app.route('/author', methods=['POST', 'GET'])
def view_author():
    return render_template('view_author.html', authors=project.get_authors())


@app.route('/error', methods=['POST', 'GET'])
def view_error():
    return render_template('view_error.html', errors=project.get_errors())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
