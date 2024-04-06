Cipher = input('Enter E for Encrypt or D for Decrypt: ').lower()


Input = input('Enter a message: ').lower()


Password = input('enter a password: ').lower()


PasswordList = list(Password)


#Keys and Subkeys
SubstitutionKey = []


KEY = []


KEYINT = []


XORSubKey1 = []


XORSubKey2 = []


XORSubKey3 = []


RFSubKey1 = []


RFSubKey2 = []


RFSubKey3 = []


ROUND1PRESET = 0


ROUND2PRESET = 0


ROUND3PRESET = 0


Alphabet = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u": 20, "v":21, "w":22, "x":23, "y":24, "z":25, "!":26, "@":27, "#":28, "$":29, "%":30, "^":31}


AlphabetInverse = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j", 10:"k", 11:"l", 12:"m", 13:"n", 14:"o", 15:"p", 16:"q", 17:"r", 18:"s", 19:"t", 20:"u", 21:"v", 22:"w", 23:"x", 24:"y", 25:"z", 26:"!", 27:"@", 28:"#", 29:"$", 30:"%", 31:"^"}


AlphabetNum = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "11":11, "12":12, "13":13, "14":14, "15":15, "16":16, "17":17, "18":18, "19":19, "20": 20, "21":21, "22":22, "23":23, "24":24, "25":25, "26":26, "27":27, "28":28, "29":29, "30":30, "31":31}


Binary = {"a":'00000', "b":'00001', "c":'00010', "d":'00011', "e":'00100', "f":'00101', "g":'00110', "h":'00111', "i":'01000', "j":'01001', "k":'01010', "l":'01011', "m":'01100', "n":'01101', "o":'01110', "p":'01111', "q":'10000', "r":'10001', "s":'10010', "t":'10011', "u": '10100', "v":'10101', "w":'10110', "x":'10111', "y":'11000', "z":'11001', "!":"11010", "@":'11011', "#":"11100", "$":'11101', "%":"11110", "^":'11111'}


BinarytInverse = {'00000':"a", '00001':"b", '00010':"c", '00011':"d", '00100':"e", '00101':"f", '00110':"g", '00111':"h", '01000':"i", '01001':"j", '01010':"k", '01011':"l", '01100':"m", '01101':"n", '01110':"o", '01111':"p", '10000':"q", '10001':"r", '10010':"s", '10011':"t", '10100':"u", '10101':"v", '10110':"w", '10111':"x", '11000':"y", '11001':"z", "11010":"!", '11011':"@", "11100":"#", '11101':"$", "11110":"%", '11111':"^"}


BinaryNum = {"0":'00000', "1":'00001', "2":'00010', "3":'00011', "4":'00100', "5":'00101', "6":'00110', "7":'00111', "8":'01000', "9":'01001', "10":'01010', "11":'01011', "12":'01100', "13":'01101', "14":'01110', "15":'01111', "16":'10000', "17":'10001', "18":'10010', "19":'10011', "20": '10100', "21":'10101', "22":'10110', "23":'10111', "24":'11000', "25":'11001', "26":"11010", "27":'11011', "28":"11100", "29":'11101', "30":"11110", "31":'11111'}




#Code for allowing Binary messages to be encrypted/decrypted


isBINARY = True
i = 0
count = 0
for i in Input:
 if i == "0":
   count += 1
 elif i == "1":
   count += 1
 elif i == " ":
   count += 1
 if count != len(Input):
 isBINARY = False


def FromBinary():
 if isBINARY:
   global Input
   while len(Input) % 5 != 0:
     if len(Input) % 5 != 0:
       d = len(Input) % 5
       e = 5 - d
       Input = input(f"Please enter a Binary Input that is {e} bits longer or {d} bits shorter: ")
  
   newInput = ""
   finalInput = ""
   j = 0
   while j < len(Input):
     newInput += Input[j]
     if ((j+1) % 5 == 0):
       finalInput += BinarytInverse[newInput]
       newInput = ""
     j += 1
   return finalInput
 else:
   return Input


def ToBinary():
 if isBINARY:
   Input2 = ""
   for i in Input:
     Input2 += Binary[i]
   return Input2
 else:
   return Input






