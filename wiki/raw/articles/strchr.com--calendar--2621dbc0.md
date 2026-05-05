---
title: "Calculating day of week and Easter date"
url: "http://www.strchr.com/calendar"
fetched_at: 2026-05-05T07:01:15.921568+00:00
source: "Peter Kankowski (strchr)"
tags: [blog, raw]
---

# Calculating day of week and Easter date

Source: http://www.strchr.com/calendar

Day of week
Given day, month, and year, this function finds the corresponding day of week. The days of week are encoded as the follows:
Sunday = 0
Monday = 1
Tuesday = 2
...
Saturday = 6
Let's calculate the number of days passed since some Sunday modulo seven. For example, 31 December 2000 was Sunday. If you can find the number of days from 31 December 2000 to the current date and divide it by seven, then the remainder will be equal to the current day of week.
For example, there are 15 days between 31 December 2000 and 15 January 2001. 15 mod 7 = 1, so 15 January 2001 is Monday. Intuitively, 15 days are two full weeks and one extra day. So if the starting date is Sunday, you can throw away the full weeks (take the remainder) and get the day of week.
365 mod 7 = 1, so
each non-leap year adds a one-day shift
. For example, 1 January 2013 was Tuesday, 1 January 2014 was Wednesday, and 1 January 2015 was Thursday. You must also add one leap day for each four years. In Gregorian calendar, the years divisible by 100 are non-leap except when they are also divisible by 400 (e.g., 1900 is non-leap and 2000 is a leap year). So you subtract one day for each 100 years and add one day for each 400 years.
Months are the most complex part because their lengths form an irregular pattern of 30 and 31 days. Moreover, February is one day longer in leap years. The function subtracts one from the year if the month is January or February, so effectively it views January and February as a part of the previous year. So
the year starts from 1 March.
This trick simplifies the calculation because the leap day is now inserted to the end of the year.
By coincidence, 29 February 1 BC was Sunday, so you can use it as a convenient starting date instead of 31 December 2000. You don't have to subtract 2000 in this case. In real life, AD 4 and 1 BC
were non-leap years,
so our formula will not work for the years before AD 5. However,
the modern seven-day week
was uncommon until the 4th century, so it does not make sense to extend our function to such dates.
The function could
sum the lengths of all months before the current one,
but it's possible to pre-calculate these values and put them into an array. Here is a short Python script to generate the array:
a = [31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 28]
for i in range(len(a)):
    print( sum(a[0:i+1]) % 7, end = ', ' )
Another solution I found in
C Snippets
involves a condition and a formula:
if (month < 3) {
    month += 12;
    year--;
}
day_of_week = ( 26 * (month + 1) / 10 ) % 7 + ...
I prefer an array here because one load from memory can be faster than a multiplication and a division by constant.
typedef enum {
    CALENDAR_JULIAN = 0,
    CALENDAR_GREGORIAN = 1
} CALENDAR_TYPE;

unsigned
dayofweek
(unsigned year, unsigned month, unsigned day, CALENDAR_TYPE type) {
    static const unsigned char month_shifts[] = {0, 5, 1, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2};
    
    year -= month <= 2;
    
    unsigned dow = year + year / 4 + month_shifts[month] + day;
    
    unsigned century = year / 100;

    dow -= (century - century / 4 - 2) & (type != CALENDAR_JULIAN ? -1 : 0);
    
    return dow % 7;
}
GCC, MSVC, and clang generate
branchless x86 code
for this function. You can rewrite it to use branches:
static const unsigned char month_shifts[] = {0, 5, 1, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2};
    
    if (month <= 2)
        year--;
    
    unsigned dow = year + year / 4 + month_shifts[month] + day;

    if (type == CALENDAR_GREGORIAN) {
        unsigned century = year / 100;
        dow -= century - century / 4 - 2;
    }
    
    return dow % 7;
