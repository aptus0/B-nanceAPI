class MovingAverage:
    def __init__(self, period):
        self.period = period
        self.prices = []

    def add_price(self, price):
        self.prices.append(price)
        if len(self.prices) > self.period:
            self.prices.pop(0)

    def calculate_simple_moving_average(self):
        if len(self.prices) < self.period:
            return None
        return sum(self.prices) / self.period

    def calculate_exponential_moving_average(self, alpha):
        if len(self.prices) < self.period:
            return None
        ema = self.prices[0]
        for price in self.prices[1:]:
            ema = alpha * price + (1 - alpha) * ema
        return ema
