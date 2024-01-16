
import requests
import statistics as stats
import csv
import math
import os
from random import uniform

import csv
import requests

url = "https://www.texaslottery.com/export/sites/lottery/Games/Lotto_Texas/Winning_Numbers/lottotexas.csv"
response = requests.get(url, timeout=10)

lines = list(line.decode('utf-8') for line in response.iter_lines())

reader = csv.reader(lines, delimiter=',')
data = list(reader)

n1s = []
n2s = []
n3s = []
n4s = []
n5s = []
n6s = []

for x in range(0,125):
    n1s.append(int(data[-125:][x][4]))
    n2s.append(int(data[-125:][x][5]))
    n3s.append(int(data[-125:][x][6]))
    n4s.append(int(data[-125:][x][7]))
    n5s.append(int(data[-125:][x][8]))
    n6s.append(int(data[-125:][x][9]))


def mean(arr):
    s = sum(arr)
    return s/len(arr)

n1 = math.floor(mean(n1s))
n2 = math.ceil(mean(n2s) * uniform(.5,2.25)) + 1
n3 = math.ceil(mean(n3s))
n4 = math.ceil(mean(n4s))
n5 = math.floor(mean(n5s) * uniform(.22,2)) + 1
n6 = math.floor(mean(n6s) * uniform(.22,2))

luckyStr = str(n1) + ", " + str(n2) + ", " + str(n3) + ", " + str(n4) + ", " + str(n5) + ", " + str(n6)

print("Lucky numbers: " + luckyStr)
