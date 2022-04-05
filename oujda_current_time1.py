from datetime import date, datetime, timedelta
import time
import calendar as cal

from pendulum import tomorrow

oujda_curr_dict = {}
oujda_curr_time_dict = {}
oujda_curr_day_dict = {}
def oujda_curr_time(oujda_curr_time_dict, oujda_curr_day_dict, oujda_curr_dict):
    """Storing Oujda Current time in a dictionary/list"""
    today = date.today() # Current time in an ISO foramt 'dd/mm/yyyy'
    oujda_curr_time_dict['Current time'] = today.isoformat()
    yesterday = today + timedelta(days=-1)
    oujda_curr_time_dict['Yesterday was'] = yesterday.isoformat()
    tomorrow = today + timedelta(days=+1)
    oujda_curr_time_dict['tomorrow will be'] = tomorrow.isoformat()

    today_curr_day = cal.day_name[today.weekday()] # Represent the name of the day 'Thusday'
    oujda_curr_day_dict['Today is'] = today_curr_day
    yesterday_curr_day = cal.day_name[yesterday.weekday()]
    oujda_curr_day_dict['yesterday was'] = yesterday_curr_day
    tomorrow = cal.day_name[tomorrow.weekday()]
    oujda_curr_day_dict['tomorrow would be'] = tomorrow


    today_time = time.ctime()
    oujda_curr_dict['more info doday'] = today_time
    yesterday_time = yesterday.ctime()
    oujda_curr_dict['more info yesterday'] = yesterday_time
    tomorrow_time = today + timedelta(days=+1)
    tomorrow_time = tomorrow_time.ctime()
    oujda_curr_dict['more info tomorrow'] = tomorrow_time





def display_oujda_curr_time(oujda_curr_time_dict, oujda_curr_day_dict, oujda_curr_dict):
    print("\n***Oujda Current time***")

    print(f"\tToday is: {oujda_curr_day_dict['Today is']}; the {oujda_curr_time_dict['Current time']};\n\t\tMore specifically: {oujda_curr_dict['more info doday']}")
    print(f"\tYesterday was: {oujda_curr_day_dict['yesterday was']}; the {oujda_curr_time_dict['Yesterday was']};\n\t\tMore Specifically: {oujda_curr_dict['more info yesterday']}")
    print(f"\tTomorrow would be: {oujda_curr_day_dict['tomorrow would be']}; the {oujda_curr_time_dict['tomorrow will be']};\n\t\tMore specifically: {oujda_curr_dict['more info tomorrow']}")



oujda_curr_time(oujda_curr_time_dict, oujda_curr_day_dict, oujda_curr_dict)
display_oujda_curr_time(oujda_curr_time_dict, oujda_curr_day_dict, oujda_curr_dict)
