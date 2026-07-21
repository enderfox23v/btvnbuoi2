n = int (input ('chon nam : '))
t = int (input ('chon so thang: '))

match t:
    case 1|3|5|7|8|10|12:
        print ("thang ", t, "co 31 ngay")
    case 4|6|9|11:
        print ("thang", t, "co 30 ngay")
    case 2:
        if n%4==0:
            print ("thang", t, "co 29 ngay")
        else :
            print ("thang", t, "co 28 ngay")
    case _:
        print ("khong hop le")
print(type(t))


