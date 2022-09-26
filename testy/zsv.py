konto = 30000
per = 0.0075

for i in range(15):
    print(str(i+1) + ". měsíc:")
    print("konto:",konto)
    print("per:", konto*per)
    konto += konto*per