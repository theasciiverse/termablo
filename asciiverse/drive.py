"""Plays Termablo for the catalog preview (asciiverse/record-preview.sh).

Reads the tmux pane and presses keys at a watchable pace: past the
title, then auto-explore (o) across the Ashen Fields. When a monster
comes into the light, the Wanderer throws Firebolts at it (f),
steps toward it when it is still out of range, and drinks a potion (q, w) when life or mana runs
low. Quits (Q) after about LENGTH seconds.
    python3 -I drive.py <tmux socket> <session> [debug]
"""
import re
import subprocess
import sys
import time

SOCK, SESS = sys.argv[1], sys.argv[2]
DEBUG = len(sys.argv) > 3
LENGTH = 36.0
T0 = time.time()


def tmux(*args):
    return subprocess.run(["tmux", "-L", SOCK, *args], capture_output=True,
                          text=True).stdout


def screen():
    return tmux("capture-pane", "-p", "-t", SESS).split("\n")


def key(k, wait=0.35):
    if DEBUG:
        print(round(time.time() - T0, 1), k, file=sys.stderr)
    tmux("send-keys", "-t", SESS, k)
    time.sleep(wait)


def bar(rows, name):
    """(now, max) from the panel's "Life  45/60" or "Mana  20/39"."""
    for r in rows:
        m = re.search(name + r"\s+(\d+)/(\d+)", r)
        if m:
            return int(m.group(1)), int(m.group(2))
    return 1, 1


PANEL_W = 32
DIRS = {(-1, 0): "h", (1, 0): "l", (0, -1): "k", (0, 1): "j",
        (-1, -1): "y", (1, -1): "u", (-1, 1): "b", (1, 1): "n"}


def map_rows(rows):
    out = []
    for r in rows:
        if r.startswith("\u2500\u2500\u2500\u2500"):
            break
        out.append(r[:100 - PANEL_W])
    return out


def toward(rows, tries=0):
    """The step from the hero toward the nearest monster (a letter); a
    later try goes round the side, when the straight step was blocked."""
    m = map_rows(rows)
    hero, foes = None, []
    for y, r in enumerate(m):
        for x, c in enumerate(r):
            if c == "@":
                hero = (x, y)
            elif c.isascii() and c.isalpha() and c not in "oO":
                foes.append((x, y))
    if not hero or not foes:
        return None
    fx, fy = min(foes, key=lambda f: max(abs(f[0] - hero[0]), abs(f[1] - hero[1])))
    dx = (fx > hero[0]) - (fx < hero[0])
    dy = (fy > hero[1]) - (fy < hero[1])
    steps = [(dx, dy), (dx, 0), (0, dy), (dx or 1, dy), (dx, dy or 1)]
    steps = [d for d in steps if d != (0, 0)]
    return DIRS.get(steps[tries % len(steps)], ".")


def hero_at(rows):
    for y, r in enumerate(map_rows(rows)):
        if "@" in r:
            return r.index("@"), y
    return None


def log(rows):
    """The message log under the map's bottom rule."""
    for i, r in enumerate(rows):
        if r.startswith("────"):
            return "\n".join(r[:100 - PANEL_W] for r in rows[i + 1:])
    return ""


time.sleep(1.2)
key("Enter", 2.0)          # the title, then Emberhold or the area
exploring = False
blocked = 0
still = None
while time.time() - T0 < LENGTH:
    rows = screen()
    text = "\n".join(rows)
    if "YOU HAVE DIED" in text:
        time.sleep(2.0)
        break
    hp, hpmax = bar(rows, "Life")
    mp, mpmax = bar(rows, "Mana")
    if toward(rows) is None:
        here = hero_at(rows)
        if not exploring or here == still:   # auto-explore stopped: again
            if "(g to pick up)" in log(rows).split("\n")[-2:][-1]:
                key("g", 0.5)
            key("o", 0.8)
            exploring = True
        else:
            time.sleep(0.8)
        still = here
        if "Nothing left to explore" in log(rows):
            break
        continue
    if exploring:          # auto-explore stops by itself when enemies appear
        exploring = False
        time.sleep(0.3)
    if hp * 3 < hpmax:
        key("q")
    elif mp < 8 and mpmax > 0:
        key("w")
    else:
        last = [l for l in log(rows).split("\n") if l.strip()][-1:]
        if last and ("out of range" in last[0] or "No target" in last[0]):
            step = toward(rows, blocked)
            key(step)
            if hero_at(screen()) == hero_at(rows):
                blocked += 1
            else:
                blocked = 0
        else:
            key("f")
time.sleep(1.0)
key("Q", 1.0)
