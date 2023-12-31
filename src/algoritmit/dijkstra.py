import time
import heapq
from math import sqrt
from kartta.kartta import kartta
from komponentit.solmut import Solmu
from komponentit.kaaret import Kaari


class Prioriteettijono:

    # Luokka, jolla huolehditaan siitä, että algoritmi priorisoi lyhyemmän etäisyyden päässä olevien naapureiden tutkimista.

    def __init__(self):
        self.pino = {}

    def lisaa_jonoon(self, objekti, prioriteetti):
        self.pino[objekti] = prioriteetti

    def poista_lahin(self):
        lahin = min(self.pino, key=lambda solmu: self.pino[solmu])
        del self.pino[lahin]
        return lahin

    def pituus(self):
        return len(self.pino)


class Dijkstra:

    # Luokka, jolla toteutetaan Dijkstran algoritmi.

    def __init__(self, kartta):
        self.solmut = []
        self.keko = Prioriteettijono()
        self.alkusolmu = None
        self.loppusolmu = None
        self.polku = []
        self.kartta = kartta

    def luo_verkko(self):

        # Luodaan solmuista ja kaarista koostuva verkko, jota algoritmi voi käyttää.

        for j in range(len(self.kartta)):
            rivi = []
            for i in range(len(self.kartta[j])):
                rivi.append(Solmu((i, j), self.kartta[j][i]))
            self.solmut.append(rivi)
        for j in range(len(self.solmut)):
            for i in range(len(self.solmut[j])):
                if self.solmut[j][i].tyyppi == 1:
                    self.alkusolmu = self.solmut[j][i]
                    self.alkusolmu.etaisyys = 0
                    self.alkusolmu.keossa = True
                if self.solmut[j][i].tyyppi == 2:
                    self.loppusolmu = self.solmut[j][i]
                if j > 0 and j < len(self.solmut) - 1:
                    if i > 0 and i < len(self.solmut[j]) - 1:
                        if self.kartta[j-1][i] != 3:
                            self.solmut[j][i].naapurit.append(
                                Kaari(self.solmut[j-1][i], 1))
                        if self.kartta[j+1][i] != 3:
                            self.solmut[j][i].naapurit.append(
                                Kaari(self.solmut[j+1][i], 1))
                        if self.kartta[j][i-1] != 3:
                            self.solmut[j][i].naapurit.append(
                                Kaari(self.solmut[j][i-1], 1))
                        if self.kartta[j][i+1] != 3:
                            self.solmut[j][i].naapurit.append(
                                Kaari(self.solmut[j][i+1], 1))
                        if self.kartta[j+1][i+1] != 3:
                            self.solmut[j][i].naapurit.append(
                                Kaari(self.solmut[j+1][i+1], sqrt(2)))
                        if self.kartta[j+1][i-1] != 3:
                            self.solmut[j][i].naapurit.append(
                                Kaari(self.solmut[j+1][i-1], sqrt(2)))
                        if self.kartta[j-1][i+1] != 3:
                            self.solmut[j][i].naapurit.append(
                                Kaari(self.solmut[j-1][i+1], sqrt(2)))
                        if self.kartta[j-1][i-1] != 3:
                            self.solmut[j][i].naapurit.append(
                                Kaari(self.solmut[j-1][i-1], sqrt(2)))
                if j == 0 and i > 0 and i < len(self.solmut[j]) - 1:
                    if self.kartta[j][i+1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j][i+1], 1))
                    if self.kartta[j][i-1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j][i-1], 1))
                    if self.kartta[j+1][i] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j+1][i], 1))
                    if self.kartta[j+1][i+1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j+1][i+1], sqrt(2)))
                    if self.kartta[j+1][i-1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j+1][i-1], sqrt(2)))
                if j == len(self.solmut) - 1 and i > 0 and i < len(self.solmut[j]) - 1:
                    if self.kartta[j][i+1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j][i+1], 1))
                    if self.kartta[j][i-1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j][i-1], 1))
                    if self.kartta[j-1][i] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j-1][i], 1))
                    if self.kartta[j-1][i+1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j-1][i+1], sqrt(2)))
                    if self.kartta[j-1][i-1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j-1][i-1], sqrt(2)))
                if i == 0 and j > 0 and j < len(self.solmut) - 1:
                    if self.kartta[j+1][i] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j+1][i], 1))
                    if self.kartta[j-1][i] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j-1][i], 1))
                    if self.kartta[j][i+1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j][i+1], 1))
                    if self.kartta[j+1][i+1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j+1][i+1], sqrt(2)))
                    if self.kartta[j-1][i+1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j-1][i+1], sqrt(2)))
                if i == len(self.solmut[j]) - 1 and j > 0 and j < len(self.solmut) - 1:
                    if self.kartta[j+1][i] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j+1][i], 1))
                    if self.kartta[j-1][i] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j-1][i], 1))
                    if self.kartta[j][i-1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j][i-1], 1))
                    if self.kartta[j-1][i-1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j-1][i-1], sqrt(2)))
                    if self.kartta[j+1][i-1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j+1][i-1], sqrt(2)))
                if j == 0 and i == 0:
                    if self.kartta[j+1][i+1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j+1][i+1], sqrt(2)))
                    if self.kartta[j][i+1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j][i+1], 1))
                    if self.kartta[j+1][i] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j+1][i], 1))
                if j == 0 and i == len(self.solmut[j]) - 1:
                    if self.kartta[j+1][i-1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j+1][i-1], sqrt(2)))
                    if self.kartta[j+1][i] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j+1][i], 1))
                    if self.kartta[j][i-1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j][i-1], 1))
                if j == len(self.solmut) - 1 and i == 0:
                    if self.kartta[j-1][i+1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j-1][i+1], sqrt(2)))
                    if self.kartta[j-1][i] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j-1][i], 1))
                    if self.kartta[j][i+1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j][i+1], 1))
                if j == len(self.solmut) - 1 and i == len(self.solmut[j]) - 1:
                    if self.kartta[j-1][i-1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j-1][i-1], sqrt(2)))
                    if self.kartta[j-1][i] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j-1][i], 1))
                    if self.kartta[j][i-1] != 3:
                        self.solmut[j][i].naapurit.append(
                            Kaari(self.solmut[j][i-1], 1))

    def reitinhaku(self):

        # Metodi, jolla Dijkstran algoritmi toteutetaan.

        alku = time.time()

        # Luodaan ensin verkko algoritmia varten.

        self.luo_verkko()

        # Varsinainen Dijkstran algoritmi.

        self.keko.lisaa_jonoon(self.alkusolmu, self.alkusolmu.etaisyys)
        while self.keko.pituus() != 0:
            solmu = self.keko.poista_lahin()
            if solmu.koordinaatit == self.loppusolmu.koordinaatit:
                break
            if solmu.kasitelty:
                continue
            solmu.kasitelty = True
            for kaari in solmu.naapurit:
                if not kaari.loppu.kasitelty:
                    nyky = kaari.loppu.etaisyys
                    uusi = solmu.etaisyys + kaari.pituus
                    if uusi < nyky:
                        kaari.loppu.etaisyys = uusi
                    if not kaari.loppu.keossa:
                        kaari.loppu.keossa = True
                        self.keko.lisaa_jonoon(
                            kaari.loppu, kaari.loppu.etaisyys)
                        kaari.loppu.edellinen = solmu
        if self.loppusolmu.etaisyys != float("inf"):
            while solmu.edellinen.koordinaatit != self.alkusolmu.koordinaatit:
                self.polku.append(solmu.edellinen)
                solmu = solmu.edellinen
        loppu = time.time()

        print()
        print("Dijkstra: ")
        if self.loppusolmu.etaisyys == float("inf"):
            print("Polkua ei löytynyt.")
        else:
            print(f"Polun pituus: {self.loppusolmu.etaisyys:.2f}")
        print(f"Aikaa kului: {loppu-alku} s.")
        print()

        if self.loppusolmu.etaisyys != float("inf"):
            # Piirretään löydetty polku kartalle.
            for solmu in self.polku:
                pos_x = solmu.koordinaatit[0]
                pos_y = solmu.koordinaatit[1]
                self.kartta[pos_y][pos_x] = 4

        # Alla olevalla koodilla saa värjättyä tutkitut ruudut kartalla.
#        for j in range(len(self.solmut)):
#            for i in range(len(self.solmut[j])):
#                pos_x = self.solmut[j][i].koordinaatit[0]
#                pos_y = self.solmut[j][i].koordinaatit[1]
#                if self.solmut[j][i].koordinaatit != self.alkusolmu.koordinaatit:
#                    if self.solmut[j][i].kasitelty:
#                        self.kartta[pos_y][pos_x] = 5
