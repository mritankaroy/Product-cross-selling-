import os
import pandas as pd
import pickle
from flask import Flask, request, Response
from healthinsurance import Healthinsurance

# loading model
model = pickle.load(open('model/modelo_lr.pkl', 'rb'))

# iniciar a API
app = Flask(__name__)


@app.route('/heathinsurance/predict', methods=['POST'])
def heath_insurance_predict():
    test_json = request.get_json()

    if test_json:  # existe dado
        if isinstance(test_json, dict):  # exemplo unico
            test_raw = pd.DataFrame(test_json, columns=index[0])
        else:  # multiplos exemplos
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())

        # instance healthinsurance class
        pipeline = HealthInsurance()

        df2 = pipeline.feature_engeneering(test_json)

        df3 = pipeline.data_preparation(df2)

        df_response = pipeline.get_prediction(model, test_raw, df3)

        return df_response

    else:
        return Response('{}', status=200, mimetype='application/json')


if __name__ == '__main__':
    port = os.environ.get( 'PORT', 5000 )
    app.run(host = '0.0.0.0', port = port)