lex = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word = input('Type the statement you want to code:')
wordarr = list(word)
shift = int(input('Type the shift number you want:'))
indx = []
new = []
new_word =""
def decrypting(lex, indx, shift):
    decrypted_list = []
    for i in indx:
        shifted = i%26
        new_val = lex[shifted]
        decrypted_list.append(new_val)
    return decrypted_list
def encrypting():
  for letter in wordarr: # j,o,h,n,d,e,l,
      for i in lex: 
        if (letter == i):
          indx.append(lex.index(i)+shift)
  
if set(wordarr).issubset(lex) is  True:
  encrypt = encrypting()
  decrypt = decrypting(lex=lex, indx=indx, shift=shift)
  new_word = new_word.join(decrypt)
  print(new_word)
else:
    print("Invalid input")

