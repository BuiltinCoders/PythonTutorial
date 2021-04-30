# create a dictionary consist of min four key value pair
# take input from the user and return the value of input key

dictionary = {
    "sets":"Sets are the collection of organized data",
    "dictionary":"Dictionay is the collection of data in the key-value pair",
    "list":"list is the collection of unorganized data",
    "mutable":"Changable",
    "immutable":"Not changable"
}

word = input("Please Enter The word :\n").lower()
print("Meaning :",dictionary.get(word))