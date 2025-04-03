def greeting(name):
  print(f"Welcome to our App {name}")
greeting('Mastering23')
#---------------------#
#        xargs
#---------------------#
print("----xargs--------")
def mat(*numbs):
  results = 0
  for numb in numbs:
      results += numb
  print(results)

mat(2, 3, 4, 5)
mat( 4,5)
mat( 2.3,-2,10,2.1)
#---------------------#
#       kwargs
#---------------------#
print("----kwargs--------")
def get_proudct(**data):
  print(data["id"],data["name"])

get_proudct(
  id ="23",
  name="Iphone",
  desc="New Iphone 16 black case"
)