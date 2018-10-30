### README- DATABASE CLEANER PROJECT


In this project basically we are cleaning our Database. Actually for each time, lets say 10 am , at 10:00:00hrs there are still many entries recorded in the database as the Crypto Currencies values are varying in milliseconds so henceforth,what we had to do was just keep the first entry that was recorded for each Hour...with hour starting from 12 hrs midnight....So hence the entries which are recorded in milliseconds are actually called timestamp...which is basically computer time in milliseconds from 1st Jan 1970...or milliseconds passed since 1st Jan 1970.
We can customise it as we want....


#### Getting Started:  
The project is comprised of 2 Components:  
	a. Extracting Data From Original Database & Deleting it  
	b. Cleaning the Extracted Data & ReFILLING the Database with values as we want.  




#### Prerequisites: [LINUX or Windows]

	a) Python Scripts- 
				  1) Python 3.x
				  2) pip for Python 3  
				  3) MySQL Server 
				  4) Python Packages- mysqlclient

	b) Database-
				  1) MySQL Server
				  	 (separate)					  




#### STEPS:
	a) First run extractor.py. & wait for it to finish.  
	b) Then run  cleaner.py & wait for it to finish.  



#### Authors:
coded with love by AAYUSH GADIA 
