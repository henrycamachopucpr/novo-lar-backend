from flask import Flask, jsonify, request
import json
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

sexoValido = ['feminino','masculino']

@app.get('/filtros/animais')
def get_animais_filtro():
    dados = carregar_animais()

    idAnimal = request.args.get('idAnimal') 
    nome = request.args.get('nome') 
    especie = request.args.get('especie') 
    cor = request.args.get('cor')
    porte = request.args.get('porte') 
    idade = request.args.get('idade')
    raca = request.args.get('raca') 
    sexo = request.args.get('sexo')

    if idAnimal:
        idAnimal = int(idAnimal)
        
    if idade:
        idade = int(idade)

    resultado = []

    for dado in dados:

        if idAnimal and dado.get('idAnimal') != idAnimal:
            continue
        if nome and dado.get('nome') != nome:
            continue
        if especie and dado.get('especie') != especie:
            continue
        if cor and dado.get('cor') != cor:
            continue
        if porte and dado.get('porte') != porte:
            continue
        if idade and dado.get('idade') != idade:
            continue
        if raca and dado.get('raca') != raca:
            continue
        if sexo and dado.get('sexo').lower() != sexo.lower():
            continue

        resultado.append(dado)

    return jsonify(resultado), 200


@app.get('/filtros/usuarios')
def get_usuarios_filtro():
    dados = carregar_usuarios()

    idUsuario = request.args.get('idUsuario') 
    nome = request.args.get('nome') 
    idade = request.args.get('idade')
    sexo = request.args.get('sexo')
    email = request.args.get('email')
    telefone = request.args.get('telefone')
    endereco = request.args.get('endereco')

    if idUsuario:
        idUsuario = int(idUsuario)
        
    if idade:
        idade = int(idade)

    resultado = []

    for dado in dados:

        if idUsuario and dado.get('idUsuario') != idUsuario:
            continue
        if nome and dado.get('nome') != nome:
            continue
        if idade and dado.get('idade') != idade:
            continue
        if sexo and dado.get('sexo').lower() != sexo.lower():
            continue
        if email and dado.get('email') != email:
            continue
        if telefone and dado.get('telefone') != telefone:
            continue
        if endereco and dado.get('endereco') != endereco:
            continue

        resultado.append(dado)

    return jsonify(resultado), 200


@app.get('/filtros/cidade')
def get_cidade_filtro():
    dados = carregar_cidade()

    idCidade = request.args.get('idCidade') 
    nome = request.args.get('nome') 
    estado = request.args.get('estado')

    if idCidade:
        idCidade = int(idCidade)

    resultado = []

    for dado in dados:

        if idCidade and dado.get('idCidade') != idCidade:
            continue
        if nome and dado.get('nome') != nome:
            continue
        if estado and dado.get('estado') != estado:
            continue

        resultado.append(dado)

    return jsonify(resultado), 200


@app.get('/filtros/doadores')
def get_doadores_filtro():
    dados = carregar_doador()

    idDoador = request.args.get('idDoador') 
    nome = request.args.get('nome') 
    idade = request.args.get('idade')
    sexo = request.args.get('sexo')
    email = request.args.get('email')
    endereco = request.args.get('endereco')

    if idDoador:
        idDoador = int(idDoador)
        
    if idade:
        idade = int(idade)
    
    resultado = []

    for dado in dados:

        if idDoador and dado.get('idDoador') != idDoador:
            continue
        if nome and dado.get('nome') != nome:
            continue
        if idade and dado.get('idade') != idade:
            continue
        if sexo and dado.get('sexo').lower() != sexo.lower():
            continue
        if email and dado.get('email') != email:
            continue
        if endereco and dado.get('endereco') != endereco:
            continue

        resultado.append(dado)

    return jsonify(resultado), 200


@app.get('/filtros/destinatarios')
def get_destinatarios_filtro():
    dados = carregar_destinatarios()

    idDestinatario = request.args.get('idDestinatario') 
    nome = request.args.get('nome') 
    idade = request.args.get('idade')
    sexo = request.args.get('sexo')
    email = request.args.get('email')
    telefone = request.args.get('telefone')
    endereco = request.args.get('endereco')

    if idDestinatario:
        idDestinatario = int(idDestinatario)

    if idade:
        idade = int(idade)

    resultado = []

    for dado in dados:

        if idDestinatario and dado.get('idDestinatario') != idDestinatario:
            continue
        if nome and dado.get('nome') != nome:
            continue
        if idade and dado.get('idade') != idade:
            continue
        if sexo and dado.get('sexo').lower() != sexo.lower():
            continue
        if email and dado.get('email') != email:
            continue
        if telefone and dado.get('telefone') != telefone:
            continue
        if endereco and dado.get('endereco') != endereco:
            continue

        resultado.append(dado)

    return jsonify(resultado), 200


