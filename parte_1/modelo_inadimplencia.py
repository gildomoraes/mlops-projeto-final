# Pacotes Básicos
import pandas as pd
import numpy as np
import os
import joblib

# Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# Carregamento dos Dados
folder_path = 'G:/Meu Drive/Gildo - Google Drive/3b. Acadêmico/MBA/14. Machine Learning Operation/c. Atividades e Trabalhos/Trabalho Final/Entregáveis/datasets'
file_name = 'loan_default.csv'
file_path = os.path.join(folder_path, file_name)
df_raw = pd.read_csv(file_path)
df = df_raw.copy()

# Data Cleaning
colunas_para_remover = ['ID', 'year']
df = df.drop(colunas_para_remover, axis=1)

# Aplicar Label Encoding para variáveis Categóricas
variaveis_label_encoding = ['loan_limit', 'Gender', 'approv_in_adv', 'loan_type', 'loan_purpose', 'Credit_Worthiness', 'open_credit', 'business_or_commercial', 'rate_of_interest', 'Interest_rate_spread', 
                       'Upfront_charges', 'Neg_ammortization', 'interest_only', 'lump_sum_payment', 'construction_type', 'occupancy_type', 'Secured_by', 'total_units', 'credit_type', 
                      'co_applicant_credit_type', 'submission_of_application', 'age', 'Region', 'Security_Type']

label_encoders = {}
for col in variaveis_label_encoding:
    if col in df.columns:
        label_encoders[col] = LabelEncoder()
        df[col] = label_encoders[col].fit_transform(df[col])

# Separação das features e da variável alvo
X = df.drop('Status', axis=1)
y = df['Status']

# Divisão dos dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinamento do modelo Random Forest
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Previsões
y_pred = model.predict(X_test)

# Avaliação do modelo
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Exibição dos resultados
print(f'Acurácia: {accuracy}')
print('Relatório de Classificação:')
print(report)

# Salva o Modelo
joblib.dump(model, 'G:/Meu Drive/Gildo - Google Drive/3b. Acadêmico/MBA/14. Machine Learning Operation/c. Atividades e Trabalhos/Trabalho Final/mlops-projeto-final/parte_1/model.joblib')
print("Modelo treinado e salvo com sucesso.")