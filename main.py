def setup(expression, expression_list):
  for character in expression:
    try:
      character = float(character)
    except:
      pass
    expression_list.append(character)
  return expression_list

def can_evaluate(item1, item2, item3):
  symbols = ["+", "-", "*", "/", "^"]
  if type(item1) == type(item2) == float and item3 in symbols:
    return True
  else:
    return False

def evaluate(item1, item2, item3): #item3 is operator
  if item3 == "+":
    return item1+item2
  elif item3 == "-":
    return item1-item2
  elif item3 == "*":
    return item1*item2
  elif item3 == "/":
    return item1/item2
  elif item3 == "^":
    return item1**item2


def simplify(expression_list):
  for i in range(len(expression_list)-2):
    item1 = expression_list[i]
    item2 = expression_list[i+1]
    item3 = expression_list[i+2]

    if can_evaluate(item1, item2, item3) == True:
      newnum = evaluate(item1, item2, item3)
      expression_list = expression_list[:i] + [newnum] + expression_list[i+3:]
      return expression_list

def main():
  expression = str(input("Please enter a postfix expression: "))
  expression_list = []
  print(setup(expression, expression_list))

  while True:
    input()
    expression_list = simplify(expression_list)
    print(expression_list)

    if len(expression_list) == 1:
      print("You're done!")
      break

main()