@app.get('/filtros/adocoes')
def get_adocoes_filtro():
    dados = carregar_adocoes()

    idAdocao = request.args.get('idAdocao') 
    idAnimal = request.args.get('idAnimal')
    idDestinatario = request.args.get('idDestinatario')
    dataDoacao = request.args.get('dataDoacao')
    endereco = request.args.get('endereco')

    if idAdocao:
        idAdocao = int(idAdocao)
    if idAnimal:
        idAnimal = int(idAnimal)
    if idDestinatario:
        idDestinatario = int(idDestinatario)

    resultado = []

    for dado in dados:

        if idAdocao and dado.get('idAdocao') != idAdocao:
            continue
        if idAnimal and dado.get('idAnimal') != idAnimal:
            continue
        if idDestinatario and dado.get('idDestinatario') != idDestinatario:
            continue
        if dataDoacao and dado.get('dataDoacao') != dataDoacao:
            continue
        if endereco and dado.get('endereco') != endereco:
            continue

        resultado.append(dado)

    return jsonify(resultado), 200

def carregar_usuarios():  
    with open('usuarios.json','r') as f:
        return json.load(f)

def salvar_usuarios(usuarios):  
    with open('usuarios.json','w') as f:
        json.dump(usuarios, f, indent=4)

def carregar_animais():  
    with open('animais.json','r') as f:
        return json.load(f)

def salvar_animais(animais):  
    with open('animais.json','w') as f:
        json.dump(animais, f, indent=4)

def carregar_doador():  
    with open('doadores.json','r') as f:
        return json.load(f)

def salvar_doador(doador): 
    with open('doadores.json','w') as f:
        json.dump(doador, f, indent=4)

def carregar_adocoes():  
    with open('adocoes.json','r') as f:
        return json.load(f)

def salvar_adocoes(adocoes):  
    with open('adocoes.json','w') as f:
        json.dump(adocoes, f, indent=4)
    
def carregar_destinatarios():  
    with open('destinatario.json','r') as f:
        return json.load(f)

def salvar_destinatarios(destinatarios):  
    with open('destinatario.json','w') as f:
        json.dump(destinatarios, f, indent=4)
    
def carregar_cidade():
    with open('cidade.json','r') as f:
        return json.load(f)

def salvar_cidade(cidade):  
    with open('cidade.json','w') as f:
        json.dump(cidade, f, indent=4)


@app.get('/listar/usuarios/<int:idUsuario>')
def get_usuario_id(idUsuario):
    dados = carregar_usuarios()

    for dado in dados:
        if dado.get('idUsuario') == idUsuario:
            return jsonify(dado), 200
        
    return jsonify({"mensagem": "Usuario não encontrado"}), 404

@app.get('/listar/usuarios')
def get_usuario_all():
    dados = carregar_usuarios()

    if not dados:
         return jsonify({"mensagem": "Não existe usuarios cadastrados!"}), 404
    
    return jsonify(dados),200

@app.get('/listar/animais/<int:idAnimal>')
def get_animal_id(idAnimal):
    dados = carregar_animais()

    for dado in dados:
        if dado.get('idAnimal') == idAnimal:
            return jsonify(dado), 200
        
    return jsonify({"mensagem": "Animal não encontrado"}), 404

@app.get('/listar/animais') 
def get_animais_all():
    dados = carregar_animais()

    if not dados:
         return jsonify({"mensagem": "Não existe animais cadastrados!"}), 404
    
    return jsonify(dados),200

@app.get('/listar/doador/<int:idDoador>')
def get_doador_id(idDoador):
    dados = carregar_doador()

    for dado in dados:
        if dado.get('idDoador') == idDoador:
            return jsonify(dado), 200
        
    return jsonify({"mensagem": "Doador não encontrado"}), 404

@app.get('/listar/doador') 
def get_doador_all():
    dados = carregar_doador()

    if not dados:
         return jsonify({"mensagem": "Não existe doadores cadastrados!"}), 404
    
    return jsonify(dados),200

