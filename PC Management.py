datorer = ["Dator 1", "Dator 2", "Dator 3", "Dator 4", "Dator 5"]
på_service = []

while len(på_service) < 3:
    print("\nTillgängliga datorer för service:")
    for i in range(len(datorer)):
        print(i + 1, "-", datorer[i])
    
    print("\nDatorer som är på service:")
    if på_service:
        for dator in på_service:
            print(dator)
    else:
        print("Inga datorer på service.")

    try:
        val = int(input("Ange numret på den dator som ska skickas på service: ")) - 1
        
        if 0 <= val < len(datorer):
            på_service.append(datorer[val])  # Lägg till datorn i på_service
            datorer.pop(val)  # Ta bort datorn från datorer
        else:
            print("Felaktigt val, försök igen.")
    except ValueError:
        print("Vänligen ange ett giltigt nummer.")

if len(på_service) == 3:
    print("Du har skickat följande datorer på service:")
    for dator in på_service:
        print("-", dator)

print("Programmet avslutas.")