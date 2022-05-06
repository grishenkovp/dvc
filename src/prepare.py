import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_openml

from settings import settings

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_colwidth', 80)
pd.set_option('display.max_rows', 50)
pd.get_option('display.precision', 2)
pd.set_option('display.float_format', '{:,}'.format)

path_data_raw = settings.path_data_raw
path_data_prepared = settings.path_data_prepared
max_percent_null = settings.max_percent_null

# Загрузка сырых данных
# housing = fetch_openml(name="house_prices")
# data = pd.DataFrame(data=housing['data'])
# target = housing['target']
# data.to_csv(f'{path_data_raw}data.csv', index = False)
# target.to_csv(f'{path_data_raw}target.csv', index = False)
# print('Datasets successfully created')

# Предобработка сырых данных
data_ = pd.read_csv(f'{path_data_raw}data.csv')
target_ = pd.read_csv(f'{path_data_raw}target.csv')

data_ = data_.drop('Id', axis=1)

for current_col in data_.columns:
    # Если в столбце нет пустых значений
    if data_[current_col].isnull().sum() == 0:
        continue
    current_percent_null = data_[current_col].isnull().sum() / data_.shape[0] * 100
    # Если количество пустых значений превышает установленный порог
    if current_percent_null > max_percent_null:
        data_ = data_.drop(current_col, axis=1)
    # Если пустые значения есть, но их количество в пределах нормы
    if current_percent_null <= max_percent_null:
        # Для числовых столбцов берем среднее
        if data_[current_col].dtype == np.float64:
            val_mean = data_[current_col].mean()
        # Для строковых столбцов берем моду
        if data_[current_col].dtype == object:
            val_mean = data_[current_col].mode()[0]
        data_[current_col] = data_[current_col].fillna(val_mean)

# Сохранение полученных результатов
X_train, X_test, y_train, y_test = train_test_split(data_, target_, test_size=0.2, random_state=42)
X_train.to_csv(f'{path_data_prepared}X_train.csv', index=False)
X_test.to_csv(f'{path_data_prepared}X_test.csv', index=False)
y_train.to_csv(f'{path_data_prepared}y_train.csv', index=False)
y_test.to_csv(f'{path_data_prepared}y_test.csv', index=False)

# print('Datasets successfully created')
