from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], 
	"excludes": ["tkinter","matplotlib","scipy","pandas","numpy","PIL"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "review_scraper",
        version = "0.1",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base)])