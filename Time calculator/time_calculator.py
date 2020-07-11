def add_time(start, duration, day=None):
    s_time, am_pm = start.split()
    s_hr, s_min = s_time.split(":")
    d_hr, d_min = duration.split(":")
    days = {
        "Sunday": 1,
        "Monday": 2,
        "Tuesday": 3,
        "Wednesday": 4,
        "Thursday": 5,
        "Friday": 6,
        "Saturday": 7,
    }
    days_list = days.items()

    s_hr = int(s_hr)
    s_min = int(s_min)
    d_hr = int(d_hr)
    d_min = int(d_min)

    if am_pm == "PM":
        s_hr += 12

    f_hr = s_hr + d_hr
    f_min = s_min + d_min
    if f_min > 60:
        f_min -= 60
        f_hr += 1

    days_count = int((f_hr * 60 + f_min) / (24 * 60))
    f_hr = f_hr % 24

    days_later = ""
    if days_count == 1:
        days_later = " (next day)"
    elif days_count > 1:
        days_later = " (" + str(days_count) + " days later)"

    if f_hr > 12:
        am_pm = "PM"
        f_hr -= 12
    elif f_hr == 12:
        am_pm = "PM"
    else:
        am_pm = "AM"

    if f_hr == 0:
        f_hr = 12

    time_str = str(f_hr) + ":" + "%02d" % f_min + " " + am_pm
    if day is not None:
        day = day.capitalize()
        day_num = (days.get(day) + days_count) % 7
        for item in days_list:
            if item[1] == day_num:
                day = item[0]
        time_str += ", " + day

    if days_count != 0:
        time_str += days_later

    return time_str
