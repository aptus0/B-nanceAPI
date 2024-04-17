class Advanced_RSI_Strategy:
    def __init__(self, rsi_periods=[14], rsi_thresholds=[70, 30], sma_period=50):
        self.rsi_periods = rsi_periods
        self.rsi_thresholds = rsi_thresholds
        self.sma_period = sma_period

    def generate_signal(self, rsi_values, trend_direction):
        signals = []
        for period, rsi_value in zip(self.rsi_periods, rsi_values):
            for threshold in self.rsi_thresholds:
                if rsi_value >= threshold and trend_direction == "Up":
                    signals.append("Sell")
                elif rsi_value <= threshold and trend_direction == "Down":
                    signals.append("Buy")
                else:
                    signals.append("Hold")
        return signals

    def calculate_trend_direction(self, price_history):
        if len(price_history) < self.sma_period:
            return "Sideways"  # SMA hesaplamak için yeterli veri yoksa, trend yönlendirme yapamayız

        sma_values = self.calculate_simple_moving_average(price_history)
        current_sma = sma_values[-1]
        previous_sma = sma_values[-2]

        if current_sma > previous_sma:
            return "Up"
        elif current_sma < previous_sma:
            return "Down"
        else:
            return "Sideways"

    def calculate_simple_moving_average(self, price_history):
        sma_values = []
        for i in range(len(price_history) - self.sma_period + 1):
            sma = sum(price_history[i:i+self.sma_period]) / self.sma_period
            sma_values.append(sma)
        return sma_values
