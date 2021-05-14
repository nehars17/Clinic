@app.route('/editOffDay', methods=['GET', 'POST'])
def off_day():
    global clinic_id
    create_user_form = OffDay(request.form)
    if request.method == 'POST':
        off_day_dict= {}
        od_db = shelve.open('clinic_od_storage.db', 'c')

        try:
            off_day_dict = od_db[clinic_id]
        except:
            print("Error in retrieving Users from storage.db.")

        clinic_od = Clinic.OffDay(create_user_form.start.data, create_user_form.end.data, create_user_form.reason.data)
        off_day_dict[clinic_od.get_id()] = clinic_od
        od_db[clinic_id] = off_day_dict
        print(clinic_id, "was stored in storage.db successfully with Clinic ID =", clinic_od.get_start())

        od_db.close()
        return redirect(url_for('retrieve_off_day'))

    return render_template('createOffDay.html', form=create_user_form)

@app.route('/retrieveOffDay')
def retrieve_off_day():
    global clinic_id
    off_day_dict = {}
    try:
        od_db = shelve.open('clinic_od_storage.db', 'r')
        off_day_dict = od_db[clinic_id] #have the dict of the operating hours
        od_db.close()
    except:
        od_db = {}
    # off_day_dict = od_db[clinic_id] #have the dict of the operating hours

    return render_template('retrieveOffDay.html', off_day_dict=off_day_dict)

@app.route('/updateOffDay/<int:id>/', methods=['GET', 'POST'])
def update_off_day(id):
    update_user_form = OffDay(request.form)
    global clinic_id
    if request.method == 'POST':
        od_db = shelve.open('clinic_od_storage.db', 'w')
        off_day_dict = od_db[clinic_id]
        off_day = off_day_dict[id]
        off_day.set_start(update_user_form.start.data)
        off_day.set_end(update_user_form.end.data)
        off_day.set_reason(update_user_form.reason.data)
        # clinic_od = Clinic.OffDay(update_user_form.start.data, update_user_form.end.data, update_user_form.reason.data)
        # period = [clinic_od.get_start(), clinic_od.get_end(), clinic_od.get_reason()]
        # off_day_dict[clinic_od.get_start()] = period
        od_db[clinic_id] = off_day_dict
        od_db.close()
        return redirect(url_for('retrieve_off_day'))
    else:
        off_day_dict = {}
        od_db = shelve.open('clinic_od_storage.db', 'w')
        off_day_dict = od_db[clinic_id] #have the dict of the operating hours
        od_db.close()

        off_day = off_day_dict[id]
        update_user_form.start.data = off_day.get_start()
        update_user_form.end.data = off_day.get_end()
        update_user_form.reason.data = off_day.get_reason()

        return render_template('updateOffDay.html', form=update_user_form)

@app.route('/deleteOffDay/<int:id>/', methods=['POST', 'GET'])
def delete_off_day(id):
    global clinic_id
    off_day_dict = {}
    try:
        od_db = shelve.open('clinic_od_storage.db', 'w')
        off_day_dict = od_db[clinic_id]
    except:
        print("Error in retrieving Users from storage.db.")
    print('hi this is start =',id)
    if id in off_day_dict:
        off_day_dict.pop(id)
    for i in off_day_dict:
        print(i)

    od_db[clinic_id] = off_day_dict
    od_db.close()


class OffDay:
    count_id = 0
    def __init__(self, start, end, reason):
        OffDay.count_id +=1
        self.__id = OffDay.count_id
        self.__start = start
        self.__end = end
        self.__reason = reason

    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id

    def set_start(self, start):
        self.__start = start
    def get_start(self):
        return self.__start

    def set_end(self, end):
        self.__end = end
    def get_end(self):
        return self.__end

    def set_reason(self, reason):
        self.__reason = reason
    def get_reason(self):
        return self.__reason

{% extends "base.html" %}
{% block title %}Library Loan System - Retrieve Users{% endblock %}

{% block content %}
<section>
<h1 class="display-4">Retrieve Off Day</h1>
<div>
<table class="table table-striped">
    <title>Off Days</title>
    <thead>
      <tr>
        <th>Start</th>
        <th>End</th>
        <th>Reason/Message</th>
        <th></th>
        <th><a href="/editOffDay" class="btn btn-warning">Add</a></th>
      </tr>
    </thead>
    <tbody>
    {% for id in off_day_dict %}
      <tr>
        <td>{{ off_day_dict[id].get_start() }}</td>
        <td>{{ off_day_dict[id].get_end() }}</td>
        <td>{{ off_day_dict[id].get_reason() }}</td>
        <td><a href="/updateOffDay/{{ id }}/" class="btn btn-warning">Update</a></td>
        <td>
          <form action="{{url_for('delete_off_day', id=off_day_dict[id].get_id())}}" method="POST">
            <input type="submit" value="Delete" class="btn btn-danger">
          </form>
        </td>
      </tr>
    {% endfor %}
    </tbody>
  </table>
</div>
</section>
{% endblock %}
