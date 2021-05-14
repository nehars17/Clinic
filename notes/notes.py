class OperatingHour:
    def __init__(self, mon_open, mon_close, mon_bstart, mon_bend, tues_open, tues_close, tues_bstart, tues_bend,
                 wed_open, wed_close, wed_bstart, wed_bend, thur_open, thur_close, thur_bstart, thur_bend, fri_open,
                 fri_close, fri_bstart, fri_bend, sat_open, sat_close, sat_bstart, sat_bend, sun_open, sun_close,
                 sun_bstart, sun_bend):
        self.__mon_open = mon_open
        self.__mon_close = mon_close
        self.__mon_bstart = mon_bstart
        self.__mon_bend = mon_bend

        self.__tues_open = tues_open
        self.__tues_close = tues_close
        self.__tues_bstart = tues_bstart
        self.__tues_bend = tues_bend

        self.__wed_open = wed_open
        self.__wed_close = wed_close
        self.__wed_bstart = wed_bstart
        self.__wed_bend = wed_bend

        self.__thur_open = thur_open
        self.__thur_close = thur_close
        self.__thur_bstart = thur_bstart
        self.__thur_bend = thur_bend

        self.__fri_open = fri_open
        self.__fri_close = fri_close
        self.__fri_bstart = fri_bstart
        self.__fri_bend = fri_bend

        self.__sat_open = sat_open
        self.__sat_close = sat_close
        self.__sat_bstart = sat_bstart
        self.__sat_bend = sat_bend

        self.__sun_open = sun_open
        self.__sun_close = sun_close
        self.__sun_bstart = sun_bstart
        self.__sun_bend = sun_bend

    def set_mon_open(self, open):
        self.__mon_open = open

    def get_mon_open(self):
        return self.__mon_open

    def set_mon_close(self, close):
        self.__mon_close = close

    def get_mon_close(self):
        return self.__mon_close

    def set_mon_break_start(self, bstart):
        self.__mon_bstart = bstart

    def get_mon_break_start(self):
        return self.__mon_bstart

    def set_mon_break_end(self, bend):
        self.__mon_bend = bend

    def get_mon_break_end(self):
        return self.__mon_bend

    def set_tues_open(self, open):
        self.__tues_open = open

    def get_tues_open(self):
        return self.__tues_open

    def set_tues_close(self, close):
        self.__tues_close = close

    def get_tues_close(self):
        return self.__tues_close

    def set_tues_break_start(self, bstart):
        self.__tues_bstart = bstart

    def get_tues_break_start(self):
        return self.__tues_bstart

    def set_tues_break_end(self, bend):
        self.__tues_bend = bend

    def get_tues_break_end(self):
        return self.__tues_bend

    def set_wed_open(self, open):
        self.__wed_open = open

    def get_wed_open(self):
        return self.__wed_open

    def set_wed_close(self, close):
        self.__wed_close = close

    def get_wed_close(self):
        return self.__wed_close

    def set_wed_break_start(self, bstart):
        self.__wed_bstart = bstart

    def get_wed_break_start(self):
        return self.__wed_bstart

    def set_wed_break_end(self, bend):
        self.__wed_bend = bend

    def get_wed_break_end(self):
        return self.__wed_bend

    def set_thur_open(self, open):
        self.__thur_open = open

    def get_thur_open(self):
        return self.__thur_open

    def set_thur_close(self, close):
        self.__thur_close = close

    def get_thur_close(self):
        return self.__thur_close

    def set_thur_break_start(self, bstart):
        self.__thur_bstart = bstart

    def get_thur_break_start(self):
        return self.__thur_bstart

    def set_thur_break_end(self, bend):
        self.__thur_bend = bend

    def get_thur_break_end(self):
        return self.__thur_bend

    def set_fri_open(self, open):
        self.__fri_open = open

    def get_fri_open(self):
        return self.__fri_open

    def set_fri_close(self, close):
        self.__fri_close = close

    def get_fri_close(self):
        return self.__fri_close

    def set_fri_break_start(self, bstart):
        self.__fri_bstart = bstart

    def get_fri_break_start(self):
        return self.__fri_bstart

    def set_fri_break_end(self, bend):
        self.__fri_bend = bend

    def get_fri_break_end(self):
        return self.__fri_bend

    def set_sat_open(self, open):
        self.__sat_open = open

    def get_sat_open(self):
        return self.__sat_open

    def set_sat_close(self, close):
        self.__sat_close = close

    def get_sat_close(self):
        return self.__sat_close

    def set_sat_break_start(self, bstart):
        self.__sat_bstart = bstart

    def get_sat_break_start(self):
        return self.__sat_bstart

    def set_sat_break_end(self, bend):
        self.__sat_bend = bend

    def get_sat_break_end(self):
        return self.__sat_bend

    def set_sun_open(self, open):
        self.__sun_open = open

    def get_sun_open(self):
        return self.__sun_open

    def set_sun_close(self, close):
        self.__sun_close = close

    def get_sun_close(self):
        return self.__sun_close

    def set_sun_break_start(self, bstart):
        self.__sun_bstart = bstart

    def get_sun_break_start(self):
        return self.__sun_bstart

    def set_sun_break_end(self, bend):
        self.__sun_bend = bend

    def get_sun_break_end(self):
        return self.__sun_bend

