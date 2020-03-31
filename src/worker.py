import asyncio
import logging
import os

from settings import QUEUES, LOG_FORMAT

from rabbit import connect_to_rabbit
from queues import declare_queue

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    datefmt='%m/%d/%Y %I:%M:%S %p'
)
logger = logging.getLogger(f'WORKER {os.getpid()}')


async def main():
    async with await connect_to_rabbit() as connection:
        channel = await connection.channel()
        queue = await declare_queue(channel, QUEUES['normal'])

        async with queue.iterator() as queue_iter:
            logger.info('Ready to process')
            async for message in queue_iter:
                async with message.process():
                    # Что-то делаем дольше чем Producer генерирует новую задачу
                    await asyncio.sleep(2)
                    logger.info(message.body.decode())

                    if queue.name in message.body.decode():
                        break


if __name__ == "__main__":
    asyncio.run(main())

