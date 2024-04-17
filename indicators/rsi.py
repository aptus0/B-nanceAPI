class RSI:
    def __init__(self, period=14):
        self.period = period
        self.prices = []
        self.gains = []
        self.losses = []

    def add_price(self, price):
        self.prices.append(price)
        self.calculate_gains_losses()

    def calculate_gains_losses(self):
        if len(self.prices) > 1:
            price_diff = self.prices[-1] - self.prices[-2]
            if price_diff > 0:
                self.gains.append(price_diff)
                self.losses.append(0)
            else:
                self.gains.append(0)
                self.losses.append(abs(price_diff))

            if len(self.gains) > self.period:
                self.gains.pop(0)
                self.losses.pop(0)

    def calculate_rsi(self):
        if len(self.gains) >= self.period:
            avg_gain = sum(self.gains[-self.period:]) / self.period
            avg_loss = sum(self.losses[-self.period:]) / self.period

            if avg_loss == 0:
                return 100
            else:
                rs = avg_gain / avg_loss
                return 100 - (100 / (1 + rs))
        else:
            return None
