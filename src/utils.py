import pytz

from datetime import datetime

date_format = '%m-%d-%Y'
time_format = '%I:%M:%S %p'
date_time_format = date_format + " " + time_format
utc_format = '%Y-%m-%dT%H:%M:%SZ'

t_zones = {
    "USA": {
        "FL": "US/Eastern",
        "GA": "US/Eastern",
        "SC": "US/Eastern",
        "NC": "US/Eastern",
        "VA": "US/Eastern",
        "WV": "US/Eastern",
        "IN": "US/Eastern",
        "OH": "US/Eastern",
        "PA": "US/Eastern",
        "MI": "US/Eastern",
        "NY": "US/Eastern",
        "ME": "US/Eastern",
        "HN": "US/Eastern",
        "MA": "US/Eastern",
        "RI": "US/Eastern",
        "CT": "US/Eastern",
        "NJ": "US/Eastern",
        "DE": "US/Eastern",
        "MD": "US/Eastern",
        "DC": "US/Eastern",
        "VI": "US/Eastern",
        "ND": "US/Central",
        "SD": "US/Central",
        "NE": "US/Central",
        "KS": "US/Central",
        "OK": "US/Central",
        "TX": "US/Central",
        "LA": "US/Central",
        "AR": "US/Central",
        "MO": "US/Central",
        "IA": "US/Central",
        "MN": "US/Central",
        "WI": "US/Central",
        "IL": "US/Central",
        "KY": "US/Central",
        "TN": "US/Central",
        "MS": "US/Central",
        "AL": "US/Central",
        "MT": "US/Mountain",
        "ID": "US/Mountain",
        "WY": "US/Mountain",
        "UT": "US/Mountain",
        "CO": "US/Mountain",
        "AZ": "US/Mountain",
        "NM": "US/Mountain",
        "WA": "US/Pacific",
        "OR": "US/Pacific",
        "CA": "US/Pacific",
        "NV": "US/Pacific",
        "H": "US/Hawaii",
        "I": "US/Hawaii",
        "a": "US/Alaska",
        "k": "US/Alaska",
        "DEFAULT": "US/Guam",
        "M": "US/NMI",
        "P": "US/NMI"
    }
}


def get_utc_timestamp(precision=0):
    """Return a timestamp.

    Keyword arguments:
    precision -- number of decimal places up to 6 (default 0)

    Note: if 0 there won't be a decimal; if negative, turned positive
    """
    precision = abs(precision)
    precision = min(precision, 6)

    if precision == 0:
        return pytz.utc.localize(datetime.utcnow()).strftime('%Y-%m-%dT%H:%M:%SZ')
    else:
        return pytz.utc.localize(datetime.utcnow()).strftime('%Y-%m-%dT%H:%M:%S.%f')[:precision - 6] + 'Z'


def get_now(time_zone='US/Eastern', d_format=date_format):
    internal_eastern_date = datetime.strptime(get_utc_timestamp(), utc_format).replace(tzinfo=pytz.utc).astimezone(
        pytz.timezone(time_zone))
    external_date = datetime.strftime(internal_eastern_date, d_format).lstrip('0').replace('/0', '/')
    return datetime.strptime(external_date, d_format)


def convert_to_readable_date(history_date, time_zone='US/Eastern'):
    #  Returns a human readable friendly date format in Eastern Time
    converted_datetime = datetime.strptime(history_date, utc_format).replace(tzinfo=pytz.utc).astimezone(
        pytz.timezone(time_zone))
    submitted_time = datetime.strftime(converted_datetime, time_format)
    submitted_date = datetime.strftime(converted_datetime, date_format).lstrip('0').replace('/0', '/')
    return submitted_date, submitted_time


if __name__ == '__main__':
    get_utc_timestamp()

