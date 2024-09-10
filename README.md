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

Using the OpenCV python library and the developed board it is possible to program effects that can be used to create lighting effects. Starting from viewing the image as 3 arrays of the RGB components. 

The process performed is to resize the image to the amount of pixels available (the more pixels the better the quality of the effects) and then slide each of the columns at a desired speed, generating a left slice of the image on the LED strip and generating different lighting effects.

![image](https://github.com/user-attachments/assets/b9785f6f-e027-4f1c-bf1d-9c6f60738f2d)

if you use a translucent body you can soften the illumination making the effect more pleasing to the eye.

---

### Second Application: LED Strip Messages

This library works to display messages on a screen made with WS2815 LED strips. References to LED strips that can be drawn LED by LED by connecting them in a serpentine pattern:

1 --->--->--->--->--->
2 <---<---<---<---<---
3 --->--->--->--->--->
4 <---<---<---<---<---
5 --->--->--->--->--->

For now, it only works with a font resolution of 8 in height x 5 in width (5 strips wide), and the view of the letters is vertical. To import the library, use:

`import Text`

To initialize, use:

`Text.INFO(pin, strips, length)`

Where:

* pin: the pin where the message will be displayed. This is designed for Raspberry Pi and uses the board library. The pin must be PWM.
* strips: the number of strips that are placed in width. For now, it's designed only for 5 lines.
* length: the length of the strip: the size of the strip you are using.

Example: 

`Text.INFO(board.D12, 5, 60)`

Methods:
* Clear(): Clears the screen.
* Mensaje(message): Displays a message on the screen. message must be a string, e.g.: "HELLO WORLD".

Additional required libraries:
`import neopixel`

Test:
The following image shows what appears on the screen when the method Mensaje is called with the string "HOLA":

 `Pan1.Mensaje("HOLA")`

![image](https://github.com/user-attachments/assets/86e93dec-50aa-4fcc-9b12-d73bee31f1e7)

 
