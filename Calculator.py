def calculate():
  """
  Performs the calculation based on user input.
  """
  # Get numbers from the user
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  # Get the operator from the user
  operator = input("Choose an operator (+, -, *, /): ")

  # Perform calculation based on operator
  if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
  elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
  elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
  elif operator == "/":
    if num2 == 0:
      print("Error: Division by zero")
    else:
      print(f"{num1} / {num2} = {num1 / num2}")
  else:
    print("Invalid operator")

# Loop to allow for multiple calculations
while True:
  calculate()

  # Ask if the user wants to perform another calculation
  choice = input("Do you want to calculate again? (y/n): ")
  if choice.lower() != 'y':
    break

if __name__ == "__main__":
  print("Welcome to the Simple Calculator!")
  calculate()
