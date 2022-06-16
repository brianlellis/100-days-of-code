import sys
import random
import string

def randAlpha():
  return random.choice(string.ascii_letters)

def randNum():
  return str( random.randint(0,9) )

def randSymbol():
  symbols = ['!','@','#','$','%','^','&','*','(',')',]
  return random.choice(symbols)

def symbolAmt(pwd_len):
  sym_len = pwd_len // 3
  amt = int( input(f"Amount of symbols required, Min/Max (2,{sym_len})? ") )
  if amt < 2 or amt > sym_len:
    print(f"Please select length in range of 2-{sym_len}")
    symbolAmt()

  return amt

def pwdGen():
  pwd_len = int( input("Length of password, Min/Max (8,24)? ") )
  if pwd_len < 8 or pwd_len > 24:
    print("Please select length in range of 8-24")
    pwdGen()
  else:
    sym_amt    = symbolAmt(pwd_len)
    alpha_amt  = random.randint(3, (pwd_len - sym_amt) )
    num_amt    = pwd_len - alpha_amt - sym_amt
    eval_arr   = [sym_amt, alpha_amt, num_amt]
    print(f'\n\nCreating {sym_amt + alpha_amt + num_amt} length password (sym: {sym_amt}, alpha: {alpha_amt}, num: {num_amt})\n\n')

    pwd_str = ""
    while sum(eval_arr) > 0:
      choice = random.randint(0,2)
      if eval_arr[choice] > 0:
        eval_arr[choice] -= 1

        if choice == 0:
          pwd_str += randSymbol()
        elif choice == 1:
          pwd_str += randAlpha()
        else:
          pwd_str += randNum()

    print(f'NEW PASSWORD:   {pwd_str}')

pwdGen()