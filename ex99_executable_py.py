# Executable Python Scripts

# Python scripts can be made directly executable, like shell scripts, by putting the line

#!/usr/bin/env python3.5

# (assuming that the interpreter is on the user’s PATH) 
# at the beginning of the script and giving the file an executable mode. 
# The #! must be the first two characters of the file. 

# The script can be given an executable mode, or permission, using the chmod command.

$ chmod +x myscript.py