#Code for MAIN KEY to Find the Sub Keys
KEYMAIN = Password
KEYSTRING = Password


KeyLengthCheck = True


while KeyLengthCheck:


   if len(KEYMAIN) < 9:
       KEYSTRING = KEYSTRING [::-1]
       KEYMAIN = KEYMAIN + KEYSTRING
   if len(KEYMAIN) == 9:
     KeyLengthCheck = False


   if len(KEYMAIN) > 9:
       KeyLengthCheck = False
  
KEY = list(KEYMAIN)


#Key to Integer
for i in KEY:
 try:
   KEYINT.append(Alphabet[i])
 except:
   KEYINT.append(int(i))




#Code for Substitution Key (for both substitution and the partial substitution)
for i in range(1000):
 try:
   LastLetter = Alphabet[KEY[(i) % len(KEY)]]
 except:
    LastLetter = AlphabetNum[KEY[(i) % len(KEY)]]
   
 SubstitutionKey.append(AlphabetInverse[((len(KEY))*(i) + LastLetter - 1) % 32])
 SubstitutionKey.append(AlphabetInverse[(len(KEY)*(i) + (LastLetter-2)) % 32])
 SubstitutionKey.append(AlphabetInverse[(len(KEY)*(i) + (LastLetter-3)) % 32])


Substitutionkey = list(dict.fromkeys(SubstitutionKey))


for i in range(40):
 Substitutionkey.append(AlphabetInverse[i % 32])


Substitutionkey = list(dict.fromkeys(Substitutionkey))




#SUBKEY 1
Add = 0
for i in KEYINT:
 Add = Add + i


XORSUBKEY1INT = Add % len(KEY)


try:
 XORSubKey1 = list(Binary[KEY[XORSUBKEY1INT]])
except:
 XORSubKey1 = list(BinaryNum[KEY[XORSUBKEY1INT]])


ROUND1PRESET = Add % 4


RFSubKey1 = Add % 15




#SUBKEY 2
ADD2 = 0
for i in KEYINT:
 if (i % 2) == 0:
   ADD2 = ADD2 + i
 else:
   ADD2 = ADD2


XORSUBKEY2INT = ADD2 % len(KEY)


try:
 XORSubKey2 = list(Binary[KEY[XORSUBKEY2INT]])
except:
 XORSubKey2 = list(BinaryNum[KEY[XORSUBKEY2INT]])




ROUND2PRESET = ADD2 % 4




RFSubKey2 = ADD2 % 15




#SUBKEY 3
MULTIPLY = 1
for i in KEYINT:
 if i == 0:
   MULTIPLY = MULTIPLY + i
 else:
   MULTIPLY = MULTIPLY * i






XORSUBKEY3INT = MULTIPLY % len(KEY)


try:
 XORSubKey3 = list(Binary[KEY[XORSUBKEY3INT]])
except:
 XORSubKey3 = list(BinaryNum[KEY[XORSUBKEY3INT]])




ROUND3PRESET = MULTIPLY % 4


RFSubKey3 = MULTIPLY % 15








#XOR


XORCOUNT = 1
def XOR():
 global Input


 In1 = list(Input)
 global XORCOUNT
 if XORCOUNT == 1:
   In2 = XORSubKey1
 elif XORCOUNT == 2:
   In2 = XORSubKey2
 else:
   In2 = XORSubKey3


 Time = True
 while Time:


   if len(In1) > len(In2):
     In2 = In2 + In2


   elif len(In2) > len(In1):
     In2 = In2[0:len(In1)]


   elif len(In2) == len(In1):
     Time = False


 List1 = []
 for i in In1:
   try:
     List1.append(Binary[i])
   except:
     List1.append(i)


 In1 = List1
  XOR = ''


 for i in In1:
   XORtemp = ''
   LIST = list(i)


    
   for i in range(len(LIST)):
     try: 
       if LIST[i] == '1' and In2[i] == '0':
         XORtemp = XORtemp + '1'


       elif LIST[i] == '0' and In2[i] == '1':
         XORtemp = XORtemp + "1"


       elif LIST[i] == '0' and In2[i] == '0':
         XORtemp = XORtemp + "0"
       elif LIST[i] == '1' and In2[i] == '1':
         XORtemp = XORtemp + "0"
       else:
         XOR = XOR + LIST[i]
     except:
       break
   try:
     XOR = XOR + BinarytInverse[XORtemp]
   except:
     XORtemp = ''   
 Input = XOR


