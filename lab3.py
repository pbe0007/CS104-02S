### This is way more fun than coding on a chromebook

import sys

### define the shift variable and ensure that it is a number, otherwise throw an error
reg_shift = sys.argv[1]
try:
  reg_shift = int(sys.argv[1])
except:
  print(f"""Error with Argument 1, ''{sys.argv[1]}'' is not a valid input. Integers only.""")
  sys.exit()

### catch if there are too many or too few arguments
if len(sys.argv) > 3:
  print(f"Remember, all arguments after '{sys.argv[2]}' are ignored. Put strings with spaces in quotes.")
elif len(sys.argv) < 3:
  print(f"put the cipher key in the first argument and the string to encode in the second argument")
  sys.exit()
### set up both output strings and the input string
message = sys.argv[2]
encrypted = ""
remessage = ""

### encode/decode function # enode means endcode or decode
def coder(char, enode, shift):
  x = 1
  if enode == False:
    x = -1
  #print(char)
  if ord(char) >= 32 and ord(char) <= 126:
    ### this shifts the numbers around so that the looping behavior can be done with a
    ### simple modulus operator, and then they are shifted back to display correctly
    ### this does leave newline characters alone, but you can't put those in CMD
    return(chr(abs((ord(char) - 32 + (shift*x)) % (126-31)) + 32))
  else:
    #print(ord(char))
    return(char)

# when the second input is true it runs the shift normally
for char in message:
  encrypted += coder(char, True, reg_shift)

print(f"\n{encrypted}")

# when the second input is false it runs the shift backwards, essentially decoding the message.
for char in encrypted:
  remessage += coder(char, False, reg_shift)

print(f"\n{remessage}")
