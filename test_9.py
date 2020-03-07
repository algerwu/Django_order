import pickle
a_dict = {'ad':123,2:[1,2,3],'23':{1:2,'dc':'asd'}}
# file = open('pickle_example.pickle','wb')
# pickle.dump(a_dict,file)
# file.close()

file = open('pickle_example.pickle','rb')
a_dict = pickle.load(file)
file.close()
print(a_dict)

with open('pickle_example.pickle','rb') as file:
    a_dict = pickle.load(file)

print(a_dict)