from flask import Flask, render_template
app = Flask(__name__)
#ruta
@app.route('/')
def raiz():
    return render_template('inicio.html')

if __name__ == '__main__':
    app.run(debug=True)