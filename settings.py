from pydantic import BaseSettings

class SettingsDB(BaseSettings):
    path_data_raw: str
    path_data_prepared: str
    path_model: str
    path_metrics: str

    max_percent_null: int

    class Config:
        env_file = 'dev.env'
        env_file_encoding = 'utf-8'

settings = SettingsDB()
