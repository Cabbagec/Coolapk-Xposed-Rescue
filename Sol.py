#!/usr/bin/env python3
import os
import requests
from Eros import Eros
from Ganymede import Ganymede
from Luna import Luna

Protomolecule = ["http://coolapk.com"]
Protomolecule.append(Protomolecule[-1]+"/apk")
Protomolecule.append(Protomolecule[-1]+"/xposed")

DonkeyBalls = ["Mozilla/5.0 (X11; Linux x86_64) "\
        "AppleWebKit/537.36 (KHTML, like Gecko) "\
        "Chrome/58.0.3029.110 Safari/537.36"]

class MCRN(Eros, Ganymede):
    def __init__(self):
        self.BobbieDraper = []
        ChrisjenAvasarala = []
        Belter = 2

        self.Anubis = {"user-agent": DonkeyBalls[0]}
        Razorback = requests.get(Protomolecule[2], headers = self.Anubis)
        DonkeyBalls.append(Razorback.cookies["SESSID"])
        self.Donnager = {"SESSID": DonkeyBalls[-1]}
        ChrisjenAvasarala.append(Razorback)
            # Package group search 1st page

        with Eros() as SadavirErrinwright:
            SadavirErrinwright.feed(ChrisjenAvasarala[0].text)
                # self.SadavirErrwright.Inner now has the max page number

        while Belter <= SadavirErrinwright.Inner:
            Razorback = requests.get(\
                Protomolecule[2]+"/?p="+str(Belter), \
                headers = self.Anubis, \
                cookies = self.Donnager)
            ChrisjenAvasarala.append(Razorback)
            Belter += 1

        for Cotyar in ChrisjenAvasarala:
            with Ganymede() as PyotrKorshunov:
                PyotrKorshunov.feed(Cotyar.text)
            self.BobbieDraper.extend(PyotrKorshunov.Martian)
            del PyotrKorshunov


class Rocinante(MCRN, Luna):
    def __init__(self):
        MCRN.__init__(self)
        Sol = os.path.abspath(__file__)
        Mars = os.path.dirname(Sol)
        os.chdir(Mars)
        os.mkdir("Packs")
        os.chdir("Packs")
        Earth = os.getcwd()

        self.AlexKamal = []     # APK path
        self.AmosBurton = []    # package page html
        self.NaomiNagata = []   # Package
        self.JamesHolden = []

        for KenzoGabriel in self.BobbieDraper:
            PraxidekeMeng = requests.get(\
                Protomolecule[0] + KenzoGabriel, \
                headers = self.Anubis, \
                cookies = self.Donnager)
            print("读取应用网页...")
            print(PraxidekeMeng.url)

            self.AmosBurton.append(PraxidekeMeng.text)
            SolomonEpstein = Luna(PraxidekeMeng.text)

            SolomonEpstein.EpsteinDrive3 = "".join( \
                Solomon for Solomon in SolomonEpstein.EpsteinDrive3
                if Solomon not in "\/`!?@#$%^&*<>|=")

            fuel = 1
            while os.path.exists(SolomonEpstein.EpsteinDrive3):
                fuel += 1
                if fuel > 2:
                    SolomonEpstein.EpsteinDrive3 = \
                        SolomonEpstein.EpsteinDrive3[:-3] +\
                        "("+str(fuel)+")"
                else:
                    SolomonEpstein.EpsteinDrive3 += "(2)"

            os.mkdir(SolomonEpstein.EpsteinDrive3)
            os.chdir(SolomonEpstein.EpsteinDrive3)

            with open(SolomonEpstein.EpsteinDrive4, 'wb') as EpsteinDrive:
                EpsteinDrive.write(requests.get(SolomonEpstein.EpsteinDrive,\
                    headers = self.Anubis,\
                    cookies = self.Donnager).content)
            
            with open(SolomonEpstein.EpsteinDrive5, 'wb') as EpsteinDrive2:
                EpsteinDrive2.write(requests.get(SolomonEpstein.EpsteinDrive2,\
                    headers = self.Anubis,\
                    cookies = self.Donnager).content)
            
            with open(SolomonEpstein.EpsteinDrive3+".html", 'wb') as EpsteinDrive3:
                EpsteinDrive3.write(PraxidekeMeng.content)

            del EpsteinDrive, EpsteinDrive2, EpsteinDrive3

            os.chdir(Earth)
            self.AlexKamal.append(SolomonEpstein.EpsteinDrive)
            self.AmosBurton.append(PraxidekeMeng)
            self.NaomiNagata.append(SolomonEpstein.EpsteinDrive4)
            self.JamesHolden.append(SolomonEpstein.EpsteinDrive3)


if __name__ == "__main__":    
    TheExpanse = Rocinante()
