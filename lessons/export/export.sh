rm -rf a.build
rm -rf a.dist
rm a.bin

python -m nuitka a.py --show-progress \
  --standalone --onefile --follow-imports \
  --windows-disable-console