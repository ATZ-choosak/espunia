from pcf8574 import PCF8574

addr1 = 0x20
addr2 = 0x21
addr3 = 0x22

bus1 = PCF8574(1 , addr1)
bus2 = PCF8574(1 , addr2)
bus3 = PCF8574(1 , addr3)

def readAllBus():
    
  data1 = list(bus1.port)
  data2 = list(bus2.port)
  data3 = list(bus3.port)
  
  return [data1[::-1], data2[::-1], data3[::-1]]

def closeAllBus():
  pass

