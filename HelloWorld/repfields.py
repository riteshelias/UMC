age = 47
print("My age is " + str(age) + " years")

print("My age is {0} years".format(age))
print()
print("Month days are - Jan : {2}, Feb : {0}, Mar : {2}, Apr : {1}, May : {2}, Jun : {1}, Jul : {2}, Aug : {2}, Sep: {1}, Oct : {2}"
      .format(28, 30, 31))
print()
print("""Month days are - 
Jan : {2}
Feb : {0}
Mar : {2}
Apr : {1}
May : {2}
Jun : {1}
Jul : {2}
Aug : {2}
Sep : {1}
Oct : {2}"""
.format(28, 30, 31))