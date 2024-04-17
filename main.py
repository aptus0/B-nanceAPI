from websocket import WebSocketClient
from indicators.rsi import RSI
from indicators.moving_average import MovingAverage
from indicators.macd import MACD
from utils.binance_api import BinanceAPI
import config

import asyncio

def main():
    symbol = "SEIUSDT"  # Kullanıcıdan işlem yapmak istediği coin'i alın
    usd_amount = float(input("İşlem yapmak istediğiniz miktarı dolar cinsinden girin: "))  # Kullanıcıdan işlem yapmak istediği miktarı dolar cinsinden alın

    # Binance API'ye erişim sağlayın
    binance = BinanceAPI(config.BINANCE_API_KEY, config.BINANCE_SECRET_KEY)

    # Coin'in mevcut fiyatını alın
    current_price = float(binance.get_price(symbol)["price"])

    # Kullanıcının girdiği dolar miktarını, mevcut BTCUSDT fiyatına bölerek işlem yapılacak coin miktarını hesaplayın
    amount = usd_amount / current_price

    # RSI, Hareketli Ortalama ve MACD hesaplayıcıları oluşturun
    rsi_calculator = RSI()
    ma_calculator = MovingAverage(period=14)
    macd_calculator = MACD()

    # WebSocket istemcisini başlatın
    client = WebSocketClient(symbol)

    async def run_client():
        await client.connect()
        print("WebSocket bağlantısı başarıyla kuruldu.")
        print("Gelen verileri işlemeye başlıyorum...")
        async for message in await client.listen():
            # Gelen fiyat verisini alın
            price = float(message)

            # RSI, Hareketli Ortalama ve MACD hesaplayıcılarına fiyatı ekleyin
            rsi_calculator.add_price(price)
            ma_calculator.add_price(price)
            macd_calculator.add_price(price)

            # Hesaplanan değerleri alın
            rsi_value = rsi_calculator.calculate_rsi()
            sma = ma_calculator.calculate_simple_moving_average()
            ema = ma_calculator.calculate_exponential_moving_average(alpha=0.2)
            macd_value = macd_calculator.calculate_macd()
            signal_line = macd_calculator.calculate_signal_line()

            # Hesaplanan değerleri yazdırın
            if rsi_value is not None:
                print("RSI değeri:", rsi_value)
            if sma is not None:
                print("Basit Hareketli Ortalama (SMA):", sma)
            if ema is not None:
                print("Üstel Hareketli Ortalama (EMA):", ema)
            if macd_value is not None:
                print("MACD değeri:", macd_value)
            if signal_line is not None:
                print("MACD sinyal hattı:", signal_line)

            # Alınan sinyalin kazanç potansiyelini hesaplayın
            potential_gain = (current_price - price) / price * 100

            print(f"Alınan sinyal fiyatı: {price}")
            print(f"Kazanç potansiyeli: {potential_gain:.2f}%")

            # İşlem yapılacak coin ve miktarı ile kazanç potansiyelini kullanıcıya gösterin
            print(f"Işlem yapılacak coin: {symbol}")
            print(f"Işlem yapılacak miktar: {amount:.8f}")
            print(f"Eğer işlem açarsanız alınan sinyal fiyatı: {price} ve %100 kazanç elde edebilirsiniz.")

    asyncio.run(run_client())

if __name__ == "__main__":
    main()
