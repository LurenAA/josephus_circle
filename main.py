from josephus_circle import JcSolution


START_INDEX = 0
INTERVAL = 2


if __name__ == '__main__':
    jc_list = ['a', 'b', 'c', 'd', 'e', 'f']
    for x in JcSolution(jc_list, START_INDEX, INTERVAL):
        print(x, end=" ")
