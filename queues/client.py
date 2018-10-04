# !/bin/env python
# -*- coding: utf-8 -*-


class Client:
    """
        A class simulating a client
        a_t: arrival time, w_t: waiting time, s_t: service time
        t_t: total time
    """

    def __init__(self, a_t, w_t, s_t):
        self.a_t = a_t
        self.w_t = w_t
        self.s_t = s_t

    def waiting_time(self):
        return self.w_t

    def arrival_time(self):
        return self.a_t

    def service_time(self):
        return self.s_t

    def total_time(self):
        return self.w_t + self.s_t

    def __str__(self):
        return "Client(arrived = {:d}, waited = {:d}, served = {:d})".format(
                self.a_t, self.w_t, self.s_t)
