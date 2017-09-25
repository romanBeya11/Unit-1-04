'''
Created By: Roman Beya
Created For: ICS3U
Created On: 25-Sep-2017
This program calculates the circumference of a circle based on a radius input by a user
'''

import ui

# constant value: pi
PI = 3.141592653

def calculate_circumference_on_touch_up_on_inside(sender):
	# input
	radius = float(view['radius_textfield'].text)
	# process
	circumference = PI * radius ** 2
	# output
	view['circumference_label'].text = "The circumference of a circle with a radius of {0} is: {1}!".format(radius, circumference)
view = ui.load_view()
view.present('sheet')
