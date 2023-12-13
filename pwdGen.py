import random as r


def generator():
  #declares all the sumbols used in python
  DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  LOCASE_CHARACTERS = [
      'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o',
      'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
  ]

  UPCASE_CHARACTERS = [
      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O',
      'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
  ]

  SYMBOLS = [
      '@',
      '#',
      '$',
  ]

  ALPHABET = LOCASE_CHARACTERS + UPCASE_CHARACTERS
  #password parts
  dig = ''
  lett = ''
  sym = ''

  #digits
  for _i in range(0, 4):
    dig += DIGITS[r.randrange(len(DIGITS))]

  #letters
  for _i in range(0, 4):
    lett += ALPHABET[r.randrange(len(ALPHABET))]

  #symbols
  for _i in range(0, 4):
    sym += SYMBOLS[r.randrange(len(SYMBOLS))]

  password = sym + dig + lett

  return password


def str_to_ascii(a):
  b = []
  for i in range(len(a)):
    b.append(ord(a[i]))
  return b


def ascii_to_str(c):
  d = []
  for i in range(len(c)):
    d.append(chr(c[i]))
  return d


def print_dictionary(d):
  for key, value in d.items():
    print(f" {key}: {value}")


def print_list(lst):
  for item in lst:
    print(item)


def questions():
  print('')
  print('We will ask you some personal questions for you password recovery')
  print("")
  a = input('1.What was your nickname in highschool? : ')
  b = input(
      "2.What was the name of your first pet? (if you had one)? If you don't have a pet , what name would you give it? : "
  )
  c = input("3.what is your name of your favorate fictional charactor? : ")
  d = input("4.What is your favorite color? : ")
  print("")
  print('We have completed our password recovery process.')
  print("")
  return [a, b, c, d]


def checker(l):
  r = True
  i = questions()
  for j in range(len(i)):
    if i[j] != l[j]:
      r = False
      break 
  return r

def ID():
    return r.randint(1000, 9999)