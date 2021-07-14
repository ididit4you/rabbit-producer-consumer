import aio_pika
from aio_pika.connection import ConnectionType

from settings import conf


async def connect() -> ConnectionType:
    """Creates connection to Rabbit instance."""
    password = conf.PASSWORD.get_secret_value()
    conn_uri = f'amqp://{conf.USERNAME}:{password}@{conf.HOST}/'
    return await aio_pika.connect_robust(
        conn_uri,
        port=conf.PORT,
    )
