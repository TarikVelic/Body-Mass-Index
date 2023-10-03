"""
Dobrodišli U PROGRAM KOJI SLUŽI ZA IZRAČUNAVANJE ITM I RIZIKA OD DIJABETESA TIPA II
PREDMET: SOFTVERSKI STUDIO 3
STUDENT: TARIK VELIC
PROFESOR: PROF. DOC. VELIMIR DEDIC
DIFERENCIJALNI PREDMET !
"""

#POČETAN PROJEKTA

print ("Odaberite jezik - Choose language - Sprache wählen ")
odgovor = int(input("Pritisnite 1 za EX-YU jezik - Press 2 for English - Drücken Sie 3 für Deutsch: "))
print("Odgovor je", odgovor )
if odgovor < 1 or odgovor > 3:
    print("Program se zatvara - The program closes - Das Programm wird geschlossen")
    exit()

if odgovor== 1:
    print("Dobro došli u program za izračunavanje indexa tjelesne mase")
    visina = float(input("Unesite svoju visinu u centimetrima: "))
    težina = float(input("Unesite svoju kilažu u kilogramima: "))

    BMI = težina / (visina * visina ) * 10000
    print("BMI - Vaš index tjelesne mase je:  ", round(BMI,2))

    if (BMI > 0):
        if (BMI <= 16):
            print("Vi ste jako mršavi")

        elif (BMI <= 18.5):
            print("Vi ste mršavi")

        elif (BMI <= 25):
            print("Vi ste normalne kilaže, i zdravi ste")

        elif (BMI <= 30):
            print("Vi imate viška kilograma")

        else:
            print("Vi imate jako puno kila, potrudite se da smršate")

    else:
        print("Unesi podatke")
        print("")

    print("Ukoliko želite da izračunate rizik za razvoj bolesti kod Vas, odgovorite na sljedeća pitanja!")
    rizik = input("Unesite Vaš spol (musko ili zensko): ")
    if rizik != 'musko' and rizik != 'zensko':
        print("***NEPOZNAT UNOS*** Program se zatvara")
        exit()
    struk = int(input("Unesite opseg Vašeg struka u centimetrima: "))
    if rizik == 'musko' and struk >= 94 and BMI <= 25:
        print("Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je NIZAK.")
        exit()
    elif struk >= 94 and BMI <= 30 and BMI > 25:
        print("Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je VISOK.")
        exit()
    elif struk >= 94 and BMI > 30:
        print("Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je VRLO VISOK.")
        exit()

    if rizik == 'musko' and struk < 94 and BMI <= 25:
        print("Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je NIZAK")
        exit()
    elif struk < 94 and BMI <= 30 and BMI > 25:
        print("Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je POVEĆAN.")
        exit()
    elif struk < 94 and BMI <= 35 and BMI > 30:
        print( "Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je VISOK.")
        exit()
    elif struk < 94 and BMI > 35:
        print("Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je VRLO VISOK.")
        exit()

    if rizik == 'zensko' and struk >= 80 and BMI <= 25:
        print("Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je NIZAK.")
        exit()
    elif struk >= 80 and BMI <= 30 and BMI > 25:
        print("Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je POVEĆAN.")
        exit()
    elif struk >= 80 and BMI <= 35 and BMI > 30:
        print("Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je VISOK.")
        exit()
    elif struk >= 80 and BMI > 35:
        print("Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je VRLO VISOK.")
        exit()

    if rizik == 'zensko' and struk < 80 and BMI <= 25:
        print("Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je NIZAK.")
    elif struk < 80 and BMI <= 30 and BMI > 25:
        print("Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je VISOK.")
    elif struk < 80 and BMI > 30:
        print("Vaš rizik za razvoj šećerne bolesti tipa II, povišenog krvnog tlaka i kardiovaskularnih bolesti je VRLO VISOK.")

