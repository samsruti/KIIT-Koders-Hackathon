#!/usr/bin/env python
# -*- coding: utf-8 -*-
# KIIT Koder Hackathon
# Copyright (C) 2016 
# Soumya Pal <soumyapal97@gmail.com>
# Ranadip Roy <ranadiproy0722@gmail.com>
# Ayush Mishra <samkumar004@gmail.com>
# Samsruti Dash <sam.sipun@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
def fibonacci(n):
	a = 0
	b = 1
	series = [0]
	series.append(a)
	for i in xrange(2,n+1):
		temp = a + b
		b = a
		a = temp
		series.append(temp)
	return series

# cauldron = []
# for i in range(2):
# 	sub_cauldron = []
# 	for j in range(2):
# 		val = 0
# 		# val = raw_input("Enter the Value for : [" + str(i)+','+	str(j) + "]: ")
# 		sub_cauldron.append(val)
# 	cauldron.append(sub_cauldron)
series= fibonacci(25)

for ingredient in range(25):
	print "\ningredient: ",ingredient
	n = float(series[ingredient])
	print int(n),": "
	# print type(series[ingredient])
	first_cell = n
	second_cell = n/2.0
	third_cell = pow((n/2.0),3)
	fourth_cell =  n * n/2.0 * pow((n/2.0),3)
	# print first_cell, second_cell , third_cell, fourth_cell
	# cauldron[0][0] = first_cell
	# cauldron[0][1] = second_cell
	# cauldron[1][0] = third_cell
	# cauldron[1][1] = fourth_cell
	total_value = first_cell + second_cell + third_cell + fourth_cell
	print "Sum: ",total_value
	if total_value == 2844678:
		print "ingredient number: ", ingredient

		
