Binance Futures Trading Bot
A Python-based trading bot for Binance Futures Testnet that supports market, limit, and stop-limit orders with comprehensive logging and error handling.

Features
✅ Market Orders: Instant execution at current market price

✅ Limit Orders: Execution at specified price or better

✅ Stop-Limit Orders: Advanced order type for risk management (Bonus feature)

✅ Account Management: View account balances and positions

✅ Order Status Tracking: Check status of placed orders

✅ Comprehensive Logging: Detailed API request/response logging

✅ Error Handling: Robust exception handling and validation

✅ CLI Interface: User-friendly command-line interface

Prerequisites
Python 3.8+

Binance Testnet account

API key and secret from Binance Testnet

Installation
Clone the repository

bash
git clone <your-repository-url>
cd trading-bot
Create virtual environment

bash
python -m venv trading-bot-env

# On Windows
trading-bot-env\Scripts\activate

# On macOS/Linux
source trading-bot-env/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Setup environment variables

bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your API credentials
BINANCE_API_KEY=your_testnet_api_key_here
BINANCE_API_SECRET=your_testnet_api_secret_here
Binance Testnet Setup
Visit Binance Futures Testnet

Register and activate your testnet account

Generate API key and secret from the API Management section

Fund your testnet account with test USDT

Update your .env file with the generated credentials

Usage
Basic Commands
Place a Market Order

bash
python main.py market BTCUSDT buy 0.001
Place a Limit Order

bash
python main.py limit BTCUSDT sell 0.001 50000
Place a Stop-Limit Order (Bonus)

bash
python main.py stop BTCUSDT buy 0.001 49000 49500
Check Account Information

bash
python main.py account
Check Order Status

bash
python main.py status BTCUSDT 123456789
Command Syntax
text
python main.py <command> [arguments]

Commands:
  market    Place market order
    Usage: market <symbol> <side> <quantity>
    Example: market BTCUSDT buy 0.001

  limit     Place limit order
    Usage: limit <symbol> <side> <quantity> <price>
    Example: limit BTCUSDT sell 0.001 50000

  stop      Place stop-limit order
    Usage: stop <symbol> <side> <quantity> <price> <stop_price>
    Example: stop BTCUSDT buy 0.001 49000 49500

  account   Get account information
    Usage: account

  status    Check order status
    Usage: status <symbol> <order_id>
    Example: status BTCUSDT 123456789
Project Structure
text
trading-bot/
├── main.py              # Main CLI interface
├── bot.py               # Core trading bot functionality
├── utils.py             # Utility functions and validation
├── config.py            # Configuration and environment setup
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (gitignored)
├── trading_bot.log      # Log file (generated at runtime)
└── README.md           # This file
Logging
The bot generates detailed logs in trading_bot.log with timestamps, including:

API requests and responses

Order placement attempts and results

Error messages and exceptions

Account information queries

Sample log output:

text
2024-01-15 10:30:45 - utils - INFO - Trading bot initialized
2024-01-15 10:30:46 - bot - INFO - Placing market order: BUY 0.001 BTCUSDT
2024-01-15 10:30:47 - bot - INFO - Market order placed successfully: {'orderId': 123456789, 'status': 'FILLED'}
Error Handling
The bot includes comprehensive error handling for:

Invalid API credentials

Network connectivity issues

Invalid order parameters

Insufficient balance

Symbol validation errors

Price and quantity validation

Bonus Features Implemented
Stop-Limit Orders: Advanced order type for better risk management

Enhanced CLI: User-friendly command-line interface with help system

Input Validation: Comprehensive validation for all user inputs

Detailed Logging: Extensive logging for debugging and monitoring

Testing
Test with small quantities first to verify functionality

Check your testnet balance before placing orders:

bash
python main.py account
Verify orders on the Binance Testnet Dashboard

Review log files for debugging information

Security Notes
🔒 Never share your API keys or commit them to version control

🔒 The .env file is included in .gitignore to prevent accidental exposure

🔒 Use testnet credentials only - no real funds are at risk

🔒 Consider using API key restrictions in production environments

Troubleshooting
Common Issues:

Invalid API Key: Verify your testnet API credentials in .env

Insufficient Balance: Fund your testnet account with USDT

Invalid Symbol: Use correct symbol format (e.g., BTCUSDT, ETHUSDT)

Network Issues: Check your internet connection and Binance API status

Debug Mode: Check the trading_bot.log file for detailed error messages.

Contributing
Fork the repository

Create a feature branch

Make your changes

Add tests if applicable

Submit a pull request

License
This project is for educational and testing purposes only. Use at your own risk.

Disclaimer
⚠️ This is a testnet trading bot - no real funds are involved
⚠️ Not financial advice - for educational purposes only
⚠️ Use at your own risk - the authors are not responsible for any losses

Support
For issues related to this trading bot, please check:

The log file trading_bot.log for error details

Binance API documentation for specific error codes

Python-Binance library documentation for implementation details

