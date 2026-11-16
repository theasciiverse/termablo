#!/bin/sh
# Records the 100x30 catalog preview, asciiverse/termablo.cast
# (hub/RECORDING.md): the title, then the Wanderer in the Ashen Fields,
# exploring by the light of a torch and burning down the Fallen and the
# dire wolves with Firebolts, played by asciiverse/drive.py, and quitting
# at the end. asciinema records a tmux pane (own socket, no status line,
# no user config) that drive.py reads and plays into. Needs asciinema 3
# and tmux.
#   asciiverse/record-preview.sh ./termablo [seed]
set -eu
binary=$(cd "$(dirname "$1")" && pwd)/$(basename "$1")
seed=${2:-7}
here=$(cd "$(dirname "$0")" && pwd)
out=$here/termablo.cast
home=$(mktemp -d)
trap 'tmux -L avrec kill-server 2>/dev/null; rm -rf "$home"' EXIT
mkdir "$home/bin" && cp "$binary" "$home/bin/termablo"
cd "$home"  # nothing in the recording names a local path
export HOME="$home" XDG_STATE_HOME="$home/state" \
  PATH="$home/bin:$PATH" USER=player LOGNAME=player \
  TERM=xterm-256color COLORTERM=truecolor LANG=C.UTF-8
tmux -L avrec -f /dev/null new-session -d -s rec -x 100 -y 30 \
  "termablo -seed $seed -area fields -level 3 -build caster" \; set -g status off
python3 -I "$here/drive.py" avrec rec &
drive=$!
asciinema rec --headless --overwrite -q \
  --window-size 100x30 --idle-time-limit 2 \
  --capture-env "TERM,COLORTERM,LANG" --title "Termablo" \
  --command "tmux -L avrec attach -t rec" "$out"
wait "$drive"
