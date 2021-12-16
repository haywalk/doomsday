# Conway's Doomsday Algorithm

This is a little program I wrote that takes in a date in ISO 8601 format (YYYY-MM-DD) and
prints out the day of the week on that date.

It uses John Horton Conway's [Doomsday rule](https://en.wikipedia.org/wiki/Doomsday_rule)
to find the day of the week, by first calculating the 'anchor day' for the given century,
then that of the given year, then finding the given day's offset from the first doomsday of
the month, which is its offset from the year's anchor day.

This program is written in Python 3.9. It is licensed under the
[GNU GPL, version 3](https://www.gnu.org/licenses/gpl-3.0.en.html). It was
written by Hayden Walker ([www.haywalk.ca](https://www.haywalk.ca/)) on 2021-12-15. 
