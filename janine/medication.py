class UserMeds:
    count_id = 0
    def __init__(self, nric, clinic, symptoms, medication, instructions, sideEffects):
        UserMeds.count_id += 1
        self.__nric = nric
        self.__clinic = clinic
        self.__symptoms = symptoms
        self.__medication = medication
        self.__instructions = instructions
        self.__sideEffects = sideEffects

    def set_nric(self, nric):
        self.__nric = nric

    def get_nric(self):
        return self.__nric

    def set_clinic(self, clinic):
        self.__clinic = clinic

    def get_clinic(self):
        return self.__clinic

    def set_symptoms(self, symptoms):
        self.__symptoms = symptoms

    def get_symptoms(self):
        return self.__symptoms

    def set_medication(self, medication):
        self.__medication = medication

    def get_medication(self):
        return self.__medication

    def set_instructions(self, instructions):
        self.__instructions = instructions

    def get_instructions(self):
        return self.__instructions

    def set_sideEffects(self, sideEffects):
        self.__sideEffects = sideEffects

    def get_sideEffects(self):
        return self.__sideEffects
