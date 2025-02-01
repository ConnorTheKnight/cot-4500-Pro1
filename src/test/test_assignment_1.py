import math

algorithm = input()
match algorithm :
    case "1" :
        x0 = 1.5
        tol = 0.000001
        i = 0
        diff = x0
        x = x0

        print(str(i) + " : " + str(x))

        while (diff>=tol):
            i+=1
            y=x
            x = (x/2) + (1/x)
            print(str(i) + " : " + str(x))
            diff = abs(x-y)
        print("\nConvergence after " + str(i) + " iterations")


    case "2" :
        left = 1
        right = 2
        tol = 0.001
        Max = 10000
        terms = 3
        coefficients = [1,4,-10]
        exponents = [3,2,0]

        i = 0
        p = left
        while abs(left-right)>tol and i<Max :
            i+=1
            p = (left+right)/2

            resultLeft = 0
            for j in range(terms) : 
                resultLeft += coefficients[j]*pow(left,exponents[j])
            resultP = 0
            for j in range(terms) : 
                resultP += coefficients[j]*pow(p,exponents[j])

            if resultLeft < 0 and resultP > 0 or resultLeft > 0 and resultP < 0 :
                right = p
            else :
                left = p
        print(str(p))


    case "3" :
        p0 = 1.5
        tol = 0.000001
        n0 = 50
        terms = 4
        coefficients = [1.0,-1,-4,10]
        exponents = [1,3,2,0]

        i = 0
        while i<n0 :
            p = 0.0
            for j in range(terms) : 
                p += coefficients[j]*pow(p0,exponents[j])
            if abs(p0-p) < tol :
                print(str(p) + " success")
                stop()
            i+=i
            p0=p
        print("Failure")


    case "4" :
        p0 = 0.78539816339
        tol = 0.0000000001
        n0 = 10

        i=0
        while i<n0 :
            derP = (-1*math.sin(p0))-1
            funP = math.cos(p0)-p0
            if derP != 0 :
                p = p0-(funP/derP)
                if abs(p0-p) < tol :
                    print(str(p) + " success")
                    exit()
                i+=1
                p0 = p
            else :
                print("Failure - derivative = 0")
                exit()
        print("Failure - max iterations")
        exit()