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

def decipher(encrypted):
	count = 1;
	decrypted = ""
	for i in encrypted:
		# print count," : ",i
		if i == ' ':
			# print "space"
			decrypted = decrypted + ''.join(" ")
			count = count - 1
		else:
			valueAtIndex = ord(i) - count
			if valueAtIndex < 65:
				pos = ord(i) - 65 + 1
				res = count - pos 
				valueAtIndex = ord('Z') - res
			decrypted = decrypted + ''.join(chr(valueAtIndex))
		count = count + 1
	return decrypted


string = decipher("SPRA CYBJ FV HZLFSSOAQU")
print string
