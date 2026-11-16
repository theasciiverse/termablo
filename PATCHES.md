# Changes from upstream

This is the Asciiverse packaging of
[Termablo](https://github.com/antonmedv/termablo) by Anton Medvedev, a
Diablo-like for the terminal in Go on Bubble Tea. Upstream is the
`upstream` remote; this build is upstream's `master` at `07dcbcc`
(2026-10-10, "the Cinder Sanctum"). Upstream has no version numbers or
tags, so our tags carry that commit's date: `v20261010-av.1`.

## The game

Unchanged: no line of upstream's Go code, text or data is touched. We
ship the main package, the game itself, which plays in the terminal it
is started in. Its SSH server mode (`-ssh`, for hosting the game for
others) stays in the binary as upstream has it, but av never starts it.

## Saves, settings and logs

None to move. Termablo writes no files: a run lasts one session, and
the language comes from `LANG` or `-lang`. It makes no network
connections unless started with `-ssh`.

## Packaging

- `.github/workflows/asciiverse-release.yml` (new): av archives for Linux
  (static, x86-64 and ARM64), macOS (Intel and Apple silicon) and Windows
  (x86-64 and ARM64), plus SHA256SUMS, cross-built with cgo off on one
  runner. Each archive holds the `termablo` binary, `LICENSE`,
  `UPDATES.md`, this file and our `README.md`.
- `asciiverse/README.md` (new): the package README, shipped in the
  archives as `README.md` (upstream's README is about hosting the SSH
  server and the balancing tools).
- `asciiverse/record-preview.sh`, `asciiverse/drive.py` (new): the
  catalog preview.
- `asciiverse/termablo.toml`, `asciiverse/termablo.md`,
  `asciiverse/termablo.cast` (new): the catalog manifest, store page and
  preview, as drafts for hub.
- `CLAUDE.md` (our notes added below upstream's one line), `PATCHES.md`
  (new): notes.
