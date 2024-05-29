x=int(input())
cnt=0
while(x>2e9):
 print('number too large, limit 2e9')
 x=int(input())

for i in range(1,x+1):
 if x%i==0:
  cnt += 1
  
print(cnt)
