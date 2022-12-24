from marketplaces.base import BaseFunctions
from selenium.common.exceptions import TimeoutException
import locators.mvideo as mv_locators
import time
import numpy as np

class Mvideo(BaseFunctions):

    def open_product_mv(self, num):
        product = self.find(
            (
                mv_locators.product_from_list[0], 
                mv_locators.product_from_list[1].format(num)
            )
        )
        product.click()

        features = self.find(mv_locators.all_features)
        features.click()
        time.sleep(4)

    def get_features_mv(self):
        data = {}

        try:
            # Цена со скидкой
            priceNow = self.find(mv_locators.priceNow) # надо обработать TimeoutException
            data['PriceNow'] = priceNow.text
        except TimeoutException:
            data['PriceNow'] = np.nan

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

        try:
            # Модель процессора
            processor_model = self.find(mv_locators.processor_model)
            data['ProcessorModel'] = processor_model.text
        except TimeoutException:
             cpu = self.find(mv_locators.processor)
             data['Processor'] = cpu.text
             data['ProcessorModel'] = np.nan

        try:
            # Тип процессора
            processor_type = self.find(mv_locators.processor_type)
            data['ProcessorType'] = processor_type.text
        except TimeoutException:
            data['ProcessorType'] = np.nan
        
        try:
            # Частота процессора
            processor_frequency = self.find(mv_locators.processor_frequency)
            data['ProcessorFrequency'] = processor_frequency.text
        except TimeoutException:
            data['ProcessorFrequency'] = np.nan

        # GpuManufacturer
        gpu_manufacturer = self.find(mv_locators.gpu_manufacturer)
        data['GpuManufacturer'] = gpu_manufacturer.text

        # gpu_controller
        gpu_controller = self.find(mv_locators.gpu_controller)
        data['GpuController'] = gpu_controller.text

        try:
            # gpu_capacity
            gpu_capacity = self.find(mv_locators.gpu_capacity)
            data['GpuCapacity'] = gpu_capacity.text
        except TimeoutException:
            data['GpuCapacity'] = np.nan

        # screen_size
        screen_size = self.find(mv_locators.screen_size)
        data['ScreenSize'] = screen_size.text

        try:
            # screen_frequency
            screen_frequency = self.find(mv_locators.screen_frequency)
            data['ScreenFrequency'] = screen_frequency.text
        except TimeoutException:
            data['ScreenFrequency'] = np.nan

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