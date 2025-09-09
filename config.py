import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_KEY = os.environ.get('BINANCE_API_KEY')
    API_SECRET = os.environ.get('BINANCE_API_SECRET')
    TESTNET = True
    BASE_URL = 'https://testnet.binancefuture.com'

    # logging config
    LOG_FILE = 'trading_bot.log'
    LOG_LEVEL = 'INFO'