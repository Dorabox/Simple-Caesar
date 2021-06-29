#List containing alphabet
lex = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#Input of the statement to be coded
word = input('Type the statement you want to code:')
#Turning the string into list
wordarr = list(word)
#Getting the shift number to be applied
shift = int(input('Type the shift number you want:'))
indx =[]
result = ""
#Gets the index of the letter in the alphabet list that exists in the input
def to_num():
  for letter in word:
    for let in lex:
      if (letter == let):
        indx.append(lex.index(let) + shift)
#Shifts the indices and turns them back to their corresponding letter as a list
def to_word():
  new_word = []
  for num in indx:
    shifted = num%26
    new_val = lex[shifted]
    new_word.append(new_val)
  return new_word
#Checks if all input exists in alphabet list
if set(wordarr).issubset(lex) is True:
  to_num = to_num()
  to_word = to_word()
  #Turns the list back into string
  result = result.join(to_word)
  print(result)
else:
  print("Invalid Input")
