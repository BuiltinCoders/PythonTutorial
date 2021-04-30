# pickling is a process of process of storing data into a file

import pickle

# cars = ['Audi', "BMW", "Maruti Suzuki"]
# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

file = 'mycar.pkl'
fileobj = open(file, 'rb')
my_car = pickle.load(fileobj)
print(my_car)