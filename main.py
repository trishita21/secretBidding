from replit import clear
import art

bids = {}

print(art.logo)
print("Welcome to the secret auction program.")

def add_bid(name, amount):
  bids[name] = amount

def calculate_highest():
  max = 0
  bidder = ""
  for name in bids:
    val = bids[name]
    if val > max:
      max = val
      bidder = name

  print(f"The winner is {bidder} with bid of ${max}")

has_next = True

while has_next:
  name = input("What is your name? ")
  bid = int(input("What's your bid? $"))
  add_bid(name=name, amount=bid )
  next = input('Are there any other bidders? Type "yes" or "no".')
  if next.lower() != "yes":
    has_next = False

  clear()

calculate_highest()

