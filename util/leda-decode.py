!#/bin/python3

import csv
import fractions

#read in file data to memory
def fileto_memory():
    data = []
    with open('rawdata.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            data += row
    # data in row appears as:
    # timestamp, then
    # data, then
    # timestamp, and so forth
    return data

# ------------------------------
# GOAL: Maintain measured precision..
# thus avoid floating point values.
# Component functions for:
# interpret()
# Functions for each sensor.
# ------------------------------

# to-do: currently, this returns a string..
# hence the quotation marks on the output.
def temp_DS1631(value): 
    # hardcoded hexidecimal values are specific to chips!
    intmask = 0x7f00 # 0111 1111 0000 0000
    signmask = 0x8000
    # not explicitly listed in data sheet:
    # for negative values, 
    # there is a 1's complement for the first bits 15 - 8 (whole number).
    # 2's complement for bits 7 - 4 (fractional)
    is_positive =  -1 if ((value & signmask) > 1) else 1
    # semantics of is_positive v.s is_negative may be flipped around, 
    # but for now it just works.
    value = ~value if (is_positive > 0) else value wholenum = (~value & intmask) >> 8
    # got whole number- at this point 1's complement not needed
    value += 0x10 if (is_positive > 0) else 0x0
    # add for 2's complement of 0001 0000 if negative sign 
    fractional = 0
    if (value & 0x80) > 0:
        fractional += 8
    elif (value & 0x40) > 0:
        fractional += 4
    elif (value & 0x20) > 0:
        fractional += 2
    elif (value & 0x10) > 0:
        fractional += 1
    print(wholenum, fractional)
    # real value = wholenum + fractional/16
    # consider as mixed fraction notation
    # returning non-mixed notation
    return (str(is_positive * (wholenum * 16 + fractional)) + '/' + str(16))

def pressure_MPX5100(value):
    #Vout = Vout = Vs(P * 0.009 + 0.04) +- (PressureError * TempMult * 0.009 * Vs)
    #where Vs = 5.0V +- 0.25V
    return value

def pressure_MPX4115V(value):
    #Vout = Vs(P * 0.007652 + 0.92) +- (PressureError * TempFactor * 0.007652 * Vs)
    #where Vs = 5V +- 0.25 Vdc
    return value

def humidity_HIH8120h(value):
    #Humidity (%RH) = ( Humidity_14bit_ADC / (2^14)-2 ) * 100
    return value

def temp_HIH8120t(value):
    #Temp (celsius) = (( Temp_14bit_ADC / (2^14)-2 ) * 165 ) - 40
    return value

# XOR checksum
def checksum(value):
    return value

# ------------------------------
# any sort of changes to how data should be read is in here
def interpret(sindexes, line):
    subsections = []
    # given hardcoded ranges in the script
    # it corresponds to 
    # 0 = Sensor Status Bitmap
    # 1 = Temp (DS1631)
    # 2 = Pressure 1
    # 3 = Pressure 2
    # 4 = Humidity
    # 5 = Temp
    # 6 - Checksum
    for each in ranges:
    # split the line into designated ranges
        subsections += [int(line[each[0] : each[1]], 16)]
    # give each sensor their own function
    # worry about sensor status bitmap later.
    subsections[1] = temp_DS1631(subsections[1])
    subsections[2] = pressure1(subsections[2])
    subsections[3] = pressure2(subsections[3])
    subsections[4] = humidity(subsections[4])
    subsections[5] = temp(subsections[5])
    subsections[6] = checksum(subsections[6])
    return subsections
    
# ------------------------------
# outputs the csv through standard output
# todo: add parameter for result of checksum evaluation
def output(text, dsections, tstamps):
# make it so the physics students will have a ~fairly~ easy time with reading the output
# assume the physics student will  L I T E R A L L Y  fuck everything up
# so add "TRANSMIT_OK, Timestamp" to the front of the labels
    csvlabels = ["TRANSMIT_OK", "Timestamp"]
    csvlabels += text
    for label in csvlabels:
        print(label + ', ', end='')
    print() # create new row for data
    for time, section in zip(tstamps, dsections):
    #Y is placeholder for evaluated checksum
        print("Y" + ',' + time + ',' + str(section).strip("[']"))
    return

# ------------------------------
# End function initializations
# ------------------------------

# datas known based on hardware datasheet and program output
# both ranges and labels should be the same length
ranges = [[0, 2], [2, 6], [6, 10], [10, 14], [14, 18], [18, 22], [22, 24]]
labels = ["Sensor Status Bitmap", "Temp (DS1631)", "Pressure 1", "Pressure 2", "Humidity", "Temp", "Checksum"]
fdata = fileto_memory()
rawdata = fdata[1::2]
timestamps = fdata[0::2]

# index size = size of rawdata * 8
# data from rawdata segmented.
datas = []
for row in rawdata:
    datas.append(interpret(ranges, row))
output(labels, datas, timestamps)
