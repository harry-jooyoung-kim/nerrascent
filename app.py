from flask import Flask, render_template, request, jsonify


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
@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/demo', methods=['POST'])
def demo():
    data = request.get_json(force=True)
    # simple stub returning fixed notes regardless of input
    response = {
        'top': ['Citrus', 'Bergamot'],
        'mid': ['Lavender', 'Rosemary'],
        'base': ['Cedarwood', 'Musk']
    }
    return jsonify(response)


if __name__ == "__main__":
    # Run the development server when the script is executed directly
    # This allows `python app.py` to start the Flask application as
    # documented in the README.
    app.run(debug=True)

