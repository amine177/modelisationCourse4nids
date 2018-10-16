# !/bin/env python
# -*- coding: utf-8 -*-


class Client:
    """
        A class simulating a client
        ar_t: arrival time, wt: waiting time, bs_t: service time's start
        st: service time
    """

    def arrive(self, ar_t):
        self.ar_t = ar_t

    def begin_serve(self, bs_t):
        self.bs_t = bs_t
        self.wt = self.bw_t - self.bs_t

    def serve_end(self, se_t):
        self.se_t = se_t
        self.st = self.bs_t - self.se_t

    def arrival_time(self):
        return self.ar_t

    def waiting_time(self):
        return self.wt

    def service_time(self):
        return self.st

    def __str__(self):
        return "Client(arrived = {:d}, waited = {:d}, served = {:d})".format(
                self.ar_t, self.wt, self.st)


class WaitingRoom:
    """
        A class simulating a waiting room
    """

    def __init__(self):
        self.queue = []
        self.index = 0

    def arrive(self, client):
        self.queue = [client] + self.queue
        self.index += 1

    def serve(self, client):
        self.index -= 1
        return self.queue.pop()

    def peek(self, client):
        return self.queue[self.index - 1]

    def isempty(self):
        return self.index == 0

    def numberOfClients(self):
        return self.index


class Server:
    """
        A server class to manage the serving event
        S event, F event
    """

    def __init__(self, lambd):
        self.lambd = lambd

    def serveClient(self, waitingRoom):
        self.client = waitingRoom.serve()


class Arrival:
    """
        A class to take care of arrivals , A events
    """

    def __init__(self, lamda, clock):
        self.number = 0
        self.lamda = lamda
        self.clock = clock
        self.arrive()

    def arrive(self):
        """
            execute an arrival and plan a next one
            t : current time of simulation
        """
        # todo plan another arrival
        time = self.clock.getTime()
        self.number += 1
        e = Event("A", time+1/self.lamda, self.arrive)
        self.clock.addEvent(e)
        print("New arrival {:} : {:5.2f}".format(self.number, time))

    def execute(self):
        pass


class Clock:
    """
        A clock class, to simulate time
    """

    def __init__(self):
        self.time = 0
        self.events = []

    def addEvent(self, event):
        self.events.append(event)
        self.events = sorted(self.events, key=lambda e: e.time, reverse=False)

    def executeEvent(self):
        if len(self.events) > 0:
            self.time = self.events[0].time
            self.events[0].execute()
            self.events.remove(self.events[0])

    def getTime(self):
        print("Debug, Clock: {}".format(self.time))
        return self.time

    def run(self):
        while True:
            if len(self.events) > 0:
                self.executeEvent()


class Event:
    """
        An event class
        tp: type , A: arrival, S: service, F: fin
    """
    def __init__(self, tp, time, f):
        self.tp = tp
        self.time = time
        self.fct = f

    def execute(self):
        self.fct()


class Queue:
    """
        The whole queue system
    """


if __name__ == "__main__":
    clock = Clock()
    ap = Arrival(5, clock)
    clock.run()
