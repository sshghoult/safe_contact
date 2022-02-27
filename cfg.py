from os import environ

API_TOKEN = environ.get('api_token', 'hui_voine')
TARGET_CHAT_ID = int(environ.get('chat_id', 'hui_voine'))

# --env-file environment.txt