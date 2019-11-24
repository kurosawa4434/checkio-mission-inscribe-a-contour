from my_solution import inscribe
from random import randint
from math import hypot


def random_point(MIN=0, MAX=300): return tuple((randint(MIN, MAX), randint(MIN, MAX)))


def distance(x1, y1, x2, y2): return hypot(x2 - x1, y2 - y1)


def colinear(x1, y1, x2, y2): return x1 * y2 == y1 * x2


def random_points(min_distance=10):
    nb_points = randint(3, 30)
    while True:
        result = []
        while len(result) != nb_points:
            # It could be an infinite loop if min_distance is too big.
            pt = random_point()
            # TEST "there won't be two (or more) similar dots"
            if pt not in result:
                if all(distance(*pt, *a) >= min_distance for a in result):
                    result.append(pt)
        # TEST "there won't be a case with all the dots on the same line"
        pt = result[0]
        vectors = ((pt[0] - a[0], pt[1] - a[1]) for a in result[1:])
        v1 = next(vectors)
        if not all(colinear(*v1, *v2) for v2 in vectors):
            return result
        # It's very unlikely for random points to be all colinears.
        # Start again if that happens...


TESTS = {
    "Basics": [
        {
            "input": [[(1, 1), (1, 2), (0, 2), (3, 5), (3, 4), (4, 4)]],
            "answer": 6.0,
            'explanation': [(0.0, 2.0), (1.0, 1.0), (4.0, 4.0), (3.0, 5.0)],
        },
        {
            "input": [[(6, 5), (10, 7), (2, 8)]],
            "answer": 20.0,
            'explanation': [(2.0, 8.0), (1.692, 5.538), (9.692, 4.538), (10.0, 7.0)],
        },
        {
            "input": [[(2, 3), (3, 8), (8, 7), (9, 2), (3, 2), (4, 4), (6, 6), (7, 3), (5, 3)]],
            "answer": 41.538,
            'explanation': [(1.846, 2.231), (8.769, 0.846), (9.923, 6.615), (3.0, 8.0)],
        },
        {
            "input": [
                [(0, 0), (0, 10), (0, 20), (100, 20), (100, 30), (120, 30), (120, 20), (120, 10), (20, 10), (20, 0)]],
            "answer": 2679.208,
            'explanation': [(-1.98, 19.802), (0.198, -1.98), (121.98, 10.198), (119.802, 31.98)],
        },
        {
            "input": [[(10, 250), (60, 300), (300, 60), (250, 10)]],
            "answer": 24000.0,
            'explanation': [(10.0, 250.0), (250.0, 10.0), (300.0, 60.0), (60.0, 300.0)],
        },
        {
            "input": [[(10, 250), (60, 300), (110, 250), (160, 300), (210, 250), (160, 200), (300, 60), (250, 10)]],
            "answer": 48000.0,
            'explanation': [(10.0, 250.0), (250.0, 10.0), (350.0, 110.0), (110.0, 350.0)],
        }
    ],
    "Extra": [
        {
            "input": [[(10, 5), (30, 105), (190, 105), (210, 5), (32, 7), (68, 15), (100, 77), (180, 30), (150, 20)]],
            "answer": 20000.0,
            'explanation': [(10.0, 105.0), (10.0, 5.0), (210.0, 5.0), (210.0, 105.0)],
        },
        {
            "input": [[(5, 0), (0, 5), (50, 55), (55, 50), (70, 105), (105, 70), (120, 125), (125, 120), (170, 175), (175, 170)]],
            "answer": 11600.503,
            'explanation': [(-23.96, 39.228), (3.993, -0.705), (198.96, 135.772), (171.007, 175.705)],
        },
        {
            "input": [[(2, 2), (3, 3), (2, 4), (4, 3), (5, 3), (6, 4), (7, 3), (9, 4), (9, 3), (8, 2)]],
            "answer": 14.0,
            'explanation': [(2.0, 2.0), (9.0, 2.0), (9.0, 4.0), (2.0, 4.0)],
        },
        {
            "input": [[(1, 2), (3, 6), (5, 2), (3, 1)]],
            "answer": 16.0,
            'explanation': [(1.0, 2.0), (4.2, 0.4), (6.2, 4.4), (3.0, 6.0)],
        },
        {
            "input": [[(0, 2), (3, 5), (6, 2), (4, 1), (2, 1)]],
            "answer": 18.0,
            'explanation': [(0.0, 2.0), (3.0, -1.0), (6.0, 2.0), (3.0, 5.0)],
        },
        {
            "input": [[(2, 2), (6, 1), (6, 3), (5, 4), (7, 5), (3, 6), (4, 3)]],
            "answer": 17.0,
            'explanation': [(2.0, 2.0), (6.0, 1.0), (7.0, 5.0), (3.0, 6.0)],
        },
        {
            'input': [[(282, 212), (160, 290), (90, 276), (288, 140), (89, 23), (46, 252), (141, 3), (183, 284), (291, 186), (7, 171), (263, 240), (191, 21), (214, 30), (17, 208), (52, 41), (32, 223), (251, 249), (24, 88), (30, 62), (107, 20), (0, 146), (107, 284), (129, 279), (16, 115), (253, 43), (289, 128), (280, 88), (272, 60), (216, 275), (162, 9)]],
            'answer': 79849.548,
            'explanation': [(61.719, -26.814), (332.724, 69.973), (239.398, 331.285), (-31.606, 234.498)],
        },
    ],
    'Random': [],
    }

for _ in range(10):
    pts = random_points()
    area, rect = inscribe(pts)
    rect = [(round(x, 3), round(y, 3)) for x, y in rect]
    TESTS['Random'].append(dict(input=[pts], answer=area, explanation=rect))


if __name__ == '__main__':
    from pprint import pprint
    from local_visualization import local_visualization
    pprint(TESTS)

    points_and_rect = [(test['input'][0], test['explanation'])
                       for lst in TESTS.values() for test in lst]
    print(f'There are {len(points_and_rect)} tests.')

    local_visualization(*points_and_rect, nb_rows=5)
