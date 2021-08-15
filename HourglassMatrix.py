# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def copyMat(HG, hg, k, l):
    for i in range(3):
        for j in range(3):
            try:
                HG[k + i][l + j] += hg[i][j]
            except ValueError:
                print("wtf")

def getHourglass():
    hg = [[1, 1, 1], [0, 1, 0], [1, 1, 1]]
    HG = []
    for i in range(6):
        HG.append([0]*6)

    for i in range(4):
        for j in range(4):
            copyMat(HG, hg, i, j)
    return HG

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(getHourglass())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
