import argparse
import sys
from config import Config
from bot import BasicBot
from utils import setup_logger, validate_symbol, validate_quantity, validate_price


def main():
    # Setup logging
    logger = setup_logger()

    # Initialize bot
    try:
        bot = BasicBot(Config.API_KEY, Config.API_SECRET, Config.TESTNET)
        logger.info("Trading bot started successfully")
    except Exception as e:
        logger.error(f"Failed to initialize bot: {e}")
        sys.exit(1)

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Binance Futures Trading Bot')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Market order parser
    market_parser = subparsers.add_parser('market', help='Place market order')
    market_parser.add_argument('symbol', help='Trading symbol (e.g., BTCUSDT)')
    market_parser.add_argument('side', choices=['buy', 'sell'], help='Order side')
    market_parser.add_argument('quantity', type=float, help='Order quantity')

    # Limit order parser
    limit_parser = subparsers.add_parser('limit', help='Place limit order')
    limit_parser.add_argument('symbol', help='Trading symbol (e.g., BTCUSDT)')
    limit_parser.add_argument('side', choices=['buy', 'sell'], help='Order side')
    limit_parser.add_argument('quantity', type=float, help='Order quantity')
    limit_parser.add_argument('price', type=float, help='Order price')

    # Stop-limit order parser (Bonus)
    stop_parser = subparsers.add_parser('stop', help='Place stop-limit order')
    stop_parser.add_argument('symbol', help='Trading symbol (e.g., BTCUSDT)')
    stop_parser.add_argument('side', choices=['buy', 'sell'], help='Order side')
    stop_parser.add_argument('quantity', type=float, help='Order quantity')
    stop_parser.add_argument('price', type=float, help='Order price')
    stop_parser.add_argument('stop_price', type=float, help='Stop price')

    # Account info parser
    subparsers.add_parser('account', help='Get account information')

    # Order status parser
    status_parser = subparsers.add_parser('status', help='Check order status')
    status_parser.add_argument('symbol', help='Trading symbol')
    status_parser.add_argument('order_id', type=int, help='Order ID')

    args = parser.parse_args()

    try:
        if args.command == 'market':
            order = bot.place_market_order(args.symbol, args.side, args.quantity)
            print(f"Market order placed successfully!")
            print(f"Order ID: {order['orderId']}")
            print(f"Status: {order['status']}")

        elif args.command == 'limit':
            order = bot.place_limit_order(args.symbol, args.side, args.quantity, args.price)
            print(f"Limit order placed successfully!")
            print(f"Order ID: {order['orderId']}")
            print(f"Status: {order['status']}")

        elif args.command == 'stop':
            order = bot.place_stop_limit_order(args.symbol, args.side, args.quantity, args.price, args.stop_price)
            print(f"Stop-limit order placed successfully!")
            print(f"Order ID: {order['orderId']}")
            print(f"Status: {order['status']}")

        elif args.command == 'account':
            account_info = bot.get_account_info()
            print("Account Information:")
            print(f"Total Wallet Balance: {account_info['totalWalletBalance']} USDT")
            print(f"Available Balance: {account_info['availableBalance']} USDT")
            print(f"Unrealized PnL: {account_info['totalUnrealizedProfit']} USDT")

        elif args.command == 'status':
            status = bot.get_order_status(args.symbol, args.order_id)
            print(f"Order Status:")
            print(f"ID: {status['orderId']}")
            print(f"Symbol: {status['symbol']}")
            print(f"Side: {status['side']}")
            print(f"Type: {status['type']}")
            print(f"Status: {status['status']}")
            print(f"Price: {status['price']}")
            print(f"Quantity: {status['origQty']}")
            print(f"Executed: {status['executedQty']}")

        else:
            parser.print_help()

    except Exception as e:
        logger.error(f"Command failed: {e}")
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()