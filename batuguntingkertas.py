from random import randint
lanjut = True
while lanjut:
    def pilihan(n):
        x=0
        y=0
        z=0
        if n == 0:
            return 'BATU'
        elif n == 1:
            return 'GUNTING'
        elif n == 2:
            return 'KERTAS'
        else:
            return 'pilihan yang tidak tersedia di menu'

    def ronde():
        ronde = 0
        menang = 0
        kalah = 0
        x=0
        y=0
        z=0
        while True:
            ronde+=1
            komputer = randint(0,2)
            print(('='*75).center(75))
            print(f' [Ronde ke-{ronde}] '.center(75,'x'))
            print(' Batu-Gunting-Kertas '.center(75,'x'))
            print("-"*75)
            print("0. BATU     1. GUNTING     2. KERTAS".center(75))
            print("-"*75)
            
            print(">>>>>>> Giliran Kamu <<<<<<<")
            n = int(input('Pilihan: '))
            print(f'Kamu memilih {pilihan(n)}')
            print(">>>>> Giliran Komputer <<<<<")
            print(f'Komputer memilih {pilihan(komputer)}')
            if n == 0 or komputer == 0:
                x+=1
                if n==komputer:
                    x+=1
            if n == 1 or komputer == 1:
                y+=1
                if n==komputer:
                    y+=1
            if n == 2 or komputer == 2:
                z+=1
                if n==komputer:
                    z+=1

            if n == komputer:
                print(f'Permainan ronde ke-{ronde} adalah seri')
            elif (komputer == 0 and n == 1) or (komputer == 1 and n == 2) or (komputer == 2 and n == 0):
                print(f'Pemenang ronde ke-{ronde} adalah Komputer')
                kalah+=1
            elif (n == 0 and komputer == 1) or (n == 1 and komputer == 2) or (n == 2 and komputer == 0):
                print(f'Pemenang ronde ke-{ronde} adalah Kamu')
                menang+=1
            else:
                print(pilihan(n))     
            print(f'Skor: Kamu {menang}-{kalah} Komputer\n')
            if menang == 3 or kalah == 3:
                if kalah == 3:
                    print(f'Permainan selesai pada ronde ke-{ronde} dan dimenangkan oleh Komputer')
                elif menang == 3:
                    print(f'Permainan selesai pada ronde ke-{ronde} dan dimenangkan oleh Kamu')

                if x==y==z:
                    modus="BATU, GUNTING, dan KERTAS"
                    ket=x
                if x==y and x>z:
                    modus="BATU dan GUNTING"
                    ket=x
                if x==z and x>y:
                    modus="BATU dan KERTAS"
                    ket=x
                if y==z and y>x:
                    modus="GUNTING dan KERTAS"
                    ket=y

                if x>y and x>z:
                    modus="BATU"
                    ket=x
                if y>x and y>z:
                    modus="GUNTING"
                    ket=y
                if z>x and z>y:
                    modus="KERTAS"
                    ket=z
                print(f"Pilihan yang sering digunakan adalah {modus} sebanyak {ket} kali")
                break
    ronde()
    respon = input('Kembali ke awal? (yes/no) ')
    if respon == "no":
        lanjut = False
    print('-'*75)
print("Terima kasih".center(75))
