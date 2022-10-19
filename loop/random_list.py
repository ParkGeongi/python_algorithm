import random

class Random_list(object):

    def __init__(self) -> None:      
        pass

    def get_extract_random(self,start, end, count):
        return random.sample(range(start,end), count) # getter 임 return 있으니까
    
    def print(self):
        print(self.get_extract_random(1, 101, 10))
"""

    @staticmethod
    def main():
        rl=Random_list()
        rl.print()

Random_list.main()

"""
if __name__ == "__main__":
    rl = Random_list()
    rl.print()

    