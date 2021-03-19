'''
Summer 2021 - Pre-release material
Python project to manage a electric mountain railway system

Author: Jared Rigby (JR)
Date: 12/01/2021
'''

# Task 1 - Start of the day
# Variables needed for electric train system
train_times_up = [900, 1100, 1300, 1500]
train_seats_up = [480, 480, 480, 480]
money_up = [0, 0, 0, 0]

train_times_down = [1000, 1200, 1400, 1600]
train_seats_down = [480, 480, 480, 640] # the last train down has 2 extra carridges
money_down = [0, 0, 0, 0]

RETURN_TICKET = 50  # constant value

def display_board():
  print("------------ Trains uphill ------------")
  for x in range(len(train_times_up)):
    print("Time:", train_times_up[x], "\tSeats:", train_seats_up[x])
  print("---------------------------------------")

  print("----------- Trains downhill -----------")
  for x in range(len(train_times_down)):
    print("Time:", train_times_down[x], "\tSeats:", train_seats_down[x])
  print("---------------------------------------")


display_board()
