from feeders.alibaba import AlibabaSource


class Client:
    def __init__(self, strategy):
        self.strategy = strategy

    def notify(self):
        self.strategy.notify()


if __name__ == '__main__':
    filters = {"Origin": 130,  # شاهرود
               "Destination": 191,  # مشهد
               "DepartureDate": "2022-05-19T00:00:00",
               "TicketType": "Family",
               "IsExclusiveCompartment": False,
               "PassengerCount": 1,
               "ReturnDate": None,
               "ServiceType": None,
               "Channel": 1,
               "AvailableTargetType": None,
               "Requester": None,
               "UserId": 0}

    client = Client(AlibabaSource(filters))
    client.notify()