@app.get('/listar/adocoes/<int:idAdocao>')
def get_adocoes_id(idAdocao):
    dados = carregar_adocoes()

    for dado in dados:
        if dado.get('idAdocao') == idAdocao:
            return jsonify(dado), 200
        
    return jsonify({"mensagem": "Adocao não encontrado"}), 404

@app.get('/listar/adocoes') 
def get_adocoes_all():
    dados = carregar_adocoes()

    if not dados:
         return jsonify({"mensagem": "Adocao não encontrado!"}), 404
    
    return jsonify(dados),200

@app.get('/listar/destinatario/<int:idDestinatario>')
def get_destinatario_id(idDestinatario):
    dados = carregar_destinatarios()

    for dado in dados:
        if dado.get('idDestinatario') == idDestinatario:
            return jsonify(dado), 200

    return jsonify({"mensagem": "Destinatário não encontrado"}), 404

@app.get('/listar/destinatario') 
def get_destinatarios_all():
    dados = carregar_destinatarios()

    if not dados:
         return jsonify({"mensagem": "Não existem destinatarios!"}), 404
    
    return jsonify(dados),200

@app.get('/listar/cidade/<int:idCidade>')
def get_cidades_id(idCidade):
    dados = carregar_cidade()

    for dado in dados:
        if dado.get('idCidade') == idCidade:
            return jsonify(dado), 200
        
    return jsonify({"mensagem": "Cidade não encontrada"}), 404

@app.get('/listar/cidade')
def get_cidades_all():
    dados = carregar_cidade()

    if not dados:
         return jsonify({"mensagem": "Não existem cidades cadastradas!"}), 404
    
    return jsonify(dados),200

@app.post('/cadastrar/usuarios')
def criar_usuario():
    dados = request.json

    if not dados.get('idUsuario'):
        return jsonify({"mensagem": "Campo idUsuario é obrigatório!"}), 400
    
    if not isinstance(dados.get('idUsuario'), int):
        return jsonify({"mensagem": "O campo 'idUsuario' deve ser um número inteiro."}), 422

    if not dados.get('nome'):
        return jsonify({"mensagem": "Campo nome é obrigatório!"}), 400

    if not dados.get('idade'):
        return jsonify({"mensagem": "Campo idade é obrigatório!"}), 400

    if not isinstance(dados.get('idade'), int):
        return jsonify({"mensagem": "'idade' deve ser um número inteiro!"}), 422

    if not dados.get('sexo'):
        return jsonify({"mensagem": "Campo sexo é obrigatório!"}), 400

    if dados.get('sexo').lower() not in sexoValido:
        return jsonify({"mensagem": "Sexo inválido!"}), 422

    if not dados.get('email'):
        return jsonify({"mensagem": "Campo email é obrigatório!"}), 400
    
    if not dados.get('endereco'):
        return jsonify({"mensagem" : "Campo do endereco e obrigatorio!"}), 400

    with open('usuarios.json','r') as f:
        usuarios = json.load(f)
        
    usuarios.append(dados)

    with open('usuarios.json','w') as f:
        json.dump(usuarios, f, indent=4)

    return jsonify({"mensagem": "Usuario cadastrado com sucesso!"}), 201

@app.post('/cadastrar/animais')
def criar_animal():
    dados = request.json

    especieAnimal = ['gato','cachorro']

    if not dados.get('idAnimal'):
        return jsonify({"mensagem" : "Campo de idAnimal e obrigatorio!"}), 400
    
    if not isinstance(dados.get('idAnimal'), int):
        return jsonify({"mensagem": "O campo 'idAnimal' deve ser um número inteiro."}), 422

    if not dados.get('nome'):
        return jsonify({"mensagem" : "Campo de nome e obrigatorio!"}), 400

    if not dados.get('idade'):
        return jsonify({"mensagem" : "Campo de idade e obrigatorio!"}), 400
    
    if not isinstance(dados.get('idade'), int):
        return jsonify({"mensagem": "O campo 'idade' deve ser um número inteiro."}), 422

    if not dados.get('especie'):
        return jsonify({"mensagem" : "Campo de especie e obrigatorio!"}), 400

    if not dados.get('raca'):
        return jsonify({"mensagem" : "Campo de raca e obrigatorio!"}), 400
        
    if not dados.get('sexo'):
        return jsonify({"mensagem" : "Campo de sexo e obrigatorio!"}), 400

    if not dados.get('porte'):
        return jsonify({"mensagem" : "Campo de porte e obrigatorio!"}), 400
    
    if dados.get('especie').lower() not in especieAnimal:
            return jsonify({"mensagem" : "Especie de animal invalido!"}),422
    
    if dados.get('sexo').lower() not in sexoValido:
        return jsonify({"mensagem" : "Sexo invalido!"}),422
    
    with open('animais.json','r') as f:
        animais = json.load(f)

    animais.append(dados)

    with open('animais.json','w') as f:
        json.dump(animais, f, indent=4)

    return jsonify({"mensagem": "Animal cadastrado com sucesso!"}), 201

