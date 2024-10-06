from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

# Inicializando o app Flask
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def call_home(request = request):
    print(request.values)
    return "Server is Running!"

# Carregando o modelo previamente treinado
#model = joblib.load('G:/Meu Drive/Gildo - Google Drive/3b. Acadêmico/MBA/14. Machine Learning Operation/c. Atividades e Trabalhos/Trabalho Final/mlops-projeto-final/parte_1/model.joblib')
model = joblib.load('model.joblib')

# Definindo a rota para previsões
@app.route('/predict', methods=['POST'])
def predict():
    # Pegando os dados da requisição JSON
    data = request.get_json(force=True)
    
    # Convertendo os dados em um DataFrame
    data_df = pd.DataFrame(data)
    
    # Fazendo a previsão com o modelo carregado
    prediction = model.predict(data_df)
    
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
    app.run(debug=True, host='0.0.0.0')