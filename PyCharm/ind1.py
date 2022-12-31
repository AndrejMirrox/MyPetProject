#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import module


if __name__ == "__main__":
    list = list(map(int, input("Введите список: ").split()))
    com = input("Введите параметр функции: ")
    print(f"Тест: {module.del1(com)(list)}")
