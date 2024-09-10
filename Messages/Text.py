import board
import neopixel
import time


'''
hola
'''



class INFO:
    
      

    def __init__(self, pin, cintas, longitud):
        '''Inicializa la cinta'''
        self.Longitud = longitud 								# Longitud de cada cinta Led
        self.Numero = cintas									# Numero de cintas Leds
        self.LED_COUNT = longitud * cintas	                                                # Number of LED pixels.
        self.LED_PIN = pin 									# GPIO pin connected to the pixels (must support PWM!).
        self.LED_BRIGHTNESS = 0.5								# Set to 0.0 for darkest and 1.0 for brightest
        self.LED_AUTO = False
        self.LED_ORDER = neopixel.GRB
        self.strip = neopixel.NeoPixel(
                        self.LED_PIN, self.LED_COUNT, brightness = self.LED_BRIGHTNESS,
                        auto_write = self.LED_AUTO,pixel_order = self.LED_ORDER)
                

    def Clean(self):
        ''' Limpia la pantalla'''
        self.strip.fill((0,0,0))
        self.strip.show()

    def hex2bin(self, letra):
        '''Convierte Hex a Bin'''
        Letra = [[int(bit) for bit in format(hex_numero, '08b')] for hex_numero in letra]
        #print(Letra) #imprime la lista binaria
        return Letra      


    def print_letra(self, letra, pos):      
        '''Imprime letra 2 hex en la pantalla'''
		
                
        color = (255, 0, 0)
        for fila in range(len(letra)):
                for i in range(8):
                        if letra[fila][i] == 1:
                                if fila % 2 == 0:
                                        self.strip[self.Longitud * fila + i + pos*8] = color
                                else:
                                        self.strip[self.Longitud * (fila+1) - 1 - i - pos*8] = color
        self.strip.show()


    def Mensaje(self,mensaje):
        mensaje = list(mensaje)
        lista = [self.hex2bin(self.abc[caracter]) for caracter in mensaje]
        for i in range(len(lista)):
              if int(self.Longitud/8)>i:
                    self.print_letra(lista[i],i)

 


    abc = {
			# MAYUSCULAS
			"A": [0x3E,0x48,0x88,0x48,0x3E],
			"B": [0x6C,0x92,0x92,0x92,0xFE],
			"C": [0x44,0x82,0x82,0x82,0x7C],
			"D": [0x7C,0x82,0x82,0x82,0xFE],
			"E": [0x82,0x92,0x92,0x92,0xFE],
			"F": [0x80,0x90,0x90,0x90,0xFE],
			"G": [0xCE,0x8A,0x82,0x82,0x7C],
			"H":  [0xFE,0x10,0x10,0x10,0xFE],
			"I":  [0x82,0x82,0xFE,0x82,0x82],
			"J":  [0x80,0xFC,0x82,0x02,0x04],
			"K":  [0x82,0x44,0x28,0x10,0xFE],
			"L":  [0x02,0x02,0x02,0x02,0xFE],
			"M":  [0xFE,0x40,0x38,0x40,0xFE],
			"N":  [0xFE,0x08,0x10,0x20,0xFE],
			"Ñ":  [0xBE,0x84,0x88,0x90,0xBE],
			"O":  [0x7C,0x82,0x82,0x82,0x7C],
			"P":  [0x60,0x90,0x90,0x90,0xFE],
			"Q":  [0x7A,0x84,0x8A,0x82,0x7C],
			"R":  [0x62,0x94,0x98,0x90,0xFE],
			"S":  [0x4C,0x92,0x92,0x92,0x64],
			"T":  [0xC0,0x80,0xFE,0x80,0xC0],
			"U":  [0xFC,0x02,0x02,0x02,0xFC],
			"V":  [0xF8,0x04,0x02,0x04,0xF8],
			"W":  [0xFE,0x02,0x1C,0x02,0xFE],
			"X":  [0xC6,0x28,0x10,0x28,0xC6],
			"Y":  [0xC0,0x20,0x1E,0x20,0xC0],
			"Z":  [0xC2,0xB2,0x92,0x9A,0x86],

			# MINUSCULAS
			"a":  [0x02,0x1E,0x2A,0x2A,0x04],
			"b":  [0x1C,0x22,0x22,0x14,0xFE],
			"c":  [0x14,0x22,0x22,0x22,0x1C],
			"d":  [0xFE,0x14,0x22,0x22,0x1C],
			"e":  [0x18,0x2A,0x2A,0x2A,0x1C],
			"f":  [0x40,0x90,0x7E,0x10,0x00],
			"g":  [0x3C,0x72,0x4A,0x4A,0x30],
			"h":  [0x1E,0x20,0x20,0x10,0xFE],
			"i":  [0x00,0x02,0xBE,0x22,0x00],
			"j":  [0x00,0xBC,0x02,0x02,0x04],
			"k":  [0x00,0x22,0x14,0x08,0xFE],
			"l":  [0x00,0x02,0xFE,0x82,0x00],
			"m":  [0x3E,0x20,0x1E,0x20,0x3E],
			"n":  [0x1E,0x20,0x20,0x10,0x3E],
			"o":  [0x1C,0x22,0x22,0x22,0x1C],
			"p":  [0x30,0x48,0x48,0x30,0x7E],
			"q":  [0x7E,0x30,0x48,0x48,0x30],
			"r":  [0x10,0x20,0x20,0x10,0x3E],
			"s":  [0x24,0x2A,0x2A,0x2A,0x12],
			"t":  [0x24,0x12,0xFC,0x20,0x20],
			"u":  [0x3E,0x04,0x02,0x02,0x3C],
			"v":  [0x38,0x04,0x02,0x04,0x38],
			"w":  [0x3C,0x02,0x0C,0x02,0x3C],
			"x":  [0x22,0x14,0x08,0x14,0x22],
			"y":  [0x7C,0x12,0x12,0x12,0x64],
			"z":  [0x22,0x32,0x2A,0x26,0x22],
			
			# NUMEROS
			"0":  [0x7C,0xA2,0x92,0x8A,0x7C],
			"1":  [0x00,0x02,0xFE,0x42,0x00],
			"2":  [0x62,0x92,0x92,0x92,0x4E],
			"3":  [0xCC,0xB2,0x92,0x82,0x84],
			"4":  [0x08,0xFE,0x48,0x28,0x18],
			"5":  [0x9C,0xA2,0xA2,0xA2,0xE4],
			"6":  [0x8C,0x92,0x92,0x52,0x3C],
			"7":  [0xE0,0x90,0x88,0x84,0x82],
			"8":  [0x6C,0x92,0x92,0x92,0x6C],
			"9":  [0x78,0x94,0x92,0x92,0x62],

			# SIMBOLOS
			"=":  [0x28,0x28,0x28,0x28,0x28],
			"(":  [0x00,0x82,0x44,0x38,0x00],
			")":  [0x00,0x38,0x44,0x82,0x00],
			":":  [0x00,0x00,0x28,0x00,0x00],
			";":  [0x00,0x00,0x2C,0x02,0x00],
			" ":  [0x00,0x00,0x00,0x00,0x00],
			",":  [0x00,0x00,0x0C,0x02,0x00],
			"?":  [0x60,0x90,0x9A,0x80,0x40],
			".":  [0x00,0x0C,0x0C,0x00,0x00],
			"%":  [0x46,0x26,0x10,0xC8,0xC4],
			"/":  [0x04,0x08,0x10,0x20,0x40],
			"@":  [0x7E,0x81,0x8F,0x89,0x46], #Tipo 1
			#"@":  [0x72,0xB1,0xB1,0x81,0x7E], # Tipo 2
			"*":  [0x00,0x50,0xE0,0x50,0x00], #Tipo 1
			#"*":  [0x14,0x08,0x3E,0x08,0x14], # Tipo 2
			"$":  [0x44,0x4A,0xFF,0x4A,0x32],
			"!":  [0x00,0x00,0xFA,0x00,0x00],
			"#":  [0x44,0xFF,0x44,0xFF,0x44],
			"+":  [0x10,0x10,0x7C,0x10,0x10],
			"-":  [0x00,0x10,0x10,0x10,0x00],
			"_":  [0x01,0x01,0x01,0x01,0x01],
			
			# ESPECIALES

			# Unidades
			"\x80":  [0x22,0x41,0x22,0xDC,0xC0], # °C
			"\x81":  [0x00,0x00,0x00,0xC0,0xC0], # ° pequeño
			"\x82":  [0x00,0x00,0xE0,0xA0,0xE0], # ° grande
			"\x83":  [0x78,0x04,0x04,0x7F,0x00], # u letra griega
			
			# Simbolos
			"\x84":  [0x00,0x00,0x10,0x00,0x00], # Punto centro Pequeño
			"\x85":  [0x00,0x1C,0x1C,0x1C,0x00], # Punto centro Grande

			# Iconos
			"\x86":  [0x30,0x78,0x3C,0x78,0x30], # Corazón relleno
			"\x87":  [0x30,0x48,0x24,0x48,0x30], # Corazón blanco
			"\x88":  [0x38,0xE4,0x27,0xE4,0x38], # Conector
			"\x89":  [0x00,0x00,0xFF,0x00,0x00], # Cable	
			"\x90":  [0xFC,0x4C,0x20,0x1F,0x03], # Nota musical
			"\x91":  [0xFF,0x4F,0x4F,0x4F,0x7F], # Celular
			"\x92":  [0x08,0x78,0xFA,0x78,0x08], # Campana
			"\x93":  [0x08,0x44,0x14,0x44,0x08], # Cara feliz
			
			#Animaciones			
			"\x94":  [0x7C,0x3E,0x1E,0x3E,0x7C], # Pacman abierto
			"\x95":  [0x7C,0xFE,0xFE,0xFE,0x7C], # Pacman cerrado
			"\x96":  [0x7C,0xCF,0xFE,0xCF,0x7C], # Fantom1
			"\x97":  [0x7F,0xCC,0xFF,0xCC,0x7F], # Fantom2		
		}
    