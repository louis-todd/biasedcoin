import random

#TODO add graph
def coinflip():
    rand = random.random()
    if rand < 0.4 :
        return False
    else:
        return True

if __name__ == '__main__':
    money = 25
    while 0<money<250:
        #kelly formula 2*p-1 (p is probability of winning) = 0.2
        print(f"You have ${money} how much do you want to stake? Kelly recommends {money*0.2}")
        stake = int(input())
        if 0<stake<=money:
            result = coinflip()
            if result:
                print("Won!")
                money+=stake
            else:
                print("Lost :(")
                money-=stake
    if money == 0:
        print("Bust!")
    else:
        print("You got to the max! ($250)")

# Test bias
# N = 1000000
# flips = [coinflip() for i in range(N)]
# print(float(flips.count(True))/N)