if __name__ == "__main__":
    #  Классы для автомобилей
    class Cars:
        """
        Базовый класс для автомобилей.
        """

        def __init__(self, brand: str, shape: str):
            self.brand = brand
            self.shape = shape

        def __str__(self) -> str:
            return f"Автомобиль: {self.brand}, форма: {self.shape}"

        def __repr__(self) -> str:
            return f"Cars(brand={self.brand!r}, shape={self.shape!r})"


    class PassengerCars(Cars):
        """
        Дочерний класс для легковых автомобилей.
        """

        def __init__(self, brand: str, shape: str, pupils: int):
            """
            Расширяем конструктор, добавляя количество пассажиров.
            """
            super().__init__(brand, shape)
            self.pupils = pupils

        def __str__(self) -> str:
            return f"Легковой автомобиль {self.brand}, {self.shape}, пассажиров: {self.pupils}"

        def __repr__(self) -> str:
            return f"PassengerCars(brand={self.brand!r}, shape={self.shape!r}, pupils={self.pupils!r})"


    class Trucks(Cars):
        """
        Дочерний класс для грузовых автомобилей.
        """

        def __init__(self, brand: str, shape: str, capacity: float):
            """
            Добавляем атрибут грузоподъемности.
            """
            super().__init__(brand, shape)
            self.capacity = capacity  # Грузоподъемность

        def __str__(self) -> str:
            return f"Грузовик {self.brand}, {self.shape}, грузоподъемность: {self.capacity} тонн"

        def __repr__(self) -> str:
            return f"Trucks(brand={self.brand!r}, shape={self.shape!r}, capacity={self.capacity!r})"


    # Классы для деревьев

    class ConiferousTrees:
        """
        Базовый класс для хвойных деревьев.
        """

        def __init__(self, species: str, height: float, age: int):
            if height <= 0:
                raise ValueError("Высота должна быть положительным числом.")
            if age < 0:
                raise ValueError("Возраст не может быть отрицательным.")
            self.species = species
            self.height = height
            self.age = age

        def __str__(self) -> str:
            return f"{self.species} - высота: {self.height} м, возраст: {self.age} лет"

        def __repr__(self) -> str:
            return f"ConiferousTrees(species={self.species!r}, height={self.height!r}, age={self.age!r})"


    class Spruce(ConiferousTrees):
        """
        Класс для ели.
        """

        def __init__(self, height: float, age: int):
            super().__init__("Ель", height, age)

        def __str__(self) -> str:
            return f"Ель - высота: {self.height} м, возраст: {self.age} лет"

        def produce_cones(self) -> str:
            """
            Уникальное поведение для ели.
            """
            return "Ель производит шишки."


    class Pine(ConiferousTrees):
        """
        Класс для сосны.
        """

        def __init__(self, height: float, age: int):
            super().__init__("Сосна", height, age)

        def __str__(self) -> str:
            return f"Сосна - высота: {self.height} м, возраст: {self.age} лет"


    # Классы для соцсетей

    class SocialMediaPlatforms:
        """
        Базовый класс для социальных сетей.
        """

        def __init__(self, name: str, user_count: int, founding_year: int):
            if user_count < 0:
                raise ValueError("Количество пользователей не может быть отрицательным.")
            if founding_year > 2025:
                raise ValueError("Год основания не может превышать текущий.")
            self.name = name
            self.user_count = user_count
            self.founding_year = founding_year

        def __str__(self) -> str:
            return f"Платформа: {self.name}, пользователей: {self.user_count}, год основания: {self.founding_year}"

        def __repr__(self) -> str:
            return (f"SocialMediaPlatforms(name={self.name!r}, "
                    f"user_count={self.user_count!r}, founding_year={self.founding_year!r})")

        def add_user(self, user_id: str) -> None:
            """
            Добавить нового пользователя на платформу.
            """
            print(f"Добавлен пользователь с ID {user_id} на {self.name}.")

        def remove_user(self, user_id: str) -> None:
            """
            Удалить пользователя с платформы.
            """
            print(f"Пользователь с ID {user_id} удалён с {self.name}.")


    class VK(SocialMediaPlatforms):
        """
        Дочерний класс для ВКонтакте.
        """

        def __init__(self, user_count: int, founding_year: int):
            super().__init__("ВКонтакте", user_count, founding_year)

        def add_user(self, user_id: str) -> None:
            """
            Перегрузка метода: специфическое поведение для VK.
            """
            print(f"Пользователь {user_id} зарегистрирован на VK.")

        def __str__(self) -> str:
            return f"VK: пользователей {self.user_count}, основана в {self.founding_year} году."


    class Facebook(SocialMediaPlatforms):
        """
        Дочерний класс для Facebook.
        """

        def __init__(self, user_count: int, founding_year: int):
            super().__init__("Facebook", user_count, founding_year)

        def remove_user(self, user_id: str) -> None:
            """
            Перегрузка метода: специфическое поведение для Facebook.
            """
            print(f"Аккаунт {user_id} удалён из Facebook.")

        def __str__(self) -> str:
            return f"Facebook: пользователей {self.user_count}, основана в {self.founding_year} году."




