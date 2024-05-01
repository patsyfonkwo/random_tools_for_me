''' DELETES ALL FILES WITH "unnamed" IN TITLE '''
''' RUN INSIDE OF DOWNLOADS DIRECTORY         '''

import os
import shutil
from pathlib import Path



if __name__ == "__main__":
        
        downloads = Path("./")

        for file in downloads.iterdir():
                if file.is_file() and ("unnamed" in os.path.basename(file)):
                        print("Moving", os.path.basename(file), "to Trash...")
                        os.remove(file)

        print("\nOperation Complete")
