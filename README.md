# Accent Letters

Toggle Russian stress marks (ударение) on selected vowels in [Sublime Text](https://www.sublimetext.com/).

## Installation

Install via **Package Control**: `Accent Letters`.

Or clone into your `Packages` directory:

```bash
git clone https://github.com/CJayM/accent_letters.git "$HOME/AppData/Roaming/Sublime Text/Packages/AccentLetters"
```

## Usage

1. Select one or more Russian vowels (`аеиоыэюяу`, case-insensitive).
2. Run `accent_letter` from the **Command Palette** or via a key binding.
3. Stress marks are toggled — run again to remove them.

### Examples

| Input | Output |
|-------|--------|
| `задача` | `зада́ча` |
| `зада́ча` | `задача` |
| `МАМА` | `МА́МА` |

### Key Binding (Optional)

Add to your user keymap (`Preferences → Key Bindings`):

```json
{ "keys": ["alt+e"], "command": "accent_letter" }
```

## License

MIT
