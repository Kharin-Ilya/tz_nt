with open(input(), encoding='utf-8')  as file:
  
    my_list = list(map(int, file.readlines()))
mid = sorted( my_list)[len(my_list) // 2]
print(sum(abs(i - mid) for i in my_list))