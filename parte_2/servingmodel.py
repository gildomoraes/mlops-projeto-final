from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

# Inicializando o app Flask
app = Flask(__name__)

# Definindo a Rota Inicial
@app.route("/", methods=['GET', 'POST'])
def call_home(request = request):
    print(request.values)
    return "Server is Running!"

# Carregando o modelo previamente treinado
modelo = joblib.load('models/modelo01.joblib')

# Definindo a rota para previsões
@app.route("/predict", methods=['GET', 'POST'])
def call_predict(request = request):
    # Pegando os dados da requisição JSON
    data = request.get_json(force=True)
    
    # Convertendo os dados em um DataFrame
    data_df = pd.DataFrame(data)
    
    # Fazendo a previsão com o modelo carregado
    prediction = modelo.predict(data_df)
    
    # Transformando as previsões em mensagens personalizadas
    result = []
    for pred in prediction:
        if pred == 0:
            result.append("O crédito foi aprovado.")
        else:
            result.append("O crédito não foi aprovado, há chances deste cliente ser inadimplente.")
    
    # Retornando a mensagem de texto como JSON
    return jsonify(result)

# Rodando a aplicação
if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')