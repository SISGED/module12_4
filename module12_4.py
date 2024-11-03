import logging
import unittest
class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

first = Runner('Вося', 10)
second = Runner('Илья', 5)
third = Runner('Арсен', 10)

t = Tournament(101, first, second)
print(t.start())


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            run1 = Runner('Вася', -1)
            for i in range(10):
                run1.walk()
            self.assertEqual(run1.distance, 100)
            logging.INFO("'test_walk' выполнен успешно")
        except ValueError as err:
            logging.WARNING("Неверная скорость для Runner", exc_info=True)


    def test_run(self):
        try:
            run2 = Runner(123, 10)
            for i in range(10):
                run2.run()
            self.assertEqual(run2.distance, 100)
            logging.INFO("'test_run' выполнен успешно'")
        except TypeError as err:
            logging.WARNING("Неверный тип данных для объекта Runner", exc_info=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode="w", filename="py.log",
                    encoding="utf-8", format="%(asctime)s | %(levelname)s | %(message)s")