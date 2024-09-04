if __name__ == '__main__':

    N = int(input())

    List=[]

    for i in range(N):

        commands=input().split()

        if commands[0] == "insert":

            List.insert(int(commands[1]),int(commands[2]))

        elif commands[0] == "append":

            List.append(int(commands[1]))

        elif commands[0] == "pop":

            List.pop()

        elif commands[0] == "print":

            print(List)

        elif commands[0] == "remove":

            List.remove(int(commands[1]))

        elif commands[0] == "sort":

            List.sort()

        else:

            List.reverse()
