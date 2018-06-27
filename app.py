def teststorage():
 import json,time,os
 m=''
 a=[]
 b=[0,1,2,3,4,5,6,7,8,9,10]
 
 if not os.path.exists('fair.txt'):
   with open('fair.txt','w') as zzil:
     json.dump(a,zzil)

 
 for i in b:
   time.sleep(1)
   if i !=10:
     if os.path.exists('fair.txt'):
       with open('fair.txt','r') as fil:
         a=json.load(fil)
         #print(a)
         a.append(i)
       with open('fair.txt','w') as til:
         json.dump(a,til)
       with open('fair.txt','r') as fel:
         m=json.load(fel)
         print(m)
     if not os.path.exists('fair.txt'):
       with open('fair.txt','w') as zil:
         a.append(i)
         json.dump(a,zil)
   #else:
    # try:
      # with open('fair.txt','w') as bil:
       #  json.dump(None,bil)
    # except TypeError:
      # print('no')




if __name__ == "__main__":
    tp=teststorage()
