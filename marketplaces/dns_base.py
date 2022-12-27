from marketplaces.base import BaseFunctions
import locators.dns as dns_locators
from selenium.common.exceptions import TimeoutException
import numpy as np
import time 

class DNS(BaseFunctions):

    def get_product_elem(self, num):
        product = self.find(
            (
                dns_locators.product_from_list[0], 
                dns_locators.product_from_list[1].format(num)
                
            )
        )
        return product

    def open_product_dns(self, num):
        if num > 2:
            for i in range(1, num):
                prod = self.get_product_elem(i)
                self.scroll_to(prod)
        product = self.get_product_elem(num)
        product.click()

        features = self.find(dns_locators.all_features)
        features.click()


    def get_features_dns(self):
        data = {}
        try:
            # Цена со скидкой
            priceNow = self.find(dns_locators.priceNow)
            data['PriceNow'] = priceNow.text

            # Цена без скидки
            priceOriginal = self.find(dns_locators.priceOriginal)
            data['PriceOriginal'] = priceOriginal.text

        except TimeoutException:
            data['PriceNow'] = np.nan
            price = self.find(dns_locators.priceMain)
            data['PriceOriginal'] = price.text
        else:
            data['PriceNow'] = data['PriceNow'].split(data['PriceOriginal'])

        # Гарантия
        try:
            guarantee = self.find(dns_locators.guarantee)
            data['Guarantee'] = guarantee.text
        except TimeoutException:
            try:
                guarantee = self.find(dns_locators.guarantee_mac)
                data['Guarantee'] = guarantee.text
            except TimeoutException:    
                data['Guarantee'] = np.nan

            

        # Страна
        data['Country'] = np.nan

        # Серия
        series = self.find(dns_locators.series)
        data['Series'] = series.text

        # ОС:
        try:
            os = self.find(dns_locators.os)
            data['OS'] = os.text
        except TimeoutException:
            data['OS'] = np.nan


        # windows
        data['windows'] = np.nan

        # Кол-во ядер
        try:
            cores = self.find(dns_locators.processor_cores)
            data['CoresNumber'] = cores.text
        except TimeoutException:
            cores = self.find(dns_locators.processor_cores_pr)
            data['CoresNumber'] = cores.text

        # Модель процессора
        processor_model = self.find(dns_locators.processor_model)
        data['ProcessorModel'] = processor_model.text
        
        # Процессор
        data['Processor'] = np.nan

        # ProcessorType
        data['ProcessorType'] = np.nan

        try:
            # Частота процессора
            processor_frequency = self.find(dns_locators.processor_frequency)
            data['ProcessorFrequency'] = processor_frequency.text
        except TimeoutException:
            data['ProcessorFrequency'] = np.nan

        # GpuManufacturer
        data['GpuManufacturer'] = np.nan

        # gpu_controller
        gpu_controller = self.find(dns_locators.gpu_controller)
        data['GpuController'] = gpu_controller.text

        try:
            # gpu_capacity
            gpu_capacity = self.find(dns_locators.gpu_capacity)
            data['GpuCapacity'] = gpu_capacity.text
        except TimeoutException:
            data['GpuCapacity'] = np.nan

        # screen_size
        screen_size = self.find(dns_locators.screen_size)
        data['ScreenSize'] = screen_size.text

        # diagonal
        data['Diagonal'] = np.nan

        try:
            # screen_frequency
            screen_frequency = self.find(dns_locators.screen_frequency)
            data['ScreenFrequency'] = screen_frequency.text
        except TimeoutException:
            data['ScreenFrequency'] = np.nan

        # ssd_size
        ssd_size = self.find(dns_locators.ssd_size)
        data['SsdSize'] = ssd_size.text

        # ram
        ram = self.find(dns_locators.ram)
        data['RAM'] = ram.text

        # ram_type
        ram_type = self.find(dns_locators.ram_type)
        data['RAM_type'] = ram_type.text

        # hdmi
        hdmi = self.find(dns_locators.hdmi)
        data['HDMI'] = hdmi.text

        # material
        material = self.find(dns_locators.material)
        data['Material'] = material.text

        # battery
        data['Battery'] = np.nan

        # weight
        weight = self.find(dns_locators.weight)
        data['Weight'] = weight.text
        
        # print(data)

        self.write_to_file(data, 'data_dns.csv')

        self.go_back()
        self.go_back()
