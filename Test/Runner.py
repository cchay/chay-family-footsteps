import os
import sys

ClassPath = "./Unit/PlayerTest.py"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append( os.path.abspath( ClassPath ) )

# Do the import
import PlayerTest

