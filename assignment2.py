import socket


class Assignment2:
    def __init__(self, age: int):
        self.age = age

    def tellBirthYear(self, currentYear: int):
        print("Your birth year is {}".format(currentYear - self.age))

    def listAnniversaries(self, n: int):
        result = []
        index = 1
        value = n
        while value < self.age:
            result.append(value)
            index += 1
            value = n * index
        return result

    def modifyAge(self, n: int):
        power = str(self.age ** n)
        res = ""
        for i in range(len(power)):
            if i % 2 == 0:
                res += power[i]
        result = str(self.age * n) + str(self.age)[0] * n + res
        return result

    @staticmethod
    def checkGoodString(string: str):
        if len(string) < 8:
            return False

        if not string[0].islower():
            return False

        result = False
        for i in range(len(string)):
            if string[i].isnumeric():
                result = True
                break

        return result

    @staticmethod
    def connectTcp(host: str, port: int):
        try:
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as e:
            return False

        try:
            host = socket.gethostbyname(host)
            soc.connect((host, port))
            return True
        except socket.gaierror:
            return False

        return False


# a = Assignment2(21)
# ret = a.listAnniversaries(5)
# print(ret)
#
# ret = a.modifyAge(5)
# print(ret)
#
# ret = Assignment2.checkGoodString("Foobar0more")
# print(ret)
#
# ret = Assignment2.checkGoodString("foobar123")
# print(ret)
#
# ret = Assignment2.connectTcp("www.google.com", 80)
# if ret:
#     print("Connection established successfully")
# else:
#     print("Some error")
