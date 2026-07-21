
ngay = int(input("Nhap ngay sinh: "))
thang = int(input("Nhap thang sinh: "))



thang_31_ngay = [1, 3, 5, 7, 8, 10, 12]
thang_30_ngay = [4, 6, 9, 11]

hop_le = True

if thang < 1 or thang > 12:
    hop_le = False
elif thang in thang_31_ngay and (ngay < 1 or ngay > 31):
    hop_le = False
elif thang in thang_30_ngay and (ngay < 1 or ngay > 30):
    hop_le = False
elif thang == 2 and (ngay < 1 or ngay > 29): # Tối đa 29 ngày cho tháng 2
    hop_le = False


if not hop_le:
    print("Ngay thang khong hop le!")
else:
    cung = ""
    if (thang == 3 and ngay >= 21) or (thang == 4 and ngay <= 19):
        cung = "Bach Duong"
    elif (thang == 4 and ngay >= 20) or (thang == 5 and ngay <= 20):
        cung = "Kim Nguu"
    elif (thang == 5 and ngay >= 21) or (thang == 6 and ngay <= 20):
        cung = "Song Tu"
    elif (thang == 6 and ngay >= 21) or (thang == 7 and ngay <= 22):
        cung = "Cu Giai"
    elif (thang == 7 and ngay >= 23) or (thang == 8 and ngay <= 22):
        cung = "Su Tu"
    elif (thang == 8 and ngay >= 23) or (thang == 9 and ngay <= 22):
        cung = "Xu Nu"
    elif (thang == 9 and ngay >= 23) or (thang == 10 and ngay <= 22):
        cung = "Thien Binh"
    elif (thang == 10 and ngay >= 23) or (thang == 11 and ngay <= 21):
        cung = "Bo Cap"
    elif (thang == 11 and ngay >= 22) or (thang == 12 and ngay <= 21):
        cung = "Nhan Ma"
    elif (thang == 12 and ngay >= 22) or (thang == 1 and ngay <= 19):
        cung = "Ma Ket"
    elif (thang == 1 and ngay >= 20) or (thang == 2 and ngay <= 18):
        cung = "Bao Binh"
    elif (thang == 2 and ngay >= 19) or (thang == 3 and ngay <= 20):
        cung = "Song Ngu"

    print("Cung hoang dao:", cung)