
### VARIANTA preferata
if 10 > 2:
    print("Adevarat")
else:
    print("Fals")

### VARIANTA  NEPREFERATA 
if (10 > 2): {
    print("Adevarat")
}
else: {
    print("Fals")
}
    


varsta = 60

if varsta < 18:
    print("Minor")
else: 
    if varsta < 25:
        print("Young adult")
    else:
        if varsta < 65:
            print("Matur")
        else:
            print("Pensionar")


if varsta < 18:
    print("Minor")
elif varsta < 25:
    print("Young adult")
elif varsta < 65:
    print("Matur")
else:
    print("Pensionar")
