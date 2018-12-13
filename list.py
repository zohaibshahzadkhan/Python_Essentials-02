favouriteFruit = ['Apple', 'Orange', 'banana'];
print(favouriteFruit);
print(favouriteFruit[0]);

#  append allow you to add new item at the end of the list 
favouriteFruit.append('Kiwi');
print(favouriteFruit);

# insert allow you to add item to given positon 
favouriteFruit.insert(1, 'Mango');
print(favouriteFruit);

# remove require name of item you want to remove and remove the item from the list 
favouriteFruit.remove("banana");
print(favouriteFruit);

# sort the item alphabatically or numerically
favouriteFruit.sort();
print(favouriteFruit);

favouriteFruit.insert(1,'1');
favouriteFruit.sort();
print(favouriteFruit);


# reverse the order of list 
favouriteFruit.reverse();
print(favouriteFruit);

# pop return the last item of the list and remove that item from the list 
favouriteFruit.pop();
print(favouriteFruit);


