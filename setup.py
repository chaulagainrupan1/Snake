import os
import cx_Freeze
os.environ['TCL_LIBRARY'] ="C:\\Users\Rupan\AppData\Local\Programs\Python\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] ="C:\\Users\Rupan\AppData\Local\Programs\Python\Python36-32\\tcl\\tk8.6"


executables = [cx_Freeze.Executable("Snake Game.py")]

cx_Freeze.setup(
    name="Slither",
    options={"build_exe":{"packages":["pygame"],"include_files":["apple.png","snakehead1.png"]}},

    description = "Slither game",
    executables = executables
     )
