import sublime
import sublime_plugin


COMBINING_ACUTE = "\u0301"
VOWELS = set("аеиоыэюяуАЕИОЫЭЮЯУ")


class AccentLetterCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                continue
            s = self.view.substr(region)
            result = []
            i = 0
            while i < len(s):
                ch = s[i]
                if ch in VOWELS:
                    next_ch = s[i + 1] if i + 1 < len(s) else ""
                    if next_ch == COMBINING_ACUTE:
                        result.append(ch)
                        i += 2
                    else:
                        result.append(ch + COMBINING_ACUTE)
                        i += 1
                elif ch == COMBINING_ACUTE:
                    i += 1
                else:
                    result.append(ch)
                    i += 1
            self.view.replace(edit, region, "".join(result))
