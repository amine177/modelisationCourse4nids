import sys


class ProcessusArrivee():
    def __init__(self,lamda,H):
        self.number=0
        self.lamda=lamda
        self.H=H
        self.NouveauClient()
    def NouveauClient(self):
        self.number+=1
        temps=self.H.instant
        A=Event("A",temps+1/self.lamda,self.NouveauClient)
        self.H.AddEvent(A)
        print("Nouvelle Arrivee: " + str(temps) + "Numero: " + str(self.number))

class Horloge():
    def __init__(self):
        self.EventList=[]
        self.instant=0

    def AddEvent(self,Event):
        self.EventList.append(Event)
        self.EventList=sorted(self.EventList,key=lambda e:e.tim,reverse=False)
    def ExecuteEvent(self):
        if len(self.EventList)>0:
            self.instant=self.EventList[0].tim
            self.EventList[0].Execute()
            self.EventList=self.EventList[1:]
    def Run(self):
        while True:
            if len(self.EventList)>0:
                self.ExecuteEvent()


class Event():
    def __init__(self,typ,tim,fct):
        self.typ=typ
        self.tim=tim
        self.fct=fct
    def Execute(self):
        self.fct()

H=Horloge()
P=ProcessusArrivee(2,H)
H.Run()
