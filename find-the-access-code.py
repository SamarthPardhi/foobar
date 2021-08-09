# # Find the Access Codes
# # =====================

# # In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it. But the only door leading to the LAMBCHOP chamber is secured with a unique lock system whose number of passcodes changes daily. Commander Lambda gets a report every day that includes the locks' access codes, but only the Commander knows how to figure out which of several lists contains the access codes. You need to find a way to determine which list contains the access codes once you're ready to go in. 

# # Fortunately, now that you're Commander Lambda's personal assistant, Lambda has confided to you that all the access codes are "lucky triples" in order to make it easier to find them in the lists. A "lucky triple" is a tuple (x, y, z) where x divides y and y divides z, such as (1, 2, 4). With that information, you can figure out which list contains the number of access codes that matches the number of locks on the door when you're ready to go in (for example, if there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access codes).

# # Write a function solution(l) that takes a list of positive integers l and counts the number of "lucky triples" of (li, lj, lk) where the list indices meet the requirement i < j < k.  The length of l is between 2 and 2000 inclusive.  The elements of l are between 1 and 999999 inclusive.  The solution fits within a signed 32-bit integer. Some of the lists are purposely generated without any access codes to throw off spies, so if no triples are found, return 0. 

# # For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the solution 3 total.

# # Languages
# # =========

# # To provide a Java solution, edit Solution.java
# # To provide a Python solution, edit solution.py

# # Test cases
# # ==========
# # Your code should pass the following test cases.
# # Note that it may also be run against hidden test cases not shown here.

# # -- Java cases --
# # Input:
# # Solution.solution([1, 1, 1])
# # Output:
# #     1

# # Input:
# # Solution.solution([1, 2, 3, 4, 5, 6])
# # Output:
# #     3

# # -- Python cases --
# # Input:
# # solution.solution([1, 2, 3, 4, 5, 6])
# # Output:
# #     3

# # Input:
# # solution.solution([1, 1, 1])
# # Output:
# #     1

# def solution(l):
#     def factors(i):
#         l=[1]
#         for j in range(1,i):
#             if i%j==0:
#                 l.append(j)
#         return l
#     ans=0
#     n1=l.count(1)
#     # for i in l:
#     #     for j in factors(i):
#     #         if j in l:
#     #             for k in factors(j):
#     #                 if k in l:
#     #                     ans+=1
#     #                     print(k,j,i)
#     #                 elif n1>0:
#     #                     ans+=1
#     #         elif n1==2:
#     #             ans+=1
    
#     return ans

# # import random
# # l=[]
# # for i in range(2000):
# #     l.append(random.randint(100000,1000000))
# # print(solution(l))

# print(solution([1,2,3,4,5,6]))
# print(solution([1,1,1]))




# def solution(l):

#     def factors(n):
#         i=1
#         l=[]
#         while i<=n/i:
#             if n%i==0:
#                 l+=[int(n/i),int(i)]
#             i+=1
#         if n==1:
#             return [1]
#         else:
#             return sorted(list(set(l)))[::-1]

#     l=sorted(l)[::-1]
#     factors_matrix=[]
#     for i in l:
#         factors_matrix.append(factors(i))
#     ans=[]
#     for i in range(len(factors_matrix)):
#         for j in range(i+1,len(factors_matrix)):
#             if factors_matrix[j][0] in factors_matrix[i]:
#                 for k in range(j+1, len(factors_matrix)):
#                     if factors_matrix[k][0] in factors_matrix[j]:
#                         if not [factors_matrix[i][0],factors_matrix[j][0],factors_matrix[k][0]] in ans:
#                             ans.append([factors_matrix[i][0],factors_matrix[j][0],factors_matrix[k][0]])
#     return len(ans)


# def solution1(l):
#     l=sorted(l)[::-1]
#     ans=0
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[i]%l[j]==0:
#                 for k in range(j+1, len(l)):
#                     if l[j]%l[k]==0 and i<j<k:
#                         print(l[k],l[j],l[i])
#                         ans+=1
#     return ans


def solution(l):
    # l=sorted(l)
    c = [0] * len(l)
    count = 0
    for i in range(0,len(l)):
        j=0
        for j in range(0, i):
            if l[i] % l[j] == 0:
                c[i] = c[i] + 1
                count = count + c[j]
    return count    

# print(solution1([7,6,1,1,5]))
# print(solution1([1,2,3,4,5,6]))



import random
for case in range(10):
    l=[]
    for i in range(5):
        l.append(random.randint(1,5))
    # l=sorted(l)
    print(l,solution1(l),solution(l))

# print(solution1([1,2,3,4,5,6]),solution([1,2,3,4,5,6]))
# print(solution1([1,1,1]),solution([1,1,1]))
# print(solution1([1,1,2,2]),solution([1,1,2,2]))