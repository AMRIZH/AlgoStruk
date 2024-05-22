# problem 121 : Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

def maxProfit(prices):
    minPrice = float('inf')  # Initialize minPrice with infinity
    maxProfit = 0

    for price in prices:
        # Update minPrice if the current price is smaller
        minPrice = min(minPrice, price)

        # Calculate the potential profit by selling at the current price
        profit = price - minPrice

        # Update maxProfit if the potential profit is higher
        maxProfit = max(maxProfit, profit)

    return maxProfit
  
"""Here's how the code works:
  
      We initialize minPrice with infinity and maxProfit with 0.
      We iterate through each price in the prices array.
      For each price, we update minPrice to be the minimum of the current price and minPrice.
      We calculate the potential profit by selling at the current price (price - minPrice).
      We update maxProfit to be the maximum of the current maxProfit and the potential profit.
      After iterating through all prices, we return the maximum profit.
      
The time complexity of this algorithm is O(n) because we iterate through the prices array once.

The space complexity is O(1) because we use a constant amount of extra space regardless of the input size.
"""

# test the function
print(maxProfit([7,1,5,3,6,4]))  # Output: 5
print(maxProfit([7,6,4,3,1]))  # Output: 0
print(maxProfit([1,2]))  # Output: 1
print(maxProfit([2,1]))  # Output: 0
print(maxProfit([2,4,1]))  # Output: 2
print(maxProfit([3,2,6,5,0,3]))  # Output: 4
print(maxProfit([2,1,2,1,0,1,2]))  # Output: 2