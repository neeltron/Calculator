def add(a, b):
  c = a + b
  return c

def sub(a, b):
  c = a - b
  return c

def mul(a, b):
  c = a * b
  return c

def div(a, b):
  c = a / b
  return c

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
op = input("Enter an operator (+, -, /, *): ")

if op == '+':
  c = add(num1, num2)
elif op == '-':
  c = sub(num1, num2)
elif op == '*':
  c = mul(num1, num2)
elif op == '/':
  c = mul(num1, num2)

print(c)