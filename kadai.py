#!/usr/bin/python3
# SPDX-FileCopyrightText: 2026 Kanki Kuruma


import sys
import math

# 数値を空白区切りで入力
data = list(map(float, input().split()))

#個数
many = len(data)

# 平均値
mean = sum(data) / len(data)

# 中央値
sorted_data = sorted(data)
n = len(sorted_data)

if n % 2 == 1:
    median = sorted_data[n // 2]
else:
    median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

# 標準偏差
variance = sum((x - mean) ** 2 for x in data) / len(data)
std_dev = math.sqrt(variance)

# 結果表示
print(f"{many:.2f}")
print(f"{mean:.2f}")
print(f"{median:.2f}")
print(f"{std_dev:.2f}")
