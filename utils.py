import logging
from datetime import datetime


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('trading_bot.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)


def validate_symbol(symbol):
    """Validate trading symbol format"""
    if not symbol.endswith('USDT'):
        raise ValueError("Symbol must end with 'USDT' (e.g., BTCUSDT)")
    return symbol.upper()


def validate_quantity(quantity):
    """Validate quantity format"""
    try:
        quantity = float(quantity)
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        return quantity
    except ValueError:
        raise ValueError("Quantity must be a valid number")


def validate_price(price):
    """Validate price format"""
    try:
        price = float(price)
        if price <= 0:
            raise ValueError("Price must be positive")
        return price
    except ValueError:
        raise ValueError("Price must be a valid number")