/*
 * WDT reset is not working. It just keeps restarting.
 */

#include <avr/io.h>
#include <stdio.h>
#include <avr/sleep.h>
#include <avr/interrupt.h>
#include <avr/wdt.h>

#include "Usart.h"
#include "Leda.h"
#include "Timer.h"



static inline void handleCmd(void);
static inline void enterSleep(void);
static inline void sendEndLine(void);
static inline void sendAck(void);

void main(void)
{
    
    leda_setup();
    sei();
    
    printf("LEDA");
    sendEndLine();
    
    for(;;)
    {
        enterSleep();
        
        while(usart_isData())
        handleCmd();
        
    } // End of forever loop.
    
} // End of main().


static inline void handleCmd(void)
{
    static uint8_t dataBuf[8];
    static uint8_t index = 0;
    
    uint8_t data = 0;
    
    data = usart_readData();
    switch(data)
    {
        case 'S':
        case 's':
        case 'R':
        case 'r':
        case 'W':
        case 'w':
            index = 0;
            dataBuf[index] = data;
            ++index;
            break;
        
        case '\n':
            dataBuf[index] = data;
            ++index;
            break;
                
        default:
            index = 0;
            break;
    }
    
    // If the CMD is too big, then reject the CMD and reset.
    if(index > 2)
        index = 0;
    
    // Accept the CMD.
    else if(index == 2 && dataBuf[1] == '\n')
        switch(dataBuf[0])
        {
            case 'S':
            case 's':
                // Make measurement request
                leda_pollAll();
                
                sendAck();
                sendEndLine();
                break;
                
            case 'R':
            case 'r':
                // Read all the data back.
                leda_getAll();
                
                sendAck();
                sendEndLine();
                break;
                
            case 'W':
            case 'w':
                // Watchdog timer system reset;
                wdt_reset();
                //set up WDT.
                WDTCSR = (uint8_t)(_BV(WDE));
                for(;;)
                    ; // Wait to die!!
                
            default:
                break;
        }

} // End of handleCmd().


static inline void enterSleep(void)
{
    sleep_enable();
    sleep_bod_disable();
    sleep_cpu();
    sleep_disable();
    
} // End of enterSleep().

static inline void sendEndLine(void)
{
    usart_writeData('\n');
}

static inline void sendAck(void)
{
    usart_writeData('Z');
}


// This function is called upon a HARDWARE RESET:
void reset(void) __attribute__((naked)) __attribute__((section(".init3")));

/*! Clear SREG_I on hardware reset. */
void reset(void)
{
    cli();
    // Note that for newer devices (any AVR that has the option to also
    // generate WDT interrupts), the watchdog timer remains active even
    // after a system reset (except a power-on condition), using the fastest
    // prescaler value (approximately 15 ms). It is therefore required
    // to turn off the watchdog early during program startup.
    MCUSR = 0; // clear reset flags
    wdt_disable();
    
} // End of reset().

