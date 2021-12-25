# how much money would one need have to spend until hitting the eurojackpot [ source for prize-money: https://www.euro-jackpot.net/gewinnverteilung ]

from random import randrange as rr
from colorama import Fore, Style

class eurojackpot():


    def printProgressBar(self, iteration):

      # attributes
      length = 100
      fill_green = f'{Fore.GREEN}█{Style.RESET_ALL}'
      fill_red = f'{Fore.RED}█{Style.RESET_ALL}'
      fill = fill_green if 0 <= iteration else fill_red

      # define your bar-size here
      display_border = 50000000
          
      # define bar-borders
      roi_in_euro = int(((abs(iteration) * 100) // display_border) // 2)
      current_earning = fill * 50 if (iteration < -display_border) or (display_border < iteration) else fill * roi_in_euro

      if roi_in_euro == 0:
          bar = '-' * ((length // 2) - 1) + fill * 1 + '-' * (length // 2)
      elif iteration < 0:
          bar = '-' * ((length // 2) - roi_in_euro) + current_earning + '-' * (length // 2)
      elif 0 < iteration:
          bar = '-' * (length // 2) + current_earning + '-' * ((length // 2) - roi_in_euro)

      print(f'\r  {-display_border:,}€ |{bar}| {display_border:,}€ | ROI: {iteration:,}€', end = "\r")

  
    def __init__(self) -> None:
      
      self.jackpot_numbers = self.getLotteryNumbers()

      print("jackpot ticket: ", f'{Fore.CYAN}{self.jackpot_numbers}{Style.RESET_ALL}')
      print("This script will now run until it draws the winning ticket and then display how much money was spend to draw this ticket. Smaller winnings will also be recognized.")
      
      # init progressBar
      self.printProgressBar(0)


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

      while True:
        
        lot = self.getLotteryNumbers()
        money_spend += 2

        eq_1 = len(set(self.jackpot_numbers[:-1]) & set(lot[:-1]))
        eq_2 = len(set(self.jackpot_numbers[-1]) & set(lot[-1]))

        if eq_1 == 5:
          if eq_2 == 2:
            money_earned += 37503867
            self.printProgressBar(money_earned - money_spend)
            return f'{(money_earned - money_spend):,}'

          elif eq_2 == 1:
            money_earned += 486548

          elif eq_2 == 0:
            money_earned += 101543

        elif eq_1 == 4:
          if eq_2 == 2:
            money_earned += 4092
          
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

        self.printProgressBar(money_earned - money_spend)


if __name__ == "__main__":
  ej = eurojackpot()
  print("Your ROI after hitting the Jackpot-ticket", ej.getRoi() + "€")
