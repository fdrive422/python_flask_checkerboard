from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', horizontal = 8, vertical = 8)

@app.route('/<num>')
def vertical(num):
    return render_template('index.html', horizontal = 8, vertical = int(num))

@app.route('/<num1>/<num2>')
def horizontal(num1,num2):
    return render_template('index.html', horizontal = int(num1), vertical = int(num2) )

@app.route('/<num1>/<num2>/<col1>/<col2>')
def Colors(num1, num2, col1, col2):
    return render_template('index.html', horizontal = int(num1), vertical = int(num2), col1= col1, col2 = col2)

if __name__ == "__main__":
    app.run(debug=True)