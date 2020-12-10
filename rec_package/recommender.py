### 1. Module Docstring
"""Module Docstring"""

### 2. Imports
import random
import rec_package.config as config

### 3. CONSTANTS (usually in all caps)

### 4. Classes and Functions
class Recommender:
    """
    Class Docstring.
    """

    def __init__(self, items: list):
        self.items = items

    def __repr__(self):
        return f"<Recommender({self.items})>"

    def simple_recommend(self, num: int) -> list:
        # type annotations, checkout the library mypy
        """
        Method Docstring.
        """
        result = random.choices(self.items, k=num)
        result = [i.lower() for i in result]
        return result

    def nmf_recommend(self):
        """
        Coming soon in version 2.0.
        """
        pass

    def cosim_recommend(self):
        """
        Coming soon in version 2.0.
        """
        pass


### 5. Main block
if __name__ == "__main__":
    # Whatever code is included below, please ONLY execute if I run "python recommender.py"
    # DO NOT, however, execute any of the code below if I merely IMPORT recommender.py, i.e. "import recommender"

    rec = Recommender(config.MOVIES)
    print(rec.simple_recommend(5))
