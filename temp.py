# this is all fcked gotta fix the entry limitations

        # # Reset rolling window on start of new day utc, which is the candle opening at 21
        # if self.Time.hour == 21:
        #     self.quote_bar_window.Reset()
        
        # # Close all open positions if not yet invested before new day
        # if self.Time.hour == 21 and self.Portfolio[self.symbol_audusd].Invested == False:
        #     self.Liquidate(self.symbol_audusd)

        # # If already invested for that day at any time, stop allnew trading for that day, until all positions closed
        # if self.Portfolio[self.symbol_audusd].Invested:
        #     return
        
        
        # if self.Time.hour == 21:
        #     self.currentday == self.Time.day

        # if self.currentday ==  None:
        #     return

        # # If had openeded a position that day or have positions (t/p  s/l ) waiting to be filled of actove positions, dont want to trade
        # if self.Transactions.GetOrderTickets(lambda order_ticket: order_ticket.Time.day == self.currentday):
        #     return