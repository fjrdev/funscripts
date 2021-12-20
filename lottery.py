# how much money would one need have to spend until hitting the eurojackpot [ source https://www.euro-jackpot.net/gewinnverteilung  ]
# the money of the prize tiers is the average price-money of eurojackpot

from random import randrange as rr
from colorama import Fore, Style

class eurojackpot():
  
    def __init__(self) -> None:
      
      self.jackpot_numbers = self.getLotteryNumbers()

      print("jackpot_ticket: ", f'{Fore.CYAN}{self.jackpot_numbers}{Style.RESET_ALL}')
      print("This script will now run until it draws the winning ticket! Then it will display how much money was spend to draw this ticket")


    def getLotteryNumbers(self) -> list:
      
      j_1 = set()
      j_2 = set()

      while len(j_1) < 5:
        j_1.add(rr(1,50))
      while len(j_2) < 2:
        j_2.add(rr(1,10))

      res = list(j_1)
      res.append(list(j_2))

      return res


    def getRoi(self) -> int:
      
      lot = []
      money_spend = 0
      money_earned = 0
      fees = 0.5

      while True:
        
        lot = self.getLotteryNumbers()
        money_spend += 2

        eq_1 = len(set(self.jackpot_numbers[:-1]) & set(lot[:-1]))
        eq_2 = len(set(self.jackpot_numbers[-1]) & set(lot[-1]))

        if eq_1 == 5:
          if eq_2 == 2:
            money_earned += 37503867
            print("You won the jackpot (37,503,867) And spend", f'{Fore.RED}{money_spend:,}€{Style.RESET_ALL}', "to reach the jackpot")
            return f'{(money_earned - fees - money_spend):,}'
          elif eq_2 == 1:
            money_earned += 486548
            print("You won ", f'{Fore.GREEN}486,548€{Style.RESET_ALL}!')
          elif eq_2 == 0:
            money_earned += 101543
            print("You won ", f'{Fore.GREEN}101,543€{Style.RESET_ALL}!')

        elif eq_1 == 4:
          if eq_2 == 2:
            money_earned += 4092
            print("You won ", f'{Fore.GREEN}4,092€{Style.RESET_ALL}!')
          elif eq_2 == 1:
            money_earned += 233
          elif eq_2 == 0:
            money_earned += 104
        
        elif eq_1 == 3:
          if eq_2 == 2:
            money_earned += 56
          elif eq_2 == 1:
            money_earned += 18
          elif eq_2 == 0:
            money_earned += 15

        elif eq_1 == 2:
          if eq_2 == 2:
            money_earned += 20
          elif eq_2 == 1:
            money_earned += 8

        elif eq_1 == 1 and eq_2 == 2:
          money_earned += 10


if __name__ == "__main__":
  ej = eurojackpot()
  print("Your ROI after hitting the Jackpot-ticket", ej.getRoi() + "€")
