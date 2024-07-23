class CheckElementDriver:
	@staticmethod
	def is_element_visible(element):
		try:
			if element.is_displayed():
				return True
		except Exception as ex:
			print(ex)
		return False

	@staticmethod
	def is_element_clickable(element):
		try:
			if element.is_displayed() and element.is_enaled():
				return True
		except Exception as ex:
			print(ex)
		return False

	@staticmethod
	def is_element_selected(element):
		try:
			if element.is_selected():
				return True
		except Exception as ex:
			print(ex)
		return False
