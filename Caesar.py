lex = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word = input('Type the statement you want to code:')
wordarr = list(word)
shift = int(input('Type the shift number you want:'))
indx =[]
result = ""
def to_num():
    for letter in word:
        for let in lex:
            if (letter == let):
                indx.append(lex.index(let) + shift)
def to_word():
    new_word = []
    for num in indx:
        shifted = num%26
        new_val = lex[shifted]
        new_word.append(new_val)
    return new_word

if set(wordarr).issubset(lex) is True:
    to_num = to_num()
    to_word = to_word()
    result = result.join(to_word)
    print(result)
else:
    print("Invalid Input")
