print("For-Break")
for letter in 'Python':
    if letter == 'h':
        break
    print ('Current Letter :', letter)

print("\nWhile-Break")
var = 10
while var > 0:
    print ('Current veriable value :', var)
    var = var -1
    if var == 5:
        break
    print ("Good bye!")