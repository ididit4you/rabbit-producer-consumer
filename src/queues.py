from aio_pika.channel import Channel
from aio_pika.queue import Queue


async def declare_queue(channel: Channel, name: str, auto_delete: bool = True) -> Queue:
    """Declare queues."""
    return await channel.declare_queue(
        name,
        auto_delete=auto_delete,
    )
