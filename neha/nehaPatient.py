class Patient:
    nric = ''
    count_id=0
    def __init__(self,purpose,clinic,date_of_arrival,time,message):
        Patient.nric = ''
        Patient.count_id+=1
        self.__user_id=Patient.count_id
        self.__nric = Patient.nric
        self.__purpose = purpose
        self.__date_of_arrival=date_of_arrival
        self.__time=time
        self.__message=message
        self.__clinic=clinic
        self.__checkbox=0

    def get_user_id(self):
        return self.__user_id
    def get_checkbox(self):
        return self.__checkbox
    def get_purpose(self):
        return self.__purpose
    def get_nric(self):
        return self.__nric

    def get_clinic(self):
        return self.__clinic

    def get_date_of_arrival(self):
        return self.__date_of_arrival

    def get_time(self):
        return self.__time

    def get_message(self):
        return self.__message

    def set_clinic(self,clinic):
        self.__clinic=clinic

    def set_purpose(self, purpose):
        self.__purpose = purpose

    def set_nric(self, nric):
        self.__nric = nric

    def set_time(self, time):
        self.__time = time

    def set_checkbox(self,checkbox):
        self.__checkbox=checkbox

    def set_date_of_arrival(self, date_of_arrival):
        self.__date_of_arrival = date_of_arrival

    def set_message(self, message):
        self.__message = message

    def set_user_id(self, user_id):
        self.__user_id = user_id





