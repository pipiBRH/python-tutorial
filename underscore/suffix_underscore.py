# list all built-in keywords
import keyword
import builtins
print(keyword.kwlist)
print("-----------------------------------")
print(vars(builtins))

# built-in functions conflict 
list = ["ehuang02", "cchen10", "cwang05"]
print(list((1, 2j, 3)))

# built-in keywords conflict
with = "ehuang02" 
def is(): pass