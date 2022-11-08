import sys

from Check import check
from IOsystem import stdIO
from SORT import Sort 
from Time import Stopwatch


def main():
    # make instance
    stdio = stdIO()
    stopwatch = Stopwatch()

    # input file
    stdio.get_file()
    stdio.get_data()

    # make instance
    err_check = check(stdio.calc_type, stdio.inputfile, stdio.json_data, stdio.outputfile)
    sorting = Sort(stdio.calc_type, stdio.json_data)

    # check error
    err_check.search_error()
    # measure time
    stopwatch.start()

    # calculate
    sorting.calc()

    stopwatch.stop()

    #output
    stdio.output(sorting.index_array)
    print("finished!!!")
    print("time:{:3.3f}μs".format( stopwatch.time_calc_micro ))



if __name__ == "__main__":
    main()
