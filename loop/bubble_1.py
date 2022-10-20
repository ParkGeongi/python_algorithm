from random_list import Random_list


class Bubble(object):
    def __init__(self) -> None:
        pass
    def print(self):
        rl = Random_list()
        ls = rl.get_extract_random(1,101,10)
        print(ls)
        for j in range(len(ls)-1):
            for i in range(len(ls)-1):
                if ls[i] > ls[i+1]:
                    ls[i] , ls[i+1] = ls[i+1] , ls[i]     
        print(ls)        

    @staticmethod
    def main():
        bubble = Bubble()
        bubble.print()


Bubble.main()