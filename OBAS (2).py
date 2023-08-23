import pwinput
accL1 = []
orderHS = []
ServiceHS = []
serv1=[]
serv2=[]
serv3=[]
accesories1 = {
	"Name":"Windscreen",
	"Price":2000, 
	"Stock":50
}
accesories2 = {
	"Name":"Bike Horn",
	"Price":125,
	"Stock":500
}
accesories3 = {
	"Name":"Lowrider Seat",
	"Price":5000,
	"Stock":50
}
accesories4 = {
	"Name":"Paddock Stand",
	"Price":6000,
	"Stock":25
}
accesories5 = {
	"Name":"Handlebar",
	"Price":3000,
	"Stock":100
}

accL1.append(accesories1)
accL1.append(accesories2)
accL1.append(accesories3)
accL1.append(accesories4)
accL1.append(accesories5)

ser1={
	"Sname":"Oil Change",
	"price":300
}
ser2={
	"Sname":"Break & clutch",
	"price":200
}
ser3={
	"Sname":"Wash & cleaning",
	"price":200
}
ser4={
	"Sname":"light & parts change",
	"price":500
}
ser5={
	"Sname":"Engine",
	"price":12000
}
ser6={
	"Sname":"Tyres",
	"price":3000
}


serv1.append(ser1)
serv1.append(ser2)
serv1.append(ser3)

serv2.append(ser5)
serv2.append(ser6)
serv2.append(ser4)

serv3.append(ser1)
serv3.append(ser2)
serv3.append(ser3)
serv3.append(ser4)
serv3.append(ser5)
serv3.append(ser6)


