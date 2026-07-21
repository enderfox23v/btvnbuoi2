x= int (input ('nhap so tien ban co: '))
t= x//28
if t>=3 :
    doi = t//3
    print ("du ", t, "vo doi them duoc", doi, " chai nua ")
    t=t+doi
print ("mua duoc ", t, "chai")