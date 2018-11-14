# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.async_support.base.exchange import Exchange

# -----------------------------------------------------------------------------

try:
    basestring  # Python 3
except NameError:
    basestring = str  # Python 2
import hashlib
import math
import json
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import PermissionDenied
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidAddress
from ccxt.base.errors import InvalidOrder
from ccxt.base.errors import OrderNotFound


class gatecoin (Exchange):

    def describe(self):
        return self.deep_extend(super(gatecoin, self).describe(), {
            'id': 'gatecoin',
            'name': 'Gatecoin',
            'rateLimit': 2000,
            'countries': ['HK'],  # Hong Kong
            'comment': 'a regulated/licensed exchange',
            'has': {
                'CORS': False,
                'createDepositAddress': True,
                'fetchDepositAddress': True,
                'fetchOHLCV': True,
                'fetchOpenOrders': True,
                'fetchOrder': True,
                'fetchTickers': True,
                'withdraw': True,
            },
            'timeframes': {
                '1m': '1m',
                '15m': '15m',
                '1h': '1h',
                '6h': '6h',
                '1d': '24h',
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/28646817-508457f2-726c-11e7-9eeb-3528d2413a58.jpg',
                'api': 'https://api.gatecoin.com',
                'www': 'https://gatecoin.com',
                'doc': [
                    'https://gatecoin.com/api',
                    'https://github.com/Gatecoin/RESTful-API-Implementation',
                    'https://api.gatecoin.com/swagger-ui/index.html',
                ],
            },
            'api': {
                'public': {
                    'get': [
                        'Public/ExchangeRate',  # Get the exchange rates
                        'Public/LiveTicker',  # Get live ticker for all currency
                        'Public/LiveTicker/{CurrencyPair}',  # Get live ticker by currency
                        'Public/LiveTickers',  # Get live ticker for all currency
                        'Public/MarketDepth/{CurrencyPair}',  # Gets prices and market depth for the currency pair.
                        'Public/NetworkStatistics/{DigiCurrency}',  # Get the network status of a specific digital currency
                        'Public/StatisticHistory/{DigiCurrency}/{Typeofdata}',  # Get the historical data of a specific digital currency
                        'Public/TickerHistory/{CurrencyPair}/{Timeframe}',  # Get ticker history
                        'Public/Transactions/{CurrencyPair}',  # Gets recent transactions
                        'Public/TransactionsHistory/{CurrencyPair}',  # Gets all transactions
                        'Reference/BusinessNatureList',  # Get the business nature list.
                        'Reference/Countries',  # Get the country list.
                        'Reference/Currencies',  # Get the currency list.
                        'Reference/CurrencyPairs',  # Get the currency pair list.
                        'Reference/CurrentStatusList',  # Get the current status list.
                        'Reference/IdentydocumentTypes',  # Get the different types of identity documents possible.
                        'Reference/IncomeRangeList',  # Get the income range list.
                        'Reference/IncomeSourceList',  # Get the income source list.
                        'Reference/VerificationLevelList',  # Get the verif level list.
                        'Stream/PublicChannel',  # Get the public pubnub channel list
                    ],
                    'post': [
                        'Export/Transactions',  # Request a export of all trades from based on currencypair, start date and end date
                        'Ping',  # Post a string, then get it back.
                        'Public/Unsubscribe/{EmailCode}',  # Lets the user unsubscribe from emails
                        'RegisterUser',  # Initial trader registration.
                    ],
                },
                'private': {
                    'get': [
                        'Account/CorporateData',  # Get corporate account data
                        'Account/DocumentAddress',  # Check if residence proof uploaded
                        'Account/DocumentCorporation',  # Check if registered document uploaded
                        'Account/DocumentID',  # Check if ID document copy uploaded
                        'Account/DocumentInformation',  # Get Step3 Data
                        'Account/Email',  # Get user email
                        'Account/FeeRate',  # Get fee rate of logged in user
                        'Account/Level',  # Get verif level of logged in user
                        'Account/PersonalInformation',  # Get Step1 Data
                        'Account/Phone',  # Get user phone number
                        'Account/Profile',  # Get trader profile
                        'Account/Questionnaire',  # Fill the questionnaire
                        'Account/Referral',  # Get referral information
                        'Account/ReferralCode',  # Get the referral code of the logged in user
                        'Account/ReferralNames',  # Get names of referred traders
                        'Account/ReferralReward',  # Get referral reward information
                        'Account/ReferredCode',  # Get referral code
                        'Account/ResidentInformation',  # Get Step2 Data
                        'Account/SecuritySettings',  # Get verif details of logged in user
                        'Account/User',  # Get all user info
                        'APIKey/APIKey',  # Get API Key for logged in user
                        'Auth/ConnectionHistory',  # Gets connection history of logged in user
                        'Balance/Balances',  # Gets the available balance for each currency for the logged in account.
                        'Balance/Balances/{Currency}',  # Gets the available balance for s currency for the logged in account.
                        'Balance/Deposits',  # Get all account deposits, including wire and digital currency, of the logged in user
                        'Balance/Withdrawals',  # Get all account withdrawals, including wire and digital currency, of the logged in user
                        'Bank/Accounts/{Currency}/{Location}',  # Get internal bank account for deposit
                        'Bank/Transactions',  # Get all account transactions of the logged in user
                        'Bank/UserAccounts',  # Gets all the bank accounts related to the logged in user.
                        'Bank/UserAccounts/{Currency}',  # Gets all the bank accounts related to the logged in user.
                        'ElectronicWallet/DepositWallets',  # Gets all crypto currency addresses related deposits to the logged in user.
                        'ElectronicWallet/DepositWallets/{DigiCurrency}',  # Gets all crypto currency addresses related deposits to the logged in user by currency.
                        'ElectronicWallet/Transactions',  # Get all digital currency transactions of the logged in user
                        'ElectronicWallet/Transactions/{DigiCurrency}',  # Get all digital currency transactions of the logged in user
                        'ElectronicWallet/UserWallets',  # Gets all external digital currency addresses related to the logged in user.
                        'ElectronicWallet/UserWallets/{DigiCurrency}',  # Gets all external digital currency addresses related to the logged in user by currency.
                        'Info/ReferenceCurrency',  # Get user's reference currency
                        'Info/ReferenceLanguage',  # Get user's reference language
                        'Notification/Messages',  # Get from oldest unread + 3 read message to newest messages
                        'Trade/Orders',  # Gets open orders for the logged in trader.
                        'Trade/Orders/{OrderID}',  # Gets an order for the logged in trader.
                        'Trade/StopOrders',  # Gets all stop orders for the logged in trader. Max 1000 record.
                        'Trade/StopOrdersHistory',  # Gets all stop orders for the logged in trader. Max 1000 record.
                        'Trade/Trades',  # Gets all transactions of logged in user
                        'Trade/UserTrades',  # Gets all transactions of logged in user
                    ],
                    'post': [
                        'Account/DocumentAddress',  # Upload address proof document
                        'Account/DocumentCorporation',  # Upload registered document document
                        'Account/DocumentID',  # Upload ID document copy
                        'Account/Email/RequestVerify',  # Request for verification email
                        'Account/Email/Verify',  # Verification email
                        'Account/GoogleAuth',  # Enable google auth
                        'Account/Level',  # Request verif level of logged in user
                        'Account/Questionnaire',  # Fill the questionnaire
                        'Account/Referral',  # Post a referral email
                        'APIKey/APIKey',  # Create a new API key for logged in user
                        'Auth/ChangePassword',  # Change password.
                        'Auth/ForgotPassword',  # Request reset password
                        'Auth/ForgotUserID',  # Request user id
                        'Auth/Login',  # Trader session log in.
                        'Auth/Logout',  # Logout from the current session.
                        'Auth/LogoutOtherSessions',  # Logout other sessions.
                        'Auth/ResetPassword',  # Reset password
                        'Bank/Transactions',  # Request a transfer from the traders account of the logged in user. This is only available for bank account
                        'Bank/UserAccounts',  # Add an account the logged in user
                        'ElectronicWallet/DepositWallets/{DigiCurrency}',  # Add an digital currency addresses to the logged in user.
                        'ElectronicWallet/Transactions/Deposits/{DigiCurrency}',  # Get all internal digital currency transactions of the logged in user
                        'ElectronicWallet/Transactions/Withdrawals/{DigiCurrency}',  # Get all external digital currency transactions of the logged in user
                        'ElectronicWallet/UserWallets/{DigiCurrency}',  # Add an external digital currency addresses to the logged in user.
                        'ElectronicWallet/Withdrawals/{DigiCurrency}',  # Request a transfer from the traders account to an external address. This is only available for crypto currencies.
                        'Notification/Messages',  # Mark all as read
                        'Notification/Messages/{ID}',  # Mark as read
                        'Trade/Orders',  # Place an order at the exchange.
                        'Trade/StopOrders',  # Place a stop order at the exchange.
                    ],
                    'put': [
                        'Account/CorporateData',  # Update user company data for corporate account
                        'Account/DocumentID',  # Update ID document meta data
                        'Account/DocumentInformation',  # Update Step3 Data
                        'Account/Email',  # Update user email
                        'Account/PersonalInformation',  # Update Step1 Data
                        'Account/Phone',  # Update user phone number
                        'Account/Questionnaire',  # update the questionnaire
                        'Account/ReferredCode',  # Update referral code
                        'Account/ResidentInformation',  # Update Step2 Data
                        'Account/SecuritySettings',  # Update verif details of logged in user
                        'Account/User',  # Update all user info
                        'Bank/UserAccounts',  # Update the label of existing user bank accounnt
                        'ElectronicWallet/DepositWallets/{DigiCurrency}/{AddressName}',  # Update the name of an address
                        'ElectronicWallet/UserWallets/{DigiCurrency}',  # Update the name of an external address
                        'Info/ReferenceCurrency',  # User's reference currency
                        'Info/ReferenceLanguage',  # Update user's reference language
                    ],
                    'delete': [
                        'APIKey/APIKey/{PublicKey}',  # Remove an API key
                        'Bank/Transactions/{RequestID}',  # Delete pending account withdraw of the logged in user
                        'Bank/UserAccounts/{Currency}/{Label}',  # Delete an account of the logged in user
                        'ElectronicWallet/DepositWallets/{DigiCurrency}/{AddressName}',  # Delete an digital currency addresses related to the logged in user.
                        'ElectronicWallet/UserWallets/{DigiCurrency}/{AddressName}',  # Delete an external digital currency addresses related to the logged in user.
                        'Trade/Orders',  # Cancels all existing order
                        'Trade/Orders/{OrderID}',  # Cancels an existing order
                        'Trade/StopOrders',  # Cancels all existing stop orders
                        'Trade/StopOrders/{ID}',  # Cancels an existing stop order
                    ],
                },
            },
            'fees': {
                'trading': {
                    'maker': 0.0025,
                    'taker': 0.0035,
                },
            },
            'commonCurrencies': {
                'BCP': 'BCPT',
                'FLI': 'FLIXX',
                'MAN': 'MANA',
                'SLT': 'SALT',
                'TRA': 'TRAC',
                'WGS': 'WINGS',
            },
            'exceptions': {
                '1005': InsufficientFunds,
                '1008': OrderNotFound,
                '1057': InvalidOrder,
                '1044': OrderNotFound,  # already canceled,
                '1054': OrderNotFound,  # already executed
            },
        })

    async def fetch_markets(self):
        response = await self.publicGetReferenceCurrencyPairs()
        markets = response['currencyPairs']
        result = []
        for i in range(0, len(markets)):
            market = markets[i]
            id = market['tradingCode']
            baseId = market['baseCurrency']
            quoteId = market['quoteCurrency']
            base = self.common_currency_code(baseId)
            quote = self.common_currency_code(quoteId)
            symbol = base + '/' + quote
            precision = {
                'amount': 8,
                'price': market['priceDecimalPlaces'],
            }
            limits = {
                'amount': {
                    'min': math.pow(10, -precision['amount']),
                    'max': None,
                },
                'price': {
                    'min': math.pow(10, -precision['amount']),
                    'max': None,
                },
                'cost': {
                    'min': None,
                    'max': None,
                },
            }
            result.append({
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'active': True,
                'precision': precision,
                'limits': limits,
                'info': market,
            })
        return result

    async def fetch_balance(self, params={}):
        await self.load_markets()
        response = await self.privateGetBalanceBalances()
        balances = response['balances']
        result = {'info': balances}
        for b in range(0, len(balances)):
            balance = balances[b]
            currencyId = balance['currency']
            code = currencyId
            if currencyId in self.currencies_by_id:
                code = self.currencies_by_id[currencyId]['code']
            account = {
                'free': balance['availableBalance'],
                'used': self.sum(
                    balance['pendingIncoming'],
                    balance['pendingOutgoing'],
                    balance['openOrder']
                ),
                'total': balance['balance'],
            }
            result[code] = account
        return self.parse_balance(result)

    async def fetch_order_book(self, symbol, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        orderbook = await self.publicGetPublicMarketDepthCurrencyPair(self.extend({
            'CurrencyPair': market['id'],
        }, params))
        return self.parse_order_book(orderbook, None, 'bids', 'asks', 'price', 'volume')

    async def fetch_order(self, id, symbol=None, params={}):
        await self.load_markets()
        response = await self.privateGetTradeOrdersOrderID(self.extend({
            'OrderID': id,
        }, params))
        return self.parse_order(response.order)

    def parse_ticker(self, ticker, market=None):
        timestamp = int(ticker['createDateTime']) * 1000
        symbol = None
        if market:
            symbol = market['symbol']
        baseVolume = self.safe_float(ticker, 'volume')
        vwap = self.safe_float(ticker, 'vwap')
        quoteVolume = None
        if baseVolume is not None and vwap is not None:
            quoteVolume = baseVolume * vwap
        last = self.safe_float(ticker, 'last')
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_float(ticker, 'high'),
            'low': self.safe_float(ticker, 'low'),
            'bid': self.safe_float(ticker, 'bid'),
            'bidVolume': None,
            'ask': self.safe_float(ticker, 'ask'),
            'askVolume': None,
            'vwap': vwap,
            'open': self.safe_float(ticker, 'open'),
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': None,
            'baseVolume': baseVolume,
            'quoteVolume': quoteVolume,
            'info': ticker,
        }

    async def fetch_tickers(self, symbols=None, params={}):
        await self.load_markets()
        response = await self.publicGetPublicLiveTickers(params)
        tickers = response['tickers']
        result = {}
        for t in range(0, len(tickers)):
            ticker = tickers[t]
            id = ticker['currencyPair']
            market = self.markets_by_id[id]
            symbol = market['symbol']
            result[symbol] = self.parse_ticker(ticker, market)
        return result

    async def fetch_ticker(self, symbol, params={}):
        await self.load_markets()
        market = self.market(symbol)
        response = await self.publicGetPublicLiveTickerCurrencyPair(self.extend({
            'CurrencyPair': market['id'],
        }, params))
        ticker = response['ticker']
        return self.parse_ticker(ticker, market)

    def parse_trade(self, trade, market=None):
        side = None
        orderId = None
        if 'way' in trade:
            side = 'buy' if (trade['way'] == 'bid') else 'sell'
            orderIdField = trade['way'] + 'OrderId'
            orderId = self.safe_string(trade, orderIdField)
        timestamp = int(trade['transactionTime']) * 1000
        if market is None:
            marketId = self.safe_string(trade, 'currencyPair')
            if marketId is not None:
                market = self.find_market(marketId)
        fee = None
        feeCost = self.safe_float(trade, 'feeAmount')
        price = trade['price']
        amount = trade['quantity']
        cost = price * amount
        feeCurrency = None
        symbol = None
        if market is not None:
            symbol = market['symbol']
            feeCurrency = market['quote']
        if feeCost is not None:
            fee = {
                'cost': feeCost,
                'currency': feeCurrency,
                'rate': self.safe_float(trade, 'feeRate'),
            }
        return {
            'info': trade,
            'id': self.safe_string(trade, 'transactionId'),
            'order': orderId,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'type': None,
            'side': side,
            'price': price,
            'amount': amount,
            'cost': cost,
            'fee': fee,
        }

    async def fetch_trades(self, symbol, since=None, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        response = await self.publicGetPublicTransactionsCurrencyPair(self.extend({
            'CurrencyPair': market['id'],
        }, params))
        return self.parse_trades(response['transactions'], market, since, limit)

    def parse_ohlcv(self, ohlcv, market=None, timeframe='1m', since=None, limit=None):
        return [
            int(ohlcv['createDateTime']) * 1000,
            ohlcv['open'],
            ohlcv['high'],
            ohlcv['low'],
            ohlcv['last'],
            ohlcv['volume'],
        ]

    async def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'CurrencyPair': market['id'],
            'Timeframe': self.timeframes[timeframe],
        }
        if limit is not None:
            request['Count'] = limit
        request = self.extend(request, params)
        response = await self.publicGetPublicTickerHistoryCurrencyPairTimeframe(request)
        ohlcvs = self.parse_ohlcvs(response['tickers'], market, timeframe, since, limit)
        return self.sort_by(ohlcvs, 0)

    async def create_order(self, symbol, type, side, amount, price=None, params={}):
        await self.load_markets()
        order = {
            'Code': self.market_id(symbol),
            'Way': 'Bid' if (side == 'buy') else 'Ask',
            'Amount': amount,
        }
        if type == 'limit':
            order['Price'] = price
        if self.twofa:
            if 'ValidationCode' in params:
                order['ValidationCode'] = params['ValidationCode']
            else:
                raise AuthenticationError(self.id + ' two-factor authentication requires a missing ValidationCode parameter')
        response = await self.privatePostTradeOrders(self.extend(order, params))
        # At self point response['responseStatus']['message'] has been verified in handleErrors()
        # to be == 'OK', so we assume the order has indeed been opened
        return {
            'info': response,
            'status': 'open',
            'id': self.safe_string(response, 'clOrderId'),  # response['clOrderId'],
        }

    async def cancel_order(self, id, symbol=None, params={}):
        await self.load_markets()
        response = await self.privateDeleteTradeOrdersOrderID({'OrderID': id})
        return response

    def parse_order_status(self, status):
        statuses = {
            '1': 'open',  # New
            '2': 'open',  # Filling
            '4': 'canceled',
            '6': 'closed',
        }
        if status in statuses:
            return statuses[status]
        return status

    def parse_order(self, order, market=None):
        side = 'buy' if (order['side'] == 0) else 'sell'
        type = 'limit' if (order['type'] == 0) else 'market'
        symbol = None
        if market is None:
            marketId = self.safe_string(order, 'code')
            if marketId in self.markets_by_id:
                market = self.markets_by_id[marketId]
        if market is not None:
            symbol = market['symbol']
        timestamp = int(order['date']) * 1000
        amount = order['initialQuantity']
        remaining = order['remainingQuantity']
        filled = amount - remaining
        price = order['price']
        cost = price * filled
        id = order['clOrderId']
        status = self.parse_order_status(self.safe_string(order, 'status'))
        trades = None
        fee = None
        if status == 'closed':
            tradesFilled = None
            tradesCost = None
            trades = []
            transactions = self.safe_value(order, 'trades')
            feeCost = None
            feeCurrency = None
            feeRate = None
            if transactions is not None:
                if isinstance(transactions, list):
                    for i in range(0, len(transactions)):
                        trade = self.parse_trade(transactions[i])
                        if tradesFilled is None:
                            tradesFilled = 0.0
                        if tradesCost is None:
                            tradesCost = 0.0
                        tradesFilled += trade['amount']
                        tradesCost += trade['amount'] * trade['price']
                        if 'fee' in trade:
                            if trade['fee']['cost'] is not None:
                                if feeCost is None:
                                    feeCost = 0.0
                                feeCost += trade['fee']['cost']
                            feeCurrency = trade['fee']['currency']
                            if trade['fee']['rate'] is not None:
                                if feeRate is None:
                                    feeRate = 0.0
                                feeRate += trade['fee']['rate']
                        trades.append(trade)
                    if (tradesFilled is not None) and(tradesFilled > 0):
                        price = tradesCost / tradesFilled
                    if feeRate is not None:
                        numTrades = len(trades)
                        if numTrades > 0:
                            feeRate = feeRate / numTrades
                    if feeCost is not None:
                        fee = {
                            'cost': feeCost,
                            'currency': feeCurrency,
                            'rate': feeRate,
                        }
        result = {
            'id': id,
            'datetime': self.iso8601(timestamp),
            'timestamp': timestamp,
            'lastTradeTimestamp': None,
            'status': status,
            'symbol': symbol,
            'type': type,
            'side': side,
            'price': price,
            'amount': amount,
            'filled': filled,
            'remaining': remaining,
            'cost': cost,
            'trades': trades,
            'fee': fee,
            'info': order,
        }
        return result

    async def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        await self.load_markets()
        response = await self.privateGetTradeOrders()
        orders = self.parse_orders(response['orders'], None, since, limit)
        if symbol is not None:
            return self.filter_by_symbol(orders, symbol)
        return orders

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = self.urls['api'] + '/' + self.implode_params(path, params)
        query = self.omit(params, self.extract_params(path))
        if api == 'public':
            if query:
                url += '?' + self.urlencode(query)
        else:
            self.check_required_credentials()
            nonce = self.nonce()
            nonceString = str(nonce)
            contentType = '' if (method == 'GET') else 'application/json'
            auth = method + url + contentType + nonceString
            auth = auth.lower()
            signature = self.hmac(self.encode(auth), self.encode(self.secret), hashlib.sha256, 'base64')
            headers = {
                'API_PUBLIC_KEY': self.apiKey,
                'API_REQUEST_SIGNATURE': self.decode(signature),
                'API_REQUEST_DATE': nonceString,
            }
            if method != 'GET':
                headers['Content-Type'] = contentType
                body = self.json(self.extend({'nonce': nonce}, params))
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    async def withdraw(self, code, amount, address, tag=None, params={}):
        self.check_address(address)
        await self.load_markets()
        currency = self.currency(code)
        request = {
            'DigiCurrency': currency['id'],
            'Address': address,
            'Amount': amount,
        }
        response = await self.privatePostElectronicWalletWithdrawalsDigiCurrency(self.extend(request, params))
        return {
            'info': response,
            'id': self.safe_string(response, 'id'),
        }

    async def fetch_deposit_address(self, code, params={}):
        await self.load_markets()
        currency = self.currency(code)
        request = {
            'DigiCurrency': currency['id'],
        }
        response = await self.privateGetElectronicWalletDepositWalletsDigiCurrency(self.extend(request, params))
        result = response['addresses']
        numResults = len(result)
        if numResults < 1:
            raise InvalidAddress(self.id + ' privateGetElectronicWalletDepositWalletsDigiCurrency() returned no addresses')
        address = self.safe_string(result[0], 'address')
        self.check_address(address)
        return {
            'currency': code,
            'address': address,
            'tag': None,
            'info': response,
        }

    async def create_deposit_address(self, code, params={}):
        await self.load_markets()
        currency = self.currency(code)
        request = {
            'DigiCurrency': currency['id'],
        }
        response = await self.privatePostElectronicWalletDepositWalletsDigiCurrency(self.extend(request, params))
        address = response['address']
        self.check_address(address)
        return {
            'currency': code,
            'address': address,
            'tag': None,
            'info': response,
        }

    async def create_user_wallet(self, code, address, name, password, params={}):
        await self.load_markets()
        currency = self.currency(code)
        request = {
            'DigiCurrency': currency['id'],
            'AddressName': name,
            'Address': address,
            'Password': password,
        }
        # not unified yet
        return await self.privatePostElectronicWalletUserWalletsDigiCurrency(self.extend(request, params))

    def handle_errors(self, code, reason, url, method, headers, body):
        if not isinstance(body, basestring):
            return  # fallback to default error handler
        if len(body) < 2:
            return  # fallback to default error handler
        if body.find('You are not authorized') >= 0:
            raise PermissionDenied(body)
        if body[0] == '{':
            response = json.loads(body)
            if 'responseStatus' in response:
                errorCode = self.safe_string(response['responseStatus'], 'errorCode')
                message = self.safe_string(response['responseStatus'], 'message')
                feedback = self.id + ' ' + body
                if errorCode is not None:
                    exceptions = self.exceptions
                    if errorCode in exceptions:
                        raise exceptions[errorCode](feedback)
                    raise ExchangeError(feedback)
                # Sometimes there isn't 'errorCode' but 'message' is present and is not 'OK'
                elif message is not None and message != 'OK':
                    raise ExchangeError(feedback)
