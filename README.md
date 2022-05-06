### Алгоритм работы с DVC

#### Структура демо-примера

---
В репозитории шесть каталогов:
1. src/ – для исходного кода;
2. data/ – для всех версий датасетов;
3. data/raw/ – для данных, полученных из внешнего источника;
4. data/prepare/ – для данных, измененных внутри;
5. model/ – для моделей машинного обучения;
6. data/metrics/ – для отслеживания показателей производительности моделей.

Каталог src/ уже содержит три файла Python:
1. prepare.py – код подготовки данных для обучения;
2. train.py – код обучения модели;
3. evalueate.py – код оценки результатов обучения модели.

#### Последовательность команд

---
* pip install - r requirements.txt
* Запуск etl-скриптов для формирования тренировочных датасетов и базовой модели
* Заполнение файла .gitignore
* ``` git init ```
* В git должны попасть все файлы кроме датасетов и модели
* ``` git add . ```
* ``` git -m commit "Init" ```

* ``` dvc init ```
* ``` dvc config core.analytics false ```
* ``` dvc remote add -d remote_storage C:\Users\Pavel\PycharmProjects\test_dvc\my_storage```

* ``` dvc add data/raw/data.csv ```
* ``` dvc add data/raw/target.csv ```
* ``` dvc add data/prepared/X_test.csv```
* ``` dvc add data/prepared/X_train.csv```
* ``` dvc add data/prepared/y_train.csv```
* ``` dvc add data/prepared/y_test.csv```
* ``` dvc add model/model ```
* ``` dvc commit ```
* ``` git add . ```
* ``` git -m commit "Experiment basic" ```
* ``` dvc push ```

* Создание побочного эксперимента (от базовой модели)
* ``` git checkout -b "Experiment_A" ```
* Пересчет модели
* ``` dvc commit ```
* ``` git add . ```
* ``` dvc push ```
* ``` git chechout main ```
* ``` dvc checkout ```

* Запуск нового эксперимента