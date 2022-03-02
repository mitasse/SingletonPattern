"""Singleton concrete class"""
from __future__ import annotations


class Singleton:
    """Singleton concrete class"""

    _unique_instance = None

    def __new__(cls) -> Singleton:
        if not cls._unique_instance:
            cls._unique_instance = super().__new__(cls)

        return cls._unique_instance


def main() -> None:
    """Main function"""
    singleton_1 = Singleton()
    singleton_2 = Singleton()
    print(singleton_1 is singleton_2)


if __name__ == "__main__":
    main()
