def string_test(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
           d["upper"]+=1
        elif c.islower():
           d["lower"]+=1
        else:
           pass
    print ("Original String: ", s)
    print ("number of upper case letters: ", d["upper"])
    print ("numbers of lower case letters: ", d["lower"])

string_test('My name is Xochitl Sosa')