n = int (input ('nhap so: '))
nt = abs (n)
nt2 = abs (n)
dem=0
while nt>0:
    nt=nt //10
    dem=dem+1
print ("co ", dem, " so")  

tong =0
for i in range (1, dem+1 ):
    tong = tong+  (nt2-nt2//10*10)
    nt2=nt2//10
print ("tong la: ", tong)
snt = True 
if n<2:
    snt = False
for i in range (2, n ):
    if n%i==0:
        snt = False
        break
if snt == True :
    print ("day la so nguyen to")
else :
    print ("day khong phai so nguyen to")
        


    



