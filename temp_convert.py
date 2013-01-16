"""
This is a small program to convert temperature degrees between different types.
Created by Songhua Liu
"""
def all_to_kelvin(x,y):
    a = ["","","","","","","",""]      # declare an empty list
    a[0] = x                		# kelvin to kelvin
    a[1] = x + 273.15       		# celsius to kelvin
    a[2] = ( x + 459.67) * 5 /9 	# Fahrenheit to kelvin
    a[3] = x * 5.0 / 9.0 		# Rankine to kelvin
    a[4] = 373.15 - x * 2 / 3 		# delisle to kelvin
    a[5] = x * 100 / 33 + 273.15 	# newton to kelvin
    a[6] = x * 5 / 4 + 273.15 		# Reaumur to kelvin
    a[7] = ( x - 7.5 ) * 40 / 21 + 273.15 #Romer to kelvin
    return a[(y-1)]
    
    
def kelvin_to_all(x,y):
    b = ["","","","","","","",""]       # declare an empty list
    b[0] = x 				 # kelvin to kelvin
    b[1] = x - 273.15 			 # kelvin to celsius
    b[2] = x * 9 / 5 - 459.67 		 # kelvin to fahrenheit
    b[3] = x * 9 / 5.0 			 # kelvin to Rankine
    b[4] = ( 373.15 - x ) * 3 /2 	 # kelvin to delisle
    b[5] = ( x - 273.15 ) * 33 /100 	 # kelvin to newton
    b[6] = ( x - 273.15) * 4 / 5 	 # kelvin to reaumur
    b[7] = ( x - 273.15) * 21/ 40 + 7.5 # kelvin to Romer
    return b[(y-1)]

temp_list = """1.Kelvin
2.Celsius
3.Fahrenheit
4.Rankine
5.Delisle
6.Newton
7.Reaumur
8.Romer
"""
name_list = "Kelvin Celsius Fahrenheit Rankine Delisle Newton Reaumur Romer".split()

print "Please choose the number before the current temperature type\n"
chosen =int( raw_input(temp_list) )              		#get current temp type

degrees = float( raw_input("Please input the degrees:\n") ) 	# get current degrees

print "Please choose the temperature you want to convert to:\n"
convert = int( raw_input(temp_list) )				#get the convert target temp type

print "%f %s degree(s) is equal to %3f %s degree(s)" % (degrees, name_list[(chosen-1)] , kelvin_to_all( all_to_kelvin(degrees, chosen ), convert ), name_list[(convert-1)] )