#!/usr/bin/python3
# SPDX-FileCopyrightText: 2026 Kanki Kuruma


import sys
import math

data = list(map(float, input().split()))

many = len(data)

mean = sum(data) / len(data)

sorted_data = sorted(data)
n = len(sorted_data)

if n % 2 == 1:
    median = sorted_data[n // 2]
else:
    median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

variance = sum((x - mean) ** 2 for x in data) / len(data)
std_dev = math.sqrt(variance)

print(many)
print(f"{mean:.2f}")
print(f"{median:.2f}")
print(f"{std_dev:.2f}")
