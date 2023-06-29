letra = input("Ingrese una letra: ").lower()

if len(letra) == 1 and letra.isalpha():
    for i in range(ord(letra), ord('z')+1):
        print(chr(i))
else:
    print("Ingrese una única letra válida.")
