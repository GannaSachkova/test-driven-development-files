from byotest import *
usd_coins = [100,50,25,10,5,1]
euro_coins = [100,50,20,10,5,2,1]
##2  create function get_change(0)

def get_change(amount, coins= euro_coins):
  """ remove if statement bcz it no longer required  
    
    if amount = = 0:
  return []

# #5 get change either 100 or 50 or 20...1   
    if amount in [100,50,20,10,5,2,1]:
        return [amount]
  """       
       
   # #6 if the coin value is less than change
   
   change = []
   for coin in coins:
         while coin <= amount:
            amount -= coin
            change.append(coin)
    return change    
    
"""
#1    When the amount of change that we require is 0, then we should get no coins back.
So we can do this by using our test_are_equal() function calling our, currently non-existent, get_change() function.
And we expect, where we've provided 0 change, to get an empty list back.
"""
test_are_equal(get_change(0), [])

# #3 call test_are_equal(get_change(), []) that return 1 coins
test_are_equal(get_change(1), [1])
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])


# #4 call test_are_equal(get_change()  to get change with 2 coins
test_are_equal(get_change(3), [2,1])
test_are_equal(get_change(7), [5,2])
test_are_equal(get_change(19), [10,5,2,2])
test_are_equal(get_change(35, usd_coins), [25,10])


print("All tests pass!")
