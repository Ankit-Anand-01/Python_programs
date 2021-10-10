# Python Program to merge two dictionaries

dict1 = { 'Alexandra' : 27,      
            'Shelina Gomez' : 22,  
            'James' : 29,  
            'Peterson' : 30  
                        }   
dict2 = {  
            'Jasmine' : 19,     
            'Maria' : 26,  
            'Helena' : 30  
}                          
print("Before merging the two dictionary ")  
print("Dictionary No. 1 is : ", dict1) 
print("Dictionary No. 1 is : ", dict2)
  
dict3 = dict1.copy()  # Copy the dict1 into the dict3
  
for key, value in dict2.items():
    dict3[key] = value  
  
print("After merging of the two Dictionary ")  
print(dict3)    
