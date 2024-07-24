PAGE_LOAD_STRATEGY = 'eager'
"""
    normal: trang tải xong html, js, css.
    eager: trang chỉ cần tải xong html.
"""

IMPLICITLY_WAIT = 10

LOAD_TIME_OUT = 120

NAME_DEVICE_MOBILE = "iPhone 12 Pro"

# =================== Option driver ==========================
LOG_LEVEL = 3

DISABLE_BLICK_FEATURES = "AutomationControlled"

REMOTE_DEBUGGING_PORT = 8000

WINDOW_SIZE = (1920, 1080)

DISABLE_FEATURES = [
	'OptimizationHints',
	'OptimizationHintsFetching',
	'Translate',
	'OptimizationTargetPrediction',
	'OptimizationGuideModelDownloading',
	'DownloadBubble',
	'DownloadBubbleV2',
	'InsecureDownloadWarnings',
	'InterestFeedContentSuggestions',
	'PrivacySandboxSettings4',
	'SidePanelPinning',
	'UserAgentClientHint',
]
