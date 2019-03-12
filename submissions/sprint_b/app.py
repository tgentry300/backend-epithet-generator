from sprint_b import app
from .helpers import EpithetGenerator
from .helpers import Vocabulary
from flask import jsonify

gen = EpithetGenerator()
vocab = Vocabulary()


@app.route('/')
def generate_epithets():
    epithet = gen.select_random('../../resources/data.json')
    return jsonify({"epithets": [epithet]})


@app.route('/vocabulary')
def vocabulary():
    words = vocab.from_file('../../resources/data.json')
    return jsonify({"vocabulary": words[0]})


@app.route('/epithets/<quantity>')
def quantity(quantity):
    num_of_epithets = []
    for _ in range(int(quantity)):
        num_of_epithets.append(gen.select_random('../../resources/data.json'))
    return jsonify({"epithets": num_of_epithets})


if __name__ == '__main__':
    app.run()
