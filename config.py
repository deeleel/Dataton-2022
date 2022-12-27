webdriver_path = r' ..\chromedriver.exe'

url_ozon = "https://www.ozon.ru/category/noutbuki-15692/" # проблемы с cloudflare
url_mvideo = "https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118?page={}" # good
url_dns = 'https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/?order=6&stock=now&p={}' # good

headers = [
    'Brand',
    'PriceNow',
    'PriceOriginal',
    'Guarantee',
    'Country',
    'Series',
    'OS',
    'windows',
    'CoresNumber',
    'ProcessorModel',
    'Processor',
    'ProcessorType',
    'ProcessorFrequency',
    'GpuManufacturer',
    'GpuController',
    'GpuCapacity',
    'ScreenSize',
    'Diagonal',
    'ScreenFrequency',
    'SsdSize',
    'RAM',
    'RAM_type',
    'HDMI',
    'Material',
    'Battery',
    'Weight'
]