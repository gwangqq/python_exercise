treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("I hit a tree %d times." % treeHit)
    if treeHit == 10:
        print("I cut the tree")

coffee = 10
money = 300
while money:
    print("I had a cup of coffee.")
    coffee = coffee - 1
    print("I have %d cups of coffee." % coffee)
    if not coffee:
        print("I run out of coffee. It is sold out")
        break