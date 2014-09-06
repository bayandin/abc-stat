#!/usr/bin/env python3
#
# Based on http://www.prooffreader.com/2014/05/graphing-distribution-of-english.html
#

import matplotlib.pyplot as plt

ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
BUCKETS_COUNT = 720
FILENAME = 'data/ru.txt'

if __name__ == '__main__':
    stat = {c: [0] * BUCKETS_COUNT for c in ALPHABET}

    with open(FILENAME, 'r') as f:
        for line in f:
            lowered_stripped_line = line.strip().lower()

            for i, c in enumerate(lowered_stripped_line):
                if c not in ALPHABET:
                    continue

                part = BUCKETS_COUNT // len(lowered_stripped_line)
                for j in range(i * part, (i + 1) * part):
                    stat[c][j] += 1

    x_min = 0
    x_max = BUCKETS_COUNT
    y_min = 0
    y_max = max(max(i) for i in stat.values())

    for c in ALPHABET:
        fig = plt.figure(figsize=(10, 10))
        plt.axis([x_min, x_max, y_min, y_max])
        plt.fill_between(
            range(BUCKETS_COUNT),
            stat[c]
        )
        fig.savefig('result/%s.png' % c)
        plt.close(fig)
