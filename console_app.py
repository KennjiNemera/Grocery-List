# This program will by means of a GUI give you a working grocery list. 
# Will display price, name and a check box

# console trial

isRunning = True
list_items = []

def addItem():
  list_items.append(input('Enter the items you would like to add\n'))
  print()

def printList():
  for i in range(len(list_items)):
    print('Item ' + str(i + 1) + ': '  + list_items[i])
    print()

while isRunning:
  addItem()
  printList()
  Continue_Val = int(input('Would you like to continue\n'))
  if Continue_Val == 1:
    continue
  else: 
    isRunning = False
    print('Have a great day you sodium consuming freak\n')
    break
    


  
