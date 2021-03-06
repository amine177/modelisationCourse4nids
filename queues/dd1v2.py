# !/bin/env python
# -*- coding: utf-8 -*-
# Implementing a D/D/1 queue based on the cs1 uchicgo's class

import queue


class Customer(object):
    CUSTOMER_ID = 0

    def __init__(self, arrival_time):
        Customer.CUSTOMER_ID += 1
        self.cid = Customer.CUSTOMER_ID
        self.arrival_time = arrival_time
        self.departure_time = None

    @property
    def wait(self):
        if self.departure_time is None:
            return None
        else:
            return self.departure_time - self.arrival_time

    def __str__(self):
        return "Customer({}, {})".format(self.cid, self.arrival_time)

    def __repr__(self):
        return str(self)


def simulate_md1(lambd, mu, max_time, maxcapacity=0, verbosity=0):
    wait = 0
    served_customers = []
    unserved_customers = []

    md1 = queue.Queue(maxcapacity)

    next_arrival = 1/lambd
    next_service = next_arrival + 1/mu

    t = next_arrival

    while t < max_time:

        if t == next_arrival:
            c = Customer(arrival_time=t)
            if not md1.full():
                md1.put(c)

                if verbosity >= 2:
                    print("{:10.2f}: Customer {} arrives".format(t, c.cid))
            else:
                print("Waiting room is full!")
            next_arrival = t + 1/lambd

        if t == next_service:
            done_customer = md1.get()
            done_customer.departure_time = t
            wait += done_customer.wait
            served_customers.append(done_customer)

            if verbosity >= 2:
                print("{:10.2f}: Customer {} departs"
                      .format(t, done_customer.cid))

            if md1.empty():
                next_service = next_arrival + 1/mu
            else:
                next_service = t + 1/mu

            if verbosity >= 1:
                print("{:10.2f}: waiting room: {}".format(t, "#"*md1.qsize()))

        t = min(next_arrival, next_service)

    while not md1.empty():
        unserved_customers.append(md1.get())

    return served_customers, unserved_customers, wait


if __name__ == "__main__":
    srv, usrv, wait = simulate_md1(1, 1, 50, maxcapacity=30, verbosity=2)
    print("Mean of waiting is: {:10.2f}".format(wait/len(srv)))
