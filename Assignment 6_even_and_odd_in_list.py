list1=[12,8,3,9,6,20,5,79,34,43]
even_count,odd_count=0,0
for num in list1:
    if num%2==0:
      even_count+=1
    else:
        odd_count+=1
print("even numbers available in the list:",even_count)
print("odd numbers available in the list:",odd_count)