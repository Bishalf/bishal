# anml=input("Enter your Favourite Animal\n")
# print(anml+"is my Favourite too")
# To over come above truthiness we can use followinfg condition
anml = input("Enter your Favourite Animal\n")
if anml:  # If animal exist it will proceeds
    print(anml + " is my Favourite too")
else:
    print("You forget to enter your Favouroite animal Name")
# def name():
#     a=input('enter your name')
# name()
