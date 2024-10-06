import requests
import json

# URL do servidor Flask
url = 'http://127.0.0.1:5000/predict'

# Exemplo de dados de entrada (deve ser um dicionário ou lista de dicionários, dependendo de quantas previsões você quer)
data = {
    #'ID': [12345],
    #'year': [2019],
    'loan_limit': [0],
    'Gender': [0],
    'approv_in_adv': [0],
    'loan_type': [1],
    'loan_purpose': [0],
    'Credit_Worthiness': [1],
    'open_credit': [1],
    'business_or_commercial': [1],
    'loan_amount': [100000],
    'rate_of_interest': [5.5],
    'Interest_rate_spread': [0.0],
    'Upfront_charges': [2000],
    'term': [360],
    'Neg_ammortization': [1],
    'interest_only': [0],
    'lump_sum_payment': [0],
    'property_value': [120000],
    'construction_type': [1],
    'occupancy_type': [0],
    'Secured_by': [0],
    'total_units': [1],
    'income': [50000],
    'credit_type': [0],
    'Credit_Score': [700],
    'co_applicant_credit_type': [0],
    'age': [3],
    'submission_of_application': [1],
    'LTV': [80],
    'Region': [1],
    'Security_Type': [1],
    'dtir1': [30]
}

# Enviando os dados para o servidor
response = requests.post(url, json=data)

# Verificar se a resposta foi bem-sucedida
if response.status_code == 200:
    # Exibir a resposta recebida do servidor
    for message in response.json():
        print('Resposta do servidor:', message)
else:
    print(f"Erro na requisição: {response.status_code}")
    print(response.text)  # Mostra o texto da resposta para depuração