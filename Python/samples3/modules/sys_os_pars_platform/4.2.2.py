#!/usr/bin/env python3
"""
Завершение работы программы
"""


def bye():
    import os
    print("Bye os world")
    os._exit(99)
    print("Never reached")


if __name__ == "__main__":
    bye()
