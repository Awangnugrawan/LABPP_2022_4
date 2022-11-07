class kubus :
    def __init__(self,inputLebar,inputTinggi,inputPanjang) :
        self.lebar=inputLebar
        self.tinggi=inputTinggi
        self.panjang=inputPanjang

    # def setLebar(self,inputLebar):
    #     self.lebar=inputLebar
    # def setTinggi(self,inputTinggi):
    #     self.tinggi=inputTinggi
    # def setPanjang(self,inputPanjang):
    #     self.panjang=inputPanjang
    def setMassa(self,inputmassa):
        self.massa=inputmassa
    def getMassaJenis(self):
        self.massaJenis=self.massa/(self.panjang*self.lebar*self.tinggi)
        return self.massaJenis

lebar=float(input())
tinggi=float(input())
panjang=float(input())
massa=float(input())

kubus=kubus(lebar,tinggi,panjang)
# kubus.setLebar(lebar)
# kubus.setTinggi(tinggi)
# kubus.setPanjang(panjang)
kubus.setMassa(massa)
print('Massa Jenis =', kubus.getMassaJenis())
kubus.setMassa(massa*2)
print('Massa Jenis =', kubus.getMassaJenis())