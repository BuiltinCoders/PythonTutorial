import time
# # # Time module
#  # time module get the time duration taken to reach that perticular time function

initial1 = time.time()
count = 0
while count<51:
    print(count)
    time.sleep(2)     # --------> here sleep method of time module is used
    count+=1
print(f"Time taken by while loop: {time.time()-initial1}s")

# t1 = time.time()        # -----> time method in time module
# for i in range(51):
#     print(i)

# print(f"Time taken by for loop: {time.time()-t1}s")



# # More Methods of Time Module

 # 1. ascttime, localtime, time
  
  # i) ascttime
   # ascttime method takes time in tuple format and convert it into string format
  
  # ii) localtime
   # localtime gives local time in tuple format
  
  # iii) time
   # time method of time module gives number of ticks
  
  # iv) sleep method
   # sleep method used when we want to wait the programe for specific time period

 # How to get local time of pc in a string representable format
localtime = time.asctime(time.localtime(time.time()))
print(localtime)

 # How to use sleep method
time.sleep(2)   

# 