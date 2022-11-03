from flask import Flask
app = Flask(__name__)


# Primeira Rota!
# Decorador:
@app.route("/<numero>", methods = ['GET','POST']) # Rota com métodos get e post
def ola(numero):
    return 'Ola Mundo!! {}'.format(numero)

if __name__ == "__main__":
    app.run(debug=True) 
    # Debug para restart automatico do codigo
    # Em produção o debug deve ser false para nao mostrar erros.

