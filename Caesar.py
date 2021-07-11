print('Welcome to Caesar Cipher 3000!\nPress 1 For Encryption\nPress 2 For Decryption')
#User picks desired operation
oper = int(input('Type the corresponding number for the operation you want to use:'))
#List containing alphabet
lex = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
opera = ''
#Checks desired operation
if oper == 1:
  opera = 'encrypt'
elif oper == 2:
  opera = 'decrypt'
else:
  print('Invalid Input')
  exit()
#Input of the statement to be encrypted/decrypted
word = input('Type the statement you want to {}:'.format(opera))
#Turning the string into list
wordarr = list(word)
#Gets the index of the letter in the alphabet list that exists in the input
def enc_to_num():
  
  for letter in word:
    for let in lex:
      if (letter == let):
        indx.append(lex.index(let) + enc_shift)
#Shifts the indices and turns them back to their corresponding letter as a list
def enc_to_word():
  new_word = []
  for num in indx:
    shifted = num%26
    new_val = lex[shifted]
    new_word.append(new_val)
  return new_word

#Gets the index of the letter in the alphabet list that exists in the input
def dec_to_num():
  
  for letter in word:
    for let in lex:
      if (letter == let):
        indx.append(lex.index(let) - i)
#Shifts the indices and turns them back to their corresponding letter as a list
def dec_to_word():
  new_word = []
  for num in indx:
    shifted = num%26
    new_val = lex[shifted]
    new_word.append(new_val)
  return new_word


if oper == 1:
  #Checks if all input exists in alphabet list
  if set(wordarr).issubset(lex) is True:
    #Getting the shift number to be applied
    enc_shift = int(input('Type the shift number you want:'))
    indx =[]
    result = ""
    enc_to_num = enc_to_num()
    enc_to_word = enc_to_word()
    #Turns the list back into string
    result = result.join(enc_to_word)
    print(result)
  else:
    print("Invalid Input")
else:
  print('Type 1 for yes and 2 for no')
  check = int(input('Do you know the shift of the code?:'))
  if check == 1:
    #Getting the shift number to be applied
    dec_shift = int(input('What is the shift of the code?:'))
    indx =[]
    result = ""
    dec_to_num = dec_to_num()
    dec_to_word = dec_to_word()
    #Turns the list back into string
    result = result.join(dec_to_word)
    print(result)
  elif check == 2:
    print('Displaying all possible combinations:')
    i = 1
    while i <27:
        indx =[]
        result = ""     
        for letter in word:
            for let in lex:
                if (letter == let):
                    indx.append(lex.index(let) - i)
        new_word = []
        for num in indx:
            shifted = num%26
            new_val = lex[shifted]
            new_word.append(new_val)
            
        #Turns the list back into string
        result = result.join(new_word)
        print(result)
        i = i + 1
    else:
        print('Invalid Input')

