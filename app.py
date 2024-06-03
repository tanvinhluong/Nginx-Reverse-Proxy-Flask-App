from flask import Flask, render_template

app = Flask(__name__, static_folder='assets')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/product/<int:product_id>')
def product(product_id):
    return f"Product {product_id}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)