# Lecture 25, nongraded assignment #P2
import numpy as np
import matplotlib.pyplot as plt
import sys, csv

def read_data(dates):
    cases = []
    for date in dates:
        with open('covid19_cases_demographics_tests_' + date + '.csv', 'r') as record:
            f_csv = csv.reader(record)
            for row in f_csv:
                if row[4] == 'Cases':
                    cases.append(float(row[5]))
                    break
    return cases

def plot_data(dates):
    cases = read_data(dates)
    case_x = np.arange(len(cases))
    plt.bar(case_x, cases)
    plt.ylim(round((max(cases)*0.9)), round((max(cases)*1.01)))
    plt.xticks(case_x, dates)
    plt.legend(labels=['Total cases'], loc='best')
    plt.xlabel("Dates")
    plt.ylabel("Numbers of cases")
    plt.title("COVID-19 cases in Colorado")
    plt.show()

# Command line usage: python 25_nongraded_p2.py 2022-02-28 2022-03-31 2022-04-29
if __name__ == '__main__':
    plot_data(sys.argv[1:])
