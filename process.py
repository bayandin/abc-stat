#!/usr/bin/env python3
#
# Based on http://www.prooffreader.com/2014/05/graphing-distribution-of-english.html
#

import colorsys
import matplotlib.pyplot as plt

ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
BUCKETS_COUNT = 720
FILENAME = 'data/ru.txt'


def color(current, minimum, maximum):
    s = (current - minimum) / (maximum - minimum)
    r, g, b = colorsys.hsv_to_rgb(1.0, s, 1.0)
    return '#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255))


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

    l = [sum(i) for i in stat.values()]
    min_ = min(l)
    max_ = max(l)

    for c in ALPHABET:
        fig = plt.figure(figsize=(10, 10))
        plt.xticks([])
        plt.yticks([])
        plt.fill_between(
            range(BUCKETS_COUNT),
            stat[c],
            facecolor=color(sum(stat[c]), min_, max_)
        )
        fig.savefig('result/%s.png' % c)
        plt.close(fig)
