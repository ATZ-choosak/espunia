from pcf8574 import PCF8574

addr1 = 0x20
addr2 = 0x21
addr3 = 0x22

bus1 = PCF8574(0 , addr1)
bus2 = PCF8574(0 , addr2)
bus3 = PCF8574(0 , addr3)

def readAllBus():
    
  data1 = bus1.port
  data2 = bus2.port
  data3 = bus3.port
  
  return [data1, data2, data3]

def closeAllBus():

  bus1.close()
  bus2.close()  
  bus3.close()


