#Tervitus
#Alusta programmi. 
#Küsi kasutajalt: "Mis sugu Te olete? (naisoost/meesoost)".
#Salvesta vastus muutujasse gender.
#Kui gender on võrdne sõnaga "naisoost", siis väljasta ekraanile: "Tere, proua Sepp!".
#Muidu, kui gender on võrdne sõnaga "meesoost", siis väljasta ekraanile: "Tere, härra Linker!".
#Muidu (kui sisestus ei olnud õige), siis väljasta ekraanile: "Vale sugu".
#Lõpeta programm.

gender = input("Mis sugu Te olete? (naissoost/meesoost):")
if gender =="naissoost":
    print("Tere, proua Sepp!")
elif gender =="meesoost":
    print("Tere, härra Linker!")
else:
    print("Vale sugu")
