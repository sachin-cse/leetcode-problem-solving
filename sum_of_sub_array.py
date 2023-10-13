def all_count_array(arr,n):
    res = 0
    sum = 0
    for i in range(n):
        for j in range(i,n):
            sum = sum + arr[j]
            
            if sum == k:
                res+=1
    return res

if __name__ == '__main__':
    
   arr = [10, 2, -2, -20, 10]
   n = len(arr)
   k = -10
   
   print(all_count_array(arr,n))   