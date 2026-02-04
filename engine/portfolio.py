'''
Docstring for engine.portfolio
Stores:
- Cash -> Uninvested money I currently hold
- Position (0 or 1) for v1
- Entry Price???
- equity = cash + position * price
- realised PnL
'''

class Portfolio():
    def __init__(self, cash):
        self.cash = cash
        self.entry_price = None
        self.position = 0
        self.realised_pnl = 0

    def _update_cash(self, money, action):
        if action == "BUY":
            self.cash -= money

        elif action == "SELL":
            self.cash += money
    
    def buy(self, price):
        assert self.position == 0
        self._update_cash(price, "BUY")
        self.position = 1
        self.entry_price = price

    def sell(self, price):
        assert self.position == 1
        self._update_cash(price, "SELL")
        self.calculate_realised_pnl(price)
        self.entry_price = None
        self.position = 0

    def calculate_equity(self, current_price):
        equity = self.cash + self.position * current_price

        return equity

    #PROFIT OR LOSS FROM OPEN POSITIONS (EXISTS ONLY WHEN POSITION == 1)
    def calculate_unrealised_pnl(self, current_price):
        unrealised_pnl = (current_price - self.entry_price) * self.position

        return unrealised_pnl
    
    #PROFIT OR LOSS FROM CLOSED TRADES (ONLY CHANGES ON SELL)
    def calculate_realised_pnl(self, sell_value):
        self.realised_pnl += (sell_value - self.entry_price)

        return self.realised_pnl
    
    def calculate_total_pnl(self, current_price):

        unrealised_pnl = 0

        if self.position == 1:
            unrealised_pnl = (current_price - self.entry_price)  * self.position
        
        total_pnl = self.realised_pnl + unrealised_pnl

        return total_pnl