import datetime
import calendar

def count(y, m, d):
    day_count = 0
    wlist = calendar.monthcalendar(int(y), int(m))
    for i in wlist:
        print(i)
        if i[int(d)] != 0:
                day_count = day_count + 1
    return day_count

def main():
    for i in range(0,7):
        print(str(i)+ ": " + calendar.day_name[i])
    d = input("Which day of the week do you want to count? ")
    while d.isnumeric() == False or (int(d) < 0 or int(d) > 6):
        print("\nERROR: Day is invalid. Please try again")
        d = input("Which day of the week do you want to count? ")

    y = input("\nPlease enter the year: ")
    while y.isnumeric() == False:
        print("\nERROR: Year is invalid.  Please try again")
        y = input("Please enter the year: ")

    print()
    for i in range(1,13):
        print(str(i)+ ": " + calendar.month_name[i])
    m = input("Which month would you like? ")
    while m.isnumeric() == False or (int(m) < 1 or int(m) > 12):
        print("\nERROR: Month is invalid. Please try again")
        m = input("Which month would you like? ")

    #https://stackoverflow.com/questions/12973691/count-number-of-sundays-in-current-month
    # day_count = len([1 for i in calendar.monthcalendar(int(y),
    #                               int(m)) if i[int(d)] != 0])

    day_count = count(y, m, d)                              
    print("\nThere are " + str(day_count) , str(calendar.day_name[int(d)]) \
         + "'s in" , str(calendar.month_name[int(m)]) , str(y))

if __name__ == "__main__":
    main()