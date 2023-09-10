#!/usr/bin/python3

def main():

    import hidden_4

    nameList = dir(hidden_4)
    for nameNum in nameList:
        if nameNum[:2] != "__":
            print("{}".format(nameNum))


if __name__ == "__main__":
    main()
