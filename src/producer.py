import argparse
import asyncio
import random
import string
from typing import NoReturn

import aio_pika
from aio_pika.channel import Channel
from loguru import logger

from conn import connect
from queues import declare_queue
from settings import QUEUES


async def produce(input_mode: bool = False) -> NoReturn:
    """Spawn tasks."""
    async with await connect() as connection:
        channel: Channel = await connection.channel()
        await declare_queue(channel, QUEUES['normal'])
        msg_number = 0

        logger.info('Ready to produce')
        while True:
            if input_mode:
                msg = input('Msg: ')
            else:
                msg_number += 1
                msg = f'#{msg_number} {random.choice(string.ascii_lowercase)}'
                await asyncio.sleep(1)
                logger.info(msg)
            if channel.default_exchange:
                await channel.default_exchange.publish(
                    aio_pika.Message(
                        body=f'{msg}'.encode(),
                    ),
                    routing_key=QUEUES['normal'],
                )

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-I', '--input_mode',
        action='store_true',
    )
    args = parser.parse_args()

    asyncio.run(
        produce(input_mode=args.input_mode),
    )
