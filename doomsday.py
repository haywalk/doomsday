'''
doomsday.py

Copyright 2021 Hayden D. Walker <planethaywalk@aol.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Conway's Doomsday Rule

Given a date in the Gregorian calendar, (YYYY-MM-DD), calculate the day
of the week using John Horton Conway's Doomsday Algorithm.

Program by Hayden Walker (www.haywalk.ca)
Written 2021-12-15
'''

def is_leap_year(year):
	'''
	Check if a year is a leap year
	'''
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_century_anchor(year):
	'''
	Return the century anchor day for a given year
	'''
	# Get century from year
	century = year // 100
	
	# Calculate and return anchor day
	century_anchor_day = (5 * (century % 4) % 7 + 2) % 7 - 1
	return century_anchor_day

def get_year_anchor(year):
	'''
	Return the anchor day for a given year
	'''
	# Get the century anchor day
	century_anchor = get_century_anchor(year)
	
	# Get the last digits of the year
	last_digits = year % 100
	
	# Calculate offset from century anchor day
	a = last_digits // 12
	b = last_digits % 12
	c = b // 4
	century_offset = a + b + c
	
	# Calculate and return the year anchor day
	year_anchor = (century_anchor + century_offset) % 7
	return year_anchor

def get_day_number(year, month, day):
	'''
	Return the day of the week (0-6) for a given date
	'''
	# First doomsdays of each month for a common year
	doomsdays_common = {1:3, 2:7, 3:7, 4:4, 5:2, 6:6, 7:4, 8:1,
		9:5, 10:3, 11:7, 12:5}

	# First doomsdays of each month for a leap year
	doomsdays_leap = {1:4, 2:1, 3:7, 4:4, 5:2, 6:6, 7:4, 8:1,
		9:5, 10:3, 11:7, 12:5}

	# Get first doomsday for this month
	if is_leap_year(year):
		this_dd = doomsdays_leap[month]
	else:
		this_dd = doomsdays_common[month]

	# Get the year anchor
	year_anchor = get_year_anchor(year)
	
	# Calculate and return the day of the week based on distance from
	# the first doomsday of the month
	this_day = (year_anchor + (day - this_dd)) % 7
	return this_day

def get_day(year, month, day):
	'''
	For a given date, return the name of the day of the week
	'''
	# Get the day number
	day_number = get_day_number(year, month, day)
	
	# Days of the week
	days = ['Monday', 'Tuesday', 'Wednesday',
		'Thursday', 'Friday', 'Saturday', 'Sunday']
	
	return days[day_number]

# Get input from user
user_input = input().split('-')

# Get year, month, and day from input
year = int(user_input[0])
month = int(user_input[1])
day = int(user_input[2])

# Calculate day of the week
weekday = get_day(year, month, day)

# Print out result
print(weekday)
