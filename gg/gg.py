from statistics import mean, stdev

from flask import Flask, render_template, request

from guesslang import Guess


app = Flask(__name__)
app.config.update(dict(DEBUG=True, SECRET_KEY='development key'))

guess = Guess()


@app.route('/', methods=['GET', 'POST'])
def input_page():
    data = {}
    data['supported'] = sorted(guess.supported_languages)
    data['predicted'] = None

    if request.method == 'POST':
        source_code = data['source_code'] = request.form['source-code']
        if not source_code.strip():
            data['predicted'] = []
        else:
            scores = guess.probabilities(source_code)
            values = [value for name, value in scores]
            threshold = mean(values) + stdev(values)
            data['predicted'] = [
                name for name, value in scores if value > threshold
            ]

    return render_template('index.html', **data)


def main():
    app.run()
