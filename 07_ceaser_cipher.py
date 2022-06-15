# Cyclical rotation formula to encrypt/decrypt

def cycleArr(base, shift):
  base_len  = len(base) 
  shift_arr = [None]*base_len
  start     = 0
  while start < base_len:
    shift_arr[shift] = base[start]
    start += 1
    shift += 1
    if shift == base_len:
      shift = 0

  return shift_arr

def encryptMsg(msg, base, cipher, shift):
  enc_msg = ""
  for char in msg:
    if char != " ":
      base_idx = base.index(char.capitalize())
      enc_msg += cipher[base_idx]
    else:
      enc_msg += " "

  print(f'Message: {enc_msg}')
  print(f'Shift:   {shift}')

def decryptMsg(msg, base, cipher):
  dec_msg = ""
  for char in msg:
    if char != " ":
      enc_idx  = cipher.index(char.capitalize())
      dec_msg += base[enc_idx]
    else:
      dec_msg += " "

  print(f'Message: {dec_msg}')

base = (
  '0','1','2','3','4','5','6','7','8','9',
  'A','B','C','D','E','F','G','H','I','J',
  'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
)

which  = input("Do you need (1) Encryption or (2) Decryption (1,2)? ")
msg    = input("What is your message? ")
shift  = int( input("What is the shift? 1-20? ") )
cipher = cycleArr(base, shift)

if which == "1":
  encryptMsg(msg, base, cipher, shift)
else:
  decryptMsg(msg, base, cipher) 
