from marketplaces.base import BaseFunctions
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
import locators.mvideo as mv_locators
import time
import numpy as np

class Mvideo(BaseFunctions):

    def get_product_elem(self, num):
        product = self.found(
            (
                mv_locators.product_from_list[0], 
                mv_locators.product_from_list[1].format(num)
            )
        )
        return product

    def open_product_mv(self, num):
        if num > 2:
            for i in range(1, num):
                prod = self.get_product_elem(i)
                self.scroll_to(prod)
        product = self.get_product_elem(num)

        # while (product == False):
        #     self.scroll_down()
        #     product = self.get_product_elem(num)
        product.click()

        features = self.find(mv_locators.all_features)
        features.click()

    def get_features_mv(self):
        time.sleep(2)
        data = {}

        try:
            # Цена со скидкой
            priceNow = self.find(mv_locators.priceNow) # надо обработать TimeoutException
            data['PriceNow'] = priceNow.text

            # Цена со скидкой
            priceOriginal = self.find(mv_locators.priceOriginal)
            data['PriceOriginal'] = priceOriginal.text
        except TimeoutException:
            data['PriceNow'] = np.nan

            price = self.find(mv_locators.priceMain)
            data['PriceOriginal'] = price.text


        # Гарантия
        guarantee = self.find(mv_locators.guarantee)
        data['Guarantee'] = guarantee.text

        # Страна
        country = self.find(mv_locators.country)
        data['Country'] = country.text

        try:
            # Серия
            series = self.find(mv_locators.series) # need update!!
            data['Series'] = series.text
        except TimeoutException:
            data['Series'] = np.nan

        # ОС
        os = self.find(mv_locators.os)
        data['OS'] = os.text

        try:
            # OC windows
            windows = self.find(mv_locators.os_windows)
            data['windows'] = windows.text
        except TimeoutException:
            data['windows'] = np.nan

        try:
            # Кол-во ядер
            cores = self.find(mv_locators.processor_cores)
            data['CoresNumber'] = cores.text
        except TimeoutException:
            data['CoresNumber'] = np.nan

        try:
            # Модель процессора
            processor_model = self.find(mv_locators.processor_model)
            data['ProcessorModel'] = processor_model.text

            cpu = self.find(mv_locators.processor)
            data['Processor'] = cpu.text
        except TimeoutException:
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

        try:
            # GpuManufacturer
            gpu_manufacturer = self.find(mv_locators.gpu_manufacturer)
            data['GpuManufacturer'] = gpu_manufacturer.text
        except TimeoutException:
            data['GpuManufacturer'] = np.nan
        
        try:
            # gpu_controller
            gpu_controller = self.find(mv_locators.gpu_controller)
            data['GpuController'] = gpu_controller.text
        except TimeoutException:
            data['GpuController'] = np.nan

        try:
            # gpu_capacity
            gpu_capacity = self.find(mv_locators.gpu_capacity)
            data['GpuCapacity'] = gpu_capacity.text
        except TimeoutException:
            data['GpuCapacity'] = np.nan

        try:
            # screen_size
            screen_size = self.find(mv_locators.screen_size)
            data['ScreenSize'] = screen_size.text

            diagonal = self.find(mv_locators.diagonal)
            data['Diagonal'] = diagonal.text
        except TimeoutException:
            data['ScreenSize'] = np.nan

        try:
            # screen_frequency
            screen_frequency = self.find(mv_locators.screen_frequency)
            data['ScreenFrequency'] = screen_frequency.text
        except TimeoutException:
            data['ScreenFrequency'] = np.nan

        try:
            # ssd_size
            ssd_size = self.find(mv_locators.ssd_size)
            data['SsdSize'] = ssd_size.text
        except TimeoutException:
            data['SsdSize'] = np.nan

        # ram
        ram = self.find(mv_locators.ram)
        data['RAM'] = ram.text

        try:
            # ram_type
            ram_type = self.find(mv_locators.ram_type)
            data['RAM_type'] = ram_type.text
        except TimeoutException:
            data['RAM_type'] = np.nan

        try:
            # hdmi
            hdmi = self.find(mv_locators.hdmi)
            data['HDMI'] = hdmi.text
        except TimeoutException:
            data['HDMI'] = np.nan

        # material
        material = self.find(mv_locators.material)
        data['Material'] = material.text

        try:
            # battery
            battery = self.find(mv_locators.battery)
            data['Battery'] = battery.text
        except TimeoutException:
            data['Battery'] = np.nan

        try:
            # weight
            weight = self.find(mv_locators.weight)
            data['Weight'] = weight.text
        except TimeoutException:
            data['Weight'] = np.nan

        self.write_to_file(data)

        self.go_back()
        self.go_back()