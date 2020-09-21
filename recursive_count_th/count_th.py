'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # base case: string is empty or has only 1 letter means 'th' was found zero times
    if len(word) <= 1:
        return 0

    # recursive step: what's going to get me closer to my base case after each pass?
    # if we got until here, it means our string is at least 2 characters long

    # keep track of the number of times there's a match
    count = 0

    # save the characters we'll be checking against
    th = 'th'

    # cut the string down to its first two letters
    two_characters = word[0:2]

    # check whether the first two letters are equal to 'th'
    if th == two_characters:
        # update count by 1
        count += 1
    # shorten the original string by two characters
    word = word[1:]

    return count + count_th(word)