if odgovor == 2:
    print ("Welcome to program that calculates your BMI")
    visina = float(input("Enter your Height in centimeters: "))
    težina = float(input("Enter your Weight in kg: "))

    BMI = težina / (visina * visina) * 10000
    print("BMI - Your body mass index is:   ", round(BMI,2))
    print("Thank you for using our program. Enjoy the rest of the day.")

    if (BMI > 0):
        if (BMI <= 16):
            print("You are very underweight")
        elif (BMI <= 18.5):
            print("You are underweight")
        elif (BMI <= 25):
            print("You are a normal weightlifter, and you are healthy")
        elif (BMI <= 30):
            print("You are overweight")
        else:
            print("You have a lot of weight, try to lose some")
    else:
        print("Enter valid details")

    print("")
    print("If you want to calculate the risk of developing your disease, answer the following questions!")
    rizik = input("Enter your gender (male or female): ")
    if rizik != 'male' and rizik != 'female':
      print("***UNKNOWN ERROR*** Program is closing")
      exit()
    struk = int(input("Enter the circumference of your waist in centimeters "))


    if rizik == 'male' and struk > 94 and BMI <= 25:
        print("Your risk for developing type II diabetes, high blood pressure and cardiovascular disease is LOW.")
    elif struk > 94 and BMI <= 30 and BMI > 25:
        print("Your risk of developing type II diabetes, high blood pressure and cardiovascular disease is HIGH.")
    elif struk > 94 and BMI > 30:
        print("Your risk for developing type II diabetes, high blood pressure and cardiovascular disease is VERY HIGH.")

    if rizik == 'male' and struk < 94 and BMI <= 25:
        print("Your risk for developing type II diabetes, high blood pressure and cardiovascular disease is LOW.")
    elif struk < 94 and BMI <= 30 and BMI > 25:
        print("Your risk of developing type II diabetes, high blood pressure and cardiovascular disease is INCREASED.")
    elif struk < 94 and BMI <= 35 and BMI > 30:
        print("Your risk of developing type II diabetes, high blood pressure and cardiovascular disease is HIGH.")
    elif struk < 94 and BMI > 35:
        print("Your risk for developing type II diabetes, high blood pressure and cardiovascular disease is VERY HIGH.")

    if rizik == 'female' and struk > 80 and BMI <= 25:
        print("Your risk for developing type II diabetes, high blood pressure and cardiovascular disease is LOW.")
    elif struk > 80 and BMI <= 30 and BMI > 25:
        print("Your risk of developing type II diabetes, high blood pressure and cardiovascular disease is INCREASED.")
    elif struk > 80 and BMI <= 35 and BMI > 30:
        print("Your risk of developing type II diabetes, high blood pressure and cardiovascular disease is HIGH.")
    elif struk > 80 and BMI > 35:
        print("Your risk for developing type II diabetes, high blood pressure and cardiovascular disease is VERY HIGH.")

    if rizik == 'female' and struk < 80 and BMI <= 25:
        print("Your risk for developing type II diabetes, high blood pressure and cardiovascular disease is LOW.")
    elif struk < 80 and BMI <= 30 and BMI > 25:
        print("Your risk of developing type II diabetes, high blood pressure and cardiovascular disease is HIGH.")
    elif struk < 80 and BMI > 30:
        print("Your risk for developing type II diabetes, high blood pressure and cardiovascular disease is VERY HIGH.")

