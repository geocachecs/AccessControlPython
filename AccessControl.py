
acceptableVariables = ['__init__','getAction','setAction','getPort','setPort','setTraffic','getTraffic','getLayer4_port','setLayer4_port','getType','setType','getWavelength','setWavelength','removePortById','getPortById','addPort','getPortList','setPortList','setName','getName','setId','getId','__getattribute__','__setattr__','__class__','__dict__']


def setterLock(self,name,value):			
	if(name=='__setattr__' or name=="__getattribute__"):
		object.__setattr__(self,name,value)
	else:
		raise(AccessViolation)
	
def getterLock(self,name):
	if(name in acceptableVariables):
		return object.__getattribute__(self,name)
	else:
		raise(AccessViolation)

def getterUnlock(variable):
		def thisUnlock(self,name):
			if(name in acceptableVariables):
				return object.__getattribute__(self,name)		
			elif(name not in self.__dict__ and name!=variable):
				raise(AccessViolation)
			else:
				return object.__getattribute__(self,name)
		return(thisUnlock)
		
def setterUnlock(variable):
	def thisUnlock(self,name,value):
		if(name==variable or name == '__setattr__' or name=='__getattribute__'):
			object.__setattr__(self,name,value)
		else:
			raise(AccessViolation)
	return(thisUnlock)
	
class AccessViolation(Exception):
	pass

class InvalidType(Exception):
	pass
	
	
	
	
	
	
	
	
	

	
	
class Device(object):
	def __init__(self):
		port_list = []
		Device.__setattr__ = setterLock
		Device.__getattribute__ = getterLock
		
	def setName(self,newName):
		if(isinstance(newName,str)):
			Device.__setattr__ = setterUnlock('name')
			Device.__getattribute__ = getterUnlock('name')	
			self.name = newName
		
			Device.__getattribute__ = getterLock
			Device.__setattr__ = setterLock
		else:
			raise(TypeError)
		
	def getName(self):
		if('name' in dir(self)):
			Device.__getattribute__ = getterUnlock('name')
			temp = self.name
			Device.__getattribute__ = getterLock
			return(temp)
		else:
			return(None)
			
	def setPortList(self,newList):
		allPort = True
		for x in newList:
			if(not isinstance(x,PhysicalPort)):
				allPort=False
		if(isinstance(newList,list) and allPort):
			Device.__setattr__ = setterUnlock('port_list')
			Device.__getattribute__ = getterUnlock('port_list')
			self.port_list = newList
			Device.__getattribute__ = getterLock
			Device.__setattr__ = setterLock
		else:
			raise(TypeError)
	
	def getPortList(self):
		Device.__getattribute__ = getterUnlock('port_list')
		temp = self.port_list
		Device.__getattribute__ = getterLock
		return(temp)
	
	def addPort(self,newPort):
		if(isinstance(newPort,PhysicalPort)):
			Device.__setattr__ = setterUnlock('port_list')
			Device.__getattribute__ = getterUnlock('port_list')
			self.port_list.append(newPort)
			Device.__getattribute__  = getterLock
			Device.__setattr__ = setterLock
		else:
			raise(TypeError)
	
	def getPortById(self,id):
		temp = None
		Device.__getattribute__ = getterUnlock('port_list')
		for x in self.port_list:
			if(x.getId()==id):
				temp = x
				break
		Device.__getattribute__ = getterLock
		return temp
		
	def removePortById(self,id):
		if(not isinstance(id,str)):
			raise(TypeError)
		else:
			temp = self.getPortById(id)
			if(temp!=None):
				Device.__setattr__ = setterUnlock('port_list')
				Device.__getattribute__ = getterUnlock('port_list')
				self.port_list.remove(temp)
				Device.__getattribute__ = getterLock
				Device.__setattr__ = setterLock
			else:
				print("Port not found in list")

				
class PhysicalPort(object):
	def __init__(self):
		PhysicalPort.__setattr__ = setterLock
		PhysicalPort.__getattribute__ = getterLock

	def setId(self, id): 
		PhysicalPort.__setattr__ = setterUnlock('id')
		PhysicalPort.__getattribute__= getterUnlock('id')
		if(isinstance(id,str)):
			self.id=id
		else:
			raise(TypeError)
		PhysicalPort.__getattribute__= getterLock
		PhysicalPort.__setattr__ = setterLock
		
	def getId(self):
		if('id' in dir(self)):
			PhysicalPort.__getattribute__ = getterUnlock('id')
			temp = self.id
			PhysicalPort.__getattribute__ = getterLock
			return temp
		else:
			return(None)
	
		
class Copper(PhysicalPort):
	pass


