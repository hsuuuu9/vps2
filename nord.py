
from nordvpn_switcher import initialize_VPN,rotate_VPN,terminate_VPN
import time 

instructions = initialize_VPN(area_input=['Japan'])
time.sleep(3)
rotate_VPN(instructions)
time.sleep(3)
terminate_VPN(instructions)
