class Solution(object):
	def maxProfit(self, prices):
		buy_price = prices[0]
		profit = 0

		for price in prices[1:]:
			if price < buy_price:
				buy_price = price
			
			profit = max(profit, price - buy_price)
		
		return profit