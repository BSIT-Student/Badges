import random

def generate_pin():
  """Generates a random 5-digit PIN."""
  pin = ""
  for _ in range(5):
    pin += str(random.randint(0, 9))
  return pin

# Generate a random PIN
pin = generate_pin()

# Print the generated PIN
print(f"Your random 5-digit PIN is: {pin}")
