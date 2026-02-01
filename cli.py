import argparse

parser = argparse.ArgumentParser()
parser.add_argument("data_path")
parser.add_argument("strategy")

args = parser.parse_args()

data_path = args.data_path
strategy = args.strategy
