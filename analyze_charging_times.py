
import sys

from dataclasses import dataclass

from data_times import apple_watch_default_mbpr



@dataclass
class ChargingEntry:
    percentage: float = 0.0
    hrmin: int = 0
    min_since_last: int = 0.0





for arr_num, a in enumerate(apple_watch_default_mbpr):  # array
    print("Analzing charging pattern #{}".format(arr_num))
    prev_percentage = 0
    prev_hrmin = 0
    for tup_num, t in enumerate(a):     # tuple
        percentage = t[0]
        hrmin = t[1]
        if percentage < prev_percentage:
            print("ERROR: current percentage ({}) is less than previous percentage ({})"
                .format(percentage, prev_percentage))
        if hrmin < prev_hrmin:
            # Might be traversing from am/pm or vice versa
            if hrmin - 100 < 100 and prev_hrmin - 1200 < 100:
                # prev_hrmin is between 1200-1259
                # hrmin is between 100-159
                print("Just crossed PM/AM boundary: {} to {}"
                    .format(prev_hrmin, hrmin))
                prev_hrmin = prev_hrmin - 1200
                print("Previous time has been changed to {}".format(prev_hrmin))
            else:
                sys.exit("ERROR: Current timestamp ({}) is less than the previous timestamp ({})"
                    .format(hrmin, prev_hrmin))
        
        prev_percentage = percentage
        prev_hrmin = hrmin
        min_since_last = hrmin - prev_hrmin
        a[tup_num] = ChargingEntry(percentage, hrmin, min_since_last)







