class Solution:
    def coin_change(self, coins, amount):
        if amount<=0:
            return 0
        Ca = [amount + 1] * (amount + 1)
        for i in range(amount + 1):
            if i in coins:
                # print('Ca[i]',Ca[i])
                Ca[i] = 1
                continue
            iterate = [Ca[i - coin] + 1 for coin in coins if i - coin > 0]

            # for coin in coins:
            #     if i - coin > 0:
            #         print('Ca[i-coin]+1',Ca[i-coin]+1) 

            if iterate:
                Ca[i] = min(iterate)

        return -1 if Ca[amount] > amount else Ca[amount]


obj1 = Solution()
coins=[int(item) for item in input("Enter variety of coins here:").split()]
amt=int(input("Amount:"))
print("Minimum coins required is", obj1.coin_change(coins,amt))