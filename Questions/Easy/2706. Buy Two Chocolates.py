class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        sorted_price = sorted(prices)
        if sorted_price[0] + sorted_price[1] > money:
            return money
        else:
            sumOfPrices = sorted_price[0] + sorted_price[1]
        leftover = money - sumOfPrices
        return leftover       