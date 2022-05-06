import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from catboost import CatBoostRegressor
import json

from settings import settings

path_data_prepared = settings.path_data_prepared
path_model = settings.path_model
path_metrics = settings.path_metrics

X_test = pd.read_csv(f'{path_data_prepared}X_test.csv')
y_test = pd.read_csv(f'{path_data_prepared}y_test.csv')

model = CatBoostRegressor()
path_model = f'{path_model}model'
model.load_model(path_model)
pred = model.predict(X_test)

mse = "%.2f" % mean_squared_error(pred, y_test)
mae = "%.2f" % mean_absolute_error(pred, y_test)
r2 = "%.2f" % r2_score(pred, y_test)

metrics = {'mse': mse, 'mae': mae, 'r2_score': r2}
path_metrics_ = f'{path_metrics}metrics.json'

with open(path_metrics_, 'w') as f:
    json.dump(metrics, f)

# print('Metrics successfully wrote')
