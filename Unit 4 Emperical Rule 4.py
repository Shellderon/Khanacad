def calc(mean,std,xxx):
    results=mean
    steps=0
    right=0
    for i in range(5):
        results+=std
        steps+=1
        if round(results,2)==round(xxx,2):
            right=steps
            break
    result=mean
    steps=0 
    left=0

    for i in range(5):
        result-=std
        steps+=1 
        if round(result,2)==round(xxx,2): 
            left=steps
            break
    return right,left
def main():
    try:
        print("1.less than x")
        choice=int(input("please choose "))

        mean=float(input("mean = "))
        std=float(input("std= "))
        xxx=float(input("x= "))

        step_values={1:34,2:47.5,3:49.85}

        
        right,left=calc(mean,std,xxx)
        value=step_values.get(right,None)or step_values.get(left,None)

        if choice==1:
            
            print(f"\033[32m {value-50}% with {right} right{left} left\033[0m")

        elif choice==2:
            print(f"\033[32m {value+50}% with {left} lefft and {right} right\033[0m") 

    except ValueError:
        print("kill yourself")
if __name__=="__main__":
    main()