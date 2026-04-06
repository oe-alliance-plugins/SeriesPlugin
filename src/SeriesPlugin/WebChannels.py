# -*- coding: utf-8 -*-

# Internal
from .Logger import log
from .TimeoutServerProxy import TimeoutServerProxy


class WebChannels:
	def __init__(self):

		self.server = TimeoutServerProxy()

	def getWebChannels(self):

		log.debug("SerienServer getWebChannels()")

		result = self.server.getWebChannels()
		log.debug("SerienServer getWebChannels result:", result)

		return result
