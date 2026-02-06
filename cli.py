import argparse
from engine.loop import Loop 
import pandas as pd


#data\AAPL_2024-01-03T00%3A00%3A00Z_2024-01-04T00%3A00%3A00Z.csv -> Test File Path
parser = argparse.ArgumentParser()
parser.add_argument("data_path")
# parser.add_argument("strategy")
parser.add_argument("starting_cash")

args = parser.parse_args()

data_path = args.data_path
starting_cash = float(args.starting_cash)

#Currently for V1 default to moving_averages, need to refactor code for this to be input
# strategy = args.strategy

engine_loop = Loop(data_path, starting_cash)

engine_loop.iterate_bars()

df = pd.DataFrame(engine_loop.trade_record_store)
equity_df = pd.DataFrame(engine_loop.equity_curve)

df.to_csv('TEST_TRADE_RECORDS.csv')
equity_df.to_csv('TEST_EQUITY_CURVE.csv')