import numpy as np
import matplotlib.pyplot as plt

d20 = np.ones(20, dtype=np.int64)
r3d6 = np.zeros(20, dtype=np.int64)
r2d10 = np.zeros(20, dtype=np.int64)
r5d4 = np.zeros(20, dtype=np.int64)
r4d4 = np.zeros(20, dtype=np.int64)
d10add10 = np.zeros(20, dtype=np.int64)
r10d2 = np.zeros(20, dtype=np.int64)
r20d1 = np.zeros(20, dtype=np.int64)
#c20 = np.zeros(20, dtype=np.int64)
flat10 = np.zeros(20,dtype=np.int64)

for r1 in range(1, 7):
    for r2 in range(1, 7):
        for r3 in range(1, 7):
            r3d6[r1 + r2 + r3] += 1

for r1 in range(1, 11):
    for r2 in range(1, 11):
        r2d10[r1 + r2] += 1

for r1 in range(1, 5):
    for r2 in range(1, 5):
        for r3 in range(1, 5):
            for r4 in range(1, 5):
                r4d4[r1 + r2 + r3 + r4] += 1
                for r5 in range(1, 5):
                    r5d4[r1 + r2 + r3 + r4 + r5] += 1

for r1 in range(1, 11):
    d10add10[r1 + 10] += 1

for r1 in range(1, 3):
    for r2 in range(1, 3):
        for r3 in range(1, 3):
            for r4 in range(1, 3):
                for r5 in range(1, 3):
                    for r6 in range(1, 3):
                        for r7 in range(1, 3):
                            for r8 in range(1, 3):
                                for r9 in range(1, 3):
                                    for r10 in range(1, 3):
                                        r10d2[r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9 + r10] += 1

for r1 in range(2):
    for r2 in range(2):
        for r3 in range(2):
            for r4 in range(2):
                for r5 in range(2):
                    for r6 in range(2):
                        for r7 in range(2):
                            for r8 in range(2):
                                for r9 in range(2):
                                    for r10 in range(2):
                                        for r11 in range(2):
                                            for r12 in range(2):
                                                for r13 in range(2):
                                                    for r14 in range(2):
                                                        for r15 in range(2):
                                                            for r16 in range(2):
                                                                for r17 in range(2):
                                                                    for r18 in range(2):
                                                                        for r19 in range(2):
                                                                            for r20 in range(2):
                                                                                r20d1[r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9 + r10 + r11 + r12 + r13 + r14 + r15 + r16 + r17 + r18 + r19 + r20] += 1

for i in range(10):
    flat10[i] = 10

fig, ax = plt.subplots()

ax.plot(np.arange(1, 21, dtype=np.int64), d20, color='k', label='1d20')
ax.plot(np.arange(1, 21, dtype=np.int64), r3d6, color='m', label='3d6')
ax.plot(np.arange(1, 21, dtype=np.int64), r2d10, color='r', label='2d10')
ax.plot(np.arange(1, 21, dtype=np.int64), r5d4, color='g', label='5d4')
ax.plot(np.arange(1, 21, dtype=np.int64), r4d4, color='tab:olive', label='4d4')
ax.plot(np.arange(1, 21, dtype=np.int64), d10add10, color='tab:pink', label='1d10+10')
ax.plot(np.arange(1, 21, dtype=np.int64), r10d2, color='b', label='10d2')
ax.plot(np.arange(1, 21, dtype=np.int64), r20d1, color='c', label='20d1')
ax.plot(np.arange(1, 21, dtype=np.int64), flat10, color='y', label='10')

ax.set_title("Rolling methods")
ax.set_xlabel("Roll")
ax.set_ylabel("Likelyhood")
ax.set_xlim(1, 20)
ax.set_xticks(np.arange(1, 21, dtype=np.int64))
ax.legend()

fig.savefig("Likelyhood.pdf")
plt.show()
