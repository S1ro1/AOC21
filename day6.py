#days = 80
days = 256
#bruteforce approach
'''
class Fishy:
    def __init__(self, timer, age):
        self.timer = timer
        self.age = age

    def reproduce(self, fish_list):
        if self.timer < 1:
            self.timer = 6
            fish_list.append(Fishy(timer=8, age=0))
        else:
            if self.age != 0:
                self.timer -= 1
        self.age += 1

def main():
    all_fish = []
    with open("data/day6.txt") as f:
        for timer in f.readline().split(","):
            all_fish.append(Fishy(timer=int(timer), age=1))
    
    for i in range(days):
        for fish in all_fish:
            fish.reproduce(all_fish)
'''

#optimized for part 2
def main():
    all_fish = [0] * 9
    with open("data/day6.txt") as f:
        for timer in f.readline().split(","):
            all_fish[int(timer)] += 1

    for i in range(days - 1):
        all_fish = all_fish[1:] + all_fish[:1]
        all_fish[7] += all_fish[0]

    print(sum(all_fish))


if __name__ == main():
    main()