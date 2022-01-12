/*
 * doomsday.c
 * 
 * Copyright 2021 Hayden D. Walker <planethaywalk@aol.com>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 *
 * Conway's Doomsday Rule
 *
 * Given a date in the Gregorian calendar, (YYYY-MM-DD), calculate the day
 * of the week using John Horton Conway's Doomsday Algorithm.
 *
 * Program by Hayden Walker (www.haywalk.ca)
 * Written 2022-01-11
 *
 */

#include <stdio.h>

int main()
{
	/* get date from user */
	int year, month, day;
	scanf("%d-%d-%d", &year, &month, &day);
	
	/* calculate century anchor day */
	int century, century_anchor;
	century = year / 100;
	century_anchor = (5 * (century % 4) % 7 + 2) % 7 - 1;
	
	/* calculate year's anchor day */
	int a, b, c, d, year_anchor;
	a = (year % 100) / 12;
	b = (year % 100) % 12;
	c = b / 4;
	d = a + b + c;
	year_anchor = (century_anchor + d) % 7;
	
	/* doomsdays for each month in normal and leap years */
	int non_leap[] = {3, 7, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5};
	int leap[] = {4, 1, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5};
	
	/* get nearest doomsday based on month and leap year */
	int nearest_doomsday;
	
	if(year % 4 == 0 && (year % 100 != 0 || year % 400 == 0))
		nearest_doomsday = leap[month - 1];
	else
		nearest_doomsday = non_leap[month - 1];
	
	/* get distance from doomsday */
	int this_day;
	this_day = (year_anchor + (day - nearest_doomsday)) % 7;
	
	/* get name of day */
	char days[7][10] = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday", "Sunday"};
	
	/* output result and end program */
	printf("%s\n", days[this_day]);
	return 0;
}