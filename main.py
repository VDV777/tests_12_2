import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


# Класс Tournament
class Tournament:
    def __init__(self, distance, *runners):
        self.distance = distance
        self.runners = list(runners)

    def start(self):
        results = {}
        for runner in self.runners:
            while runner.distance < self.distance:
                runner.run()
            results[runner.distance] = runner.name
        return dict(sorted(results.items()))

# Тестовый класс TournamentTest
class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}  # Словарь для хранения результатов всех тестов

    def setUp(self):
        # Создаём бегунов
        self.runner_usain = Runner("Usain", speed=10)
        self.runner_andrei = Runner("Andrei", speed=9)
        self.runner_nik = Runner("Nik", speed=3)

    @classmethod
    def tearDownClass(cls):
        print("\nAll Results:")
        for test_name, result in cls.all_results.items():
            print(f"{test_name}: {result}")

    def test_usain_and_nik(self):
        # Забег Усэйна и Ника
        tournament = Tournament(90, self.runner_usain, self.runner_nik)
        results = tournament.start()
        TournamentTest.all_results["test_usain_and_nik"] = results
        self.assertTrue(
            list(results.values())[-1] == "Nik",
            "Nik should be the last runner"
        )

    def test_andrei_and_nik(self):
        # Забег Андрея и Ника
        tournament = Tournament(90, self.runner_andrei, self.runner_nik)
        results = tournament.start()
        TournamentTest.all_results["test_andrei_and_nik"] = results
        self.assertTrue(
            list(results.values())[-1] == "Nik",
            "Nik should be the last runner"
        )

    def test_usain_andrei_and_nik(self):
        # Забег Усэйна, Андрея и Ника
        tournament = Tournament(90, self.runner_usain, self.runner_andrei, self.runner_nik)
        results = tournament.start()
        TournamentTest.all_results["test_usain_andrei_and_nik"] = results
        self.assertTrue(
            list(results.values())[-1] == "Nik",
            "Nik should be the last runner"
        )

# Запуск тестов
if __name__ == "__main__":
    unittest.main()
