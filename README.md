# PiRelay
Relay shield for Raspberry Pi to control upto 4 devices/appliances.



### Specifications 

* 4 - High quality Relay and loads up to 7A/240VAC or 10A/125VDC</li>
* LED’s for indicating status of each relay</li>
* Standardized shield shape and design</li>
* LED working status indicators for each relay</li>
* Raspberry Pi 4, 3, 2, and ZERO compatible 40-Pin Stacking Header</li>
<p></p>

**Steps for PiRelay software installation -**

1. Open Terminal and clone/download the repository by typing below command in terminal: 

   ```
   git clone https://github.com/sbcshop/PiRelay.git
   
   ```
   
2. Your code will be downloaded to '/home/pi' directory. Use 'ls' command to check the list of directories

3. 'Test.py' is example code for PiRelay. Run test file and play with PiRelay

### GPIO 4 Relay Not working Fix

1. Press Start button >> Preferences >> Raspberry Pi Configuration, Then click on Interfaces Tab and make sure 1-Wire is disabled. 
2. Click on OK button then reboot Raspberry pi.

<img src="https://github.com/sbcshop/PiRelay/blob/master/Images/Relay4Fix.PNG"/>


