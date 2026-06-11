import sublime
import sublime_plugin


CHANGED_LETTERS = "аеиоыэюяу"
ACCENTED_LETTERS = "а́е́и́о́ы́э́ю́я́у́"

class AccentLetterCommand(sublime_plugin.TextCommand):
	def run(self, edit):


				
		for region in self.view.sel():
			if not region.empty():
				s = self.view.substr(region)
				res = []
				for letter in s:
					lowered = s.lower()
					pos = CHANGED_LETTERS.index(s.lower())
					if pos >=0:
						res.extend(ACCENTED_LETTERS[pos*2:pos*2+2])
					else:
						res.append(lowered)
				


				self.view.replace(edit, region, "".join(res))
