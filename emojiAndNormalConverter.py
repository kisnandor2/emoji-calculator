# NOTE: the following code was built in juptye notebook and copy pasted here - that's why you can not easily find any logic in the code structure

# Build a list of all possible digits and put them into a dictionary
class myDigit:
  def __init__(self, normal, emoji):
    self.normal = normal
    self.emoji = emoji

  def getNormal(self):
    return str(self.normal)
  
  def getEmoji(self):
    return self.emoji
  
  def getEmojiUTF8(self):
    return self.emoji.decode("utf-8")

  def __str__(self):
    return str(self.normal) + ' ' + self.getEmojiUTF8() + '\n'

# Build a list of all possible operators and put them into a dict
class myOperator: # redeclaring everything again? superClass would be prettier :/
  def __init__(self, normal, emoji, word):
    self.normal = normal
    self.emoji = emoji
    self.word = word

  def getNormal(self):
    return self.normal
  
  def getEmoji(self):
    return self.emoji
  
  def getWord(self):
    return self.word
  
  def getEmojiUTF8(self):
    return self.emoji.decode("utf-8")
  
  def __str__(self):
    return self.normal + ' ' + self.getEmojiUTF8() + ' ' + self.word

class emojiAndNormalConverter:
  def __init__(self, digits, operators):
    self.digits = digits
    self.operators = operators
    self.validCharacters = ['+','-','*','/']
    for i in range(0,10):
      self.validCharacters.append(str(i))
    
  # let's start with converting a simple number to emoji output    
  def convertNumberToEmoji(self, number):
    number = str(number)
    # handle these two special cases
    number = number.replace('100', self.digits[100].getEmojiUTF8())
    number = number.replace('10', self.digits[10].getEmojiUTF8())
    # we don't use the billiard 8 at all
    for i in range(0,10):
      number = number.replace(str(i), self.digits[i].getEmojiUTF8())
    return number
  
  def convertEmojiStringToNormalOutput(self, myStr):
    # remove spaces since we don't need them
    myStr = myStr.replace(' ', '')
    # replace all emoji digits
    myStr = myStr.replace(self.digits[100].getEmojiUTF8(), self.digits[100].getNormal())
    myStr = myStr.replace(self.digits[10].getEmojiUTF8(), self.digits[10].getNormal())
    myStr = myStr.replace(self.digits[-1].getEmojiUTF8(), self.digits[-1].getNormal())
    for i in range(0, 10):
      myStr = myStr.replace(self.digits[i].getEmojiUTF8(), self.digits[i].getNormal())
    for i in self.operators:
      # replace all emoji operators
      myStr = myStr.replace(self.operators[i].getEmojiUTF8(), self.operators[i].getNormal())
      # replace all word operators
      myStr = myStr.replace(self.operators[i].getWord(), self.operators[i].getNormal())    
    myStr = myStr.replace('x','*')
    myStr = myStr.replace('%','/')
    # remove newlines
    myStr = myStr.replace('\n','')
    # check if invalid output in string
    stringForCheck = myStr
    for i in self.validCharacters:
      stringForCheck = stringForCheck.replace(i, '')
    # if we have invalid characters
    if len(stringForCheck) > 0:
      raise ValueError("Invalid characters as input: `" + stringForCheck + '` which has len: ' + str(len(stringForCheck)))
    return myStr
  
# Init the values
myOperators = {}
myOperators['+'] = myOperator('+', "➕".encode(), 'plus')
myOperators['-'] = myOperator('-', "➖".encode(), 'minus')
myOperators['*'] = myOperator('*', "✖️".encode(), 'times')
myOperators['/'] = myOperator('/', "➗".encode(), 'dividedby')
# -------------------------------------------------------------
# -- why is ✖️ and ✖ different in the examples.txt?
# -- based on the description - the second one was not handled
# -- if needed then a new operator should be declared
# -------------------------------------------------------------

# the below list is ordered: 9..0
# NOTE: the emoji numbers from the example had \xef\xb8\x8f as special character at the end of the digit while the one from the https://apps.timwhitlock.info/emoji/tables/unicode page had \xE2\x83\xA3
# TODO: check what's the difference between those two types of emoji digits
emojiDigits = [b'\x39\xef\xb8\x8f', b'\x38\xef\xb8\x8f', b'\x37\xef\xb8\x8f', b'\x36\xef\xb8\x8f', b'\x35\xef\xb8\x8f', b'\x34\xef\xb8\x8f', b'\x33\xef\xb8\x8f', b'\x32\xef\xb8\x8f', b'\x31\xef\xb8\x8f', b'\x30\xef\xb8\x8f']
myDigits = {}
for i in range(0,10):
  myDigits[i] = myDigit(i,emojiDigits[9-i])
myDigits[10] = myDigit(10, b'\xF0\x9F\x94\x9F')
myDigits[100] = myDigit(100, b'\xF0\x9F\x92\xAF')
myDigits[-1] = myDigit(8, b'\xF0\x9F\x8E\xB1') #special case with the 8

myToEmojiConverter = emojiAndNormalConverter(myDigits, myOperators)

# try:
#   myToEmojiConverter = emojiAndNormalConverter(myDigits, myOperators)
#   expression = myToEmojiConverter.convertEmojiStringToNormalOutput("1%0")
#   eq, status = parser(expression)
#   if status > 0:
#     print("🤷")
#   output = int(calculate(eq))
#   print(myToEmojiConverter.convertNumberToEmoji(output))
# except Exception as e:
#   print(e)
#   print("Some 🤷")