#Substitution
def SUB():
 global Input


 InputList = list(Input)


 Encrypt = Substitutionkey
 Decrypt = {}
 CountDecrypt = 0
 for a in Substitutionkey:
   Decrypt[a] = CountDecrypt
   CountDecrypt = CountDecrypt + 1
  Output = ""


 Time = True


 while Time:


   if Cipher == 'e':


     for j in InputList:


       if j in Alphabet:
        
         Output = Output + Encrypt[Alphabet[j]]
       else:
         Output = Output + j


     Time = False


   elif Cipher == 'd':


     for m in InputList:
      
       if m in Alphabet:
         Output = Output + AlphabetInverse[Decrypt[m]]
       else:
         Output = Output + m


    
     Time = False


   else:
     print('Not an option.')
  Input = Output




RFCOUNT = 1
#Rail fence
def RF():
 global Input
 global RFCOUNT
 m=Input
 if RFCOUNT == 1:
   key = int(RFSubKey1)
 elif RFCOUNT == 2:
   key = int(RFSubKey2)
 else:
   key = int(RFSubKey3)
 encryption_type = Cipher
 if key <= 1:
   encryption_type = 'a'


 if encryption_type == "e":
   grid=[["" for i in range(len(m))] for j in range(key)]
   direction=0
   row=0


   for i in range(len(m)):
     grid[row][i]=m[i]
     if row==0:
       direction=0
     elif row==key-1:
       direction=1
     if direction==0:
       row+=1
     else:
       row-=1
    
   final=[]
   for i in range(key):
     for j in range(len(m)):
           if grid[i][j]!="":
               final.append(grid[i][j])
   c="".join(final)
   Input = c
 elif encryption_type == "d":
   grid=[[" " for i in range(len(m))] for j in range(key)]
   direction=0
   row=0
   new = ""
   for i in range(len(m)):
     grid[row][i]= "@"
     if row==0:
       direction=0
     elif row==key-1:
       direction=1
     if direction==0:
       row+=1
     else:
       row-=1
   count = 0
   for i in range(key):
     for j in range(len(m)):
         if grid[i][j] == "@":
             grid[i][j] = m[count]
             count += 1
   roww = 0
   for i in range(len(m)):
     new += grid[roww][i]
     if roww==0:
       direction=0
     elif roww==key-1:
       direction=1
     if direction==0:
       roww+=1
     else:
       roww -=1
   Input = new






#Relatively Prime Substitution
def RPS():
 global Input
  def gcd(a, b):
     while b != 0:
         a, b = b, a % b
     return a


 def coprime(a, b):
     return gcd(a, b) == 1


 def rpboolean(a):
   i = 0
   list = []
   while i <= a:
     if coprime(i,a):
         list.append(i)
     i += 1
   return(list)


 text = Input


  textlist = list(text)
 keylist = Substitutionkey
 rplist = rpboolean(len(text))


 Encrypt = {}
 Decrypt = {}
 CountEncrypt = 0


 for i in keylist:
   Encrypt[CountEncrypt] = i
   CountEncrypt = CountEncrypt + 1


 CountDecrypt = 0
 for a in keylist:
   Decrypt[a] = CountDecrypt
   CountDecrypt = CountDecrypt + 1


 Output = ""


 Time = True


 while Time: 
   if Cipher == 'e':
  
     for j in textlist:


       if j in Alphabet:
         Output = Output + Encrypt[Alphabet[j]]
       else:
         Output = Output + j
     Time = False


  
     for i in rplist:
       textlist[i] = Output[i]
    


   elif Cipher == "d":
     for t in textlist:
        
         if t in Alphabet:
           Output = Output + AlphabetInverse[Decrypt[t]]
         else:
           Output = Output + t
     Time = False


     for m in rplist:
       textlist[m] = Output[m]
    


   else:
     print("error")
 FINAL = "".join(textlist)
 Input = FINAL












def PRESET0 ():
 XOR()
 SUB()
 RF()
 RPS()
 XOR()
 def PRESET1 ():
 SUB()
 XOR()
 RPS()
 XOR()
 RF()
 
