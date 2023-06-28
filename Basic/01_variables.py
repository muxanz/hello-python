# variables

my_str_var = "My string variable"
print(my_str_var)

my_int_var = 10
print(my_int_var)

my_bool_var = True
print(my_bool_var)

my_int_to_str = str(my_int_var)
print(my_int_to_str)
print(type(my_int_to_str))

# concatenation variables
print(my_str_var, my_int_var, my_bool_var)
print("My int var:", my_int_var)


# length
print(len("Hello, world!!"))
print(len(my_str_var))

# declaring multiple variable in a line
name, surname, alias, country, age = "Samuel", "Florez", "Muxanz", "Colombia", "100"

print("Fist name:", name,
      "\nLast name:", surname,
      "\nNickname:", alias,
      "\nCountry:", country,
      "\nAge:", age
)

# inputs
first_name = input("What is your name? ")
age_user = input("How old are you? ")
print(first_name, age_user)

# forze type
address: str = "Cold Street, 120"
print(type(address))
address = 100
print(address)
print(type(address))