class accesories:
	def viewaccA(self):
		print("*************************************************************************")
		print("*				Accesories				*")
		print("*									*")
		print("*	%-5s%-18s%-8s%-8s				*" % ("No","Name","Price","Stock"))
		n = 1
		for i in accL1:
			print("*	%-5i%-18s%-8i%-8i				*"% (n,i['Name'],i['Price'],i['Stock']))
			n+=1
		print("*									*")
		print("*************************************************************************")
		print()

	def viewaccU(self):
		print("*************************************************************************")
		print("*				Accesories				*")
		print("*									*")
		print("*	%-5s%-18s%-8s%-8s				*" % ("No","Name","Price","Stock"))
		n = 1
		for i in accL1:
			if i['Stock'] == 0:
				print("*	%-5i%-18s%-8i%-8s			*"% (n,i['Name'],i['Price'],"Out Of Stock"))
				n += 1
			if i['Stock'] != 0:
				print("*	%-5i%-18s%-8i%-8s			*"% (n,i['Name'],i['Price'],"Available"))
				n += 1
		print("*									*")		
		print("*************************************************************************")
		print()	

	def buyaccU(self):
		dict = {}
		print("*************************************************************************")
		print("*				Accesories				*")
		print("*									*")
		print("*	%-5s%-18s%-8s%-8s				*" % ("No","Name","Price","Stock"))
		n = 1
		for i in accL1:
			if i['Stock'] == 0:
				print("*	%-5i%-18s%-8i%-8s			*"% (n,i['Name'],i['Price'],"Out Of Stock"))
				n += 1
			if i['Stock'] != 0:
				print("*	%-5i%-18s%-8i%-8s			*"% (n,i['Name'],i['Price'],"Available"))
				n += 1	
			
		print("*									*")
		accName = input("*	Enter the Name of Accesorie you want to buy: ")
		print("*									*")
		accQuan = int(input("*	Enter the Quantity: "))
		print("*									*")
		print("*				Your Order				*")
		print("*									*")
		for i in accL1:
			if i['Name'] == accName:
				print("*	Accesorie: ",accName,"						*")
				print("*	Quantity: ",accQuan,"							*")
				price = accQuan * i['Price']
				print("*	Price: ",price,"							*")
				dict['accName'] = accName
				dict['accQuan'] = accQuan
				dict['Price'] = price
				i['Stock'] = i['Stock'] - accQuan
		print("*									*")		
		print("*************************************************************************")
		print()	
		orderHS.append(dict)

	def orderHistory(self):
		print("*************************************************************************")
		print("*				Order History				*")
		print("*									*")
		n = 1
		print("*	%-5s%-18s%-12s%-8s			*" % ("No","Name","Quantity","Price"))
		for i in orderHS:
			print("*	%-5i%-18s%-12i%-8i			*"%(n,i['accName'],i['accQuan'],i['Price']))
			n += 1
		print("*									*")		
		print("*************************************************************************")
		print()	

	def order(self):
		print("*************************************************************************")
		print("*				Order					*")
		print("*									*")
		n = 1
		print("*	%-5s%-18s%-12s%-8s			*" % ("No","Name","Quantity","Price"))
		for i in orderHS:
			print("*	%-5i%-18s%-12i%-8i			*"%(n,i['accName'],i['accQuan'],i['Price']))
			n += 1
		print("*									*")		
		print("*************************************************************************")
		print()		


	def addAcc(self):
		dict = {}
		print("*************************************************************************")
		print("*				Add Accesories				*")
		print("*									*")
		dict['Name'] = input("*	Enter Accesorie Name: ")
		dict['Price'] = int(input("*	Enter Price of Accesorie: "))
		dict['Stock'] = int(input("*	Enter Stock of Accesorie: "))
		accL1.append(dict)
		print("*			Accesories Added				*")
		print("*									*")
		print("*************************************************************************")
		print()

	def delAcc(self):
		print("*************************************************************************")
		print("*			Delete Accesories				*")
		print("*									*")
		print("*	%-5s%-18s%-8s%-8s				*" % ("No","Name","Price","Stock"))
		n = 1
		for i in accL1:
			print("*	%-5i%-18s%-8i%-8i				*"% (n,i['Name'],i['Price'],i['Stock']))
			n += 1
		print("*									*")
		ask = input("*	Enter the Name of Accesorie you want to delete: ")
		for i in accL1:
			if i['Name'] == ask:
				accL1.remove(i)
		print("*									*")	
		print("*	Accesorie Deleted						*")
		print("*************************************************************************")
		print()
		print("*************************************************************************")
		print("*	%-5s%-18s%-8s%-8s				*" % ("No","Name","Price","Stock"))
		n1 = 1
		for i in accL1:
			print("*	%-5i%-18s%-8i%-8i				*"% (n1,i['Name'],i['Price'],i['Stock']))
			n1 += 1
		print("*									*")	
		print("*************************************************************************")
		print()

	def updtacc(self):
		print("*************************************************************************")
		print("*			Update Accesories				*")
		print("*									*")
		print("*	%-5s%-18s%-8s%-8s				*" % ("No","Name","Price","Stock"))
		n = 1
		for i in accL1:
			print("*	%-5i%-18s%-8i%-8i				*"% (n,i['Name'],i['Price'],i['Stock']))
			n += 1
		print("*									*")
		ask = input("*	Enter the name of Accesorie you want to update: ")
		print("*									*")
		for i in accL1:
			if i['Name'] == ask:
				print("*	1. Name								*")
				print("*	2. Price							*")
				print("*	3. Stock							*")
				print("*									*")
				ask2 = int(input("*	Enter what do you want to update? "))
				print("*									*")
				if ask2 == 1:
					newName = input("*	Enter New Name: ")
					i['Name'] = newName
					print("*	Name Updated!!!						*")
					print("*									*")
					print("*	%-18s%-8s%-8s				*" % ("Name","Price","Stock"))
					print("*	%-18s%-8i%-8i				*"% (i['Name'],i['Price'],i['Stock']))

				if ask2 == 2:
					newPrice = int(input("*	Enter New Price: "))
					i['Price'] = newPrice
					print("*	Price Updated!!!						*")
					print("*									*")
					print("*	%-18s%-8s%-8s				*" % ("Name","Price","Stock"))
					print("*	%-18s%-8i%-8i				*"% (i['Name'],i['Price'],i['Stock']))

				if ask2 == 3:
					newStock = int(input("*	Enter New Stock: "))
					i['Stock'] = i['Stock']+newStock
					print("*	Stock Updated!!!						*")
					print("*									*")
					print("*	%-18s%-8s%-8s				*" % ("Name","Price","Stock"))
					print("*	%-18s%-8i%-8i				*"% (i['Name'],i['Price'],i['Stock']))

		print("*									*")	
		print("*************************************************************************")
		print()