def PRESET2 ():
 RF()
 RPS()
 XOR()
 SUB()
 XOR()
def PRESET3 ():
 XOR()
 RF()
 RPS()
 XOR()
 SUB()


def PRESET0D ():
 XOR()
 RPS()
 RF()
 SUB()
 XOR()
def PRESET1D ():
 RF()
 XOR()
 RPS()
 XOR()
 SUB()
def PRESET2D ():
 XOR()
 SUB()
 XOR()
 RPS()
 RF()
def PRESET3D ():
 SUB()
 XOR()
 RPS()
 RF()
 XOR()


#ENCRYPTION
if Cipher == 'e':
 Input = FromBinary()
#ROUND1
 if ROUND1PRESET == 0:
   PRESET0()




 elif ROUND1PRESET == 1:


   PRESET1()


 elif ROUND1PRESET == 2:


   PRESET2()
  


 elif ROUND1PRESET == 3:
   PRESET3()


  










 #ROUND2
 if ROUND2PRESET == 0:
   XORCOUNT = XORCOUNT + 1
   RFCOUNT = RFCOUNT + 1
   PRESET0()


 elif ROUND2PRESET == 1:
   XORCOUNT = XORCOUNT + 1
   RFCOUNT = RFCOUNT + 1
   PRESET1()


 elif ROUND2PRESET == 2:


   XORCOUNT = XORCOUNT + 1
   RFCOUNT = RFCOUNT + 1
   PRESET2()




 elif ROUND2PRESET == 3:
   XORCOUNT = XORCOUNT + 1
   RFCOUNT = RFCOUNT + 1
   PRESET3()


 #ROUND3
 if ROUND3PRESET == 0:
   XORCOUNT = XORCOUNT + 1
   RFCOUNT = RFCOUNT + 1
   PRESET0()
   Input = ToBinary()




 elif ROUND3PRESET == 1:
   XORCOUNT = XORCOUNT + 1
   RFCOUNT = RFCOUNT + 1
   PRESET1()
   Input = ToBinary()


 elif ROUND3PRESET == 2:
   XORCOUNT = XORCOUNT + 1
   RFCOUNT = RFCOUNT + 1
   PRESET2()
   Input = ToBinary()


 elif ROUND3PRESET == 3:
   XORCOUNT = XORCOUNT + 1
   RFCOUNT = RFCOUNT + 1
   PRESET3()
   Input = ToBinary()




if Cipher == 'd':
 Input = FromBinary()
  #ROUND3
 if ROUND3PRESET == 0:
   XORCOUNT = 3
   RFCOUNT = 3
   PRESET0D()


 elif ROUND3PRESET == 1:
   XORCOUNT = 3
   RFCOUNT = 3
   PRESET1D()


 elif ROUND3PRESET == 2:
   XORCOUNT = 3
   RFCOUNT = 3
   PRESET2D()


 elif ROUND3PRESET == 3:
   XORCOUNT = 3
   RFCOUNT = 3
   PRESET3D()
 #ROUND2
 if ROUND2PRESET == 0:
   XORCOUNT = 2
   RFCOUNT = 2
   PRESET0D()


 elif ROUND2PRESET == 1:
   XORCOUNT =2
   RFCOUNT = 2
   PRESET1D()


 elif ROUND2PRESET == 2:
   XORCOUNT = 2
   RFCOUNT = 2
   PRESET2D()


 elif ROUND2PRESET == 3:
   XORCOUNT = 2
   RFCOUNT =2
   PRESET3D()


#ROUND1
 if ROUND1PRESET == 0:
   XORCOUNT = 1
   RFCOUNT = 1
   PRESET0D()
   Input = ToBinary()




 elif ROUND1PRESET == 1:
   XORCOUNT = 1
   RFCOUNT = 1
   PRESET1D()
   Input = ToBinary()




 elif ROUND1PRESET == 2:
   XORCOUNT = 1
   RFCOUNT = 1
   PRESET2D()
   Input = ToBinary()
  


 elif ROUND1PRESET == 3:
   XORCOUNT = 1
   RFCOUNT = 1
   PRESET3D()
   Input = ToBinary()
print(Input)