@app.post('/cadastrar/doador')
def criar_doador():
    dados = request.json

    if not dados.get('idDoador'):
        return jsonify({"mensagem" : "Campo de idDoador e obrigatorio!"}), 400
    
    if not isinstance(dados.get('idDoador'), int):
        return jsonify({"mensagem": "O campo 'idDoador' deve ser um número inteiro."}), 422

    if not dados.get('nome'):
        return jsonify({"mensagem" : "Campo de nome e obrigatorio!"}), 400

    if not dados.get('idade'):
        return jsonify({"mensagem" : "Campo de idade e obrigatorio!"}), 400
    
    if not isinstance(dados.get('idade'), int):
        return jsonify({"mensagem": "O campo 'idade' deve ser um número inteiro."}), 422
    
    if not dados.get('sexo'):
        return jsonify({"mensagem" : "Campo de sexo e obrigatorio!"}), 400
    
    if dados.get('sexo').lower() not in sexoValido:
        return jsonify({"mensagem" : "Sexo invalido!"}),422

    if not dados.get('email'):
        return jsonify({"mensagem" : "Campo de email e obrigatorio!"}), 400

    if not dados.get('endereco'):
        return jsonify({"mensagem" : "Campo do endereco e obrigatorio!"}), 400

    
    with open('doadores.json','r') as f:
        doadores = json.load(f)

    doadores.append(dados)

    with open('doadores.json','w') as f:
        json.dump(doadores, f, indent=4)

    return jsonify({"mensagem": "Doador cadastrado com sucesso!"}), 201

@app.post('/cadastrar/adocoes')
def cadastrar_adocoes():
    dados = request.json

    if not dados.get('idAdocao'):
        return jsonify({"mensagem" : "Campo idAdocao e obrigatório!"}), 400
    
    if not isinstance(dados.get('idAdocao'), int):
        return jsonify({"mensagem": "O campo 'idAdocao' deve ser um número inteiro."}), 422

    if not dados.get('idAnimal'):
        return jsonify({"mensagem" : "Campo idAnimal e obrigatorio!"}), 400
    
    if not isinstance(dados.get('idAnimal'), int):
        return jsonify({"mensagem": "O campo 'idAnimal' deve ser um número inteiro."}), 422
       
    if not dados.get('idDestinatario'):
        return jsonify({"mensagem" : "Campo idDestinatario e obrigatorio!"}), 400
    
    if not isinstance(dados.get('idDestinatario'), int):
        return jsonify({"mensagem": "O campo 'idDestinatario' deve ser um número inteiro."}), 422

    if not dados.get('dataDoacao'):
        return jsonify({"mensagem" : "Campo dataDoacao e obrigatorio!"}), 400

    if not dados.get('endereco'):
        return jsonify({"mensagem" : "Campo do endereco e obrigatorio!"}), 400

    with open('adocoes.json','r') as f:
        adocoes = json.load(f)

    adocoes.append(dados)

    with open('adocoes.json','w') as f:
        json.dump(adocoes, f, indent=4)

    return jsonify({"mensagem": "Adocao cadastrada com sucesso!"}), 201

