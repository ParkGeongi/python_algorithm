from random_list import Random_list

class Bubble(object):
    def __init__(self) -> None:      
        pass
    
    def sort(self):
        pass

    def print(self):
        rl=Random_list()
        ls_a = rl.get_extract_random(1,101,100)
        for i in range(len(ls_a)- 1):
            print(f"element : {ls_a[i]}")



    @staticmethod
    def main():
        bubble=Bubble()
        bubble.print()
        
Bubble.main()