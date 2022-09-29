x = 0
z=0
y=0
n=0
stop = False
while stop == False :
    stop1 = False
    print("qual canditado deseja votar?")
    print("889 para candidato x")
    print("847 para candidato y")
    print("515 para candidato z")
    print("0 para nulo")
    try:
        voto = int(input())
    
        def eleicao (voto):
            if voto == 889:
                resu = 1
            elif voto == 847:
                resu = 2
            elif voto == 515:
                resu = 3
            else:
                resu = 0
            return resu
        apu = eleicao(voto)
        if apu == 1:
            x = x+1
        if apu == 2:
            y= y+1
        if apu == 3:
            z = z+1
        if apu == 0 :
            n = n+1
        stop1 = False
        while stop1 == False:
            encer = input("deseja para a votação?[s/n] : ")
            if encer == "s":
                stop1 =True
                stop = True
            elif encer == "n" :
                stop1 = True
            else:
                print("não entendi sua resposta")
    except:
        print("sua resposta foi invalida")
if x>z and x>y :
    print("o vencedor da eleição foi o x")
elif z>x and z>y :
    print("o vencedor da eleição foi o z")
elif y>z and y>x :
    print("o vencedor da eleição foi o z")
else:
    print("esse eleição teve um empate")
print("o candidato x teve ", x, "voto(s)")
print("o candidato y teve ", y, "voto(s)")
print("o candidato z teve ", z, "voto(s)")
print("nulo:", n)