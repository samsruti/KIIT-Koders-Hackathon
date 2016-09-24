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

def find():
	pos = 1
	for i in xrange(0,667):
		if pos > 0 and pos < 9:
			flag = 1
		else:
			flag =0
		if pos == 6:
			flag = 0
		if flag == 0:
			pos = pos - 3
		else:
			pos = pos + 2

	return pos

final_pos = find()
print "Final Position: ", final_pos
