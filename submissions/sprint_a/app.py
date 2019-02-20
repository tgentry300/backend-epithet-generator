from sprint_a import app


@app.route('/')
def generate_epithets():
    return '{"epithets": []}'


@app.route('/vocabulary')
def vocabulary():
    return '{"vocabulary": {}}'
