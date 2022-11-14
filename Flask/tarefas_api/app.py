import json

from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = [
    {
        'id': 0,
        'responsavel': 'Silvio',
        'tarefa': 'Desenvolver metodo GET',
        'status': 'concluido'
    },

    {
        'id': 1,
        'responsavel': 'Eduardo',
        'tarefa': 'Desenvolver metodo POST',
        'status': 'pendente'
    },
    
    {
        'id': 2,
        'responsavel': 'Sales',
        'tarefa': 'Desenvolver metodo PUT',
        'status': 'pendente'
    }
]


@app.route('/tarefa/<int:id>/', methods = ['GET','PUT','DELETE'])
def tarefa_by_id(id):
    if request.method == 'GET':
        for i in tarefas:
            if i['id'] == id:
                return jsonify(i)
        return jsonify({'mensagem': 'tarefa inexistente'})
           
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        tarefas[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        for i in tarefas:
            if i['id'] == id:
                tarefas.pop(id) 
                return jsonify({'status':'sucesso', 'mensagem':'Registro Excluido!'})
        return jsonify({'mensagem': 'tarefa inexistente'})

@app.route('/tarefas', methods = ['POST'])
def tarefa():
    
    data = request.json
    data['id'] = len(tarefas)
    tarefas.append(data)

    return jsonify({'mensagem':'tarefa criada'})


if __name__ == '__main__':
    app.run(debug=True)
