#  Dictinory is a key value pair
priceOfCamera = {'sony': 500, 'nikon': 600, 'canon': 700 };
print(priceOfCamera['sony']);

priceOfCamera['canon'] = 800 ;
print(priceOfCamera["canon"]);

contactPerson = {'Zohaib': { 'phone': '0336235'}}
print(contactPerson['Zohaib']);

# dictionary.keys()
print(priceOfCamera.keys())

# dictionary.values()
print(priceOfCamera.values());

# dictionary.copy(); copies the key value pairs
copyOfpriceOfCamera = priceOfCamera.copy();
print(copyOfpriceOfCamera);

#  delete key value 
del priceOfCamera["sony"];
print(priceOfCamera);

# dictionary.clear() clears the dictionary 

copyOfpriceOfCamera.clear();
print(copyOfpriceOfCamera);


