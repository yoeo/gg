# GG, the Guessing Game

![GG](gg/static/favicon.png)

Programming Languages Guessing Game

## Rules

The rules are simple:

1. copy/paste a source code,
2. hit `Guess` button,
2. GG will instantly **guess the programming language**.

## Installation

* Python 3.6+ required

Run the following command from the cloned repository:

```bash
python3 setup.py install
```

## Usage

Launch GG server

```bash
gg-gunicorn
```

Then go to `http://localhost:8000/`

## License and stuff...

* [Language detection powered by Guesslang](https://github.com/yoeo/guesslang)

* [Guesslang documentation](https://guesslang.readthedocs.io/en/latest/)

* Icon created by
  [Mooms (Creative Commons)](https://thenounproject.com/term/thinking/949356/)

* GG — Copyright (c) 2020 Y. SOMDA, [MIT License](LICENSE)
