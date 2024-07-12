import re
from datetime import datetime, timedelta
import random
import string


def get_time_now(minutes=0):
	time_now = datetime.now() + timedelta(minutes=minutes)
	return time_now.strftime('%d/%m/%Y %H:%M')


def get_random_digit(length_string=8):
	result = ""
	for _ in range(length_string):
		result += str(random.choice(string.digits))
	return result


def random_string(length=8):
	if not isinstance(length, int):
		return "Please enter \'length\' is integer"
	s = ""
	for _ in range(length):
		s += random.choice(string.ascii_lowercase)
	return s


def convert_vietnamese_to_url(string):
	a_vietnamese = 'á|à|̀ạ|ã|ả|ấ|ầ|ậ|ẫ|ẩ|ắ|ằ|ẳ|ẵ|ặ|é|è|̀ẹ|ê|ẻ|ế|ề|ệ|ễ|ể|ế|ề|ể|ễ|ặ|í|ì|̀ị|ĩ|ỉ|ấ|ầ|ậ|ẫ|ẩ|ắ|ằ|ẳ|ẵ|ặ|ó|ò|̀ọ|õ|ỏ|ố|ồ|ộ|ỗ|ổ|ố|ồ|ổ|õ|ụ|ù|̀ụ|ũ|ủ|ấ|ầ|ậ|ẫ|ẩ|ắ|ằ|ẳ|ẵ|ặ|ý|ỳ|̀ỵ|ỹ|ỷ|ấ|ầ|ậ|ẫ|ẩ|ắ|ằ|ẳ|ẵ|ặ'
	e_vietnamese = 'a|a|a|a|a|a|a|a|a|a|a|a|a|a|a|e|e|e|e|e|e|e|e|e|e|e|e|e|e|e|i|i|i|i|i|i|i|i|i|i|i|i|i|i|i|o|o|o|o|o|o|o|o|o|o|o|o|o|o|o|u|u|u|u|u|u|u|u|u|u|u|u|u|u|u|y|y|y|y|y|y|y|y|y|y|y|y|y|y|y'
	res = re.sub(a_vietnamese, e_vietnamese, string)
	return res

