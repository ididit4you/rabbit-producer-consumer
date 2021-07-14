from pydantic import BaseSettings
from pydantic.types import SecretStr


class RabbitConfig(BaseSettings):
    """Project settings."""

    HOST: str
    PORT: int = 5672
    USERNAME: str
    PASSWORD: SecretStr

    class Config:
        env_prefix = 'RABBITMQ_'


QUEUES = {
    'normal': 'normal_queue',
}

conf = RabbitConfig()
