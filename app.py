from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tarefas = [
    {"responsavel":"Maria", "tarefa":"Limpar a Casa", "status":"Concluido", "id":0},
    {"responsavel":"Francisquinha", "tarefa":"Responder Chats", "status":"Em Andamento", "id":1}
]

@app.route('/dev', methods=['GET', 'POST'])
def todas_tarefas():
    if request.method == 'POST':
        try:
            dados = json.loads(request.data)
            lista = []
            for i in tarefas:
                lista.append(i["id"])
                print("ID detectado: " + str(i["id"]))
            posicao = max(lista) + 1
            print("Posicao encontrada: " + str(posicao))
            lista = []
            dados["id"] = posicao
            tarefas.append(dados)
            lenposition = len(tarefas) - 1
            return jsonify(tarefas[lenposition])
        except:
            return jsonify({'status':'erro', 'mensagem':'Houve um erro durante a insercao do registro'})
    elif request.method == 'GET':
        try:
            return jsonify(tarefas)
        except:
            return jsonify({'status':'Erro', 'mensagem':'Um erro foi encontrado'})

@app.route('/dev/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def tarefa_unica(id):
    if request.method == 'GET':
        try:
            tarefa = tarefas[id]
            return jsonify(tarefa)
        except:
            return jsonify({'status':'Erro', 'mensagem':'ID inexistente'})
    elif request.method == 'DELETE':
        try:
            tarefas.pop(id)
            return jsonify({'status':'Sucesso', 'mensagem':'Registro excluido com sucesso'})
        except:
            return jsonify({'status':'Erro', 'mensagem':'ID inexistente'})
    elif request.method == 'PUT':
        try:
            dados = json.loads(request.data)
            if len(dados) == 3:
                dados["id"] = id
                tarefas[id] = dados
                return jsonify({'status':'Sucesso', 'mensagem':'Dados alterados com sucesso'})
            else:
                tarefas[id] = dados
                return jsonify({'status':'Sucesso', 'mensagem':'Dados alterados com sucesso'})
        except:
            return jsonify({'status':'Erro', 'mensagem':'Um erro foi encontrado'})

if __name__ == '__main__':
    app.run(debug=True, port=80)