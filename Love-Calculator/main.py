# logic:

def calculate_love_score(name1, name2):
    # Convert both names to lowercase for case-insensitive counting
    combined_names = (name1 + name2).lower()

    # Calculate the total number of times the letters in "TRUE" appear
    true_count = combined_names.count('t') + combined_names.count('r') + \
                 combined_names.count('u') + combined_names.count('e')

    # Calculate the total number of times the letters in "LOVE" appear
    love_count = combined_names.count('l') + combined_names.count('o') + \
                 combined_names.count('v') + combined_names.count('e')

    # Combine the counts to form the love score
    love_score = int(str(true_count) + str(love_count))

    print(f"Your love score is {love_score}")

# Example usage
name1 = "Chhun Lay"
name2 = "Romdoul"
calculate_love_score(name1, name2)