However, this code will be slower because of the hard-to-predict branch depending on month. Gregorian calendar is used in most cases, so you can calculate the shift between Julian and Gregorian calendars (century — century / 4 — 2) and apply it only for Gregorian calendar. Always calculating the shift will usually be faster than checking if you should calculate it.
Easter
Here is my implementation of
Gauss algorithm
for calculating the date of Easter.
For Western churches, use EASTER_WESTERN after the transition to Gregorian calendar (which occurred
between 1582 and 1752 in most European countries
) and EASTER_JULIAN before the transition. For Orthodox churches (Greece, Russia, Serbia, Georgia, etc.), use EASTER_ORTHODOX after the transition and EASTER_JULIAN before the transition. For example, Denmark changed to the Gregorian calendar in 1700, so you should use EASTER_JULIAN before 1700 and EASTER_WESTERN since 1700.
#define MAKE_DATE(month, day) (((unsigned)(day) << 8) | (unsigned)(month))
#define GET_DAY(date) ((unsigned)(date) >> 8)
#define GET_MONTH(date) ((unsigned)(date) & 0xFF)

typedef enum {
    EASTER_WESTERN, // Catholic and protestant churches
    EASTER_ORTHODOX, // Orthodox church
    EASTER_JULIAN // Before the transition to Gregorian calendar
} EASTER_TYPE;

unsigned
easter
(unsigned year, EASTER_TYPE type) {
    // Gauss algorithm implementation

    // Calculate the difference between Julian and Gregorian calendars for the given year
    unsigned century = year / 100;
    unsigned gregorian_shift = century - century / 4 - 2;
    
    unsigned x = 15, y = 6;
    
    // Metonic cycle correction
    x += (2 - (13 + 8 * century) / 25 + gregorian_shift) & (type == EASTER_WESTERN ? -1 : 0);
    y += gregorian_shift & (type == EASTER_WESTERN ? -1 : 0);
    
    // The core formula
    unsigned g = year % 19;
    unsigned d = (g * 19 + x) % 30; // Paschal Full Moon
    unsigned e = (2 * (year % 4) + 4 * year - d + y) % 7; // Sunday after PFM
    
    unsigned day = d + e;

    // Correction for the length of the moon month
    day -= (e == 6) & ( (d == 29) | ((d == 28) & (g > 10)) ) ? 7 : 0;
    
    // Convert Orthodox Easter to Grigorian calendar
    day += gregorian_shift & (type == EASTER_ORTHODOX ? -1 : 0);
    
    // Calculate month and day
    int is_may = (day >= 40);
    int is_not_march = (day >= 10);

    unsigned month = 3 + is_not_march + is_may;
    day += 22 - (is_not_march ? 31 : 0) - (is_may ? 30 : 0);

    return MAKE_DATE( month, day );
}
The function is compiled to branchless code by MSVC and clang. GCC still inserts a couple of branches.
Jewish holidays
Gauss also devised
a formula for the date of Pesach (Passover).
The formula can be easily adapted to other holidays. I used Rosh Hashanah (Jewish New Year) as a reference point and translated all calculations from floating point to 32-bit integers:
unsigned
roshhashanah
(unsigned year, CALENDAR_TYPE type) {
    assert(sizeof(unsigned) >= 4); // 32-bit integer type is required
    
    unsigned r = (12 * year + 12) % 19;

    // Calculate the number of parts (Talmudic units)
    int parts = 765433 * r - 1565 * year - 445405 + 123120 * (year % 4);
    
    // Take into account the difference between Gregorian and Julian calendars
    unsigned century = year / 100;
    unsigned gregorian_shift = (century - century / 4 - 2) & (type != CALENDAR_JULIAN ? -1 : 0);
    
    parts -= parts <= 0 ? 492479 : 0; // Floored division
    
    int day = parts / 492480 + gregorian_shift;
    
    parts %= 492480;
    
    // Postponement rules
    unsigned dow = (year + year / 4 - gregorian_shift + day + 2) % 7;
    
    day += (dow == 0) | (dow == 3) | (dow == 5);

    day += (dow == 1) & (parts >= 442111) & (r > 11);
    
    day += 2 * ((dow == 2) & (parts >= 311676) & (r > 6));
    
    // Calculate month and day
    int is_october = (day > 30);
    int is_not_august = (day > 0);
    
    unsigned month = 8 + is_not_august + is_october;
    
    day += is_not_august ? 0 : 31;
    day -= is_october ? 30 : 0;
    
    return MAKE_DATE(month, day);
}
GCC, MSVC, and clang generate branchless code for this function.
Download the code (zip archive, 2 KB)
Recommended reading
