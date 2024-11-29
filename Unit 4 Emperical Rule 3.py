def calc(mean,std,xxx,why):
    steps=0
    results_m=mean
    left=0

    for i in range(5):
        results_m+=std
        steps+=1 
        
        if round(results_m,2)==round(xxx,2):
            left=steps
            break
    steps=0
    results_m=mean
    right=0

    for i in range(5):
        results_m-=std
        steps+=1
        
        if round(results_m,2)==round(xxx,2): 
            right=steps
            break
    return left,right
    
def main():
    try:
        print("1.less than x") 
        print("2.more than x")
        choice=input("please choose")

        mean=float(input("mean= "))
        std=float(input("std= "))
        xxx=float(input("x= "))
        why=float(input("y= "))

        if choice=='1':
            right,left=calc(mean,std,xxx,why)
            if right==1:
                print("84% with 1 step to the right")
            elif right==2:
                print("97.5% with 2 step to the right")
            elif right==3:
                print("99.85% with 3 step to the right")
            
            if left==1:
                print("16% with 1 step to the left") 
            elif left==2:
                print("2.5% with 2 steps to the left") 
            elif left==3:
                print("0.15% with 3 steps to the left") 
                #m80s10x70L
        if choice=='2':
            right,left=calc(mean,std,xxx,why)
            if right==1:
                print(" 16% with 1 steps to the aright") 
            elif right==2:
                print("2.5% with 2 steps to the right")
            elif right==3:
                print("0.15% with 3 steps to the right")

            if left==1:
                print("84% with 1 step to the left")
            elif left==2:
                print("97.5% with 2 step to the left")
            elif left==3:
                print("99.85% with 1 step to the left")
        if choice=='3':
            

            

    except ValueError:
        print("what the fuck are you doing? ")

if __name__ == "__main__":
    main()