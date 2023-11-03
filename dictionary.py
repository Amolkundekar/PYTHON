######## dictionary #########
#contains key - value pair
#### unordered collection , changable , indexed

dict1 = {"car1": "bmw", "car2": "audi", "car3" : "fararii"}

print(type(dict1))
print(dict1)

for i in dict1.items():
    print(i)
    
for i in dict1.keys():
    print(i)
    
for i in dict1.values():
    print(i)
    
####adding new item to the dictionary
dict1["car4"] = "lamborgini"

    
for i in dict1.values():
    print(i)
    
### nested  dictionary
std1_d = {"amol": 29}
std2_d = {"vishal": 39}
std3_d = {"ravi": 49}
std4_d = {"ram": 59}

std_details = {'std1':std1_d, 'std2':std2_d, 'std3':std3_d} 
print(std_details)

####accessing dictionary items

print(std_details['std1'])
print(std_details['std1']['amol'])
