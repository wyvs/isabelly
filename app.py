from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a segunda página (após o Sim)
@app.route('/aceitou')
def aceitou():
    return render_template('page2.html')

if __name__ == '__main__':
    # Roda o servidor localmente na porta 5000
    app.run(debug=True)
