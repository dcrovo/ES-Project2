#include <bcm2835.h>
#include <stdio.h>



#define LED_1 RPI_V2_GPIO_P1_36 // Define el pin 36




int main()
{	
	if (!bcm2835_init())
      		return 1;
	bcm2835_gpio_fsel(LED_1, BCM2835_GPIO_FSEL_OUTP); // configura el pin como salida
;

	while(1)
	{
		
		bcm2835_gpio_write(LED_1, HIGH);
		bcm2835_delayMicroseconds(2.5); // Espera 2.5 us para una frecuencia de 200KHz, solo para probar con LED

		bcm2835_gpio_write(LED_1,LOW);
		bcm2835_delayMicroseconds(2.5);// Espera 2.5 us para una frecuencia de 200KHz, solo para probar con LED
		

	}
	return 0;
}

/*
 * For compilation run 
 * gcc -o p2 programa2.c -l bcm2835
 * */
