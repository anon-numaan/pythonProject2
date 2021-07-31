import subprocess
import optparse
import re
print(""" _   _
| \ | |      _ __ ___   __ _  ___
|  \| |_____| '_ ` _ \ / _` |/ __|
| |\  |_____| | | | | | (_| | (__
|_| \_|     |_| |_| |_|\__,_|\___|

****** coded by anon-Numaan ******
*      *    *      *      *      *
***---website:https://darknet.org.in---***    

""")


def macchanger(interface,macaddress):

	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",macaddress])
	subprocess.call(["ifconfig",interface,"up"])

	print("[+] Changing Mac Address of Interface to",interface,macaddress)

def get_argument():

	parser=optparse.OptionParser()
	parser.add_option("-i","--interface",dest="interface",help="Interface to change the mac address")
	parser.add_option("-m","--mac",dest="new_mac",help="add new mac address")
	(options,arguments) = parser.parse_args()

	if not options.interface:
		parser.error("[-] Specify an Interface use python N_mac.py --help for more details")
	elif not options.new_mac:
		parser.error("[-] Specify an MacAddress use python N_mac.py --help for more details")

	return options

def getmac(interface):

	ifconfig_result = subprocess.check_output(["ifconfig",interface])
	current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)

	if current_mac:
		return current_mac.group(0)
	else:
		return None

options= get_argument()

macchanger(options.interface,options.new_mac)

final_mac = getmac(options.interface)

if final_mac == options.new_mac :
	print("[+]Mac Address Successfully Chaged with new mac ",final_mac)
else:
	print("Error Occured Fix It")