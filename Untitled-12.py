def calc(std,mean,xxx,why):
    steps=0
    result=mean
    for i in range(5):
        result+=std
        steps+=1
        if abs(result-xxx)<0.01: 
            if steps==1:
                print("\033[32m something \033[0m")
            elif steps==2:
                print("\033[32m veggie\033[0m")
                
def main():
    try:
        print("1.less than x")
        print("2.more than x")
        print("3.inbetween x and y")
        choice=input("please choose")

        mean=float(input(f"mean=  "))
        std=float(input(f"std=  "))
        why=float(input(f"y=  "))
        xxx=float(input(f"x=  "))

        if choice=='1':
            calc(mean,std,xxx,why,)
        


    except ValueError:
        print("not found")
if __name__=="__main__":
    main()