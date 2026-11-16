# Termablo

**Keep your torch high. The dark down there isn't empty. It's hungry.**

A king once cut a single coal out of the burning rock far below and
carried it up in his bare hands. The town he built around it is
Emberhold, the last lit town before the dark: every lantern lit from
Hadrik's forge, the forge from the Ember, and the dark stops at the gate.
So everything below climbs toward it instead. You are the stranger
Captain Voss hires to go down and meet it.

Termablo is Anton Medvedev's Diablo-like for the terminal, and its light
is real. Every torch, street lamp, campfire, brazier, glowing crystal,
lava pool and spell throws coloured, flickering light, and you see only
what the light reaches. A monster standing in the dark is not there at
all until light touches it.

Down through the Ashen Fields to the Bone King's throne of ribs, out to
the barrow where the Buried Captain still stands watch, into the Sunken
Grotto under Blackmarsh where the Drowned Oracle sings, under Emberhold's
own graveyard for Hadrik's stolen coal and the Cinder Prior, and at last
to the bottom of the Burning Abyss, where the Last Wanderer puts out
every light near him, your torch included. In between, Emberhold to come
home to: talk to anyone by walking into them, ask about every
highlighted word, buy, sell and gamble at Hadrik's forge, and let Mirela
patch you up.

## Playing

Run `termablo` in a terminal of at least 80x24 with true colour; a
bigger terminal shows more of the map.

- **Arrow keys**, **h j k l y u b n** or the numpad: move, and attack by
  walking into a monster
- **f**: Firebolt; **r**: Frost Nova; **Tab** / **Shift+Tab**: target
- **q** / **w**: healing / mana potion; **t**: Scroll of Town Portal
- **g**: pick up; **o**: explore; **.** or **5**: wait
- **i** inventory, **c** character, **m** map, **J** quests, **?** help,
  **Q** quit

Options: `-seed 42` for the same world every time (share it, race a
friend), `-lang de` for another language (en, de, fr, it, ru, ar, zh;
otherwise it follows `LANG`), `-bot fighter` or `-bot caster` to watch a
scripted hero play.

Termablo writes no files: each run lasts one session.

## Credits

- Termablo: Anton Medvedev, https://github.com/antonmedv/termablo
  (MIT, see LICENSE)
- Built with Bubble Tea by Charm
- This package: Asciiverse, for the av launcher and the catalog at
  https://asciiverse.sh. What we changed is in PATCHES.md, and what
  changed in the game is in UPDATES.md.

## Building

`CGO_ENABLED=0 go build -trimpath .` with Go 1.27 or newer builds the
game as one static binary; the release workflow
(`.github/workflows/asciiverse-release.yml`) cross-builds it for Linux,
macOS and Windows. The upstream README in the repository covers hosting
the game over SSH and the self-play balancing tools.
