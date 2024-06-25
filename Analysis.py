import numpy as np
import matplotlib.pyplot as plt

d20 = np.ones(20, dtype=float)
r3d6 = np.zeros(20, dtype=float)
r2d10 = np.zeros(20, dtype=float)
r5d4 = np.zeros(20, dtype=float)
r4d4 = np.zeros(20, dtype=float)
d10add10 = np.zeros(20, dtype=float)
r10d2 = np.zeros(20, dtype=float)
r20d1 = np.zeros(20, dtype=float)
flat10 = np.zeros(20, dtype=float)

for r1 in range(1, 7):
    for r2 in range(1, 7):
        for r3 in range(1, 7):
            r3d6[r1 + r2 + r3 - 1] += 1

for r1 in range(1, 11):
    for r2 in range(1, 11):
        r2d10[r1 + r2 - 1] += 1

for r1 in range(1, 5):
    for r2 in range(1, 5):
        for r3 in range(1, 5):
            for r4 in range(1, 5):
                r4d4[r1 + r2 + r3 + r4 - 1] += 1
                for r5 in range(1, 5):
                    r5d4[r1 + r2 + r3 + r4 + r5 - 1] += 1

for r1 in range(1, 11):
    d10add10[r1 + 9] += 1

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
                                        r10d2[r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9 + r10 - 1] += 1

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
                                                                            r20d1[r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9 + r10 + r11 + r12 + r13 + r14 + r15 + r16 + r17 + r18 + r19] += 1

flat10[9] = 20


fig, ax = plt.subplots()

ax.plot(np.arange(1, 21, dtype=float), d20 / sum(d20), color='k', label='1d20')
ax.plot(np.arange(1, 21, dtype=float), r3d6 / sum(r3d6), color='m', label='3d6')
ax.plot(np.arange(1, 21, dtype=float), r2d10 / sum(r2d10), color='r', label='2d10')
ax.plot(np.arange(1, 21, dtype=float), r5d4 / sum(r5d4), color='g', label='5d4')
ax.plot(np.arange(1, 21, dtype=float), r4d4 / sum(r4d4), color='tab:olive', label='4d4')
ax.plot(np.arange(1, 21, dtype=float), d10add10 / sum(d10add10), color='tab:pink', label='1d10+10')
ax.plot(np.arange(1, 21, dtype=float), r10d2 / sum(r10d2), color='b', label='10d2')
ax.plot(np.arange(1, 21, dtype=float), r20d1 / sum(r20d1), color='c', label='20d1')
ax.plot(np.arange(1, 21, dtype=float), flat10 / sum(flat10), color='y', label='10')

ax.set_title("Likelyhoods")
ax.set_xlabel("Roll")
ax.set_ylabel("Likelyhood")
ax.set_ylim(0, 1)
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


d20_skill = np.zeros((6, 13), dtype=float)
r3d6_skill = np.zeros((6, 13), dtype=float)
r2d10_skill = np.zeros((6, 13), dtype=float)
r5d4_skill = np.zeros((6, 13), dtype=float)
r4d4_skill = np.zeros((6, 13), dtype=float)
d10add10_skill = np.zeros((6, 13), dtype=float)
r10d2_skill = np.zeros((6, 13), dtype=float)
r20d1_skill = np.zeros((6, 13), dtype=float)
flat10_skill = np.zeros((6, 13), dtype=float)

for mod in range(13):
    for dc in range(6):
        for roll in range(1, 21):
            if roll + mods[mod] >= dcs[dc] and roll < dcs[dc]:
                d20_skill[dc][mod] += d20[roll - 1]
                r3d6_skill[dc][mod] += r3d6[roll - 1]
                r2d10_skill[dc][mod] += r2d10[roll - 1]
                r5d4_skill[dc][mod] += r5d4[roll - 1]
                r4d4_skill[dc][mod] += r4d4[roll - 1]
                d10add10_skill[dc][mod] += d10add10[roll - 1]
                r10d2_skill[dc][mod] += r10d2[roll - 1]
                r20d1_skill[dc][mod] += r20d1[roll - 1]
                flat10_skill[dc][mod] += flat10[roll - 1]
        d20_skill[dc][mod] /= sum(sum(d20_skill)) if sum(sum(d20_skill)) != 0 else 1
        r3d6_skill[dc][mod] /= sum(r3d6_skill[dc]) if sum(r3d6_skill[dc]) != 0 else 1
        r2d10_skill[dc][mod] /= sum(r2d10_skill[dc]) if sum(r2d10_skill[dc]) != 0 else 1
        r5d4_skill[dc][mod] /= sum(r5d4_skill[dc]) if sum(r5d4_skill[dc]) != 0 else 1
        r4d4_skill[dc][mod] /= sum(r4d4_skill[dc] ) if sum(r4d4_skill[dc]) != 0 else 1
        d10add10_skill[dc][mod] /= sum(d10add10_skill[dc]) if sum(d10add10_skill)[dc] != 0 else 1
        r10d2_skill[dc][mod] /= sum(r10d2_skill[dc]) if sum(r10d2_skill[dc]) != 0 else 1
        r20d1_skill[dc][mod] /= sum(r20d1_skill[dc]) if sum(r20d1_skill[dc]) != 0 else 1
        flat10_skill[dc][mod] /= sum(flat10_skill[dc]) if sum(flat10_skill[dc]) != 0 else 1