if odgovor == 3:
    print("Willkommen beim Body-Mass-Index-Berechnungsprogramm")
    visina = float(input("Geben Sie Ihre Körpergröße in Zentimetern ein: "))
    težina = float(input("Geben Sie Ihr Gewicht in Kilogramm ein: "))

    BMI = težina / (visina * visina ) * 10000
    print("BMI - Ihr Body-Mass-Index ist:  ", round(BMI,2))
    print("Vielen Dank, dass Sie unser Programm verwenden. Genieße den Rest des Tages.")

    if (BMI > 0):
        if (BMI <= 16):
            print("Du bist sehr dünn")
        elif (BMI <= 18.5):
            print("Du bist dünn")
        elif (BMI <= 25):
            print("Sie sind normalgewichtig und gesund")
        elif (BMI <= 30):
            print("Sie sind normalgewichtig und gesund")
        else:
            print("Sie haben viel Gewicht, versuchen Sie, Gewicht zu verlieren")
    else:
        print("Daten eingeben")

    print("")
    print("Wenn Sie das Erkrankungsrisiko berechnen möchten, beantworten Sie die folgenden Fragen!")
    rizik = int(input("Geben Sie Ihr Geschlecht ein (mann oder frau): "))
    if rizik != 'mann' and rizik != 'frau':
        print("*** UNBEKANNTER FEHLER *** Programm wird geschlossen")
        exit()
    struk = int(input("Geben Sie Ihren Taillenumfang in Zentimetern ein: "))

    if rizik == 'mann' and struk > 94 and BMI <= 25:
        print("Ihr Risiko, Typ-II-Diabetes, Bluthochdruck und Herz-Kreislauf-Erkrankungen zu entwickeln, ist NIEDRIG.")
    elif struk > 94 and BMI <= 30 and BMI > 25:
        print("Ihr Risiko, Typ-II-Diabetes, Bluthochdruck und Herz-Kreislauf-Erkrankungen zu entwickeln, ist HOCH.")
    elif struk > 94 and BMI > 30:
        print("Ihr Risiko, Typ-II-Diabetes, Bluthochdruck und Herz-Kreislauf-Erkrankungen zu entwickeln, ist SEHR HOCH.")

    if rizik == 'mann' and struk < 94 and BMI <= 25:
        print("Ihr Risiko, Typ-II-Diabetes, Bluthochdruck und Herz-Kreislauf-Erkrankungen zu entwickeln, ist NIEDRIG.")
    elif struk < 94 and BMI <= 30 and BMI > 25:
        print("Ihr Risiko, Typ-II-Diabetes, Bluthochdruck und Herz-Kreislauf-Erkrankungen zu entwickeln, ist ERHÖHT.")
    elif struk < 94 and BMI <= 35 and BMI > 30:
        print("Ihr Risiko, Typ-II-Diabetes, Bluthochdruck und Herz-Kreislauf-Erkrankungen zu entwickeln, ist HOCH.")
    elif struk < 94 and BMI > 35:
        print("Ihr Risiko, Typ-II-Diabetes, Bluthochdruck und Herz-Kreislauf-Erkrankungen zu entwickeln, ist SEHR HOCH.")

    if rizik == 'frau' and struk > 80 and BMI <= 25:
        print("Ihr Risiko, Typ-II-Diabetes, Bluthochdruck und Herz-Kreislauf-Erkrankungen zu entwickeln, ist NIEDRIG.")
    elif struk > 80 and BMI <= 30 and BMI > 25:
        print("Ihr Risiko, Typ-II-Diabetes, Bluthochdruck und Herz-Kreislauf-Erkrankungen zu entwickeln, ist ERHÖHT.")
    elif struk > 80 and BMI <= 35 and BMI > 30:
        print("Ihr Risiko, Typ-II-Diabetes, Bluthochdruck und Herz-Kreislauf-Erkrankungen zu entwickeln, ist HOCH.")
    elif struk > 80 and BMI > 35:
        print("Ihr Risiko, Typ-II-Diabetes, Bluthochdruck und Herz-Kreislauf-Erkrankungen zu entwickeln, ist SEHR HOCH.")

    if rizik == 'frau' and struk < 80 and BMI <= 25:
        print("Ihr Risiko, Typ-II-Diabetes, Bluthochdruck und Herz-Kreislauf-Erkrankungen zu entwickeln, ist NIEDRIG.")
    elif struk < 80 and BMI <= 30 and BMI > 25:
        print("Ihr Risiko, Typ-II-Diabetes, Bluthochdruck und Herz-Kreislauf-Erkrankungen zu entwickeln, ist HOCH.")
    elif struk < 80 and BMI > 30:
        print("Ihr Risiko, Typ-II-Diabetes, Bluthochdruck und Herz-Kreislauf-Erkrankungen zu entwickeln, ist SEHR HOCH.")

