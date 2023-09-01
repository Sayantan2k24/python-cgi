# Exception Handling

print("welcome")

try:
    ch = input("enter your choice: ")
    if int(ch) == 1:
        print("this is 1")
        try:
            print("this is 1")
        except:
            print("try other")
    elif int(ch) == 2:
        print("this is 2")
    else:
        print("not number")

except SyntaxError:
    print("mail to admin there us syntax issue")
except ValueError:
    print("ask you to only put number like 1,2...")
except:
    print("idk mail admin")
finally:
    print("I am logging out good bye....")
