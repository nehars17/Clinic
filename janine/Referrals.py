from User import *
from Prescription import *

class Referrals():
    nric=''
    def __init__(self, reason, organisation):
        Referrals.nric=''
        self.__reason = reason
        self.__organisation = organisation

    def set_reason(self, reason):
        self.__reason = reason

    def get_reason(self):
        return self.__reason

    def set_organisation(self, organisation):
        self.__organisation = organisation

    def get_organisation(self):
        return self.__organisation

    def set_nric(self,nric):
        self.__nric=nric

    def get_nric(self):
        return self.__nric
