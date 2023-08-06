import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3: 
        print("Usage: python dna.py data.csv sequence.txt") 

    # TODO: Read database file into a variable
    d = open(sys.argv[1])
    db = csv.DictReader(d)
        
    # TODO: Read DNA sequence file into a variable
    s = open(sys.argv[2]) 
    sq = csv.reader(s)
    sq = list(sq)[0][0]
    
    # TODO: Find longest match of each STR in DNA sequence
    AGATC = longest_match(sq, 'AGATC')
    TTTTTTCT = longest_match(sq, 'TTTTTTCT')
    AATG = longest_match(sq, 'AATG')
    TCTAG = longest_match(sq, 'TCTAG')
    GATA = longest_match(sq, 'GATA')
    TATC = longest_match(sq, 'TATC')
    GAAA = longest_match(sq, 'GAAA')
    TCTG = longest_match(sq, 'TCTG')
    
    
    # TODO: Check database for matching profiles
    count = 0 
    for dict in db: 
        try: 
            # in case the user used large.csv 
            x = [int(dict['AGATC']), int(dict['TTTTTTCT']), int(dict['AATG']), int(dict['TCTAG']), int(dict['GATA']), int(dict['TATC']), int(dict['GAAA']), int(dict['TCTG'])]
            y = [AGATC,TTTTTTCT,AATG,TCTAG,GATA,TATC,GAAA,TCTG] 
        except: 
            # in case the user used small.csv 
            x = [int(dict['AGATC']), int(dict['AATG']), int(dict['TATC'])]
            y = [AGATC,AATG,TATC] 
            
        if x == y: 
            print(dict['name'])
            count += 1 
        
    if count == 0: 
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