OperatingHour.__init__(self, mon_open, mon_close, mon_bstart, mon_bend, tues_open, tues_close, tues_bstart,
                               tues_bend, wed_open, wed_close, wed_bstart, wed_bend, thur_open, thur_close, thur_bstart,
                               thur_bend, fri_open, fri_close, fri_bstart, fri_bend, sat_open, sat_close, sat_bstart,
                               sat_bend, sun_open, sun_close, sun_bstart, sun_bend)

mon_open = TimeField('Opening Time:', [validators.Optional()])
mon_close = TimeField('Closing Time:', [validators.Optional()])
mon_break_start = TimeField('Break Start Time:', [validators.Optional()])
mon_break_end = TimeField('Break End Time:', [validators.Optional()])

tues_open = TimeField('Opening Time:', [validators.Optional()])
tues_close = TimeField('Closing Time:', [validators.Optional()])
tues_break_start = TimeField('Break Start Time:', [validators.Optional()])
tues_break_end = TimeField('Break End Time:', [validators.Optional()])

wed_open = TimeField('Opening Time:', [validators.Optional()])
wed_close = TimeField('Closing Time:', [validators.Optional()])
wed_break_start = TimeField('Break Start Time:', [validators.Optional()])
wed_break_end = TimeField('Break End Time:', [validators.Optional()])

thur_open = TimeField('Opening Time:', [validators.Optional()])
thur_close = TimeField('Closing Time:', [validators.Optional()])
thur_break_start = TimeField('Break Start Time:', [validators.Optional()])
thur_break_end = TimeField('Break End Time:', [validators.Optional()])

fri_open = TimeField('Opening Time:', [validators.Optional()])
fri_close = TimeField('Closing Time:', [validators.Optional()])
fri_break_start = TimeField('Break Start Time:', [validators.Optional()])
fri_break_end = TimeField('Break End Time:', [validators.Optional()])

sat_open = TimeField('Opening Time:', [validators.Optional()])
sat_close = TimeField('Closing Time:', [validators.Optional()])
sat_break_start = TimeField('Break Start Time:', [validators.Optional()])
sat_break_end = TimeField('Break End Time:', [validators.Optional()])

sun_open = TimeField('Opening Time:', [validators.Optional()])
sun_close = TimeField('Closing Time:', [validators.Optional()])
sun_break_start = TimeField('Break Start Time:', [validators.Optional()])
sun_break_end = TimeField('Break End Time:', [validators.Optional()])

def edit_clinic_info():
    # create_user_form = ClinicInfoForm(request.form)
    # if request.method == 'POST' and create_user_form.validate():
    #     users_dict = {}
    #     db = shelve.open('clinic_storage.db', 'c')
    #
    #     try:
    #         users_dict = db['Users']
    #     except:
    #         print("Error in retrieving Users from storage.db.")
    #
    #     user = User.ClinicInfo(create_user_form.mon_open.data, create_user_form.mon_close.data, create_user_form.mon_break_start.data, create_user_form.mon_break_end.data,
    #                            create_user_form.tues_open.data, create_user_form.tues_close.data, create_user_form.tues_break_start.data, create_user_form.tues_break_end.data,
    #                            create_user_form.wed_open.data, create_user_form.wed_close.data, create_user_form.wed_break_start.data, create_user_form.wed_break_end.data,
    #                            create_user_form.thur_open.data, create_user_form.thur_close.data, create_user_form.thur_break_start.data, create_user_form.thur_break_end.data,
    #                            create_user_form.fri_open.data, create_user_form.fri_close.data, create_user_form.fri_break_start.data, create_user_form.fri_break_end.data,
    #                            create_user_form.sat_open.data, create_user_form.sat_close.data, create_user_form.sat_break_start.data, create_user_form.sat_break_end.data,
    #                            create_user_form.sun_open.data, create_user_form.sun_close.data, create_user_form.sun_break_start.data, create_user_form.sun_break_end.data,
    #                            create_user_form.off_start.data, create_user_form.off_end.data, create_user_form.off_reason.data, create_user_form.mon_break_end.data,
    #                            create_user_form.password.data, create_user_form.cfm_password.data, create_user_form.name.data,
    #                            create_user_form.address.data, create_user_form.email.data, create_user_form.phone.data)
    #     users_dict[user.get_clinic_id()] = user
    #     db['Users'] = users_dict
    #
    #     # Test codes
    #     users_dict = db['Users']
    #     user = users_dict[user.get_clinic_id()]
    #     print(user.get_name(), "was stored in storage.db successfully with Clinic ID =", user.get_clinic_id())
    #
    #     db.close()
    #     return redirect(url_for('login_clinic'))
    return render_template('clinicInfo.html')
