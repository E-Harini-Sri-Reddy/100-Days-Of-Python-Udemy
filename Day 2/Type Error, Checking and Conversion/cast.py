len("12345")

#how to check the data type: This is called Type checking
print(type("12345"))  #str
print(type(12345))  #int
print(type(123_456_678))  #int
print(type(123.45))  #float
print(type(True))  #bool
print(type(False))  #bool

print("\n")

#typecasting:
print("123" + "456")  #Here it is still string so, the + sign performs concatenation
print(int("123") + int("456"))  #"123" and "456" are being typecast as integers

print("\n")

print("Number of letters in your name: " + str(len(input("Enter your name: "))))
