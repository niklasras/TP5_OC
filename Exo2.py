somme = 0
sommecoef = 0
S3 = []
S4 = []

for i in range(5):
    S1=input("Veuillez entrer la note et le coefficient correspondant: ")
    S2 = S1.split(" ")
    S3.append(int(S2[0]))
    S4.append(int(S2[1]))


for i in range(len(S3)):
    somme += S3[i] * S4[i]
    sommecoef += S4[i]

print (f"la moyenne est {somme/sommecoef}")