class service:
	def orderser1(self):
		dict = {}
		print("*************************************************************************")
		print("*				PERIODIC SERVICE 			*")
		print("*									*")
		print("*	%-5s%-25s%-8s				*"% ("No","Service Name","Price"))
		n = 1
		for i in serv1:
			print("*	%-5i%-25s%-8i				*"% (n,i['Sname'],i['price']))
			n+=1
		print("*									*")
		ask = input("*	Do you want to get Peridoic Service for your bike? ").capitalize()
		print("*									*")
		if ask == "Yes":
			ask2 = input("*	Enter Bike Model: ")
			print("*									*")
			print("*	Thank you for taking our services for your bike: ",ask2,"	*")
			print("*									*")
			print("*				Services				*")
			print("*									*")
			print("*	%-5s%-25s%-8s				*"% ("No","Service Name","Price"))
			n1 = 1
			total = 0
			for i in serv1:
				print("*	%-5i%-25s%-8i				*"% (n1,i['Sname'],i['price']))
				total += i['price']
				n1+=1
			print("*									*")	
			print("*	Total Cost for Service is: ",total,"				*")
			dict['ServName'] = "Peridoic Service"
			dict['Bike_Model'] = ask2
			dict['Total_Cost'] = total
			ServiceHS.append(dict)
			print("*									*")

		if ask == "No":
			pass

		print("*************************************************************************")
		print()

	def orderser2(self):
		dict={}
		print("*************************************************************************")
		print("*				MAJOR SERVICE				*")
		print("*									*")
		print("*	%-5s%-25s%-8s				*" % ("No","Service Name","Price"))
		n = 1
		for i in serv2:
			print("*	%-5i%-25s%-8i				*"% (n,i['Sname'],i['price']))
			n+=1
		print("*									*")
		ask = input("*	Do you want to get Major Service for your bike? ").capitalize()
		print("*									*")
		if ask == "Yes":
			ask2 = input("*	Enter Bike Model: ")
			print("*									*")
			print("*	Thank you for taking our services for your bike: ",ask2,"	*")
			print("*									*")
			print("*				Services				*")
			print("*									*")
			print("*	%-5s%-25s%-8s				*"% ("No","Service Name","Price"))
			n1 = 1
			total = 0
			for i in serv2:
				print("*	%-5i%-25s%-8i				*"% (n1,i['Sname'],i['price']))
				total += i['price']
				n1+=1
			print("*									*")	
			print("*	Total Cost for Service is: ",total,"				*")
			dict['ServName'] = "Major Service"
			dict['Bike_Model'] = ask2
			dict['Total_Cost'] = total
			ServiceHS.append(dict)
			print("*									*")

		if ask == "No":
			pass

		print("*************************************************************************")
		print()	

	def orderser3(self):
		dict={}
		print("*************************************************************************")
		print("*				FULL SERVICE				*")
		print("*									*")
		print("*	%-5s%-25s%-8s				*" % ("No","Service Name","Price"))
		n = 1
		for i in serv3:
			print("*	%-5i%-25s%-8i				*"% (n,i['Sname'],i['price']))
			n+=1
		print("*									*")
		ask = input("*	Do you want to get Full Service for your bike? ").capitalize()
		print("*									*")
		if ask == "Yes":
			ask2 = input("*	Enter Bike Model: ")
			print("*									*")
			print("*	Thank you for taking our services for your bike: ",ask2,"	*")
			print("*									*")
			print("*				Services				*")
			print("*									*")
			print("*	%-5s%-25s%-8s				*"% ("No","Service Name","Price"))
			n1 = 1
			total = 0
			for i in serv3:
				print("*	%-5i%-25s%-8i				*"% (n1,i['Sname'],i['price']))
				total += i['price']
				n1+=1
			print("*									*")	
			print("*	Total Cost for Service is: ",total,"				*")
			dict['ServName'] = "Full Service"
			dict['Bike_Model'] = ask2
			dict['Total_Cost'] = total
			ServiceHS.append(dict)
			print("*									*")

		if ask == "No":
			pass
		print("*************************************************************************")
		print()

	def servicePurchace(self):
		print("*************************************************************************")
		print("*			Services Purchased				*")
		print("*									*")
		n = 1
		print("*	%-5s%-18s%-12s%-8s			*" % ("No","Name","Bike Model","Total Cost"))
		for i in ServiceHS:
			print("*	%-5i%-18s%-12s%-8i			*"%(n,i['ServName'],i['Bike_Model'],i['Total_Cost']))
			n += 1
		print("*									*")		
		print("*************************************************************************")
		print()

	def delSer(self):
		print("*************************************************************************")
		print("*				Delete Service				*")
		print("*									*")
		print("*	1. PERIODIC SERVICE 						*")
		print("*	2. MAJOR SERVICE 						*")
		print("*	3. FULL SERVICE							*")
		print("*									*")
		ask=int(input("*	Enter service from which you want delete: "))
		print("*									*")
		if ask==1:
			self.viewser1()
			ask = input("*	Enter name of service you want to delete: ")
			print("*									*")
			for i in serv1:
				if i['Sname'] == ask:
					serv1.remove(i)
					print("*			Service Deleted!!!				*")
					print("*									*")
			self.viewser1()				
		elif ask==2:
			self.viewser2()
			ask = input("*	Enter name of service you want to delete: ")
			print("*									*")
			for i in serv2:
				if i['Sname'] == ask:
					serv2.remove(i)
					print("*			Service Deleted!!!				*")
					print("*									*")
			self.viewser2()		
		elif ask==3:
			self.viewser3()
			ask = input("*	Enter name of service you want to delete: ")
			print("*									*")
			for i in serv3:
				if i['Sname'] == ask:
					serv3.remove(i)
					print("*			Service Deleted!!!				*")
					print("*									*")
			self.viewser3()	

	def viewser1(self):
		print("*************************************************************************")
		print("*				PERIODIC SERVICE 			*")
		print("*									*")
		print("*	%-5s%-25s%-8s				*"% ("No","Service Name","Price"))
		n = 1
		for i in serv1:
			print("*	%-5i%-25s%-8i				*"% (n,i['Sname'],i['price']))
			n+=1
		print("*									*")

	def viewser2(self):
		print("*************************************************************************")
		print("*				MAJOR SERVICE				*")
		print("*									*")
		print("*	%-5s%-25s%-8s				*" % ("No","Service Name","Price"))
		n = 1
		for i in serv2:
			print("*	%-5i%-25s%-8i				*"% (n,i['Sname'],i['price']))
			n+=1
		print("*									*")

	def viewser3(self):
		print("*************************************************************************")
		print("*				FULL SERVICE				*")
		print("*									*")
		print("*	%-5s%-25s%-8s				*" % ("No","Service Name","Price"))
		n = 1
		for i in serv3:
			print("*	%-5i%-25s%-8i				*"% (n,i['Sname'],i['price']))
			n+=1
		print("*									*")
		

	def addser(self):
		dict = {}
		print("*************************************************************************")
		print("*				Add Service				*")
		print("*									*")
		dict['Sname'] = input("*	Enter Service Name: ")
		dict['price'] = int(input("*	Enter Price of Service: "))
		print("*									*")
		print("*				Services				*")
		print("*	1. PERIODIC SERVICE 						*")
		print("*	2. MAJOR SERVICE 						*")
		print("*	3. FULL SERVICE							*")
		print("*									*")

		ask=int(input("*	Enter service in which you want add : "))
		print("*									*")
		if ask==1:
			serv1.append(dict)
			self.viewser1()
		elif ask==2:
			serv2.append(dict)
			self.viewser2()
		elif ask==3:
			serv3.append(dict)
			self.viewser3()
		
		print("*			Service Added					*")
		print("*									*")
		print("*************************************************************************")
		print()


	def updateser(self):
		print("*************************************************************************")
		print("*			  Update Service				*")
		print("*									*")
		print("*	1. PERIODIC SERVICE 						*")
		print("*	2. MAJOR SERVICE 						*")
		print("*	3. FULL SERVICE							*")
		print("*									*")
		ask = int(input("*	Enter the Service you want to update: "))
		print("*									*")
		if(ask==1):
			self.viewser1()
			ask1=input("*	Enter service name from above you want to update : ")
			print("*									*")
			for i in serv1:
				if i['Sname']==ask1:
					print("*	1. Name								*")
					print("*	2. Price							*")
					print("*									*")
					ask2 = int(input("*	Enter what do you want to update? "))
					print("*									*")
					if ask2 == 1:
						newName = input("*	Enter New Name: ")
						i['Sname'] = newName
						print("*	Name Updated!!!						*")
						print("*									*")
						print("*	%-18s%-8s					*" % ("Name","Price"))
						print("*	%-18s%-8i					*"% (i['Sname'],i['price']))
						self.viewser1()


					if ask2 == 2:
						newPrice = int(input("*	Enter New Price: "))
						print("*									*")
						i['price'] = newPrice
						print("*	Price Updated!!!						*")
						print("*									*")
						print("*	%-18s%-8s					*" % ("Name","Price"))
						print("*	%-18s%-8i					*"% (i['Sname'],i['price']))
						self.viewser1()

					
		elif(ask==2):
			self.viewser2()
			ask1=input("*	Enter service name from above you want to update : ")
			print("*									*")
			for i in serv2:
				self.viewser2()
				print("*	1. Name								*")
				print("*	2. Price							*")
				print("*									*")
				ask2 = int(input("*	Enter what do you want to update? "))
				print("*									*")
				if ask2 == 1:
					newName = input("*	Enter New Name: ")
					print("*									*")
					i['Sname'] = newName
					print("*	Name Updated!!!						*")
					print("*									*")
					print("*	%-18s%-8s				*" % ("Name","Price"))
					print("*	%-18s%-8i				*"% (i['Sname'],i['price']))

				if ask2 == 2:
					newPrice = int(input("*	Enter New Price: "))
					print("*									*")
					i['price'] = newPrice
					print("*	Price Updated!!!						*")
					print("*									*")
					print("*	%-18s%-8s				*" % ("Name","Price"))
					print("*	%-18s%-8i				*"% (i['Sname'],i['price']))

		elif(ask==3):
			self.viewser3()
			ask1=input("*	Enter service name from above you want to update : ")
			print("*									*")
			for i in serv3:
				self.viewser3()
				print("*	1. Name								*")
				print("*	2. Price							*")
				print("*									*")
				ask2 = int(input("*	Enter what do you want to update? "))
				print("*									*")
				if ask2 == 1:
					newName = input("*	Enter New Name: ")
					print("*									*")
					i['Sname'] = newName
					print("*	Name Updated!!!						*")
					print("*									*")
					print("*	%-18s%-8s				*" % ("Name","Price"))
					print("*	%-18s%-8i				*"% (i['Sname'],i['price']))

				if ask2 == 2:
					newPrice = int(input("*	Enter New Price: "))
					print("*									*")
					i['price'] = newPrice
					print("*	Price Updated!!!						*")
					print("*									*")
					print("*	%-18s%-8s				*" % ("Name","Price"))
					print("*	%-18s%-8i				*"% (i['Sname'],i['price']))

		print("*									*")	
		print("*************************************************************************")
		print()

