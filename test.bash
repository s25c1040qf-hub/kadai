#!/bin/bash

res=0

NG() {
    echo "NG at line $1"
    res=1
}

# テスト1
out=$(echo "1 2 3 4 5" | python3 kadai.py)

echo "$out" | grep -qx "5" || NG $LINENO
echo "$out" | grep -qx "3.00" || NG $LINENO
echo "$out" | grep -qx "3.00" || NG $LINENO
echo "$out" | grep -qx "1.41" || NG $LINENO

# テスト2
out=$(echo "10 20 30" | python3 kadai.py)

echo "$out" | grep -qx "3" || NG $LINENO
echo "$out" | grep -qx "20.00" || NG $LINENO

if [ $res -eq 0 ]; then
    echo OK
fi

exit $res
