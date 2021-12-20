#Pengisytiharkan pemboleh ubah dan pemalar
#Input
berat=float(input("Sila masukkan berat(kg) anda:"))
tinggi=float(input("Sila masukkan tinggi(m) anda:"))

#Proses
def nilai_BMI(b,t):
    BMI=b/(t*t)
    return BMI

#Output
def kategori(x):
    if(x<18.5):
        print("BMI anda ialah",round(BMI,2),".","Anda adalah dalam kategori Kurang Berat Badan.")
    elif(18.5<x<24.9):
        print("BMI anda ialah",round(BMI,2),".","Anda adalah dalam kategori Berat Badan Ideal.")
    elif(25.0<x<29.9):
        print("BMI anda ialah",round(BMI,2),".","Anda adalah dalam kategori Lebih Berat Badan.")
    else:
        print("BMI anda ialah",round(BMI,2),".","Anda adalah dalam kategori Obes.")

nilai_BMI(berat,tinggi)
BMI=nilai_BMI(berat,tinggi)
kategori(BMI)
    
