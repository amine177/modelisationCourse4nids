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
            return self.departue_time - self.arrival_time

    def __str__(self):
        return "Customer({}, {})".format(self.cid, self.arrival_time)

    def __repr__(self):
        return str(self)


def simulate_md1(lambd, mu, max_time, verbosity=0):
    served_customers = []
    unserved_customers = []

    md1 = queue.LifoQueue()

    next_arrival = 1/lambd
    next_service = next_arrival + 1/mu

    t = next_arrival

    while t < max_time:

        if t == next_arrival:
            c = Customer(arrival_time=t)
            md1.put(c)

            if verbosity >= 2:
                print("{:10.2f}: Customer {} arrives".format(t, c.cid))

            next_arrival = t + 1/lambd

        if t == next_service:
            done_customer = md1.get()
            done_customer.departure_time = t
            served_customers.append(done_customer)

            if verbosity >= 2:
                print("{:10.2f}: Customer {} departs"
                      .format(t, done_customer.cid))

            if md1.empty():
                next_service = next_arrival + 1/mu
            else:
                next_service = t + 1/mu

            if verbosity >= 1:
                print("{:10.2f}: {}".format(t, "#"*md1.qsize()))

        t = min(next_arrival, next_service)

    while not md1.empty():
        unserved_customers.append(md1.get())

    return served_customers, unserved_customers


if __name__ == "__main__":
    simulate_md1(2, 1, 100, verbosity=2)
