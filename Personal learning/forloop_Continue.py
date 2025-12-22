#printing all numbers from 1 to 20 but skips any number that is divisible by 3
for num in range(1, 21):
    if num % 3 == 0:
        continue
    print(num)
