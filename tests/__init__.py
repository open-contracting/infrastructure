from collections import OrderedDict

languages = {
    'en': 'English',
    # 'es': 'Español',
}

test_basic_params = OrderedDict([
    ('en', 'Toolkit'),
    # ('es', 'Inicio'),
])

test_navigation_params = [
    ('en', 'Next'),
    # ('es', 'Siguiente'),
]

test_search_params = [
    ('en', r'found \d+ page\(s\) matching'),
    # ('es', r'encontró \d+ página\(s\) acorde'),
]
