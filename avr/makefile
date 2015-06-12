
# echo setting.
# Light Blue
LIGHT_BLUE=\033[1;34m
# Blue
BLUE=\033[0;34m
#Cyan
CYAN=\033[0;36m
# Dark Gray
DARK_GRAY=\033[1;30m
# Red
RED=\033[0;31m
# No Color
NC=\033[0m


# AVR setting.
MMCU=atmega328p
F_CPU=16000000UL

# Compiler and Linker setting. 
# Warnings
WALL=	-Waddress \
		-Warray-bounds \
		-Wchar-subscripts \
		-Wenum-compare \
		-Wimplicit-int \
		-Wimplicit-function-declaration \
		-Wcomment \
		-Wformat \
		-Wmaybe-uninitialized \
		-Wmissing-braces \
		-Wnonnull \
		-Wopenmp-simd \
		-Wparentheses \
		-Wpointer-sign \
		-Wsequence-point \
		-Wstrict-aliasing \
		-Wstrict-overflow=1 \
		-Wswitch \
		-Wtrigraphs \
		-Wuninitialized \
		-Wunknown-pragmas \
		-Wunused-function \
		-Wunused-label \
		-Wunused-value \
		-Wunused-variable \
		-Wvolatile-register-var
		#-Wc++11-compat \
		#-Wreorder \
		#-Wreturn-type \
		#-Wsign-compare \
		#-Wmain \

CC=avr-gcc
CFLAGS= $(WALL) -std=c11 -DF_CPU=$(F_CPU) -O3 -g
OBJS= main.o Adc.o CircularBuffer.o Leda.o Timer.o Twi.o Usart.o

# Project setting.
PROJECTNAME=Leda

all: $(PROJECTNAME).hex

#Compiler.
%.o : %.c
	@echo -e "Compiling: ${LIGHT_BLUE}$@${NC} <-- ${CYAN}$<${NC}"
	@$(CC) $(CFLAGS) -mmcu=$(MMCU) -c $<

%.o : %.c %.h 
	@echo -e "Compiling: ${LIGHT_BLUE}$@${NC} <-- ${CYAN}$< (.h)${NC}"
	@$(CC) $(CFLAGS) -mmcu=$(MMCU) -c $<

#Linker.
$(PROJECTNAME).elf: $(OBJS)
	@echo -e "Linking:   ${LIGHT_BLUE}$@${NC} <-- [${CYAN}$^${NC}]"
	@$(CC) $(CFLAGS) -mmcu=$(MMCU) -o $@ $^

#Generate Intel Hex File. 
$(PROJECTNAME).hex: $(PROJECTNAME).elf
	@echo -e "Generating Intel Hex File: ${LIGHT_BLUE}$@${NC} <-- ${CYAN}$<${NC}"
	@avr-objcopy -j .text -j .data -O ihex $< $@

#Avrdude Setting. 
F_PART=m328p
F_PORT=usb
F_FLASHER=avrispmkII

flash: $(PROJECTNAME).hex
	sudo avrdude -p $(F_PART) -P $(F_PORT) -c $(F_FLASHER) -U flash:w:$<

readFuse:
	sudo avrdude -p $(F_PART) -P $(F_PORT) -c $(F_FLASHER) -U lfuse:r:-:h -U hfuse:r:-:h -U efuse:r:-:h
# Fresh Project.
fresh: clean all

# To just compile code to objects.
objects: $(OBJS)

# Clean Project. 
clean:
	@echo -e "Removing:  ${CYAN}$(OBJS) $(PROJECTNAME).elf $(PROJECTNAME).hex $(PROJECTNAME).lst${NC}"
	@rm $(OBJS) $(PROJECTNAME).elf $(PROJECTNAME).hex $(PROJECTNAME).lst || true

# avr-size
size: $(PROJECTNAME).elf
	@avr-size -C --mcu=$(MMCU) $<
	

# disassembles the binary file and intersperses the source code
disassembly: $(PROJECTNAME).lst

$(PROJECTNAME).lst: $(PROJECTNAME).elf
	@echo -e "Disassembly: ${LIGHT_BLUE}$@${NC} <-- ${CYAN}$<${NC}"
	@avr-objdump -h -S $< > $@ 


