class logEntry(object):
	def __init__(self, line):
		self.line = line
		self.info = line.split(' ', 5)

	def printLine(self):
		print(self.line)
		for entry in self.info:
			print(entry)
		print()

s = 'Mar 26 15:17:01 root CRON[12321]: (root) CMD (    cd / && run-parts --report /etc/cron.hourly) '

log = logEntry(s)
log.printLine()

s = 'Mar 26 15:17:01 root systemd[1]: Started Network manager Script dispatcher service '
nextLog = logEntry(s)
nextLog.printLine()
