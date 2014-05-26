import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# print edit
		# print self.view.size()
		# print  self.view.settings()
		# print   self.view.sel()[0]

		fileRegion = sublime.Region(0, self.view.size())
		settings = self.view.settings()
		selection = self.view.sel()[0]

		pos = self.view.sel()[0].a
		preTxt = self.view.substr(sublime.Region(0, pos));

		preTxt = preTxt.replace(' ',"")
		preTxt = preTxt.replace('\t',"")
		preTxt = preTxt.replace('\r\n',"")
		# for linux
		preTxt = preTxt.replace('\n',"")
		preTxt = preTxt.replace('"',"\\\"")

		self.view.erase(edit, sublime.Region(0, pos))
		self.view.insert(edit, 0, preTxt)