@app.post('/cadastrar/destinatario')
def cadastrar_destinatario():
    dados = request.json

    if not dados.get('idDestinatario'):
        return jsonify({"mensagem" : "Campo de idDestinatario e obrigatorio!"}), 400
    
    if not isinstance(dados.get('idDestinatario'), int):
        return jsonify({"mensagem": "O campo 'idDestinatario' deve ser um número inteiro."}), 422

    if not dados.get('nome'):
        return jsonify({"mensagem" : "Campo de nome e obrigatorio!"}), 400

    if not dados.get('idade'):
        return jsonify({"mensagem" : "Campo de idade e obrigatorio!"}), 400
    
    if not dados.get('sexo'):
        return jsonify({"mensagem" : "Campo de sexo e obrigatorio!"}), 400
    
    if dados.get('sexo').lower() not in sexoValido:
        return jsonify({"mensagem" : "Sexo invalido!"}),422

    if not dados.get('email'):
        return jsonify({"mensagem" : "Campo de email e obrigatorio!"}), 400
    
    if not dados.get('endereco'):
        return jsonify({"mensagem" : "Campo do endereco e obrigatorio!"}), 400

    with open('destinatario.json','r') as f:
        destinatario = json.load(f)

    destinatario.append(dados)

    with open('destinatario.json','w') as f:
        json.dump(destinatario, f, indent=4)

    return jsonify({"mensagem": "Destinatario cadastrado com sucesso!"}), 201

@app.post('/cadastrar/cidades')
def cadastrar_cidade():
    dados = request.json

    if not dados.get('idCidade'):
        return jsonify({"mensagem" : "Campo idCidade e obrigatorio!"}), 400

    if not isinstance(dados.get('idCidade'), int):
        return jsonify({"mensagem": "O campo 'idCidade' deve ser um número inteiro."}), 422
    
    if not dados.get('nome'):
        return jsonify({"mensagem" : "Campo nome e obrigatorio!"}), 400
    
    if not dados.get('estado'):
        return jsonify({"mensagem" : "Campo estado e obrigatorio!"}), 400

    with open('cidade.json','r') as f:
        cidades = json.load(f)

    cidades.append(dados)

    with open('cidade.json','w') as f:
        json.dump(cidades, f, indent=4)

    resposta = {
        "Mensagem": "Cidade cadastrada com sucesso!"
    }
    
    return jsonify(resposta), 201

@app.put('/atualizar/animais/<int:idAnimal>')
def atualizar(idAnimal):
    animal = carregar_animais()
    dados = request.json

    if "idade" in dados and not isinstance(dados["idade"], int):
        return jsonify({"mensagem":"O campo idade deve ser um número inteiro!"}), 422

    if "sexo" in dados:
        if dados["sexo"].lower() not in sexoValido:
            return jsonify({"mensagem":"Sexo inválido!"}), 422

    if "especie" in dados:
        if dados["especie"].lower() not in ['gato','cachorro']:
            return jsonify({"mensagem":"Espécie de animal inválida!"}), 422

    for dado in animal:
        if dado.get('idAnimal') == idAnimal:
            dado.update(dados)
            salvar_animais(animal)
            return jsonify({"mensagem":"Ok"}), 200
    return jsonify({"mensagem":"Nenhum animal encontrado"}), 404

@app.put('/atualizar/usuarios/<int:idUsuario>')
def atualizar_usuario(idUsuario):
    usuario = carregar_usuarios()
    dados = request.json

    if "idade" in dados and not isinstance(dados["idade"], int):
        return jsonify({"mensagem":"O campo idade deve ser um número inteiro!"}), 422

    if "sexo" in dados:
        if dados["sexo"].lower() not in sexoValido:
            return jsonify({"mensagem":"Sexo inválido!"}), 422

    for dado in usuario:
        if dado.get('idUsuario') == idUsuario:
            dado.update(dados)
            salvar_usuarios(usuario)
            return jsonify({"mensagem":"Ok"}), 200
    return jsonify({"mensagem":"Nenhum usuario encontrado"}), 404

@app.put('/atualizar/destinatario/<int:idDestinatario>')
def atualizar_destinatario(idDestinatario):
    destinatario = carregar_destinatarios()
    dados = request.json

    if "idade" in dados and not isinstance(dados["idade"], int):
        return jsonify({"mensagem":"O campo idade deve ser um número inteiro!"}), 422

    if "sexo" in dados:
        if dados["sexo"].lower() not in sexoValido:
            return jsonify({"mensagem":"Sexo inválido!"}), 422

    for dado in destinatario:
        if dado.get('idDestinatario') == idDestinatario:
            dado.update(dados)
            salvar_destinatarios(destinatario)
            return jsonify({"mensagem":"Ok"}), 200
    return jsonify({"mensagem":"Nenhum destinatário encontrado"}), 404

