@AGENTS.md

# Termablo (Asciiverse packaging)

Anton Medvedev's Termablo (Go, Bubble Tea, MIT), packaged for the
Asciiverse catalog (id `termablo`, kind `game`, genre `roguelike`). Not
our code: the game stays as its author made it; list every change in
PATCHES.md.

- `upstream` is github.com/antonmedv/termablo (branch `master`); ours is
  branch `asciiverse`, `origin` github.com/theasciiverse/termablo
  (private).
- Build: `CGO_ENABLED=0 go build -trimpath .` (the game is the main
  package; `cmd/` holds upstream's dev tools, not shipped). Go from
  go.mod, 1.27+.
- Release: upstream has no versions or tags, so tags are
  `v<date of the upstream commit>-av.<n>` (first `v20261010-av.1`); push
  it and `.github/workflows/asciiverse-release.yml` cross-builds Linux,
  macOS and Windows on one runner.
- av runs the plain terminal game, never `-ssh`. The game writes no
  files at all (no saves, settings or logs: a run lasts one session);
  the language comes from `LANG` or `-lang`.
- Tests, scripted runs and recordings: scratch `HOME` and
  `XDG_STATE_HOME` in the same command, under
  `systemd-run --user --scope -p MemoryMax=4G` with `GOMAXPROCS=4`.
- Needs 80x24 and true colour (it writes 24-bit colour escapes itself).
- Preview: `asciiverse/record-preview.sh ./termablo`.
- Catalog drafts: `asciiverse/termablo.toml` and `.md`; package README
  `asciiverse/README.md` (shipped as README.md in the archives).
