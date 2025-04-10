x=(input("Enter your character: "))
if len(x)>1:
    print("Enter only one character for check")


elif x>="a" and x<="z" or x>="A" and x<="Z":
        print(x,"is a alphabet")

elif x.isnumeric():
      print(x,"Its a number")

else:
      print("Its not an alphabet")