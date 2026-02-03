from collections import deque

'''
v1 version, once correctness has been checked, use a rolling sum instead of looping through deque each time
'''

class SMA:
    def __init__(self):
        self.slow_window = deque([])
        self.fast_window = deque([])
        self.slow_window_length = 50
        self.fast_window_length = 10
        self.prev_fast_SMA = None
        self.prev_slow_SMA = None

    def slow_window_length_check(self):
        slow_check = len(self.slow_window) == self.slow_window_length

        return slow_check
    
    def fast_window_length_check(self):
        fast_check = len(self.fast_window) == self.fast_window_length

        return fast_check

    def update_window(self, close_price):
        self.slow_window.append(close_price)
        self.fast_window.append(close_price)

        if len(self.slow_window) > self.slow_window_length:
            self.slow_window.popleft()

        if len(self.fast_window) > self.fast_window_length:
            self.fast_window.popleft()

    def calculate_slow_SMA(self):
        total = 0
        for x in self.slow_window:
            total+=x
        
        slow_SMA = total/self.slow_window_length

        return slow_SMA
    
    def calculate_fast_SMA(self):
        total = 0
        for x in self.fast_window:
            total+=x
        
        fast_SMA = total/self.fast_window_length

        return fast_SMA

    def long_signal(self, slow_SMA, fast_SMA):

        t_minus_one_check = self.prev_fast_SMA <= self.prev_slow_SMA
        t_check = fast_SMA > slow_SMA

        return t_minus_one_check and t_check
        
    def flat_signal(self, slow_SMA, fast_SMA):
        
        t_minus_one_check = self.prev_fast_SMA >= self.prev_slow_SMA
        t_check = fast_SMA < slow_SMA

        return t_minus_one_check and t_check
    
    def store_states(self, slow_SMA, fast_SMA):
        self.prev_fast_SMA = fast_SMA
        self.prev_slow_SMA = slow_SMA

    def on_bar(self, close_price):
        signal = "NO_CHANGE"
        self.update_window(close_price)

        fast_length_check = self.fast_window_length_check()
        slow_length_check = self.slow_window_length_check()

        if not(fast_length_check and slow_length_check):
            return "NO_CHANGE"
        
        fast_SMA = self.calculate_fast_SMA()
        slow_SMA = self.calculate_slow_SMA()

        if self.prev_fast_SMA is not None and self.prev_slow_SMA is not None:
            long = self.long_signal(slow_SMA, fast_SMA)
            flat = self.flat_signal(slow_SMA, fast_SMA)

            if long:
                signal = "LONG"
            
            elif flat:
                signal = "FLAT"

        self.store_states(slow_SMA, fast_SMA)

        return signal if signal else "NO_CHANGE"
