'''
Orchestrates
'''
from strategies.moving_averages import SMA 
from execution import ExecutionV1
from portfolio import Portfolio
import csv
import pandas as pd
#TAKES ROW OF DATA AND PARSES IT -> SEND TO EXECUTION
#ADD EQUITY CURVES WHEN NEEDED :3

class Loop():
    def __init__(self):
        self.strategy = SMA()
        self.portfolio = Portfolio(1000) #AT THIS POINT JUST INITIALISE CASH AS 1000, CAN CHANGE LATER FROM CLI INPUT
        self.execution = ExecutionV1(0, 0, self.portfolio) #FEES AND SLIPPAGE AT 0 FOR V1
        self.pending_signal = "NO_CHANGE"
        self.trade_record_store = []

    def iterate_bars(self, file_path):
        #data\AAPL_2024-01-03T00%3A00%3A00Z_2024-01-04T00%3A00%3A00Z.csv
        #header = timestamp,open,high,low,close,volume,volume_weighted_average_price,number_of_trades
        with open(file_path) as data:

            reader_obj = csv.reader(data)
            next(reader_obj)

            for row in reader_obj:
                timestamp = row[0]
                open_price = float(row[1])
                close_price = float(row[4])

                trade_record = self.execution.execute(self.pending_signal, self.portfolio.position, open_price, timestamp, 1)
                self.store_records(trade_record)
                self.pending_signal = self.strategy.on_bar(close_price)


    def store_records(self, trade_record):
        if trade_record != "NO_CHANGE":
            self.trade_record_store.append(trade_record)






