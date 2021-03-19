"""
Summer 2021 - Pre-release material
Python project to manage a electric mountain railway system

Author: Jared Rigby (JR)
Most recent update: 19/03/2021
"""

# Task 1 - Start of the day
train_times_up = [900, 1100, 1300, 1500]    # Train times for going up the mountain
train_seats_up = [480, 480, 480, 480]       # Number of seats available up the mountain
money_up = [0, 0, 0, 0]                     # The amount of money made by each train up the mountain

train_times_down = [1000, 1200, 1400, 1600] # Train times for going up the mountain
train_seats_down = [480, 480, 480, 640]     # Number of seats available up the mountain
money_down = [0, 0, 0, 0]                   # The amount of money made by each train up the mountain

RETURN_TICKET = 50  # CONSTANT - the price of a return ticket
JOURNEYS_EACH_DAY = len(train_times_up) # CONSTANT - the number of return journeys each day


# Reusable procedure which lists all train times and the seats available
def display_board():
    print("\n------------ Trains uphill ------------")
    for x in range(len(train_times_up)):
        print("Time:", train_times_up[x], "\tSeats:", train_seats_up[x])
    print("----------- Trains downhill -----------")
    for x in range(len(train_times_down)):
        print("Time:", train_times_down[x], "\tSeats:", train_seats_down[x])


display_board() # Use the display_board() procedure to list all train times and seats for the day

# Task 2 - Purchasing tickets
customer_type = 0   # Stores the type of customer booking (single or group)

tickets_needed = 0  # Stores the user input for the number of tickets needed
free_tickets = 0    # Stores how many free tickets the user will receive
total_price = 0     # Stores the total price of the transaction

departure_time = 0  # Will store user input for time up the mountain
return_time = 0     # Will store user input for time down the mountain

departure_index = -1    # Stores the array element for the train up the mountain
return_index = -1       # Stores the array element for the train down the mountain

enough_seats_up = False     # Flag variable for available seats
enough_seats_down = False   # Flag variable for available seats

# Shopping loop - will run until the end of the day calculation is requested
while customer_type != 3:
    customer_type = 0   # Reset customer_type for each transaction
    enough_seats_up = False     # Reset flags for each transaction
    enough_seats_down = False   # Reset flags for each transaction

    print("\nPlease make a selection")
    print("--------------------------")
    print("1 - Single customer booking")
    print("2 - Group customer booking")
    print("3 - To close the ticket booth and output today's totals\n")

    while customer_type != 1 and customer_type != 2 and customer_type != 3:
        customer_type = int(input("Please enter 1, 2 or 3: "))



    # Validation loop - will only exit when the customer selects a possible number of tickets
    while enough_seats_up is False or enough_seats_down is False:
        # Reset all validation variables
        tickets_needed = 0
        departure_index = -1
        return_index = -1

        if customer_type == 1:
            print("Single customer booking")
            tickets_needed = 1  # Single bookings only need 1 ticket
        elif customer_type == 2:
            # Input and validation for the number of tickets needed for a group booking
            print("Group customer booking")
            while tickets_needed < 2:
                tickets_needed = int(input("Please enter the number of tickets required... "))
        else:
            print("Calculating today's totals")
            break

        # Input and validation of the train times
        while departure_index == -1 or return_index == -1:

            # Ask the user to enter train times
            departure_time = int(input("Please enter the departure time... "))
            return_time = int(input("Please enter the return time... "))

            # Check if the journey up the mountain exists
            for x in range(JOURNEYS_EACH_DAY):
                if departure_time == train_times_up[x]:
                    print("Train at", departure_time, "found!")
                    departure_index = x

            if departure_index == -1:
                print("No train found at", departure_time)

            # Check if the journey down the mountain exists
            for y in range(JOURNEYS_EACH_DAY):
                if return_time == train_times_down[y]:
                    print("Train at", return_time, "found!")
                    return_index = y

            if return_index == -1:
                print("No train found at", return_time)

            # Check the logical order of the journeys (up happens before down)
            if departure_time > return_time:
                return_index = -1
                departure_index = -1
                print("Error - you can't depart after you return")

        # Check enough seats are available
        if train_seats_up[departure_index] - tickets_needed < 0:
            print("Error - not enough seats available up the mountain")
        else:
            enough_seats_up = True

        if train_seats_down[return_index] - tickets_needed < 0:
            print("Error - not enough seats available down the mountain")
        else:
            enough_seats_down = True

    # Calculate the price
    if tickets_needed < 10:
        total_price = tickets_needed * RETURN_TICKET
    elif tickets_needed >= 10:
        free_tickets = tickets_needed // 10
        if free_tickets > 8:  # Set an upper limit for free tickets
            free_tickets = 8
        total_price = (tickets_needed * RETURN_TICKET) - (free_tickets * RETURN_TICKET)

    # Do not show the invoice for customer type 3
    if customer_type != 3:
        print("\n------ CUSTOMER INVOICE ------")
        print("Tickets:", tickets_needed)
        print("Total price:", total_price)
        print("Free tickets:", free_tickets)
        print("------------------------------\n")

    # Update the data for the display board
    train_seats_up[departure_index] = train_seats_up[departure_index] - tickets_needed
    train_seats_down[return_index] = train_seats_down[return_index] - tickets_needed

    money_up[departure_index] = money_up[departure_index] + (total_price / 2)
    money_down[return_index] = money_down[return_index] + (total_price / 2)

    # Output the display board with the latest values
    display_board()
