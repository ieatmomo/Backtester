# NEXT CLASS
'''
V1 Exeuction:

'''

class ExecutionV1():
    def __init__(self, fees, slippage, portfolio):
        #TEMPORARLILY ZERO, will pass in 0 later at object creation, will need to change
        self.fees = fees
        self.slippage = slippage
        self.portfolio = portfolio

    def signal_to_action(self, signal, position):

        if position == 0 and signal == "LONG":
            return "BUY"
        
        elif position == 1 and signal == "FLAT":
            return "SELL"
        
        else:
            return "NO_CHANGE"

    #DECIDE FILL PRICE? NEED MORE EXPLANATION
    #BASICALLY, RULE: if strategy says to BUY at bar t, then to avoid look ahead bias I MUST trade at t+1's open price, same for sell
    def decide_fill_price(self, position, signal, next_bar_open):
        if signal == "LONG" and position == 0 or signal == "FLAT" and position == 1:
            fill_price = next_bar_open
            return fill_price
    
        else:
            pass
        

    #ADD TO FILL_PRICE????
    def apply_fees(self):
        pass

    def trade_record(self, timestamp, action, quantity, signal, fill_price):
        #ALL BUYS AND SELLS
        trade_record = {
            "timestamp": timestamp,
            "action": action,
            "fill_price": fill_price,
            "quantity": quantity, #WILL BE 1 for v1
            "signal": signal
        }

        return trade_record

    def execution(self, signal, position, next_bar_open):
        action = self.signal_to_action(signal, position)
        price = self.decide_fill_price(position, signal, next_bar_open)

        if action == "BUY":
            self.portfolio.buy(price)

        elif action == "SELL":
            self.portfolio.sell(price)

        else:
            return "NO_CHANGE"

        