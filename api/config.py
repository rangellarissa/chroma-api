from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    chroma_host: str
    chroma_port: int
    supabase_key: str
    supabase_url: str

settings = Settings()