class Fiber(PhysicalPort):
	def __init__(self):
		PhysicalPort.__setattr__ = setterLock
		PhysicalPort.__getattribute__ = getterLock
	
	def setWavelength(self,wavelength):
		if(isinstance(wavelength,str)):
				PhysicalPort.__setattr__ = setterUnlock('wavelength')
				PhysicalPort.__getattribute__ = getterUnlock('wavelength')
				self.wavelength = wavelength

				PhysicalPort.__getattribute__ = getterLock
				PhysicalPort.__setattr__ = setterLock
		else:
				raise(TypeError)

	def getWavelength(self):
		if('wavelength' in dir(self)):
				PhysicalPort.__getattribute__ = getterUnlock('wavelength')
				temp = self.wavelength
				PhysicalPort.__getattribute__ = getterLock
				return(temp)
		else:
				return(None)


class Traffic(object):
	def setName(self,name):
		if(isinstance(name,str)):
				Traffic.__setattr__ = setterUnlock('name')
				Traffic.__getattribute__ = getterUnlock('name')
				self.name = name
				Traffic.__getattribute__ = getterLock
				Traffic.__setattr__ = setterLock
		else:
				raise(TypeError)

	def getName(self):
		if('name' in dir(self)):
				Traffic.__getattribute__ = getterUnlock('name')
				temp = self.name
				Traffic.__getattribute__ = getterLock
				return(temp)
		else:
				return(None)

	def setType(self,type):
		if(isinstance(type,str)):
				Traffic.__setattr__ = setterUnlock('type')
				Traffic.__getattribute__ = getterUnlock('type')
				self.type = type

				Traffic.__getattribute__ = getterLock
				Traffic.__setattr__ = setterLock
		else:
				raise(TypeError)

	def getType(self):
		if('type' in dir(self)):
				Traffic.__getattribute__ = getterUnlock('type')
				temp = self.type
				Traffic.__getattribute__ = getterLock
				return(temp)
		else:
				return(None)



	def setLayer4_port(self,layer4_port):
		if(isinstance(layer4_port,int)):
				Traffic.__setattr__ = setterUnlock('layer4_port')
				Traffic.__getattribute__ = getterUnlock('layer4_port')
				self.layer4_port = layer4_port

				Traffic.__getattribute__ = getterLock
				Traffic.__setattr__ = setterLock
		else:
				raise(TypeError)

	def getLayer4_port(self):
		if('layer4_port' in dir(self)):
				Traffic.__getattribute__ = getterUnlock('layer4_port')
				temp = self.layer4_port
				Traffic.__getattribute__ = getterLock
				return(temp)
		else:
				return(None)


class TrafficXPort(object):
	def __init__(self):
		TrafficXPort.__setattr__ = setterLock
		TrafficXPort.__getattribute__ = getterLock
	
	def setTraffic(self,traffic_i):
		if(isinstance(traffic_i,Traffic)):
				TrafficXPort.__setattr__ = setterUnlock('traffic_i')
				TrafficXPort.__getattribute__ = getterUnlock('traffic_i')
				self.traffic_i = traffic_i

				TrafficXPort.__getattribute__ = getterLock
				TrafficXPort.__setattr__ = setterLock
		else:
				raise(TypeError)

	def getTraffic(self):
		if('traffic_i' in dir(self)):
				TrafficXPort.__getattribute__ = getterUnlock('traffic_i')
				temp = self.traffic_i
				TrafficXPort.__getattribute__ = getterLock
				return(temp)
		else:
				return(None)

	def setPort(self,port):
		if(isinstance(port,PhysicalPort)):
				TrafficXPort.__setattr__ = setterUnlock('port')
				TrafficXPort.__getattribute__ = getterUnlock('port')

				self.port = port

				TrafficXPort.__getattribute__ = getterLock
				TrafficXPort.__setattr__ = setterLock
		else:
				raise(TypeError)

	def getPort(self):
		if('port' in dir(self)):
				TrafficXPort.__getattribute__ = getterUnlock('port')
				temp = self.port
				TrafficXPort.__getattribute__ = getterLock
				return(temp)
		else:
				return(None)
				
	def setAction(self,action):
		if(isinstance(action,str)):
				TrafficXPort.__setattr__ = setterUnlock('action')
				TrafficXPort.__getattribute__ = getterUnlock('action')
				self.action = action

				TrafficXPort.__getattribute__ = getterLock
				TrafficXPort.__setattr__ = setterLock
		else:
				raise(TypeError)

	def getAction(self):
		if('action' in dir(self)):
				TrafficXPort.__getattribute__ = getterUnlock('action')
				temp = self.action
				TrafficXPort.__getattribute__ = getterLock
				return(temp)
		else:
				return(None)


	
	
