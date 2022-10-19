import random

class Bubble(object):
    def __init__(self) -> None:      
        pass
        
    def extract_random(self):      
        return random.sample(range(1,101), 10)
    
    def print(self):
        for i in self.extract_random():
            if i % 2 ==0:
                print(f"짝수 {i}")
            else:
                print(f"홀수 {i}")
        
    @staticmethod
    def main():
        bubble=Bubble()
        bubble.print()
        
Bubble.main()