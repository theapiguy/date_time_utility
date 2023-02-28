from utils import get_utc_timestamp, get_now, convert_to_readable_date, t_zones, date_time_format


if __name__ == '__main__':
    country = 'USA'
    done = False
    while not done:
        state = input("Enter USA state abbreviation or END:  ")
        state = state.upper()
        if state == 'END':
            exit(0)
        if state not in t_zones[country]:
            #  Should we log data and use US/Eastern?
            print(f"{state} not found, try NC.")
        else:
            time_zone = t_zones[country][state]
            the_time = get_now(time_zone, date_time_format)
            utc_time = get_utc_timestamp()
            #  utc_time is the current utc time
            state_date, state_time = convert_to_readable_date(utc_time, time_zone)
            print(f"It is {state_time} on {state_date} in {state}.")

