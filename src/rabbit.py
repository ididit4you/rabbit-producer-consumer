import aio_pika

from settings import HOST, PORT, USER


async def connect_to_rabbit():
    return await aio_pika.connect_robust(
        f'amqp://{USER["username"]}:{USER["password"]}@{HOST}/',
        port=PORT
    )
