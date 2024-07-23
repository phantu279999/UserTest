import re


def build_url_news(title):
	mapping_chars = {
		"àáảãạâầấẩẫậăằắẳẵặ": "a",
		"èéẻẽẹêềếểễệ": "e",
		"đ": "d",
		"ìíỉĩị": "i",
		"òóỏõọôồốổỗộơờớởỡợ": "o",
		"ùúủũụưừứửữự": "u",
		"ỳýỷỹỵ": "y"
	}
	title = title.lower()

	for viet_chars, ascii_char in mapping_chars.items():
		title = re.sub(r"[{}]+".format(viet_chars), ascii_char, title)
	title = re.sub(r"[^\w\d]+", "-", title)

	return title


def convert_vietnamese_to_asscii(text):
	mapping_chars = {
		"àáảãạâầấẩẫậăằắẳẵặ": "a",
		"èéẻẽẹêềếểễệ": "e",
		"đ": "d",
		"ìíỉĩị": "i",
		"òóỏõọôồốổỗộơờớởỡợ": "o",
		"ùúủũụưừứửữự": "u",
		"ỳýỷỹỵ": "y"
	}

	for viet_chars, ascii_char in mapping_chars.items():
		text = re.sub(r"[{}]+".format(viet_chars), ascii_char, text)
	return text


if __name__ == '__main__':
	print(build_url_news("Xin chào mọi người có khỏe không"))
	print(convert_vietnamese_to_asscii("Xin chào mọi người có khỏe không"))
