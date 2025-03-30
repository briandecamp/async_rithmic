import asyncio
from async_rithmic import RithmicClient, Gateway, InstrumentType, LastTradePresenceBits, DataType

USER = "brian@blackstonebay.com"
PASSWORD = "6DrKgOLV"

async def main():
    client = RithmicClient(user=USER, password=PASSWORD, system_name="Rithmic Test", app_name="my_test_app", app_version="1.0", gateway=Gateway.TEST)
    await client.connect()
    
    account_id = "MY_ACCOUNT"
    
    # Try searching for both MCL and CL
    symbol = "CLN5"
    results = await client.search_symbols(symbol, instrument_type=InstrumentType.FUTURE)
    print(f"\nSearch result for {symbol}:")
    for result in results:
        print(result)
    
    if results:
        for result in results:
            symbol, exchange = result.symbol, result.exchange  # Use the first result
            print(f"Using symbol: {symbol}, exchange: {exchange}")
            
            try:
                security_code = await client.get_front_month_contract(symbol, exchange)
                print(f"Security code for {symbol}: {security_code}")
            except Exception as e:
                print(f"Error getting front month contract for {symbol}: {e}")

    await client.disconnect()

async def market_data_callback(data: dict):
    if data["presence_bits"] & LastTradePresenceBits.LAST_TRADE:
        print("received", data)

async def stream_market_data():
    client = RithmicClient(user=USER, password=PASSWORD, system_name="Rithmic Test", app_name="my_test_app", app_version="1.0", gateway=Gateway.TEST)
    await client.connect()

    # Request front month contract
    symbol, exchange = "CLN5", "NYMEX"
    security_code = await client.get_front_month_contract(symbol, exchange)
    
    # Stream market data
    print(f"Streaming market data for {security_code}")
    data_type = DataType.LAST_TRADE
    client.on_tick += market_data_callback
    await client.subscribe_to_market_data(security_code, exchange, data_type)

    # Wait 10 seconds, unsubscribe and disconnect
    await asyncio.sleep(10)
    await client.unsubscribe_from_market_data(security_code, exchange, data_type)
    await client.disconnect()

asyncio.run(main())