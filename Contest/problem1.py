N = int(input())
hand = input()
lose = 0
tie = 0
win = 0
dict = {"HIGH CARD":0,"PAIR":1,"TWO PAIR":2, "THREE OF A KIND":3, "STRAIGHT":4, "FLUSH":5, "FULL HOUSE":6, "FOUR OF A KIND":7, "STRAIGHT FLUSH":8, "ROYAL FLUSH":9}
for i in range(N):
    nextHand = input()
    if dict[hand] > dict[nextHand]:
        win += 1
    elif dict[hand] < dict[nextHand]:
        lose += 1
    else:
        tie += 1
print(f"{win} {tie} {lose}")
