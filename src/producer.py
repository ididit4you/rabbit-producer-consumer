import asyncio
import argparse
import string
import random
import logging
import os

import aio_pika

from settings import QUEUES, LOG_FORMAT

from queues import declare_queue
from rabbit import connect_to_rabbit

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    datefmt='%m/%d/%Y %I:%M:%S %p'
)
logger = logging.getLogger(f'PRODUCER {os.getpid()}')


async def main(input_mode: bool = False):
    async with await connect_to_rabbit() as connection:
        channel = await connection.channel()
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
            await channel.default_exchange.publish(
                aio_pika.Message(
                    body=f'{msg}'.encode()
                ),
                routing_key=QUEUES['normal']
            )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-I', '--input_mode',
        action='store_true',
    )
    args = parser.parse_args()

    asyncio.run(
        main(input_mode=args.input_mode)
    )
