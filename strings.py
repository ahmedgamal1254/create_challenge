"""
                The idea of this problem
                split string to small string equals
Take a text from the user and then divide this text into equal pieces so that the beginning
and end of each text are the same in all texts
If the text is not indivisible into pieces of equal size
print a message to him "This text cannot be divided into similar pieces"

if no cannot divide string print message "This text cannot be divided into similar pieces"

exmaples

input 1 ==> s="anaanaanaana"
output ==> SOS SPS SQS SOR
explain :-
    char in index 2 = char in index 3 and char in index 0 = char in index=2
    :- this string is able to divide ==> |s| = 12 / 3 ==> rslt 4 sub string

input 2 ==> s="anaanaanaana"
output ==> ana ana ana ana

input 3 ==> s="sossoaasosa"
output ==> These texts cannot be divided into pieces because the small texts are not equal

note :-
    As long as the text is not divisible, you can print any message you find appropriate
"""
s='SOSSPSSQSSOR'
def split_string(s):
    val = 0
    for i in range(len(s)):
        if i < len(s) - 1:
            if s[i] == s[i + 1]:
                val = i + 1
                break
    count=val-0
    if val == 0:
        print('This text cannot be divided into similar pieces')
    elif s[val] != s[0]:
        print(
            'This text cannot be divided into similar pieces because The first and last letter of the text are not the same')
    elif len(s) % count != 0:
        print('These texts cannot be divided into pieces because the small texts are not equal')
    else:
        for i in range(0, len(s), val):
            print(s[i:i + val], end=' ')
split_string(s) # SOS SPS SQS SOR
split_string('anaanaanaana') # ana ana ana ana
split_string('sossoaasosa') # These texts cannot be divided into pieces because the small texts are not equal
split_string('dhmeddahmeddahmed') # These texts cannot be divided into pieces because the small texts are not equal