fig2, ax2 = plt.subplots(3, 3, figsize=(10, 10))

for i in range(6):
    ax2[0][0].plot(np.array(mods), d20_skill[i], color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'][i], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'][i])
    ax2[0][1].plot(np.array(mods), r3d6_skill[i], color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'][i], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'][i])
    ax2[1][0].plot(np.array(mods), r2d10_skill[i], color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'][i], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'][i])
    ax2[2][0].plot(np.array(mods), r5d4_skill[i], color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'][i], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'][i])
    ax2[2][1].plot(np.array(mods), r4d4_skill[i], color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'][i], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'][i])
    ax2[1][1].plot(np.array(mods), d10add10_skill[i], color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'][i], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'][i])
    ax2[0][2].plot(np.array(mods), r10d2_skill[i], color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'][i], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'][i])
    ax2[2][2].plot(np.array(mods), r20d1_skill[i], color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'][i], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'][i])
    ax2[1][2].plot(np.array(mods), flat10_skill[i], color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'][i], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'][i])

ax2[0][0].set_title("1d20")
ax2[0][1].set_title("3d6")
ax2[1][0].set_title("2d10")
ax2[2][0].set_title("5d4")
ax2[2][1].set_title("4d4")
ax2[1][1].set_title("1d10 + 10")
ax2[0][2].set_title("10d2")
ax2[2][2].set_title("20d1")
ax2[1][2].set_title("10")
for i in range(3):
    for j in range(3):
        ax2[i][j].set_xlim(-1, 11)
        #ax2[i][j].set_ylim(0, 1)
        ax2[i][j].set_xticks(np.arange(-1, 12, 1, dtype=np.int64))
        #ax2[i][j].set_yticks(np.arange(0, 1.1, .1, dtype=float))
        ax2[i][j].set_xlabel('Modifier')
        ax2[i][j].set_ylabel('Effect of skill')
        ax2[i][j].legend()

fig2.tight_layout(pad=1)
fig2.savefig("Skill.pdf")
plt.show()


fig3, ax3 = plt.subplots(3, 3, figsize=(10, 10))

for i in range(6):
    ax3[0][0].plot(np.array(mods), np.ones(13, dtype=float) - d20_skill[i], color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'][i], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'][i])
    ax3[0][1].plot(np.array(mods), np.ones(13, dtype=float) - r3d6_skill[i], color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'][i], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'][i])
    ax3[1][0].plot(np.array(mods), np.ones(13, dtype=float) - r2d10_skill[i], color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'][i], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'][i])
    ax3[2][0].plot(np.array(mods), np.ones(13, dtype=float) - r5d4_skill[i], color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'][i], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'][i])
    ax3[2][1].plot(np.array(mods), np.ones(13, dtype=float) - r4d4_skill[i], color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'][i], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'][i])
    ax3[1][1].plot(np.array(mods), np.ones(13, dtype=float) - d10add10_skill[i], color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'][i], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'][i])
    ax3[0][2].plot(np.array(mods), np.ones(13, dtype=float) - r10d2_skill[i], color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'][i], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'][i])
    ax3[2][2].plot(np.array(mods), np.ones(13, dtype=float) - r20d1_skill[i], color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'][i], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'][i])
    ax3[1][2].plot(np.array(mods), np.ones(13, dtype=float) - flat10_skill[i], color=['green', 'blue', 'purple', 'yellow', 'orange', 'red'][i], label=['DC 5', 'DC 10', 'DC 15', 'DC 20', 'DC 25', 'DC 30'][i])

ax3[0][0].set_title("1d20")
ax3[0][1].set_title("3d6")
ax3[1][0].set_title("2d10")
ax3[2][0].set_title("5d4")
ax3[2][1].set_title("4d4")
ax3[1][1].set_title("1d10 + 10")
ax3[0][2].set_title("10d2")
ax3[2][2].set_title("20d1")
ax3[1][2].set_title("10")
for i in range(3):
    for j in range(3):
        ax3[i][j].set_xlim(-1, 11)
        #ax3[i][j].set_ylim(0, 1)
        ax3[i][j].set_xticks(np.arange(-1, 12, 1, dtype=np.int64))
        #ax3[i][j].set_yticks(np.arange(0, 1.1, .1, dtype=float))
        ax3[i][j].set_xlabel('Modifier')
        ax3[i][j].set_ylabel('Effect')
        ax3[i][j].legend()

fig3.tight_layout(pad=1)
fig3.savefig("Luck.pdf")
plt.show()