@app.put('/atualizar/adocoes/<int:idAdocao>')
def atualizar_adocao(idAdocao):
    adocao = carregar_adocoes()
    dados = request.json

    if "idAnimal" in dados and not isinstance(dados["idAnimal"], int):
        return jsonify({"mensagem":"O campo idAnimal deve ser um número inteiro!"}), 422

    if "idDestinatario" in dados and not isinstance(dados["idDestinatario"], int):
        return jsonify({"mensagem":"O campo idDestinatario deve ser um número inteiro!"}), 422

    for dado in adocao:
        if dado.get('idAdocao') == idAdocao:
            dado.update(dados)
            salvar_adocoes(adocao)
            return jsonify({"mensagem":"Ok"}), 200
    return jsonify({"mensagem":"Nenhuma adoção encontrada"}), 404

@app.put('/atualizar/cidade/<int:idCidade>')
def atualizar_cidade(idCidade):
    cidade = carregar_cidade()
    dados = request.json

    if "idCidade" in dados and not isinstance(dados["idCidade"], int):
        return jsonify({"mensagem":"O campo idCidade deve ser um número inteiro!"}), 422

    for dado in cidade:
        if dado.get('idCidade') == idCidade:
            dado.update(dados)
            salvar_cidade(cidade)
            return jsonify({"mensagem":"Ok"}), 200
    return jsonify({"mensagem":"Nenhuma cidade encontrada"}), 404

@app.put('/atualizar/doador/<int:idDoador>')
def atualizar_doador(idDoador):
    doador = carregar_doador()
    dados = request.json

    if "idade" in dados and not isinstance(dados["idade"], int):
        return jsonify({"mensagem":"O campo idade deve ser um número inteiro!"}), 422

    if "sexo" in dados:
        if dados["sexo"].lower() not in sexoValido:
            return jsonify({"mensagem":"Sexo inválido!"}), 422

    for dado in doador:
        if dado.get('idDoador') == idDoador:
            dado.update(dados)
            salvar_doador(doador)
            return jsonify({"mensagem":"Ok"}), 200
    return jsonify({"mensagem":"Nenhum doador encontrado"}), 404

@app.delete('/deletar/animais/<int:idAnimal>')
def deletar(idAnimal):
    animal = carregar_animais()

    for dado in animal:
        if dado.get('idAnimal') == idAnimal:
            animal.remove(dado)
            salvar_animais(animal)
            return '', 204
    return jsonify({"mensagem":"Nenhum animal encontrado"}), 404

@app.delete('/deletar/usuarios/<int:idUsuario>')
def deletar_usuario(idUsuario): 
    usuario = carregar_usuarios()

    for dado in usuario:
        if dado.get('idUsuario') == idUsuario:
            usuario.remove(dado)
            salvar_usuarios(usuario)
            return '', 204
    return jsonify({"mensagem":"Nenhum usuario encontrado"}), 404

@app.delete('/deletar/doador/<int:idDoador>')
def deletar_doador(idDoador):
    doador = carregar_doador()

    for dado in doador:
        if dado.get('idDoador') == idDoador:
            doador.remove(dado)
            salvar_doador(doador)
            return '', 204
    return jsonify({"mensagem":"Nenhum doador encontrado"}), 404

@app.delete('/deletar/destinatario/<int:idDestinatario>')
def deletar_destinatario(idDestinatario):   
    destinatario = carregar_destinatarios()

    for dado in destinatario:
        if dado.get('idDestinatario') == idDestinatario:
            destinatario.remove(dado)
            salvar_destinatarios(destinatario)
            return '', 204
    return jsonify({"mensagem":"Nenhum destinatário encontrado"}), 404

@app.delete('/deletar/adocoes/<int:idAdocao>')
def deletar_adocao(idAdocao):
    adocao = carregar_adocoes()

    for dado in adocao:
        if dado.get('idAdocao') == idAdocao:
            adocao.remove(dado)
            salvar_adocoes(adocao)
            return '', 204
    return jsonify({"mensagem":"Nenhuma adoção encontrada"}), 404   

@app.delete('/deletar/cidade/<int:idCidade>')
def deletar_cidade(idCidade):
    cidade = carregar_cidade()

    for dado in cidade:
        if dado.get('idCidade') == idCidade:
            cidade.remove(dado)
            salvar_cidade(cidade)
            return '', 204
    return jsonify({"mensagem":"Nenhuma cidade encontrada"}), 404

app.run(debug=True)