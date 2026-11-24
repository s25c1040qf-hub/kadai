# statcalc

標準入力から与えられた数値列について、個数、平均値、中央値、標準偏差を計算するコマンドです。

## 動作環境

- Python 3.12

## インストール

```bash
$ git clone https://github.com/s25c1040qf-hub/kadai.git
$cd kadai
$chmod +x kadai.py
$chmod +x test.bash
```

## 使い方

数値を空白区切りで入力します。

```bash
$ echo "1 2 3 4 5" | python3 kadai.py
5
3.00
3.00
1.41
```

出力内容

1. 個数
2. 平均値
3. 中央値
4. 標準偏差

別の例

```bash
$ echo "10 20 30" | python3 kadai.py
3
20.00
20.00
8.16
```

## テスト

```bash
$ bash test.bash
OK
```

## ライセンス

- SPDX-License-Identifier: BSD-3-Clause

## 著作権

Copyright (c) 2026 来馬寛生
