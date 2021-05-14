import shelve

class CreditInfo:
    def __init__(self, address, city, zip, country, card_type, card_name, card_num, expiry_month, expiry_year, cvv, keep_details):
        self.__address = address
        self.__city = city
        self.__zip = zip
        self.__country = country
        self.__card_type = card_type
        self.__card_name = card_name
        self.__card_num = card_num
        self.__expiry_month = expiry_month
        self.__expiry_year = expiry_year
        self.__cvv = cvv
        self.__keep_details = keep_details

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_zip(self):
        return self.__zip

    def get_country(self):
        return self.__country

    def get_card_type(self):
        return self.__card_type

    def get_card_name(self):
        return self.__card_name

    def get_card_num(self):
        return self.__card_num

    def get_expiry_month(self):
        return self.__expiry_month

    def get_expiry_year(self):
        return self.__expiry_year

    def get_cvv(self):
        return self.__cvv

    def get_keep_details(self):
        return self.__keep_details


    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_zip(self, zip):
        self.__zip = zip

    def set_country(self, country):
        self.__country = country

    def set_card_type(self, card_type):
        self.__card_type = card_type

    def set_card_name(self, card_name):
        self.__card_name = card_name

    def set_card_num(self, card_num):
        self.__card_num = card_num

    def set_expiry_month(self, month):
        self.__expiry_month = month

    def set_expiry_year(self, year):
        self.__expiry_year = year

    def set_cvv(self, cvv):
        self.__cvv = cvv

    def set_keep_details(self, keep_details):
        self.__keep_details = keep_details


if __name__ == "__main__":

    db = shelve.open('storage.db', 'r')
    info = db['creditInfo']
    print(info["T1234567E"].get_card_num())
