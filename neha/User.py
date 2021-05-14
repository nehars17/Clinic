import random, string

class PublicUser:
    def __init__(self, name, nric, email, phone, address, gender, password, cfm_password):
        self.__name = name
        self.__nric = nric
        self.__email = email
        self.__phone = phone
        self.__address = address
        self.__gender = gender
        self.__password = password
        # self.set_password(password, cfm_password)
        # self.set_nric(nric)
        # self.set_phone(phone)

    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

    def set_nric(self, nric):
        if nric[0].isalpha and nric[-1].isalpha and nric[1:-1].isnumeric:
            self.__nric = nric.upper()
        else:
            self.__nric = 'Invalid'
    def get_nric(self):
        return self.__nric

    def set_email(self, email):
        self.__email = email
    def get_email(self):
        return self.__email

    def set_phone(self, phone):
        if phone[0] == '8' or phone[0] == '9' or phone == '6':
            self.__phone = phone
        else:
            self.__phone = 'Invalid'
    def get_phone(self):
        return self.__phone

    def set_address(self, address):
        self.__address = address
    def get_address(self):
        return self.__address

    def set_gender(self, gender):
        self.__gender = gender
    def get_gender(self):
        return self.__gender

    def set_password(self, password, cfm_password):
        if password == cfm_password:
            self.__password = password
        else:
            self.__password = 'error'
    def get_password(self):
        return self.__password

    # def set_cfm_password(self, cfm_password):
    #     self.__cfm_password = cfm_password
    # def get_cfm_password(self):
    #     return self.__cfm_password


# class ClinicUser:
#     def __init__(self, name, address, email, phone, password, cfm_password):
#         self.__name = name
#         self.__address = address
#         self.__email = email
#         self.__phone = phone
#         self.__password = password
#         self.__cfm_password = cfm_password
#         self.__clinic_id = ''
#         # self.set_password(password, cfm_password)
#         # self.set_phone(phone)
#         self.set_clinic_id()
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def set_address(self, address):
#         self.__address = address
#
#     def get_address(self):
#         return self.__address
#
#     def set_email(self, email):
#         self.__email = email
#
#     def get_email(self):
#         return self.__email
#
#     def set_phone(self, phone):
#         self.__phone = phone
#         # if phone[0] == '8' or phone[0] == '9' or phone == '6':
#         #     self.__phone = phone
#         # else:
#         #     self.__phone = 'Invalid'
#
#     def get_phone(self):
#         return self.__phone
#
#     def set_password(self, password, cfm_password):
#         if password == cfm_password:
#             self.__password = password
#         else:
#             self.__password = 'error'
#
#     def get_password(self):
#         return self.__password
#
#     # def set_cfm_password(self, cfm_password):
#     #     self.__cfm_password = cfm_password
#     # def get_cfm_password(self):
#     #     return self.__cfm_password
#
#     def set_clinic_id(self):
#         digits = string.digits
#         letters = string.ascii_letters
#         id = ''
#         while len(id) != 6:
#             for i in range(1):
#                 id += random.choice(letters)
#             for i in range(1):
#                 id += random.choice(digits)
#         self.__clinic_id = id
#
#     def get_clinic_id(self):
#         return self.__clinic_id
#
#
# class ClinicInfo(ClinicUser):
#     def __init__(self, mon_open, mon_close, mon_bstart, mon_bend, tues_open, tues_close, tues_bstart, tues_bend,
#                  wed_open, wed_close, wed_bstart, wed_bend, thur_open, thur_close, thur_bstart, thur_bend, fri_open,
#                  fri_close, fri_bstart, fri_bend, sat_open, sat_close, sat_bstart, sat_bend, sun_open, sun_close,
#                  sun_bstart, sun_bend, off_start, off_end, off_reason, password, cfm_password, name, address, email,
#                  phone):
#         ClinicUser.__init__(self, name, address, email, phone, password, cfm_password)
#         self.__off_start = off_start
#         self.__off_end = off_end
#         self.__off_reason = off_reason
#
#     def set_off_start(self, off_start):
#         self.__off_start = off_start
#
#     def get_off_start(self):
#         return self.__off_start
#
#     def set_off_end(self, off_end):
#         self.__off_end = off_end
#
#     def get_off_end(self):
#         return self.__off_end
#
#     def set_off_reason(self, reason):
#         self.__off_reason = reason
#
#     def get_off_reason(self):
#         return self.__off_reason
#
#
# if __name__ == '__main__':
#     name = input('Name: ')
#     nric = input('Nric: ')
#     address = input('address: ')
#     email = input('email: ')
#     phone = input('phone: ')
#     gender = input('gender: ')
#     password = input('password: ')
#     cfm_password = input('confirm password: ')
#     p = PublicUser(name, nric, email, phone, gender, password, cfm_password)
#     c = ClinicUser(name, address, email, phone, password, cfm_password)
#     print(p.get_password(), p.get_nric(), c.get_clinic_id(), p.get_phone())
