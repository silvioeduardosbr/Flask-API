from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'id':'0',
    'nome': 'Rafael',
    'habilidades': ['Python', 'Flask']
    },
    {'id':'1',
    'nome': 'Galeani',
    'habilidades': ['Python', 'Django']} 
]

# Devolve um dev, pelo ID. Tbm altera e deleta um dev
@app.route('/dev/<int:id>/', methods = ['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status':'erro', 
                        'mensg':'dev de ID {} nao exist'.format(id)}
        except Exception:
            mensg = 'Erro desconhecido.'
            response = {'status':'erro', 'mensg':'Nao existe!'}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso',
                        'mensg':'registro excluido!'})

# Lista todos os devs e inclui um novo dev
@app.route('/dev/', methods = ['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])

    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)


