from itertools import permutations


def to_number(word, d):
    # replace each letter with its digit and join them into one number
    number = ""
    for letter in word:
        number = number + str(d[letter])
    return int(number)


# ---- Take the puzzle as input ----
word1 = input("Enter first word: ").upper()
word2 = input("Enter second word: ").upper()
result = input("Enter result word: ").upper()

# ---- Find the different letters in the puzzle ----
letters = ""
for letter in word1 + word2 + result:
    if letter not in letters:
        letters = letters + letter

# ---- Check that the puzzle is possible ----
if len(letters) > 10:
    print("Too many different letters (maximum is 10)")
else:
    found = False

    # try every way of giving different digits (0-9) to the letters
    for digits in permutations(range(10), len(letters)):
        d = dict(zip(letters, digits))      # e.g. {'S': 9, 'E': 5, ...}

        # the first letter of a word cannot be 0
        if d[word1[0]] == 0 or d[word2[0]] == 0 or d[result[0]] == 0:
            continue

        num1 = to_number(word1, d)
        num2 = to_number(word2, d)
        total = to_number(result, d)

        if num1 + num2 == total:            # the puzzle is solved
            print()
            print("Puzzle:", word1, "+", word2, "=", result)
            print()
            print("Letter values:")
            for letter in letters:
                print(letter, "=", d[letter])
            print()
            print(num1, "+", num2, "=", total)
            found = True
            break

    if not found:
        print("No solution found for this puzzle")
