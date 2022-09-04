import keyring

keyring_service_id = "TELEGRAM_BOT_APP"
token_key = 'telegram_bot_token_key'
TOKEN = keyring.get_password(keyring_service_id, token_key)
