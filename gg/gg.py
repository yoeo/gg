from flask import Flask, render_template, request

from guesslang import Guess


app = Flask(__name__)
app.config.update(dict(DEBUG=True, SECRET_KEY='development key'))

guess = Guess()


@app.route('/', methods=['GET', 'POST'])
def input_page():
    data = {}
    data['supported'] = sorted(guess.languages)
    data['predicted'] = None

    if request.method == 'POST':
        source_code = data['source_code'] = request.form['source-code']
        if not source_code.strip():
            data['predicted'] = []
        else:
            data['predicted'] = guess.probable_languages(source_code)

    return render_template('index.html', **data)


def main():
    app.run()
