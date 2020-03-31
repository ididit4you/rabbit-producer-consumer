async def declare_queue(channel, name='default', auto_delete=True):
    return await channel.declare_queue(
        name,
        auto_delete=auto_delete,
    )
