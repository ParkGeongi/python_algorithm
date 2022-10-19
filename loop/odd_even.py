from random_list import Random_list

class Odd_even:
    def __init__(self) -> None:
        pass

    def print(self):
        rl = Random_list() 
        print(rl.get_extract_random(1,101,10))
        
        for i in rl.get_extract_random(1,101,10):
            if i % 2 == 0:
                print(f"even {i}")
            else:
                print(f"odd {i}")
        
    @staticmethod
    def main():
        oe = Odd_even()
        oe.print()

Odd_even.main()