accClass = accesories()
serClass = service()
while True:
	print("*************************************************************************")
	print("*									*")
	print("*				Login					*")
	print("*									*")
	print("*									*")
	uname = input("*	Username: ")
	pwd = pwinput.pwinput("*	Password: ")
	print("*									*")
	print("*									*")
	print("*************************************************************************")


	if uname == "Admin" and pwd == "8649":
		while True:
			print("*************************************************************************")
			print("*									*")
			print("*	1. Accesories							*")
			print("*	2. Services							*")
			print("*	3. Logout							*")
			print("*									*")
			ch = int(input("*	What you want to do? "))
			print("*************************************************************************")

			if ch == 1:
				while True:
					print("*************************************************************************")
					print("*				Accesories				*")
					print("*	1. View Accesories						*")
					print("*	2. Add Accesories						*")
					print("*	3. Update Accesories						*")
					print("*	4. Delete Accesories						*")
					print("*	5. Order							*")
					print("*	6. Exit								*")
					print("*									*")
					ch1 = int(input("*	What you want to do? "))
					print("*************************************************************************")

					if ch1 == 1:
						accClass.viewaccA()

					if ch1 == 2:
						accClass.addAcc()

					if ch1 == 3:
						accClass.updtacc()

					if ch1 == 4:
						accClass.delAcc()

					if ch1 == 5:
						accClass.order()

					if ch1 == 6:
						break

			if ch == 2:
				while True:
					print("*************************************************************************")
					print("*				Services				*")
					print("*	1. Add Service 							*")
					print("*	2. Update Service 						*")
					print("*	3. Delete Service						*")
					print("*	4. Service Purchase						*")
					print("*	5. Exit								*")
					print("*									*")
					ch1 = int(input("*	What you want to do? "))
					print("*************************************************************************")

					if ch1 == 1:
						serClass.addser()

					if ch1 == 2:
						serClass.updateser()

					if ch1 == 3:
						serClass.delSer()

					if ch1 == 4:
						serClass.servicePurchace()

					if ch1 == 5:
						break

			if ch == 3:
				break



	if uname == "Kirtan" and pwd == "756":
		while True:
			print("*************************************************************************")
			print("*									*")
			print("*	1. Accesories							*")
			print("*	2. Services							*")
			print("*	3. Logout							*")
			print("*									*")
			ch = int(input("*	What you want to do? "))
			print("*************************************************************************")

			if ch == 1:
				while True:
					print("*************************************************************************")
					print("*				Accesories				*")
					print("*	1. View Accesories						*")
					print("*	2. Buy Accesories						*")
					print("*	3. Order History						*")
					print("*	4. Exit								*")
					print("*									*")
					ch1 = int(input("*	What you want to do? "))
					print("*************************************************************************")

					if ch1 == 1:
						accClass.viewaccU()

					if ch1 == 2:
						accClass.buyaccU()

					if ch1 == 3:
						accClass.orderHistory()		

					if ch1 == 4:
						break

			if ch == 2:
				while True:
					print("*************************************************************************")
					print("*				Services				*")
					print("*	1. Periodic Service 						*")
					print("*	2. Major Service 						*")
					print("*	3. Full Service							*")
					print("*	4. Exit								*")
					print("*									*")
					ch1 = int(input("*	What you want to do? "))
					print("*************************************************************************")

					if ch1 == 1:
						serClass.orderser1()

					if ch1 == 2:
						serClass.orderser2()

					if ch1 == 3:
						serClass.orderser3()
						
					if ch1 == 4:
						break

			if ch == 3:
				break

	if uname == "3":
		exit()		