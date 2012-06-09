
ServiceRunner

ServiceRunner Copyright 2011 Michael Geier.
ServiceRunner is licensed under Microsoft Public License (Ms-PL).

http://servicerunner.codeplex.com/
http://www.mickbitsoftware.com/

ServiceRunner makes it possible to run "ordinary" applications as service. 
This might be helpful for autostart applications which do not provide to 
install themselves as service. ServiceInstaller helps to install 
ServiceRunner as Windows service. Both is developed in C#.

How to use ServiceRunner:

1. Enter the desired values in the configuration file.

   The configuration file must be named "config.txt". It must be located 
   in the same directory as the executable files "ServiceInstaller.exe" and 
   "ServiceRunner.exe".
   
   "config.txt" must contain two or three lines:
   1st line: the service name used to register the service on your system.
   2nd line: the full path and filename of the executable file to be executed 
   by ServiceRunner.
   3rd line (optional): The arguments to be passed to the executable specified
   in the 2nd line.
   
   Example:
   Windows Remote Service
   C:\Program Files\wrs\wrs.exe
   -s
   
   Be sure not to have a 4th or 6th blank line in your config file! Also avoid
   leading or trailing spaces.
   
2. Start "ServiceInstaller.exe" as Administrator or with administrative 
   privileges.
   
   Click on the button "Install". It installs "ServiceRunner.exe" as service 
   using the name specified in the first line of the config file (svcname)
   using the following command line:
   
   sc create [svcname] binpath= "[path]\ServiceRunner.exe" 
   DisplayName= [svcname] type= own start= auto
   
   Btw, clicking "Uninstall" executes the following command:
  
   sc delete [svcname]
  
3. Start your newly created service by clicking "Start".

  If you want to configure your service use the command line tool sc or go to 
  the Windows Control Panel -> Services. Here you can, for example, change the
  user account under which the service will be started.
  
  From Control Panel -> Services you can also start and stop your service.
  
4. You can now close "ServiceInstaller". If the start type of the service is 
  set to "Automatic" it will be started automatically on booting Windows before
  reaching the logon screen.
  
5. To uninstall your service run "ServiceInstaller.exe" and click "Uninstall".
  Be sure you have stopped the service before uninstalling it!
  
Additional information:

"ServiceRunner.exe" cannot be run by double-clicking the file.
It contains the service code and can only be started as service.

You don't have to use "ServiceInstaller.exe" to install the 
"ServiceRunner.exe" service. It exists only for your convenience.
Use the tool sc from the command line if you want to install the
service manually (using a similar command line as shown somewhere 
above in this document).

When starting the ServiceRunner-service "ServiceRunner.exe" starts
the program you specified in config.txt. But as it is started in 
the context of a service you won't see a user interface - even if
you specify to run the service using some user account (like
"Adoministrator"). This is an intended limitation of Windows.
Check the task manager (tab "Processes") to check if your program
was started successfully and is currently running.

If you need to see a user interface (for configuring your application,
for example) don't use "ServiceRunner.exe". Instead stop the service 
and run the program directly ("as usual").

If you stop the ServiceRunner-service "ServiceRunner.exe" kills the
process it started before.

In case of an error or in case of unexpected behavior take a look at 
the logfile log.txt.