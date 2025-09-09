import logging
from datetime import datetime

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('trading_bot.log'),
            logging.StreamHandler()]
    )
    return logging.getLogger(__name__)

def validate_symbol(symbol):
    """Validate Trading Symbol formatches Binance API"""
    if not symbol.endswith('USDT'):
        raise ValueError('Symbol must end with USDT')
    return symbol.upper()

def validate_quantity(quantity):
    """Validate quantity is a positive integer"""
    if not isinstance(quantity, int):
        raise ValueError('Quantity must be an integer')
    if quantity <= 0:
        raise ValueError('Quantity must be positive')
    return quantity

def validate_price(price):
    """Validate price is a positive float"""
    if not isinstance(price, float):
        raise ValueError('Price must be a float')
    if price <= 0:
        raise ValueError('Price must be positive')
    return price
