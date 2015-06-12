
#include <avr/io.h>
#include <stdio.h>
#include <avr/sleep.h>
#include <avr/interrupt.h>
#include <avr/cpufunc.h>

#include "Usart.h"
#include "Twi.h"
#include "Adc.h"
#include "Timer.h"
#include "Leda.h"
 

static inline uint8_t setup_DS1631(void);

static inline uint8_t pollDS1631(void);
static inline uint8_t readDS1631(void);

static inline uint8_t pollHIH8120(void);
static inline uint8_t readHIH8120(void);

static inline void readMPX5100(void);
static inline void readMPXV4115V(void);


static inline uint8_t read1ByteI2C(const uint8_t, const uint8_t, uint8_t *);
static inline uint8_t write1ByteI2C(const uint8_t, const uint8_t, uint8_t);
static inline void signExtend12to16(uint16_t *);


// 7
static uint16_t dataDS1631 = 0;
// 6
static uint16_t dataMPX5100 = 0;
// 5
static uint16_t dataMPXV4115V = 0;
// 4
static uint8_t dataHIH8120h = 0;
// 3
static uint8_t dataHIH8120t = 0;
// 2, don't care.
// 1, don't care.
//0
volatile uint8_t sensorStatus = 0;

static FILE leda_stdout = FDEV_SETUP_STREAM(usart_putchar, NULL,_FDEV_SETUP_WRITE);



void leda_setup(void)
{
    // Setup avr.
    setup_usart();
    setup_twi();
    setup_adc();
    
    stdout = &leda_stdout;
    
    set_sleep_mode(SLEEP_MODE_IDLE);
    
    
    sensorStatus = 0xFF;
    
    // Setup sensors.
    if(setup_DS1631() != 0)
        // Clear the sensor status bit for DS1631 if it fails setup.
        sensorStatus &= (uint8_t)~(_BV(7));
        
    PORTB &= (uint8_t)~(_BV(PB5));

} // End of leda_setup()


void leda_pollAll(void)
{

    // start time.
    timer0_start();
    
    // Start DS1631.
    // Needs 750ms.
    // Make measurement request
    if(sensorStatus & _BV(7))
        if(pollDS1631() != 0)
            // Disable the sensor if it fails.
            sensorStatus &= (uint8_t)~(_BV(7));
            
    // Start HIH
    // Needs 37ms.
    // Make measurement request
    if(sensorStatus & (_BV(4) | _BV(3)))
        if(pollHIH8120() != 0) 
            // Disable the sensor if it fails.
            sensorStatus &= (uint8_t)~(_BV(4) | _BV(3));

    
    // There is no way to test if the MPX* sensors failed.
    // Read MPX5100AP.
    readMPX5100();    
    // Read MPXV4115VC6U.
    readMPXV4115V();

    // Read HIH.
    if(sensorStatus & (_BV(4) | _BV(3)))
    {
        // If time is greater than 37ms. 
        // Read HIH.
        while(getCount0() < (uint16_t)37);
        
        if(readHIH8120() != 0)
            // Disable the sensor if it fails.
            sensorStatus &= (uint8_t)~(_BV(4) | _BV(3));
            
    } else {
        dataHIH8120h = 0;
        dataHIH8120t = 0;
    }
    
    //Read DS1631.
    if(sensorStatus & _BV(7))
    {
        // If time is greater than 750ms. 
        // Read DS1631.
        while(getCount0() < (uint16_t)750);
        
        if(readDS1631() != 0)
            // Disable the sensor if it fails.
            sensorStatus &= (uint8_t)~(_BV(7));
            
    } else 
        dataDS1631 = 0;
        
    // stop time.
    timer0_stop();
    
} // End of leda_pollAll().

void leda_getAll(void)
{
    uint8_t xor_sum = 0;
    uint8_t * arr = 0;
    
    // Send sensor status.
    printf("%02X", sensorStatus);
    xor_sum ^= sensorStatus;
    
    // Temperature Sensor.
    printf("%04X", dataDS1631);
    arr = (uint8_t *)&dataDS1631;
    xor_sum ^= arr[1] ^ arr[0];
    
    // Pressure Sensors.
    printf("%04X",dataMPX5100);
    arr = (uint8_t *)&dataMPX5100;
    xor_sum ^= arr[1] ^ arr[0];
    
    printf("%04X", dataMPXV4115V);
    arr = (uint8_t *)&dataMPXV4115V;
    xor_sum ^= arr[1] ^ arr[0];
    
    // Humidity Sensor.
    printf("%04X", dataHIH8120h);
    arr = (uint8_t *)&dataHIH8120h;
    xor_sum ^= arr[1] ^ arr[0];
    
    // Temperature Sensor.
    printf("%04X", dataHIH8120t);
    arr = (uint8_t *)&dataHIH8120t;
    xor_sum ^= arr[1] ^ arr[0];
    
    // Write out the checksum.
    printf("%02X", xor_sum);
    
} // End of leda_getAll().




