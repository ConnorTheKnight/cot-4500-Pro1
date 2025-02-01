algorithm = input()
match algorithm :
    case "1" :
        x0 = float(input())
        tol = float(input())
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
        left = float(input())
        right = float(input())
        tol = float(input())
        Max = int(input())
        terms = int(input())
        coefficients = []
        exponents = []
        for j in range(terms) :
            coefficients.append(float(input()))
            exponents.append(float(input()))

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
        p0 = float(input())
        tol = float(input())
        n0 = float(input())
        terms = int(input())
        coefficients = []
        exponents = []
        for j in range(terms) :
            coefficients.append(float(input()))
            exponents.append(float(input()))

        i = 0
        while i<n0 :
            p = 0
            for j in range(terms) : 
                p += coefficients[j]*pow(p0,exponents[j])
            if(abs(p-p0)<tol):
                print(str(p) + " success")
                exit()
            i+=i
            p0=p
        print("Failure")


    case "4" :
        p0 = float(input())
        tol = float(input())
        n0 = int(input())
        terms = int(input())
        coefficients = []
        exponents = []
        coefficientsD = []
        exponentsD = []
        for j in range(terms) :
            coefficients.append(float(input()))
            exponents.append(float(input()))
            if exponents[j] == 0 :
                coefficientsD.append(0)
                exponentsD.append(0)
            else :
                coefficientsD.append(coefficients[j]*exponents[j])
                exponentsD.append(exponents[j]-1)

        i=0
        while i<n0 :
            derP = 0
            for j in range(terms) : 
                derP += coefficientsD[j]*pow(p0,exponentsD[j])
            funP = 0
            for j in range(terms) : 
                funP += coefficients[j]*pow(p0,exponents[j])
            if derp!=0 :
                p = p0-funP/derP
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