def testList(list_one, list_two):
  if list_one == list_two:
    print("The lists are the same")
  else: 
    print("These lists are not the same")

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
testList(list_one, list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
testList(list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
testList(list_one, list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
testList(list_one, list_two)