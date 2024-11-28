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
        choice=input("please choose")

        mean=float(input("mean= "))
        std=float(input("std= "))
        xxx=float(input("x= "))
        why=float(input("y= "))

        if choice=='1':
            right,left=calc(mean,std,xxx,why)
            if right==1:
                print("68% with 1 step to the right")
            elif right==2:
                print("95% with 2 step to the right")
            elif right==3:
                print("99.85% with 3 step to the right")
            
            if left==1:
                print("soemthing") 
            elif left==2:
                print("d") 
            elif left==3:
                print("f")  

            

    except ValueError:
        print("what the fuck are you doing? ")

if __name__ == "__main__":
    main()