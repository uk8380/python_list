thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
print(type(thislist))
# note the double round-brackets
thislist = list(("apple", "banana", "cherry")) 
print(thislist)
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
#append
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#insert
thislist.insert(1, "orange")
print(thislist)
#Extend List
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#remove
thislist.remove("banana")
print(thislist)
#pop
thislist.pop()
print(thislist)
#loops in list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#alternate
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#List comprehension
newlist = [x for x in fruits if "a" in x]

print(newlist)
#sort
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

