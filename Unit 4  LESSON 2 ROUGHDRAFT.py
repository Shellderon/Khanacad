#m18s5x14 -0.33
#m67s2x66 -0.2
#m76s3x71  
import requests
from bs4 import BeautifulSoup

m = float(input("Put your mean in: "))
s = float(input("Put your standard deviation in: "))
x = float(input("Put your x value in: "))

# Calculate the Z-score

def calculation():
    z_score = (x - m) / s
    zint=int(z_score)
    first_decimal = int(abs(z_score - zint) * 10)
    first_half = float(f"{zint}.{first_decimal}")
    second_half=round(abs(first_half-z_score),2)



    return  z_score,zint, first_decimal, first_half,second_half
z_score,zint,first_decimal,first_half,second_half=calculation()

print(f"the full Z-Score is this: {round(z_score,2)}")
print(f"the first half is this:\033[1;32m{first_half}\033[0m") 
print(f"the second half is:\033[1;32m{second_half}\033[0m") 

