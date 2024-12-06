def calc(mean,std,xxx,why):
    results=mean
    steps=0
    stepps=0
    right=0
    x=0
    for i in range(5):
        results+=std
        steps+=1
        stepps+=1
        if round(results,2)==round(xxx,2):
            right=steps
        if round(results,2)==round(why,2):
            x=stepps

            break
    result=mean
    steps=0
    stepps=0 
    left=0
    y=0

    for i in range(5):
        result-=std
        steps+=1 
        if round(result,2)==round(xxx,2): 
            left=steps
        if round(result,2)==round(why,2):
            y=stepps
            break
    return right,left,x,y
def main():
    try:
        print("1.less than x")
        print("2.more than x")
        print("3.inbetween x and y")

        choice=int(input("please choose "))

        mean=float(input("mean = "))
        std=float(input("std= "))
        xxx=float(input("x= "))
        why=float(input("y= "))

        step_values={1:34,2:47.5,3:49.85}

        
        right,left,x,y=calc(mean,std,xxx,why)
        

        value=step_values.get(right,None)or step_values.get(left,None)

        if choice==1:
            if mean>xxx:
                print(f"\033[32m {value-50}% with {right} right{left} left\033[0m")
            elif mean<xxx:
                print(f"\033[32m {value+50}% with {right} right{left} left\033[0m")
                

        elif choice==2:
            if mean>xxx:   
                print(f"\033[32m {value+50}% with {right} right{left} left\033[0m")    
            if mean<xxx:
                print(f"\033[32m {value-50}% with {right} right{left} left\033[0m") 

        elif choice == 3:
            valuey = step_values.get(y, None)
            valuex =  step_values.get(x, None)   
            valueright = step_values.get(right,None) 
            valueleft=step_values.get(left,None)

            if xxx < mean < why:  
                print(f"\033[32m{valuex+valueleft} with {x,right} right steps and {y,left}  left steps\033[0m") 
            elif xxx<mean and mean>why:
                print(f"\033[32m{valuex}penis,{valuey} with {x,right} right steps and {y,left}  left steps\033[0m")
                
            elif xxx> mean and why> mean:
                print(f"\033[32m {valueright-valuex}% {right} right and {x} even more righ\033[0m") 
                
            else:
                print("Mean is not between x and y.")  

    except ValueError:
        print("kill yourself")
if __name__=="__main__":
    main()