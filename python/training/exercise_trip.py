class Trip:
    """This class represents trips from city A to city B.
    A2B and B2A are timetables with times in minutes
    that represent the traveling times between cities A and B respectively.
    The journey itself takes time defined as travel_time.
    The task is to find time at the end of all trips.
    e.g. One always starts in A and then moves to B.
    After one returns to A, the trip is deemed complete.
    After that trip, another trip can start. Of course,
    if the time of ones arrival to a city is less than first
    departure time in corresponding timetable,
    then the traveler needs to wait for next available transport.
    """

    def __init__(self, a2b, b2a, trips) -> None:
        self.a2b = list(a2b)
        self.b2a = list(b2a)
        self.trips = int(trips)
        self.position = "A"
        self.current_time = 0

    def move_to_b(self, travel_time=90) -> None:
        found = False
        while not found:
            if self.a2b:
                time_of_departure_from_a = self.a2b.pop(0)
                if time_of_departure_from_a >= self.current_time:
                    self.position = "B"
                    self.current_time = time_of_departure_from_a + travel_time
                    found = True
            else:
                break

    def move_to_a(self, travel_time=130) -> None:
        found = False
        while not found:
            if self.b2a:
                time_of_departure_from_b = self.b2a.pop(0)
                if time_of_departure_from_b >= self.current_time:
                    self.position = "A"
                    self.current_time = time_of_departure_from_b + travel_time
                    found = True
            else:
                break

    def calculate(self) -> int:
        while self.trips:
            self.move_to_b()
            self.move_to_a()
            self.trips -= 1
        return self.position, self.current_time


if __name__ == "__main__":
    trip = Trip(
        a2b=[50, 200, 460, 600, 660, 760, 800, 1200], b2a=[149, 300, 499, 600, 750, 850, 900, 1010, 1300], trips=4
    )
    result: int = trip.calculate()
    print(result)
    assert result[1] == 1430

    trip2 = Trip(
        a2b=[50, 200, 460, 600, 660, 760, 800, 1200], b2a=[149, 300, 499, 600, 750, 850, 900, 1010, 1300], trips=1
    )
    result: int = trip2.calculate()
    print(result)
    assert result[1] == 279

    trip3 = Trip(
        a2b=[0, 300, 460, 600, 660, 760, 800, 1200], b2a=[109, 420, 499, 600, 750, 850, 900, 1010, 1300], trips=2
    )
    result: int = trip3.calculate()
    print(result)
    assert result[1] == 550