static inline uint8_t setup_DS1631(void)
{
    // make sure that the DS1631 is running 12bit 1SHOT mode.
    uint8_t data = 0;
    uint8_t c = 0;
    
    c = read1ByteI2C(DS1631_I2C_ADDR, 0xAC, &data);
    
    // Test for 12bit and 1SHOT mode. 
    if(!c && data != 0x0D)
        return write1ByteI2C(DS1631_I2C_ADDR, 0xAC, 0x0D);
        
    return 0;
    
} // End of setup_DS1631().

static inline uint8_t pollDS1631(void)
{
    uint8_t c = 0;
    
    c = twi_start();
    c = c || twi_write(DS1631_I2C_ADDR | TW_WRITE);
    c = c || twi_write(0x51);
    twi_stop();
    
    return c;
    
} // End of pollDS1631().

/* ---- Temperature Sensor ---- */
static inline uint8_t readDS1631(void)
{
    uint8_t c = 0;
    uint8_t dataL = 0;
    uint8_t dataH = 0;
    
    c = twi_start();
    c = c ||twi_write(DS1631_I2C_ADDR | TW_WRITE);
    c = c || twi_write(0xAA); // send read temp cmd.
    c = c || twi_start(); // bus restart
    c = c || twi_write(DS1631_I2C_ADDR | TW_READ);
    c = c || twi_readAck(&dataH);
    c = c || twi_readNack(&dataL);
    twi_stop();
    
    if(!c) {
        
        dataDS1631 = (dataH << 8) | dataL;
        signExtend12to16(&dataDS1631);
        return 0;
        
    } else {
        dataDS1631 = 0;
        return 1;
    }
    
} // End of readDS1631().




static inline uint8_t pollHIH8120(void)
{
    uint8_t c = 0;
        
    // Make measurement request
    c = twi_start();
    c = c || twi_write(HIH8120_12C_ADDR | TW_WRITE);
    twi_stop(); // Free the bus.
    
    // Block for 36.65 ms. 
    return c;
    
} // End of pollHIH8120().


static inline uint8_t readHIH8120(void)
{
    uint8_t data[4];
    uint8_t c = 1;
    
    // Skip the reading of the status of the IC.
    /*
    // Wait until the data is ready.
    do 
    {
		twi_start(); 
		twi_write(HIH8120_12C_ADDR | TWI_READ);
		twi_readNack(data[0]); // What is happeing here?? 
		twi_readNack(data[0]);
    
	} while((data[0] & 0xC0) != 0);
	*/
	
	c = twi_start(); 
	c = c || twi_write(HIH8120_12C_ADDR | TW_READ);
	c = c || twi_readAck(data);
	c = c || twi_readAck(data + 1);
	c = c || twi_readAck(data + 2);
	c = c || twi_readNack(data + 3);
	twi_stop();
	
	// Update the Humidity
    if(!c)
    {
        dataHIH8120h = (data[0] << 8) | (data[1]);
        dataHIH8120h &= 0x3FFF;
        
        // Update the Temperature. 
        dataHIH8120t = (data[2] << 8) | (data[3]);
        dataHIH8120t = (dataHIH8120t >> 2) & 0x3FFF;
        return 0;
    
    } else {
        
        dataHIH8120h = 0;
        dataHIH8120t = 0;
        return 1;
    }

} // End of readHIH8120().



static inline void readMPX5100(void)
{
	adc_read(MPX5100_ADC_CH);
	dataMPX5100 = ADC;
}

static inline void readMPXV4115V(void)
{
	adc_read(MPXV4115V_ADC_CH);
	dataMPXV4115V = ADC;
}

// This is for the DS1631.
static inline uint8_t read1ByteI2C(const uint8_t addr, const uint8_t reg, uint8_t * data)
{
    uint8_t c = 0;
    
    c = twi_start();
    c = c || twi_write(addr | TW_WRITE);
    c = c || twi_write(reg);
    c = c || twi_start(); // reset bus.
    c = c || twi_write(addr | TW_READ);
    c = c || twi_readNack(data);
    c = c || twi_stop();
    
    return c;
    
} // End of read1ByteI2C().

// This is for the DS1631.
static inline uint8_t write1ByteI2C(const uint8_t addr, const uint8_t reg, uint8_t data)
{
    uint8_t c = 0;

    c = twi_start();
    c = c || twi_write(addr | TW_WRITE);
    c = c || twi_write(reg);
    c = c || twi_write(data);
    twi_stop();
    
    return c; 

} // End of write1ByteI2C().

static inline void signExtend12to16(uint16_t *n)
{
    *n <<= 4;
    *n >>= 4;
    
} // End of signExtend12to16().
