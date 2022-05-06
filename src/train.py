import pandas as pd
import numpy as np
from catboost import CatBoostRegressor

from settings import settings

path_data_prepared = settings.path_data_prepared
path_model = settings.path_model

X_train = pd.read_csv(f'{path_data_prepared}X_train.csv')
y_train = pd.read_csv(f'{path_data_prepared}y_train.csv')

categorical_features_indices = np.where((X_train.dtypes != np.float64) & (X_train.dtypes != np.int64))[0]

model = CatBoostRegressor(iterations=150,
                          loss_function='RMSE',
                          cat_features=categorical_features_indices,
                          verbose=False)
model.fit(X_train, y_train)

path_model = f'{path_model}model'
model.save_model(path_model,
                 format="cbm",
                 export_parameters=None,
                 pool=None)

# print('Model successfully created')
