This small hack allows you to manage your personal terminal cheatsheet and execute commands directly from it over SSH using [Kitty Terminal](https://github.com/kovidgoyal/kitty).

### Prerequisites

- [Kitty](https://github.com/kovidgoyal/kitty)
- [navi](https://github.com/denisidoro/navi)

### Installation

1. Put [cheatsheet-kitten.py](./cheatsheet-kitten.py) into your kitty's config directory.
2. Assign a new shortcut for the kitten in kitty's config. An example: `map cmd+h kitten cheatsheet-kitten.py` ([More on kitty's mappings](https://sw.kovidgoyal.net/kitty/mapping/))
3. Run `sed -i '' "s|YOUR_PATH|$PATH|" cheatsheet-kitten.py` add your `$PATH` to the script so that kitty can invoke `navi`
   - The step above is necessary on Mac. On Linux, you can remove the `env` varible from the script
