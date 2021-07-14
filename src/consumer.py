import asyncio
from typing import NoReturn

from loguru import logger

from conn import connect
from queues import declare_queue
from settings import QUEUES


async def consume() -> NoReturn:
    async with await connect() as connection:
        channel = await connection.channel()
        queue = await declare_queue(channel, QUEUES['normal'])

        async with queue.iterator() as queue_iter:
            logger.info('Ready to process')
            async for message in queue_iter:
                async with message.process():
                    await asyncio.sleep(1)
                    logger.info(message.body.decode())

                    if queue.name in message.body.decode():
                        break


if __name__ == '__main__':
    asyncio.run(consume())
