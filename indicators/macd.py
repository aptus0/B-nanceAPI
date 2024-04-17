class MACD:
    def __init__(self, short_period=12, long_period=26, signal_period=9):
        self.short_period = short_period
        self.long_period = long_period
        self.signal_period = signal_period
        self.prices = []

    def add_price(self, price):
        self.prices.append(price)
        if len(self.prices) > self.long_period:
            self.prices.pop(0)

    def calculate_macd(self):
        if len(self.prices) < self.long_period:
            return None
        short_ema = self.calculate_exponential_moving_average(self.short_period)
        long_ema = self.calculate_exponential_moving_average(self.long_period)
        return short_ema - long_ema

    def calculate_signal_line(self):
        if len(self.prices) < self.long_period:
            return None
        macd_values = []
        for i in range(self.long_period - self.signal_period, len(self.prices)):
            short_ema = self.calculate_exponential_moving_average(self.short_period, start_index=i - self.signal_period)
            long_ema = self.calculate_exponential_moving_average(self.long_period, start_index=i - self.signal_period)
            macd_values.append(short_ema - long_ema)
        return self.calculate_exponential_moving_average(self.signal_period, values=macd_values)

    def calculate_exponential_moving_average(self, period, values=None, start_index=0):
        if values is None:
            values = self.prices[start_index:]
        alpha = 2 / (period + 1)
        ema = values[0]
        for value in values[1:]:
            ema = alpha * value + (1 - alpha) * ema
        return ema
