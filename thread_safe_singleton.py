"""Thread-safe Singleton concrete class"""
from __future__ import annotations

import threading


class ThreadSafeSingleton:
    """Singleton concrete class"""

    _unique_instance = None
    _lock = threading.Lock()

    def __new__(cls) -> ThreadSafeSingleton:
        """Double-checked locking"""
        if not cls._unique_instance:
            with cls._lock:
                if not cls._unique_instance:
                    cls._unique_instance = super().__new__(cls)

        return cls._unique_instance


def main() -> None:
    """Main function"""
    singleton_1 = ThreadSafeSingleton()
    singleton_2 = ThreadSafeSingleton()
    print(singleton_1 is singleton_2)


if __name__ == "__main__":
    main()
