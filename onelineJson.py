import sublime, sublime_plugin

class OneLineJsonCommand(sublime_plugin.TextCommand):
# class ClearrCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		def get_line_indentation_pos(view, point):
			line_region = view.line(point)
			pos = line_region.a
			end = line_region.b
			while pos < end:
				ch = view.substr(pos)
				if ch != ' ' and ch != '\t':
					break
				pos += 1
			return pos
		# print edit
		# print self.view.size()
		# print  self.view.settings()
		# print   self.view.sel()[0]

		settings = self.view.settings()

		# selection = self.view.sel()[0]
		sel = self.view.sel()[0]
		# pos = self.view.sel()[0].a
		# print self.view.sel()[0]
		# preTxt = self.view.substr(sublime.Region(0, pos));

		# used for format selected region
		# start = get_line_indentation_pos(self.view, min(sel.a, sel.b))
		# region = sublime.Region(
		# 	self.view.line(start).a,  # line start of first line
		# 	self.view.line(max(sel.a, sel.b)).b)  # line end of last line

		# format whole text
		wholeRegion = sublime.Region(0, self.view.size())
		preTxt = self.view.substr(wholeRegion);

		preTxt = preTxt.replace(' ',"")
		preTxt = preTxt.replace('\t',"")
		preTxt = preTxt.replace('\r\n',"")
		# for linux
		preTxt = preTxt.replace('\n',"")
		preTxt = preTxt.replace('"',"\\\"")

		# self.view.erase(edit, sublime.Region(0, pos))
		self.view.erase(edit, wholeRegion)
		self.view.insert(edit, 0, "\"" + preTxt + "\"")

