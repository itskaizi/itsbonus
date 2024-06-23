# Assign statements given by each suspect
statement_1 = not False  # 1 said he is not the thief
statement_2 = (3 == is_thief)  # 2 said 3 is the thief
statement_3 = (4 == is_thief)  # 3 said 4 is the thief
statement_4 = (not (3 == is_thief))  # 4 said 3 is a liar

# Count the number of true statements
true_count = (statement_1 + statement_2 + statement_3 + statement_4)

# Determine the thief
if true_count == 3:
    # Find the false statement
    if statement_1 != True:
        is_thief = 1
    elif statement_2 != True:
        is_thief = 2
    elif statement_3 != True:
        is_thief = 3
    elif statement_4 != True:
        is_thief = 4
    print(f"The true thief is suspect {is_thief}.")
else:
    print("Invalid statements.")