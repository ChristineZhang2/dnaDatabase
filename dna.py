import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        # 3 should be script name, database file, and DNA sequence file
        print("Error")
        sys.exit(1)

    # Read database file into a variable
    database = []
    # open csv file in the first command line argument
    with open(sys.argv[1], 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        # iterate through each row in CSV file
        for row in reader:
            # add each row to database list to become list of dictionaries
            database.append(row)

    # Read DNA sequence file into a variable
    with open(sys.argv[2], 'r') as file:  # Fixed typo here
        # read entire file content and remove whitespace
        sequence = file.read().strip()

    # Find longest match of each STR in DNA sequence
    str_counts = {}
    #get all STR names from database
    str_names = list(database[0].keys())[1:]
    # calculate the longest run of each STR in the sequence
    for str_name in str_names:
        # store result of str_counts dictionary
        str_counts[str_name] = longest_match(sequence, str_name)

    # Check database for matching profiles
    match_found = False
    # iterate through each person in the database
    for person in database:
        # compare each STR count
        if all(int(person[str_name]) == str_counts[str_name] for str_name in str_names):
            # print if match found
            print(person['name'])
            match_found = True
            # Exit loop after finding a match
            break
    # print no match if match is not found 
    if not match_found:
        print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
