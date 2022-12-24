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

        # Цена со скидкой
        priceNow = self.find(mv_locators.priceNow) # надо обработать TimeoutException
        data['PriceNow'] = priceNow.text

        # Цена со скидкой
        priceOriginal = self.find(mv_locators.priceOriginal)
        data['PriceOriginal'] = priceOriginal.text

        # Гарантия
        guarantee = self.find(mv_locators.guarantee)
        data['Guarantee'] = guarantee.text

        # Страна
        country = self.find(mv_locators.country)
        data['Country'] = country.text

        # Серия
        series = self.find(mv_locators.series) # need update!!
        data['Series'] = series.text

        # ОС: установлена -> не установлена
        os = self.find(mv_locators.os)
        data['OS'] = os.text

        # OC windows
        windows = self.find(mv_locators.os_windows)
        data['windows'] = windows.text

        # Кол-во ядер
        cores = self.find(mv_locators.processor_cores)
        data['CoresNumber'] = cores.text

        # Модель процессора
        processor_model = self.find(mv_locators.processor_model)
        data['ProcessorModel'] = processor_model.text

        # Тип процессора
        processor_type = self.find(mv_locators.processor_type)
        data['ProcessorType'] = processor_type.text

        # Частота процессора
        processor_frequency = self.find(mv_locators.processor_frequency)
        data['ProcessorFrequency'] = processor_frequency.text

        # GpuManufacturer
        gpu_manufacturer = self.find(mv_locators.gpu_manufacturer)
        data['GpuManufacturer'] = gpu_manufacturer.text

        # gpu_controller
        gpu_controller = self.find(mv_locators.gpu_controller)
        data['GpuController'] = gpu_controller.text

        # gpu_capacity
        gpu_capacity = self.find(mv_locators.gpu_capacity)
        data['GpuCapacity'] = gpu_capacity.text

        # screen_size
        screen_size = self.find(mv_locators.screen_size)
        data['ScreenSize'] = screen_size.text

        # screen_frequency
        screen_frequency = self.find(mv_locators.screen_frequency)
        data['ScreenFrequency'] = screen_frequency.text

        # ssd_size
        ssd_size = self.find(mv_locators.ssd_size)
        data['SsdSize'] = ssd_size.text

        # ram
        ram = self.find(mv_locators.ram)
        data['RAM'] = ram.text

        # ram_type
        ram_type = self.find(mv_locators.ram_type)
        data['RAM_type'] = ram_type.text

        # hdmi
        hdmi = self.find(mv_locators.hdmi)
        data['HDMI'] = hdmi.text

        # material
        material = self.find(mv_locators.material)
        data['Material'] = material.text

        # battery
        battery = self.find(mv_locators.battery)
        data['Battery'] = battery.text

        # weight
        weight = self.find(mv_locators.weight)
        data['Weight'] = weight.text

        print(data)