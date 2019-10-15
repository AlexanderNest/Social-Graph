import networkx as nx
import pylab as plt
import random


def findcount(val, array):
    count = 0

    for i in array:
        if i[0] == val:
            count += 1

    return count




def createGraph():
    f = open('facebook_combined.txt', 'w')

    random.seed()

    for i in range(100):
        a = random.randint(0, 100)
        b = random.randint(0, 100)

        while a == b:
            a = random.randint(0, 40)
            b = random.randint(0, 40)
        f.write(str(a) + ' ' + str(b) + '\n')

    f.close()

    f = open('facebook_combined.txt')
    lst = f.read()

    friends = []
    lst = lst.split('\n')
    for i in lst:
        friends.append(i.split())

    towrite = []
    for i in friends:
        if findcount(i[0], friends) == 0:
            towrite.append(i)

    print(towrite)


    print(friends)










createGraph()
g = nx.read_edgelist("facebook_combined.txt")

nx.draw(g, with_labels=True)
plt.draw()
plt.show()



