import pandas as pd

date1 = '2011-05-03'
date2 = '2011-05-10'
mydates = pd.bdate_range(date1, date2).tolist()
print(mydates)
for i in mydates:
    print(i)

import datetime

start = datetime.datetime.strptime("21-06-2014", "%d-%m-%Y")
end = datetime.datetime.strptime("07-07-2014", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]

for date in date_generated:
    print(date.strftime("%d-%m-%Y"))

if od_dict != {}:
            for start in od_dict:
                off_day_start = datetime.datetime.strptime(od_dict[start][0], '%d %m %Y')
                off_day_end = datetime.datetime.strptime(od_dict[start][1], '%d %m %Y')
                off_day_range = [off_day_start + datetime.timedelta(days=x) for x in range(0, (off_day_end - off_day_start).days)]
        else:
            off_day_range = []
