from flask import Flask, render_template
import time
import logging

app = Flask(__name__)


def calculate_pi():
    start = time.time()
    # Initialize denominator
    k = 1

    # Initialize sum
    s = 0

    for i in range(3000000):

        # even index elements are positive
        if i % 2 == 0:
            s += 4 / k
        else:

            # odd index elements are negative
            s -= 4 / k

        # denominator is odd
        k += 2
    end = time.time()
    elapsed = end-start
    logging.warning(f"execution time {elapsed}")
    return s, elapsed


@app.route('/')
def hello_world():  # put application's code here
    return render_template("register.html")


@app.route('/pi')
def slow():
    pi, elapsed= calculate_pi()
    return f'{pi} calculated in {elapsed}s'


if __name__ == '__main__':
    calculate_pi()
    app.run()
