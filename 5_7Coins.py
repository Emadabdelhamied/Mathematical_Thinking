def change(amount):
  dict={24:[5, 5, 7, 7],25:[5,5,5,5,5],26:[7,7,7,5],27:[5,5,5,5,7],28:[7,7,7,7]}
  if amount in dict.keys():
    return dict[amount]
  else:
    coins=change(amount-5)
    coins.append(5)
    return coins
