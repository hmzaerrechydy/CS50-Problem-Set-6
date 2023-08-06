# CS50 Problem Set 6

Link: https://cs50.harvard.edu/x/2023/psets/6/


## Mario 



Implement a program that prints out a double half-pyramid of a specified height, per the below.

```
$ python mario.py
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

```Python
height = 0

while height <= 0: 
    height = int(input("Height: ")) 

count = 1 

for x in range(height): 
    for s in range(height - count): 
        print(" ", end="")
    
    for y in range(count): 
        print("#", end="")
    
    print("  ", end="")
        
    for h in range(count): 
        print("#", end="")
        
    count += 1
    print()
    
```

First keep prompting the user for a positive number 1 or more using the while loop. 

Let's say the user entered 4 as a height, we loop 4 times and in each iteration we do the following: we print space for the pyramid on the left, and how we figure out how many spaces to print before a hash tag? it's the difference between height and count, count is a variable we update by 1 in each iteration, at the beginning height - count is 3 so we print 3 spaces before the first hash tag in the pyramid on the left, next iteration we update to count to 2 so we print 2 spaces, ... etc. 

Then we print hash tags count times. 

After printing a row of # in the left pyramid we print two spaces then we print a row of # of the right pyramid (we don't need to print spaces here since Python prints # from the right). 

Then at the end we call print() to go back in line for the next row.  


## Credit 


American Express uses 15-digit numbers, MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers.

All American Express numbers start with 34 or 37; most MasterCard numbers start with 51, 52, 53, 54, or 55 (they also have some other potential starting numbers which we won’t concern ourselves with for this problem); and all Visa numbers start with 4.


#### Luhn’s Algorithm: 


So what’s the secret formula? Well, most cards use an algorithm invented by Hans Peter Luhn of IBM. According to Luhn’s algorithm, you can determine if a credit card number is (syntactically) valid as follows:

Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
Add the sum to the sum of the digits that weren’t multiplied by 2.
If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!
That’s kind of confusing, so let’s try an example with David’s Visa: 4003600000000014.

For the sake of discussion, let’s first underline every other digit, starting with the number’s second-to-last digit:

4003600000000014

Okay, let’s multiply each of the underlined digits by 2:

1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2

That gives us:

2 + 0 + 0 + 0 + 0 + 12 + 0 + 8

Now let’s add those products’ digits (i.e., not the products themselves) together:

2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13

Now let’s add that sum (13) to the sum of the digits that weren’t multiplied by 2 (starting from the end):

13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20

Yup, the last digit in that sum (20) is a 0, so David’s card is legit!


#### Solution: 


```Python
try: 
    number = int(input("Number: "))
except: 
    print("Enter a number!")

lst = list(str(number)) 

len = len(lst)
if len < 13 or len > 16: 
    print("INVALID")

sum = 0 
for i in lst[::2]:
    product = int(i) * 2
    if product >= 10: 
        product = list(str(product))
        sum += int(product[0]) + int(product[1])
    else: 
        sum += product  

for j in lst[1::2]: 
    sum += int(j) 

if sum % 10 == 0: 
    first_2 = int(str(number)[:2])
    print(first_2)
    if first_2 == 34 or first_2 == 37: 
        print("American Express")
    if first_2 >= 51 and first_2 <= 55: 
        print("MasterCard")
    elif first_2 >= 40 and first_2 < 50: 
        print("Visa")  

print("sum", sum)
```



## Readability


Implement a program that computes the approximate grade level needed to comprehend some text, per the below.

```
$ python readability.py
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
```

What does it mean, though, for a book to be at a particular reading level?

Well, in many cases, a human expert might read a book and make a decision on the grade (i.e., year in school) for which they think the book is most appropriate. But an algorithm could likely figure that out too!

So what sorts of traits are characteristic of higher reading levels? Well, longer words probably correlate with higher reading levels. Likewise, longer sentences probably correlate with higher reading levels, too.

A number of “readability tests” have been developed over the years that define formulas for computing the reading level of a text. One such readability test is the Coleman-Liau index. The Coleman-Liau index of a text is designed to output that (U.S.) grade level that is needed to understand some text. The formula is

```
index = 0.0588 * L - 0.296 * S - 15.8
```


where L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.


```
$ ./readability
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
```


The text the user inputted has 65 letters, 4 sentences, and 14 words. 65 letters per 14 words is an average of about 464.29 letters per 100 words (because 65 / 14 * 100 = 464.29). And 4 sentences per 14 words is an average of about 28.57 sentences per 100 words (because 4 / 14 * 100 = 28.57). Plugged into the Coleman-Liau formula, and rounded to the nearest integer, we get an answer of 3 (because 0.0588 * 464.29 - 0.296 * 28.57 - 15.8 = 3): so this passage is at a third-grade reading level.



#### Solution: 

```Python
text = input("Text: ")

words = 0 
letters = 0 
sentences = 0 

for word in text.split(): 
    words += 1
    for letter in word:  
        if letter.isalpha(): 
            letters += 1
        if letter in [".", "?", "!"]: 
            sentences += 1

L = letters / words * 100
S = sentences / words * 100 

index = 0.0588 * L - 0.296 * S - 15.8

if index > 16: 
    print("Grade 16+")
elif index < 1: 
    print("Before Grade 1")
else: 
    print("Grade: ", round(index))
```


## DNA


One place where DNA tends to have high genetic diversity is in Short Tandem Repeats (STRs). An STR is a short sequence of DNA bases that tends to repeat consecutively numerous times at specific locations inside of a person’s DNA. The number of times any particular STR repeats varies a lot among individuals. In the DNA samples below, for example, Alice has the STR AGAT repeated four times in her DNA, while Bob has the same STR repeated five times.


What might such a DNA database look like? Well, in its simplest form, you could imagine formatting a DNA database as a CSV file, wherein each row corresponds to an individual, and each column corresponds to a particular STR.

```
name,AGAT,AATG,TATC
Alice,28,42,14
Bob,17,22,19
Charlie,36,18,25
```

The data in the above file would suggest that Alice has the sequence AGAT repeated 28 times consecutively somewhere in her DNA, the sequence AATG repeated 42 times, and TATC repeated 14 times. Bob, meanwhile, has those same three STRs repeated 17 times, 22 times, and 19 times, respectively. And Charlie has those same three STRs repeated 36, 18, and 25 times, respectively.

So given a sequence of DNA, how might you identify to whom it belongs? Well, imagine that you looked through the DNA sequence for the longest consecutive sequence of repeated AGATs and found that the longest sequence was 17 repeats long. If you then found that the longest sequence of AATG is 22 repeats long, and the longest sequence of TATC is 19 repeats long, that would provide pretty good evidence that the DNA was Bob’s. Of course, it’s also possible that once you take the counts for each of the STRs, it doesn’t match anyone in your DNA database, in which case you have no match.

Your task is to write a program that will take a sequence of DNA and a CSV file containing STR counts for a list of individuals and then output to whom the DNA (most likely) belongs.


#### Solution: 


```Python
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
```
