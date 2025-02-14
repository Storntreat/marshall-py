# Lesson 5

money = float(input())
orderlist = input()

bigCookies = orderlist.count("b")
cookies = orderlist.count("c")

cost = cookies*0.5 + bigCookies*0.75
revenue = cookies*1.25 + bigCookies*2

profit = revenue-cost

print(bigCookies + cookies)
print(profit)
print(profit + money)