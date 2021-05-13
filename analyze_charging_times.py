
import sys

from dataclasses import dataclass

from data_times import apple_watch_default_mbpr

from datetime import datetime



@dataclass
class ChargingEntry:
    percentage: float = 0.0     # A value of 10 = 10%
    hrmin: int = 0
    min_since_last: int = 0.0





for arr_num, arr in enumerate(apple_watch_default_mbpr):  # Go through each array
    print("Analzing charging pattern #{}".format(arr_num))

    # Assume everything is AM. If we cross into 12 o'clock, switch to PM
    meridiem_indicator = "AM"

    prev_percentage = float('-inf')
    prev_hr = int(arr[0][1] / 100)
    prev_time_obj = -1

    for tup_num, tup in enumerate(arr):         # Go through each tuple in array

        for i_num, val in enumerate(tup):       # Go through values in tuple

            if i_num == 0:                  # Charging percentage
                percentage = val
                if percentage < prev_percentage:
                    sys.exit("ERROR: current percentage ({}) is less than "
                             "previous percentage ({})"
                             .format(percentage, prev_percentage))
                prev_percentage = percentage

            if i_num == 1:                  # Time as an integer
                hr = int(val / 100)
                min = val % 100
                if prev_hr % 12 > hr % 12:
                    meridiem_indicator = "PM"
                    print("\tCrossed AM/PM boundary")
                    print("\t\tPrevious: {}, current: {}".format(prev_hr, hr))

                format = "%I:%M %p"
                time_str = "{}:{} {}".format(hr, min, meridiem_indicator)
                time_obj = datetime.strptime(time_str, format)

                if prev_time_obj == -1:
                    mins_elapsed = 0
                else:
                    mins_elapsed = (time_obj - prev_time_obj).total_seconds() / 60


                print("Value {} has been converted to {}, {} min difference since last"
                      .format(val,
                              time_obj.strftime(format),
                              mins_elapsed))

                prev_hr = hr
                prev_time_obj = time_obj
            
            # TODO: Overwrite objects in array with ChargingEntry








