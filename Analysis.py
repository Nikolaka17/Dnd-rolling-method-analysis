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
flat10 = np.zeros(20, dtype=np.int64)

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

ax.set_title("Likelyhoods")
ax.set_xlabel("Roll")
ax.set_ylabel("Likelyhood")
ax.set_xlim(1, 20)
ax.set_xticks(np.arange(1, 21, dtype=np.int64))
ax.legend()

fig.savefig("Likelyhood.pdf")
plt.show()


"""
      DC 5  DC 10  DC 15  DC 20  DC 25  DC 30
Lvl 1
Lvl 4
Lvl 5
Lvl 8
Lvl 9
Lvl 13
Lvl 17
"""
mods = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
dcs = [5, 10, 15, 20, 25, 30]


d20_skill = np.zeros((6, 13), dtype=np.float)
r3d6_skill = np.zeros((6, 13), dtype=np.float)
r2d10_skill = np.zeros((6, 13), dtype=np.float)
r5d4_skill = np.zeros((6, 13), dtype=np.float)
r4d4_skill = np.zeros((6, 13), dtype=np.float)
d10add10_skill = np.zeros((6, 13), dtype=np.float)
r10d2_skill = np.zeros((6, 13), dtype=np.float)
r20d1_skill = np.zeros((6, 13), dtype=np.float)
flat10_skill = np.zeros((6, 13), dtype=np.float)

for mod in range(13):
    for dc in range(6):
        for roll in range(20):
            if roll + mod >= dc and roll < dc:
                d20_skill[dc][mod] += d20[roll]
                r3d6_skill[dc][mod] += r3d6[roll]
                r2d10_skill[dc][mod] += r2d10[roll]
                r5d4_skill[dc][mod] += r5d4[roll]
                r4d4_skill[dc][mod] += r4d4[roll]
                d10add10_skill[dc][mod] += d10add10[roll]
                r10d2_skill[dc][mod] += r10d2[roll]
                r20d1_skill[dc][mod] += r20d1[roll]
                flat10_skill[dc][mod] += flat10[roll]
        d20_skill[dc][mod] /= sum(d20)
        r3d6_skill[dc][mod] /= sum(r3d6)
        r2d10_skill[dc][mod] /= sum(r2d10)
        r5d4_skill[dc][mod] /= sum(r5d4)
        r4d4_skill[dc][mod] /= sum(r4d4)
        d10add10_skill[dc][mod] /= sum(d10add10)
        r10d2_skill[dc][mod] /= sum(r10d2)
        r20d1_skill[dc][mod] /= sum(r20d1)
        flat10_skill[dc][mod] /= sum(flat10)

fig2, ax2 = plt.subplot(3, 3)

ax2[0, 0].plot(np.array(mods), d20_skill, color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'])
ax2[0, 1].plot(np.array(mods), r3d6_skill, color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'])
ax2[1, 0].plot(np.array(mods), r2d10_skill, color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'])
ax2[2, 0].plot(np.array(mods), r5d4_skill, color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'])
ax2[2, 1].plot(np.array(mods), r4d4_skill, color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'])
ax2[1, 1].plot(np.array(mods), d10add10, color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'])
ax2[0, 2].plot(np.array(mods), r10d2_skill, color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'])
ax2[2, 2].plot(np.array(mods), r20d1_skill, color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'])
ax2[1, 2].plot(np.array(mods), flat10_skill, color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'])

ax2.set_title('Effect of skills')
ax2[0, 0].set_title("1d20")
ax2[0, 1].set_title("3d6")
ax2[1, 0].set_title("2d10")
ax2[2, 0].set_title("5d4")
ax2[2, 1].set_title("4d4")
ax2[1, 1].set_title("1d10 + 10")
ax2[0, 2].set_title("10d2")
ax2[2, 2].set_title("20d1")
ax2[1, 2].set_title("10")
for i in range(3):
    for j in range(3):
        ax2[i, j].set_xlim(-1, 11)
        ax2[i, j].set_ylim(0, 1)
        ax2[i, j].set_xticks(np.arange(-1, 12, 1, dtype=np.int64))
        ax2[i, j].set_yticks(np.arange(0, 1.1, .1, dtype=np.float))
        ax2[i, j].set_xlabel('Modifier')
        ax2[i, j].set_ylabel('Effect')
        ax2[i, j].legend()

fig2.savefig("Skill.pdf")
plt.show()
