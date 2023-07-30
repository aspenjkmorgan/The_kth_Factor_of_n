'''You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.
Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 
if n has less than k factors.
'''
class Solution:
      
    def kthFactor(n: int, k: int) -> int:
        
        # get list of factors in sorted order
        factors_list = [1]
        end = int(n/2) + 1
        for i in range(2, end):
            remainder = n % i
            if remainder == 0:
                factors_list.append(i)
        factors_list.append(n) # add n itself last

        if len(factors_list) >= k:
            return factors_list[k - 1]
        else:
            return -1
    
def main():
    n = int(input('Enter n: '))
    k = int(input('Enter k: '))
    print(Solution.kthFactor(n, k))

if __name__ == "__main__":
    main()