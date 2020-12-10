"""
Running your source code from the root level of the package.

The __init__.py file of our package (rec_package) is automatically 
run for us everytime we import the package, which can help hide the 
hierarchical complexity of our module structure behind the scenes.
"""

# from rec_package import recommender, config ### <--- BEFORE __init__.py
from rec_package import Recommender, MOVIES  ### <--- AFTER __init__.py


import pandas as pd

if __name__ == "__main__":
    # rec = recommender.Recommender(config.MOVIES) ### <--- BEFORE __init__.py
    rec = Recommender(MOVIES)  ### <--- AFTER __init__.py
    print(rec.simple_recommend(5))
    print(pd.__file__)
