import sys
print("""-=-=-=-=-=-=-=-=-=-=-=-=-=-=
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~ Welcome to Pizzaz cinema ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
print()
# This is the list for all the movies
movies = []
# This is where the movies are being defined
# The 2nd last value is the time in minutes, the last value is the room number
one = ["The Shining", "1980", "2h 26m", "10:00", "Room 1", 600, 1]
two = ["Your Name", "2016", "1h 52m", "13:00", "Room 1", 780, 1]
three = ["Fate/Stay Night: Heaven's Feel - III. Spring Song", "2020", "2h 0m",
         "15:00", "Room 1", 900, 1]
four = ["The Night Is Short, Walk on Girl", "2017", "1h 32m", "17:30",
        "Room 1", 1050, 1]
five = ["The Truman Show", "1998", "1h 47m", "19:30", "Room 1", 1170, 1]
six = ["Genocidal Organ", "2017", "1hr 55m", "21:45", "Room 1", 1305, 1]
seven = ["Jacob's Ladder", "1990", "1h 56m", "10:00", "Room 2", 600, 2]
eight = ["Parasite", "2019", "2h 12m", "12:15", "Room 2", 735, 2]
nine = ["The Dark Knight", "2008", "2h 32min", "14:45", "Room 2", 885, 2]
ten = ["Blade Runner 2049", "2017", "2h 44m", "17:45", "Room 2", 1065, 2]
eleven = ["The Mist", "2007", "2h 6m", "21:00", "Room 2", 1260, 2]
twelve = ["Demon Slayer: Mugen Train", "2020", "1h59min", "23:20", "Room 2",
          1400, 2]
thirteen = ["The Matrix", "1999", "2h 16m", "10:00", "Room 3", 600, 3]
fourteen = ["Inception", "2010", "2h 42m", "11:30", "Room 3", 690, 3]
fifteen = ["Shutter Island", "2010", "2h 19m", "14:30", "Room 3", 870, 3]
sixteen = ["Soul", "2020", "1hr 40m", "17:00", "Room 3", 1020, 3]
seventeen = ["Mrs. Brown", "1997", "1h 41min", "19:00", "Room 3", 1140, 3]
eighteen = ["Peppa Pig: Festival of Fun", "2019", "1h 8min", "21:00",
            "Room 3", 1260, 3]
nineteen = ["Titanic", "1997", "3h 30min", "22:15", "Room 3", 1335, 3]
# They are now stored in a single list within their own nested lists
movies.append(one)
movies.append(two)
movies.append(three)
movies.append(four)
movies.append(five)
movies.append(six)
movies.append(seven)
movies.append(eight)
movies.append(nine)
movies.append(ten)
movies.append(eleven)
movies.append(twelve)
movies.append(thirteen)
movies.append(fourteen)
movies.append(fifteen)
movies.append(sixteen)
movies.append(seventeen)
movies.append(eighteen)
movies.append(nineteen)
theatre_one_capacity = 18
theatre_two_capacity = 68
theatre_three_capacity = 21

# Defining the error message for unrecognised swtich options
def unrecognised_switch_options():
    print("Sorry. This program does not recognise the switch options.\n")
    print("Bye.")
    exit()
# Testing to see if switch one exists
try:
    switch_one = sys.argv[1]
except IndexError:
    print("Usage: python3 pizzaz.py [--show <timenow> | --book | --group]")
    exit()
else:
    if switch_one == "--show":  # Checking the input for switch one
        # Defining the m
        def no_more_shows():
            print("Bye.")
            exit()

        def unrecognised_format():
            print("Sorry. This program does not recognise the time format "
                  "entered.\n")
            print("Bye.")
            exit()

        try:
            switch_two = sys.argv[2]
        except IndexError:
            unrecognised_switch_options()
        else:   # Checking that time format is a valid 24-hour time
            if len(switch_two) == 5:
                if switch_two[0].isdigit():
                    if switch_two[1].isdigit():
                        if switch_two[2] == ":":
                            if (switch_two[3].isdigit()
                                    and int(switch_two[3]) < 6):
                                if switch_two[4].isdigit():
                                    if len(switch_two) == 5:
                                        hours = switch_two[0] + switch_two[1]
                                        minute = switch_two[3] + switch_two[4]
                                        mins = int(hours)*60 + int(minute)
                                        if int(mins) < 1440:
                                            # Checking time is at or before
                                            # the latest movie time
                                            if int(mins) <= 1400:
                                                for a in movies:
                                                    printable_movies = []
                                                    # Determining all movies
                                                    # after given time
                                                    if a[-2] > int(mins):
                                                        printable_movies\
                                                            .append(a)
                                                        # Printing movies
                                                        for b in\
                                                            printable_movies:
                                                            print(*b[0:5],
                                                                  sep = ". ")
                                            # Error messages for ivalid or
                                            # missing switch options or times
                                            else:
                                                no_more_shows()
                                        else:
                                            unrecognised_format()
                                    else:
                                        unrecognised_format()
                                else:
                                    unrecognised_format()
                            else:
                                unrecognised_format()
                        else:
                            unrecognised_format()
                    else:
                        unrecognised_format()
                else:
                    unrecognised_format()
            else:
                unrecognised_format()
        print()
        print("Bye.")
        exit()
    elif switch_one == "--book":    # Checking the input for switch one
        try:    # Checking to make sure there is no switch two
            switch_two = sys.argv[2]
        except IndexError:  # I.e. switch two does not exist
            while True:
                movie = input("What is the name of "
                              "the movie you want to watch? ")
                c = 0    # Loop to compare given input to movie titles
                while c < len(movies):
                    d = 0
                    movie_title = movies[c][0]
                    movie_selection = movies[c]
                    c = c + 1
                    if movie.lower() == movie_title.lower():
                        print()
                        while True:  # Loop to ask about popcorn
                            yesno = input("Would you like "
                                          "to order popcorn? Y/N ")
                            if (yesno == "Y" or yesno == "N" or
                                    yesno == "y" or yesno == "n"):
                                if yesno == "Y" or yesno == "y":
                                    while True:  # Repeat quesiton until
                                                 # correct input given
                                        popcorn = input("You want popcorn. "
                                                        "What size Small, "
                                                        "Medium or Large? "
                                                        "(S/M/L) ")
                                        if (popcorn == "S" or popcorn == "M" or
                                            popcorn == "L" or popcorn == "s" or
                                            popcorn == "m" or popcorn == "l"):
                                            print()
                                            print("The seat number for "
                                                  "person 1 is #17")
                                            break
                                        else:
                                            continue
                                        break
                                    break   # Break loop of popcorn question
                                elif yesno == "N" or "n":
                                    print()
                                    print("The seat number for "
                                          "person 1 is #17")
                                    popcorn = "n"
                                    print()
                                    break
                            else:
                                continue
                        d = 1   # Indicates that movie has been selected
                                # so that it can skip if condition on
                                # line 197
                        break
                    else:   # Exception for Spring Song
                        if movie.lower() == "fate/stay night: "\
                                            "heaven's feel - iii":
                            movie = "Fate/Stay Night: "\
                                    "Heaven's Feel - III. Spring Song"
                            continue
                        else:   # Continuing the loop if no match was found
                            continue
                if d == 0:  # If no loop is found
                    print()
                    while True:  # Loop question until y or n given
                        yesno = input("Sorry, we could not find that movie. "
                                      "Enter Y to try again or N to quit. ")
                        if yesno == "Y" or yesno == "y":    #Checking answer
                            print()
                            break
                        elif yesno == "N" or yesno == "n":
                            print()
                            print("Bye.")
                            exit()
                        else:
                            continue
                    continue
                break   # Exiting loop once a correct movie is inputted
        else:   # Error message if switch two exists
            unrecognised_switch_options()
    elif switch_one == "--group":   # Checking the input for switch one
        try:    # Checking to make sure there is no switch two
            switch_two = sys.argv[2]
        except IndexError:  # I.e. switch two does not exist
            # Defining the function to count tickets and popcorn orders
            def pax_and_popcorn():
                print()
                people_having_popcorn = []  # List of popcorn orders to be
                                            # used later when doing pricing
                while True:  # Loop so that each person is asked about popocorn
                    e = 1
                    while e <= pax:  # Loop that counts every person
                        yesno = input("For person {}, would you like to "
                                      "order popcorn? Y/N ".format(str(e)))
                        if (yesno == "Y" or yesno == "N" or yesno == "y" or
                                yesno == "n"):  # Checking their response
                            if yesno == "Y" or yesno == "y":
                                while True:  # Asking for popcorn size
                                    popcorn = input("Person {} wants "
                                                    "popcorn. What size "
                                                    "Small, Medium or Large? "
                                                    "(S/M/L) ".format(str(e)))
                                    if (popcorn == "S" or popcorn == "M" or
                                        popcorn == "L" or popcorn == "s" or
                                            popcorn == "m" or popcorn == "l"):
                                        # Adding a correspondin s ,m ,l to
                                        # the list for each person
                                        people_having_popcorn.append(popcorn)
                                        break
                                    else:
                                        continue
                                    break
                                e = e + 1   # Continuing the loop
                            else:
                                # Adding a correspondin n to the list for each
                                # person
                                people_having_popcorn.append("n")
                                e = e + 1   # Continuing the loop
                        else:
                            continue
                    break
                return(people_having_popcorn)   # Gives a list with each
                                                # persons popcorn preferences
                                                # (n, s, m, l)
            # Defininf an error message if pax exceeds the seating capacity
            def too_many_pax(x):
                print()
                while True:  # Loop to repeat yes no question
                    yesno = input("Sorry, we do not have enough space to "
                                  "hold {} people in the theater room of {} "
                                  "seats. Enter Y to try a different movie "
                                  "name or N to quit. ".format(pax, x))
                    if (yesno == "Y" or yesno == "N" or yesno == "y" or
                            yesno == "n"):
                        if yesno == "Y" or yesno == "y":
                            d = 2   # Inidcates user wants to start again
                                    # so that program will skip if condition
                                    # on line 374
                            print()
                            break
                        else:
                            print()
                            print("Bye.")
                            exit()
                    else:
                        continue
                return(d)
            # Definint function to allocate seats
            def seat_allocation():
                j = 1
                k = 1
                while not j > len(pax_and_popcorn):
                    print("The seat number for person {} is #{}".format(j, k))
                    j = j + 1
                    k = (2*j) - 1

            while True: #Asking for a movie title
                movie = input("What is the name of the movie you want to "
                              "watch? ")
                d = 0         # Defining an arbitrary value te be used later
                              # in an if statement
                for c in range(0, 19):  # Comparing input to movie titles
                    movie_titleone = movies[c][0]
                    movie_selectionone = movies[c]
                    if movie.lower() == movie_titleone.lower():
                        movie_title = movie_titleone
                        movie_selection = movie_selectionone
                        d = 1   # Indicates a movie has been inputted
                        print()
                        while True:     # Loop used to check pax and popcorn
                                        # preferences
                            pax = input("How many persons will you like to "
                                        "book for? ")
                            try:        # Checking pax is an accepted value
                                pax = int(pax)
                            except ValueError:
                                continue
                            else:
                                if pax > 1:
                                    if movie_selection[-1] == 1:
                                        # Checking theatre capacities
                                        if pax < theatre_one_capacity:
                                            h = 0
                                            # Checking popcorn preferences
                                            pax_and_popcorn =\
                                                pax_and_popcorn()
                                            print()
                                            seat_allocation()
                                        else:
                                            # Too many pax message
                                            d = too_many_pax\
                                                (theatre_one_capacity)
                                    elif movie_selection[-1] == 2:
                                        if pax < theatre_two_capacity:
                                            h = 0
                                            pax_and_popcorn =\
                                                pax_and_popcorn()
                                            print()
                                            seat_allocation()
                                        else:
                                            d = too_many_pax\
                                                (theatre_two_capacity)
                                    elif movie_selection[-1] == 3:
                                        if pax < theatre_three_capacity:
                                            h = 0
                                            pax_and_popcorn =\
                                                pax_and_popcorn()
                                            print()
                                            seat_allocation()
                                        else:
                                            d = too_many_pax\
                                                (theatre_three_capacity)
                                    break
                                else:  # If pax is less than two
                                    while True:
                                        yesno = input("Sorry, you must have "
                                                      "at least two "
                                                      "customers for a group "
                                                      "booking. Enter Y to "
                                                      "try again or N "
                                                      "to quit. ")
                                        if (yesno == "Y" or yesno == "N" or
                                                yesno == "y" or yesno == "n"):
                                            if yesno == "Y" or yesno == "y":
                                                break
                                            elif yesno == "N" or yesno == "n":
                                                print()
                                                print("Bye.")
                                                exit()
                                            else:
                                                continue
                    else:    # Exception for Spring Song
                        if movie.lower() == "fate/stay night: heaven's "\
                                            "feel - iii":
                            movie = "Fate/Stay Night: Heaven's Feel "\
                                    "- III. Spring Song"
                            continue
                        else:
                            continue
                if d == 0:  # If input does not match movie title
                    print()
                    while True:
                        yesno = input("Sorry, we could not find that movie. "
                                      "Enter Y to try again or N to quit. ")
                        if yesno == "Y" or yesno == "y":
                            print()
                            break
                        elif yesno == "N" or yesno == "n":
                            print()
                            print("Bye.")
                            exit()
                elif d == 1:  # Movie has been found, now can continue
                    break
                elif d == 2:  # User would like to search for movie again
                    continue
        else:
            unrecognised_switch_options()
    else:
        unrecognised_switch_options()
# Below is where the finance and transactions occur
if sys.argv[1] == "--book":  # Checking the input for switch one
    if movie_selection[-2] < 960:   # Defining ticket price before/after 16:00
        ticket_price = 13.00
    else:
        ticket_price = 15.00
    # Defining the function that prints the total cost without popcorn
    def price_without_popcorn(l, m):
        print("For 1 person, the initial cost is".ljust(34, ' ') + "$" +
              "{:.2f}".format(l).rjust(5, ' '))
        print(" Person 1: Ticket {} 16:00".format(m).ljust(34, ' ') + "$" +
              "{:.2f}".format(l).rjust(5, ' '))
        print()
        print(" No discounts applied".ljust(34, ' ') + "$" + "0.00"
              .rjust(5, ' '))
        print()
        print("The final price is".ljust(34, ' ') + "$" + "{:.2f}".format(l)
              .rjust(5, ' '))
        return(l)
    # Defining the function that prints the total cost with popcorn
    def price_with_popcorn(l, m, n, o):
        final_cost = (o + l)
        print()
        print("For 1 person, the initial cost is".ljust(34, ' ') + "$" +
              "{:.2f}".format(final_cost).rjust(5, ' '))
        print(" Person 1: Ticket {} 16:00".format(m).ljust(34, ' ') + "$" +
              "{:.2f}".format(l).rjust(5, ' '))
        print(" Person 1: {} popcorn".format(n).ljust(34, ' ') + "$" +
              "{:.2f}".format(o).rjust(5, ' '))
        print()
        print(" No discounts applied".ljust(34, ' ') + "$" +
              "0.00".rjust(5, ' '))
        print()
        print("The final price is".ljust(34, ' ') + "$" + "{:.2f}"
              .format(final_cost).rjust(5, ' '))
        return(final_cost)
    # Checking whether popcorn was or wasn't ordered and executing the
    # relevant function with relevant inputs
    if (popcorn == "s" or popcorn == "S" or popcorn == "M" or
            popcorn == "m" or popcorn == "L" or popcorn == "l"):
        if movie_selection[-2] < 960:
            if popcorn == "s" or popcorn == "S":
                final_cost =\
                    price_with_popcorn(ticket_price, "before", "Small", 3.50)
            elif popcorn == "m" or popcorn == "M":
                final_cost =\
                    price_with_popcorn(ticket_price, "before", "Medium", 5.00)
            elif popcorn == "l" or popcorn == "L":
                final_cost =\
                    price_with_popcorn(ticket_price, "before", "Large", 7.00)
        elif movie_selection[-2] > 960:
            if popcorn == "s" or popcorn == "S":
                final_cost =\
                    price_with_popcorn(ticket_price, "from", "Small", 3.50)
            elif popcorn == "m" or popcorn == "M":
                final_cost =\
                    price_with_popcorn(ticket_price, "from", "Medium", 5.00)
            elif popcorn == "l" or popcorn == "L":
                final_cost =\
                    price_with_popcorn(ticket_price, "from", "Large", 7.00)
    else:       # If popcorn wasn't ordered
        if movie_selection[-2] < 960:
            final_cost = price_without_popcorn(ticket_price, "before")
        elif movie_selection[-2] > 960:
            final_cost = price_without_popcorn(ticket_price, "from")
elif sys.argv[1] == "--group":  # Checking the input for switch one
    p = 0   # Defining a value for the loop
    initial_cost = 0    # Defining some key monetary values
    total_popcorn_cost = 0
    total_ticket_cost = 0
    nums_popcorn = 0
    while p < pax:  # Loop used to add up total for all pax based on movie
                    # time and popcorn order for each person
        if pax_and_popcorn[p] == "s" or pax_and_popcorn[p] == "S":
            if movie_selection[-2] < 960:
                individual_cost = 13.00 + 3.50
                popcorn_cost = 3.50
                ticket_cost = 13.00
                nums_popcorn += 1
            elif movie_selection[-2] > 960:
                individual_cost = 15.00 + 3.50
                popcorn_cost = 3.50
                ticket_cost = 15.00
                nums_popcorn += 1
        elif pax_and_popcorn[p] == "m" or pax_and_popcorn[p] == "M":
            if movie_selection[-2] < 960:
                individual_cost = 13.00 + 5.00
                popcorn_cost = 5.00
                ticket_cost = 13.00
                nums_popcorn += 1
            elif movie_selection[-2] > 960:
                individual_cost = 15.00 + 5.00
                popcorn_cost = 5.00
                ticket_cost = 15.00
                nums_popcorn += 1
        elif pax_and_popcorn[p] == "l" or pax_and_popcorn[p] == "L":
            if movie_selection[-2] < 960:
                individual_cost = 13.00 + 7.00
                popcorn_cost = 7.00
                ticket_cost = 13.00
                nums_popcorn += 1
            elif movie_selection[-2] > 960:
                individual_cost = 15.00 + 7.00
                popcorn_cost = 7.00
                ticket_cost = 15.00
                nums_popcorn += 1
        else:
            if movie_selection[-2] < 960:
                individual_cost = 13.00
                popcorn_cost = 0.00
                ticket_cost = 13.00
            elif movie_selection[-2] > 960:
                individual_cost = 15.00
                popcorn_cost = 0.00
                ticket_cost = 15.00
        # Adding up cumulative total
        initial_cost = initial_cost + individual_cost
        # Adding up popcorn and ticket totals so that discounts can be
        # calculated if needed
        total_popcorn_cost = total_popcorn_cost + popcorn_cost
        total_ticket_cost = total_ticket_cost + ticket_cost
        p = p + 1
    # Defining a function to print each persons ticket and popcorn cost
    def individual_expanded_cost(q, r, s, t, u):
        print(" Person {}: Ticket {} 16:00".format(q, r).ljust(34, ' ') +
              "$" + "{:.2f}".format(s).rjust(5, ' '))
        if pax_and_popcorn[q-1] == "n" or pax_and_popcorn[q-1] == "N":
            pass
        else:
            print(" Person {}: {} popcorn".format(q, t).ljust(34, ' ') +
                  "$" + "{:.2f}".format(u).rjust(5, ' '))

    print()
    # Printing the initial cost
    print("For {} persons, the initial cost is".format(pax).ljust(35, ' ') +
          "$" + "{:.2f}".format(initial_cost).rjust(5, ' '))
    v = 1 # Defining values for following loop
    w = 0
    while w < pax:  # Using the functions with given inputs based on popcorn
                    # preferences to print each persons individual cost
        if movie_selection[-2] < 960:
            if pax_and_popcorn[w] == "n" or pax_and_popcorn[w] == "N":
                individual_expanded_cost(v, "before", 13.00, "Large", 7.00)
            else:
                if pax_and_popcorn[w] == "s" or pax_and_popcorn[w] == "S":
                    individual_expanded_cost(v, "before", 13.00, "Small",
                                             3.50)
                elif pax_and_popcorn[w] == "m" or pax_and_popcorn[w] == "M":
                    individual_expanded_cost(v, "before", 13.00, "Medium",
                                             5.00)
                elif pax_and_popcorn[w] == "l" or pax_and_popcorn[w] == "L":
                    individual_expanded_cost(v, "before", 13.00, "Large",
                                             7.00)
        elif movie_selection[-2] > 960:
            if pax_and_popcorn[w] == "n" or pax_and_popcorn[w] == "N":
                individual_expanded_cost(v, "from", 15.00, "Large", 7.00)
            else:
                if pax_and_popcorn[w] == "s" or pax_and_popcorn[w] == "S":
                    individual_expanded_cost(v, "from", 15.00, "Small", 3.50)
                elif pax_and_popcorn[w] == "m" or pax_and_popcorn[w] == "M":
                    individual_expanded_cost(v, "from", 15.00, "Medium", 5.00)
                elif pax_and_popcorn[w] == "l" or pax_and_popcorn[w] == "L":
                    individual_expanded_cost(v, "from", 15.00, "Large", 7.00)
        w = w + 1
        v = v + 1
    if initial_cost <= 100:  # Checking whether the group gets a discount
        print()
        print(" No discounts applied".ljust(34, ' ') + "$" + "0.00"
              .rjust(5, ' '))
        print()
        print("The final price is".ljust(34, ' ') + "$" + "{:.2f}"
              .format(initial_cost).rjust(5, ' '))
        final_cost = initial_cost # Since no discount, final = initial
    else:   # Group will get discount
        popcorn_discount = total_popcorn_cost*0.2   # Calculating discount
        ticket_discount = total_ticket_cost*0.1
        final_cost = initial_cost - popcorn_discount - ticket_discount
        ticket_discount = round(ticket_discount, 2)
        popcorn_discount = round(popcorn_discount, 2)
        print()
        # Printing details of discount
        print(' Discount applied tickets x{}'.format(len(pax_and_popcorn))
              .ljust(33, ' ') + '-$' + '{:.2f}'.format(ticket_discount)
              .rjust(5, ' '))
        print(' Discount applied popcorn x{}'.format(nums_popcorn)
              .ljust(33, ' ') + '-$' + '{:.2f}'.format(popcorn_discount)
              .rjust(5, ' '))
        print()
        print("The final price is".ljust(34, ' ') + "$" + "{:.2f}"
              .format(final_cost).rjust(5, ' '))
final_cost = float(final_cost)  # Formatting final cost to dollars and cents
final_cost = format(final_cost, '.2f')
print()
# This is where we handle the transaction and change
while True:
    # Inputting payment and formatting it
    amount_paid = float(input("Enter the amount paid: $"))
    amount_paid = format(amount_paid, '.2f')
    # Checking that the smallest increment is 5 cents
    if int(amount_paid[-1]) == 0 or int(amount_paid[-1]) == 5:
        amount_paid = round(float(amount_paid), 2)
        # If payment is exact, no change is given
        if float(amount_paid) == float(final_cost):
            print("Change: $0")
            print()
            print("Bye.")
            exit()
        # If payment is correct (i.e enough is paid and divisible by 5c)
        elif float(amount_paid) > float(final_cost):
            notes_and_coins = []
            change = float(amount_paid) - float(final_cost)
            total_change = change
            # Defining each note and coin
            five_cent = 0.05
            ten_cent = 0.10
            twenty_cent = 0.20
            fifty_cent = 0.50
            one_dollar = 1.00
            two_dollar = 2.00
            five_dollar = 5.00
            ten_dollar = 10.00
            twenty_dollar = 20.00
            fifty_dollar = 50.00
            hundred_dollar = 100.00
            # Defining a function to add the change to a list to print later
            def counting_change(x, y, z):
                notes_and_coins.append(x)
                z = z - y
                return(z)

            while True:  # A loop that checks whether a note or coin is the
                         # biggest amount that can currently be given as
                         # change, and then repeats until there is no more
                         # change to give
                change = round(change, 2)
                if hundred_dollar <= change:
                    change = counting_change("$100", 100.00, change)
                elif fifty_dollar <= change:
                    change = counting_change("$50", 50.00, change)
                elif twenty_dollar <= change:
                    change = counting_change("$20", 20.00, change)
                elif ten_dollar <= change:
                    change = counting_change("$10", 10.00, change)
                elif five_dollar <= change:
                    change = counting_change("$ 5", 5.00, change)
                elif two_dollar <= change:
                    change = counting_change("$ 2", 2.00, change)
                elif one_dollar <= change:
                    change = counting_change("$ 1", 1.00, change)
                elif fifty_cent <= change:
                    change = counting_change("50c", 0.50, change)
                elif twenty_cent <= change:
                    change = counting_change("20c", 0.20, change)
                elif ten_cent <= change:
                    change = counting_change("10c", 0.10, change)
                elif five_cent <= change:
                    change = counting_change("5 c", 0.05, change)
                else:
                    break
            z = 0
            # Formatting the total change to dollars and cents and printing
            total_change = format(total_change, '.2f')
            print("Change: ${}".format(total_change))
            # A loop to print the itemised change
            while z < len(notes_and_coins):
                # Checking if note or coin hasn't already been printed
                if notes_and_coins[z] != notes_and_coins[z-1]:
                    print("{}: ".format(notes_and_coins[z]).rjust(6, ' ') +
                          "{}".format(notes_and_coins.count
                              (notes_and_coins[z])))
                    z += 1
                else:
                    z += 1
        else:   # Error message if payment is short
            difference = float(final_cost) - float(amount_paid)
            print("The user is ${:.2f} short. Ask the user to pay the "
                  "correct amount.".format(difference))
            continue
        break
    else:   # Error message if smallest increment is not 5c
        print("The input given is not divisible by 5c. Enter a valid "
              "payment.")
        continue
print()
# Closing of program with message
print("Bye.")
exit()
