# Led Controller with Raspberry-Pi

The Raspberry Pi, a super versatile and affordable mini-computer, unlocks endless possibilities for controlling LED systems, from simple on/off switches to creating advanced animations and patterns. By combining the flexibility of the Raspberry Pi with the power and brightness of LED strips, you can build custom lighting setups, interactive displays, or even home automation projects.

To connect an LED strip we can make use of the GPIO outputs of the raspberry, especially those that offer PWM signals, because they are the appropriate ones to feed the LED strip. 

LED strips have 3 main pins: V+ normally 5V or 12V. GND (ground) and Data pin to control the LEDs. 

Now, the outputs of the raspberry Pi pins are 3.3V. In the case of the LED strips, the references I use are 12 V. So it is first necessary to develop a board that allows:

* Convert the 12 V to 5V to power the raspberry PI and use a single power supply for the Raspberry PI and the LED strips.
* Convert the high frequency PWM signal sent by the raspberry from 3.3V to 5V to control the LED strips.
* Add an RTC for time and date functionality in case the raspberry is not connected to the Internet. (could be optional)

First Ouput: a PCB taking advance of the RPI socket with these three funcionalities.

![image](https://github.com/user-attachments/assets/90a6e174-1a30-4b19-a55f-9525031529ef)

---

### First Application: LED Column
