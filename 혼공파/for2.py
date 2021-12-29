numbers =[1,2,3,4,5,6,7,8,9]
output =[ [], [], [] ]
for number in numbers:
    output[(number-1)%3].append(number)
      #  output[(1-1)%3].append(1)  > output[0].append(1)
      #  output[(2-1)%3].append(2)  > output[1].append(2)
      #  output[(3-1)%3].append(3)  > output[2].append(3)
      #  output[(4-1)%3].append(4)  > output[0].append(4)
print(output)