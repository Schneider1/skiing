from time import sleep


def set_power(power):
	print "Setting power to %.2f dBm"%power
	
def set_frequency(frequency):
	print "Setting frequency to %.6e Hz"%frequency
	
def get_all():
	get_frequency()
	get_power()
	while True:
		if get_status():
			break
		sleep(.5) #wait until the mw source is ready
		
def get_status():
	return False #*STB? does not work for this device, just a quick fix...
	
	if vinstrument.ask("*STB?")=="0"
		return True
	else:
		return False
		