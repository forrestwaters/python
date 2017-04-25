Write a function that computes the volume of a sphere given its radius.

def vol(rad):
    return (4.0/3)*3.14(rad**3)

Write a function that checks whether a number is in a given range (Inclusive of high and low)

def ran_check(num,low,high):
    if high + 1 < num > low:
      return true
    else return false


Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output :
No. of Upper case characters : 4
No. of Lower case Characters : 33

def length_of_string('Hello Mr. Rogers, how are you this fine Tuesday?'):
for letter in 'Hello Mr. Rogers, how are you this fine Tuesday?':
  if letter.isupper()
    print letter
