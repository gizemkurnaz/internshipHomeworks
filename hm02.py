import operator

limit = 6
divisorList = [2,3]
operatorList = {"+": operator.add,"*": operator.mul}

operatorChar = "*"
operator = operatorList[operatorChar]

def multiplesOfNumbers(limit,divisorList,operator):
    sum = 0
    multiplying = 1
    result = 0

    if(limit <= 0):
        print("Limit must be greater than zero.")

    elif(len(divisorList) == 0):
        print("Divisor List must not be empty.")

    else:
        for i in range(1,limit + 1):
            for j in range(len(divisorList)):
                if (i % divisorList[j] == 0):
                    if(operatorChar == "+"):
                        sum = operator(sum, i)
                        result = sum
                    else:
                        multiplying = operator(multiplying,i)
                        result = multiplying
                    break
        print(result)

multiplesOfNumbers(limit,divisorList,operator)