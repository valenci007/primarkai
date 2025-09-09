from binance import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
import logging
from utils import validate_symbol, validate_quantity, validate_price


class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        self.logger = logging.getLogger(__name__)
        self.logger.info("Trading bot initialized")

    def place_market_order(self, symbol, side, quantity):
        """Place market order"""
        try:
            symbol = validate_symbol(symbol)
            quantity = validate_quantity(quantity)

            self.logger.info(f"Placing market order: {side} {quantity} {symbol}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='MARKET',
                quantity=quantity
            )

            self.logger.info(f"Market order placed successfully: {order}")
            return order

        except (BinanceAPIException, BinanceOrderException, ValueError) as e:
            self.logger.error(f"Market order failed: {e}")
            raise

    def place_limit_order(self, symbol, side, quantity, price):
        """Place limit order"""
        try:
            symbol = validate_symbol(symbol)
            quantity = validate_quantity(quantity)
            price = validate_price(price)

            self.logger.info(f"Placing limit order: {side} {quantity} {symbol} @ {price}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='LIMIT',
                timeInForce='GTC',
                quantity=quantity,
                price=price
            )

            self.logger.info(f"Limit order placed successfully: {order}")
            return order

        except (BinanceAPIException, BinanceOrderException, ValueError) as e:
            self.logger.error(f"Limit order failed: {e}")
            raise

    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        """Place stop-limit order (Bonus feature)"""
        try:
            symbol = validate_symbol(symbol)
            quantity = validate_quantity(quantity)
            price = validate_price(price)
            stop_price = validate_price(stop_price)

            self.logger.info(f"Placing stop-limit order: {side} {quantity} {symbol} @ {price} (stop: {stop_price})")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='STOP',
                timeInForce='GTC',
                quantity=quantity,
                price=price,
                stopPrice=stop_price
            )

            self.logger.info(f"Stop-limit order placed successfully: {order}")
            return order

        except (BinanceAPIException, BinanceOrderException, ValueError) as e:
            self.logger.error(f"Stop-limit order failed: {e}")
            raise

    def get_account_info(self):
        """Get account information"""
        try:
            info = self.client.futures_account()
            self.logger.info("Account information retrieved")
            return info
        except BinanceAPIException as e:
            self.logger.error(f"Failed to get account info: {e}")
            raise

    def get_order_status(self, symbol, order_id):
        """Check order status"""
        try:
            status = self.client.futures_get_order(symbol=symbol, orderId=order_id)
            self.logger.info(f"Order status: {status}")
            return status
        except BinanceAPIException as e:
            self.logger.error(f"Failed to get order status: {e}")
            raise