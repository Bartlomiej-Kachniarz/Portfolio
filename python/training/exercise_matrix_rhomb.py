# OOP SOLUTION #
class Rhomb:
    """This class represents a single exercise - rhomb.
    The input consists of matrix with integer values and a radius.
    The radius is the distance between cells in the matrix.
    The goal is to find such a point that has maximum
    sum of values in the distance equal to the radius provided
    (but in a shape of a rhomb).
    e.g.: For such a matrix: and radius: 1...
    [[1, 2, 3, 4],
     [3, 4, 5, 4],
     [6, 7, 8, 5],
     [2, 4, 2, 0]]
     ...there are 4 points that can be taken into account.

     For example point [1][1] => 4:
     The sum of values in this example is:
     2 + 3 + 7 + 5 = 17

     For another point: e.g. [2][1] => 7:
     The sum of values in this example is:
     4 + 6 + 8 + 4 = 22

     The result should be the maximum sum of rhombs.
     Therefore the answer is 22 (there are 2 more points to check).
    """

    def __init__(self, matrix, radius) -> None:
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        self.radius = radius
        self.centers = []
        self.offsets = []

    def determine_valid_centers(self) -> None:
        for row in range(self.radius, self.rows - self.radius):
            for col in range(self.radius, self.cols - self.radius):
                self.centers.append((row, col))

    def determine_offsets(self) -> None:
        for x in range(-self.radius, self.radius + 1, 1):
            for y in range(-self.radius, self.radius + 1, 1):
                if abs(x) + abs(y) == self.radius:
                    self.offsets.append((x, y))

    def calculate_sum(self) -> None:
        list_of_values = []
        for cent in self.centers:
            list_per_center = []
            for row_off, col_off in self.offsets:  # apply offsets
                list_per_center.append(self.matrix[int(cent[0] + row_off)][int(cent[1] + col_off)])
            list_of_values.append((cent, sum(list_per_center)))

        return max(list_of_values, key=lambda x: x[1])

    def calculate(self) -> int:
        self.determine_valid_centers()
        self.determine_offsets()
        return self.calculate_sum()


# FUNCTIONAL SOLUTION #
def solution(matrix, radius):
    # centers = []
    rows = len(matrix)
    cols = len(matrix[0])
    sum_max = 0
    summ = 0

    for row in range(radius, rows - radius):
        for col in range(radius, cols - radius):
            summ = 0
            for k in range(-radius, radius + 1):
                if abs(k) == radius:
                    summ += matrix[row][col + k]
                else:
                    summ += matrix[row + (radius - abs(k))][col + k]
                    summ += matrix[row - (radius - abs(k))][col + k]
            sum_max = max(summ, sum_max)
    return sum_max


# TESTING #
if __name__ == "__main__":
    trip = Rhomb(
        matrix=[
            [0, 1, 3, 6, 6, 7, 8, 1],
            [1, 3, 4, 6, 5, 5, 9, 3],
            [4, 3, 1, 1, 2, 0, 9, 8],
            [2, 6, 0, 7, 9, 1, 0, 4],
            [2, 4, 6, 2, 8, 9, 6, 1],
            [9, 8, 2, 1, 6, 2, 0, 3],
            [8, 3, 1, 5, 4, 2, 9, 7],
            [6, 7, 3, 5, 1, 7, 3, 3],
        ],
        radius=3,
    )
    center, result = trip.calculate()
    print(center, result)
    assert result == 56

    trip2 = Rhomb(
        matrix=[
            [5, 2, 2, 6, 1, 0, 2],
            [0, 3, 0, 1, 2, 9, 7],
            [1, 3, 4, 6, 5, 5, 9],
            [2, 6, 0, 7, 9, 1, 0],
            [3, 2, 6, 0, 7, 9, 1],
        ],
        radius=1,
    )
    center, result = trip2.calculate()
    print(center, result)
    assert result == 24

    trip3 = Rhomb(
        matrix=[
            [3, 2, 6, 0, 7, 9, 1, 0, 1],
            [9, 3, 0, 6, 0, 5, 9, 1, 5],
            [0, 4, 2, 5, 8, 9, 2, 0, 2],
            [9, 3, 2, 1, 1, 1, 0, 9, 8],
            [2, 3, 5, 2, 8, 7, 6, 4, 6],
            [2, 4, 6, 3, 2, 6, 4, 7, 0],
            [9, 3, 0, 6, 0, 5, 9, 1, 5],
            [0, 4, 2, 5, 8, 9, 2, 0, 2],
        ],
        radius=3,
    )
    center, result = trip3.calculate()
    print(center, result)
    assert result == 64

    # FUNCTIONAL #
    matrix_ = [
        [3, 2, 6, 0, 7, 9, 1, 0, 1],
        [9, 3, 0, 6, 0, 5, 9, 1, 5],
        [0, 4, 2, 5, 8, 9, 2, 0, 2],
        [9, 3, 2, 1, 1, 1, 0, 9, 8],
        [2, 3, 5, 2, 8, 7, 6, 4, 6],
        [2, 4, 6, 3, 2, 6, 4, 7, 0],
        [9, 3, 0, 6, 0, 5, 9, 1, 5],
        [0, 4, 2, 5, 8, 9, 2, 0, 2],
    ]
    radius_ = 3
    result = solution(matrix=matrix_, radius=radius_)
    print(result)
    assert result == 64
