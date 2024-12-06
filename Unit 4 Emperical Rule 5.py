def calc(mean,std,xxx,why):
    results=mean
    steps=0
    stepps=0
    right=0
    for i in range(5):
        results+=std
        steps+=1
        stepps+=1
        if round(results,2)==round(xxx,2):
            right=steps
        elif round(results,2)==round(why,2):
            x=stepps

            break
    result=mean
    steps=0
    stepps=0 
    left=0

    for i in range(5):
        result-=std
        steps+=1 
        if round(result,2)==round(xxx,2): 
            left=steps
        elif round(result,2)==round(why,2):
            y=stepps
            break
    return right,left
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

        
        right,left=calc(mean,std,xxx,why)
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
            if xxx < mean < why:
                print(f"\033[32m{value} between x and y with {right} right steps and {left} left steps\033[0m")
                
            else:
                print("Mean is not between x and y.") 


    except ValueError:
        print("kill yourself")
if __name__=="__main__":
    main()