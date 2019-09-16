def count_uppper_case(message):
    count = 0
  
    for c in message:
     if c.isupper():
        count +=1
    return count
assert count_uppper_case("") == 0, "empty string"
assert count_uppper_case("W") == 1, "1 uppere case"
assert count_uppper_case("o") == 0, "1 lower case"
assert count_uppper_case("%^^") == 0, "special symbols"
assert count_uppper_case("dsRReTet") == 3, "special symbols"


print("All tests passed")

        
