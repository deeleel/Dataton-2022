from marketplaces.base import BaseFunctions
import locators.mvideo as mv_locators

class Mvideo(BaseFunctions):

    def open_product_mv(self):
        product = self.find(mv_locators.product_from_list)
        product.click()

        features = self.find(mv_locators.all_features)
        features.click()

    def get_features_mv(self):
        data = {}
        # Гарантия
        guarantee = self.find(mv_locators.guarantee)
        data['Guarantee'] = guarantee.text

        # Страна
        country = self.find(mv_locators.country)
        data['Country'] = country.text

        # Серия
        series = self.find(mv_locators.series)
        data['Series'] = series.text

        # ОС: установлена -> не установлена
        os = self.find(mv_locators.os)
        data['OS'] = os.text

        

        print(data)