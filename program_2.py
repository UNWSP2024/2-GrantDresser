def average_age():
    # Get User Input
    age1 = int (input("Enter age of friend 1:16 "))
    age2 = int (input("Enter age of friend 2:17 "))
    age3 = int (input("Enter age of friend 3:19 "))
    age4 = int (input("Enter age of friend 4:16 "))
    age5 = int (input("Enter age of friend 5:18 "))


    # Sum ages
    total_age = age1 + age2 + age3 + age4 + age5

    # Average the ages
    average = total_age / 5
    # Print the results
    print("The average age is:", average)

# Line which calls the above function.
average_age()