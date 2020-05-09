# PythonKeyLogger
This is a basic Keylogger program used for logging user ids and passwords in a text file.
If this program is running int the background then it will log everything that is typed, during that Session under a file called "log.txt".
It uses the pynput library of Python which allows us to control the inpyt devices like Keyboard and Mouse.
We use the with keyword, quite extensively as you would see. It is so because we know that listeners and opening files, leads to allocation of some  resourcess and we 
have to release the resources using close() etc. To avoid that we use the 'with' keyword.
