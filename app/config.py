from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_PORT: int=6500
    POSTGRES_PASSWORD: str="examplepassword"
    POSTGRES_USER: str="exampleusername"
    POSTGRES_DB: str="examplename"
    POSTGRES_HOST: str="examplehostname"
    POSTGRES_HOSTNAME: str="127.0.0.1"
    
    class Config:
        env_file = './.env'


settings = Settings()
