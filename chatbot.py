def coffee_bot():
  print("Welcome to the cafe!")

#size of drink
def get_size():
  res = input("what size drink can i get for you?\n[a]small\n[b]medium\n[c]large\n")
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()
  

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

#drink type
def get_drink_type():
  res = input("What type of drink would you like?\n[a] Brewed Coffee\n[b] Mocha\n[c] Latte\n")
  if res == 'a':
    return 'Brewed Coffee'
  elif res == 'b':
    return 'Mocha'
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

#type of milk
def order_latte():
  res = input("And what kind of milk for your latte?\n[a] 2% milk\n[b] Non-fat milk\n[c] Soy milk\n")
  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
    print_message()
    return order_type()

# type of cup
def cup_type():
  res = input("Would you like a \n[a]Plastic cup\n[b]reusable cup?\n")
  if res == 'a':
    return 'plastic cup'
  elif res == 'b':
    return 'reusable cup'
  else:
    print_message()
    return cup_type()

#hot / iced
def hot_or_iced():
  res = input("Would you like your drink\n[a]hot or\n[b]iced\n")
  if res == 'a':
    return 'hot'
  elif res == 'b':
    return 'iced'
  else:
    print_message()
    return hot_or_iced()

# new drink
def additional_drink():
  res = input("do you want another drink?")
  if res == 'yes':
    get_size()
    get_drink_type()
    cup_type()
    hot_or_iced()
  else:
    print("Thank you for ordering!")


coffee_bot()

size = get_size()


drink_type = get_drink_type()


type_of_cup = cup_type()


hot_iced = hot_or_iced()


print("Alright, that's one {} {} {} coming up!".format(size,hot_iced,drink_type))


name = input("Can I get your name please?")
print("Thanks, {}! Your drink will be ready shortly.".format(name))

another_drink = additional_drink()
print("That's one {} {} {} for you".format(size,hot_iced,drink_type))
print("Your drinks will be ready shortly")
