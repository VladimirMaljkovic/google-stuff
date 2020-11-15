"""should look into back tracking
or maybe a graph implementation
god knows

im gonna start with a greedy algorithm
u fazonu
ako sam u i=0, trazim najmanje j
idem tu
sad mi je i=j
za to i sad trazim novo j
gledam sta ce se desiti
dodajem kontrolu za infinite loop
pokusavam da se usmerim (maybe) ka cilju u odnosu na vreme
plakacu

marko:
da napravim listu apsolutno svih mogucnosti
tipa
kad sam u o,o
da pisem t i delta t za svako polje na koje mogu da idem
pa onda pravim novu listu gde upisujem sva ostala polja ged mogu da idem
to je sve super ali jebeno nemam pojma kako da se krecem ja kroz tu strukturu posle
"""


def attempt1(m, time):
    pass


if __name__ == '__main__':
    matrix = [
        [0, 2, 2, 2, -1],  # 0 = Start
        [9, 0, 2, 2, -1],  # 1 = Bunny 0
        [9, 3, 0, 2, -1],  # 2 = Bunny 1
        [9, 3, 2, 0, -1],  # 3 = Bunny 2
        [9, 3, 2, 2, 0],  # 4 = Bulkhead
    ]

    attempt1(matrix, 1)