from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/how-it-works')
def how_it_works():
    return render_template('howitworks.html')

@app.route('/pebble')
def pebble():
    return render_template('order.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/compose')
def compose():
    return render_template('create.html')

@app.route('/library')
def library():
    return render_template('recipes.html')

if __name__ == '__main__':
    app.run(debug=True)
