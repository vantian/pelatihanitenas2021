from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
    
@app.route("/sample")
def sample():
    return render_template('sample/kepler.gl.html')

app.run(debug=True)