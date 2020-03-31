import os

QUEUES = {
    'normal': 'normal_queue'
}
HOST = os.environ.get('HOST', '127.0.0.1')
PORT = os.environ.get('PORT', 5672)
USER = {
    'username': os.environ.get('USERNAME', 'user'),
    'password': os.environ.get('PASSWORD', 'password')
}

LOG_FORMAT = '[%(asctime)s][%(name)s][%(levelname)s] %(message)s'