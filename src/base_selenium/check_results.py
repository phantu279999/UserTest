class ProcessResultAction:
	def __init__(self, driver, self_base):
		self.driver = driver
		self.base = self_base

	def process_result(self, obj):
		res = {}
		if 'result' not in obj:
			return {
				"status": True,
				"msg": "Passed"
			}

		self.base.accept_alert()
		if 'type' not in obj['result']:
			res['status'] = False
			res['msg'] = "Not found \'type\' in result"
		elif obj['result']['type'] == 'title':
			status, msg = self.process_result_title(obj)
			res['status'] = status
			res['msg'] = msg
		elif obj['result']['type'] == 'xpath':
			status, msg = self.process_result_xpath(obj)
			res['status'] = status
			res['msg'] = msg
		elif obj['result']['type'] == 'display':
			status, msg = self.process_result_display(obj)
			res['status'] = status
			res['msg'] = msg
		elif obj['result']['type'] == 'xpath_text':
			status, msg = self.process_result_xpath_text(obj)
			res['status'] = status
			res['msg'] = msg
		else:
			res['status'] = False
			res['msg'] = "Not found \'type\' in result"
		return res

	def process_result_title(self, obj):
		if 'value' not in obj['result']:
			status = False
			msg = '(title)Not found \'value\'Check result need two fields: type, value'
		else:
			current_title = self.base.get_title()
			desired_title = obj['result']['value']
			if current_title.strip() == desired_title.strip():
				status = True
				msg = "(title)Passed"
			else:
				status = False
				msg = '(title)You provide title is not equal with current page title'

		return status, msg

	def process_result_xpath(self, obj):
		if 'xpath' not in obj['result']:
			status = False
			msg = '(xpath)Not found \'xpath\'Check result need two fields: type, xpath'
		else:
			element = self.base.get_element(obj['result']['xpath'])
			if element:
				status = True
				msg = "(xpath)Passed"
			else:
				status = False
				msg = '(xpath)You provide xpath not found in current page. Please check again'

		return status, msg

	def process_result_display(self, obj):
		if 'xpath' not in obj['result']:
			status = False
			msg = '(display)Not found \'xpath\'Check result need two fields: type, xpath'
		else:
			element = self.base.get_element(obj['result']['xpath'])
			if element:
				if self.base.is_element_display(element):
					status = True
					msg = "(display)Passed"
				else:
					status = False
					msg = '(display)You provide xpath not display in current page. Please check again'
			else:
				status = False
				msg = '(display)You provide xpath not found in current page. Please check again'

		return status, msg

	def process_result_xpath_text(self, obj):
		if ('xpath' not in obj['result']) or ('value' not in obj['result']):
			status = False
			msg = '(xpath_text)Not found \'xpath\' or \'value\' Check result need two fields: type, xpath, value'
		else:
			element = self.base.get_element(obj['result']['xpath'])
			if element:
				xpath_text = self.base.get_element_text(element)
				disired_text = obj['result']['value']
				# print(xpath_text)
				# print(disired_text)
				if xpath_text.strip() == disired_text.strip():
					status = True
					msg = "(xpath_text)Passed"
				else:
					status = False
					msg = '(xpath_text)You provide text is not equal with xpath text'
			else:
				status = False
				msg = '(xpath_text)You provide xpath not found in current page. Please check again'
		return status, msg

	def process_result_url(self, obj):
		if 'value' not in obj['result']:
			status = False
			msg = '(display)Not found \'xpath\'Check result need two fields: type, value'
		else:
			current_url = self.base.get_current_url()
			disired_url = obj['result']['value']
			if current_url.strip() == disired_url.strip():
				status = True
				msg = "(url)Passed"
			else:
				status = False
				msg = '(url)You provide url is not equal with current url'

		return status, msg

