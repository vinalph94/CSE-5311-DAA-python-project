import numpy as np
import os

def printLcs(str1, str2, m, n, matrix): 
  
    # set to store all the possible LCS 
    s = set()  
    # Base case
    if m == 0 or n == 0: 
        s.add("") 
        return s 
  
    # If the last characters are same 
    if str1[m - 1] == str2[n - 1]: 
  
        # recurse with m-1 and n-1 in the matrix
        tmp = printLcs(str1, str2, m - 1, n - 1,matrix) 
  
        # append current character to all possible LCS of the two strings 
        for i in tmp: 
            s.add(i + str1[m - 1]) 
  
    # If the last characters are not same 
    else: 
  
        # If LCS can be constructed from top side of matrix
        if matrix[m - 1][n] >= matrix[m][n - 1]: 
            s = printLcs(str1, str2, m - 1, n,matrix) 
  
        # If LCS can be constructed from left side of matrix 
        if matrix[m][n - 1] >= matrix[m - 1][n]: 
            tmp = printLcs(str1, str2, m, n - 1,matrix) 
  
            # Merge two sets if matrix[m-1][n] == matrix[m][n-1] 
            # s will be empty if matrix[m-1][n] != matrix[m][n-1] 
            for i in tmp: 
                s.add(i) 
    return s 
  
# To find the length of LCS 
def lengthOfLcs(str1, str2): 
    m = len(str1)
    n = len(str2)
    c = [[0]*(n+1) for i in range(m+1)]
    b = [[0]*(n+1) for i in range(m+1)]

    
    for i in range(m + 1): 
        for j in range(n + 1): 
            
            if i == 0 or j == 0: 
                c[i][j] = 0
                
            elif str1[i - 1] == str2[j - 1]: 
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "\\"

            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = '^'
            
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = '<'
    return c,b
   

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
climate_data = np.genfromtxt(os.path.join(DIR_PATH, 'LCS1.txt'), delimiter = ',', skip_header = 1)


def readFile(fileName):
    rows = []
    with open(fileName, 'r') as f:
        for line in f:
            columns = line.strip().split(',')
            rows.append(columns)
    return rows

def printMatrix(s,m,n):
    # Do heading
    print()
    print("-"*((len(n)+1)*7))
    print(" "*8+"|"+""*7,end="")
    for i in range(0,len(n)):
        if i==0 : print("%5s " % "", end="")
        else : print("%5s " %i,end="")
    print()
    print("     ", end="")
    print(" "*3+"|"+""*5,end="")
    for element in n:
        #if element[0] : print("|%5s " % element, end="") else :
         print("%5s " % element, end="")
    print()
    for j in range(len(s[0])):
        print("--------", end="")
    print()
    # Matrix contents
    for i in range(len(s)):
        if i==0 : print("%3s " % "", end="")
        else : print("%3s " % (i), end="") # Row nums
        print("%3s |" % (m[i]), end="")
        
        for j in range(len(s[0])):
            print("%5s " % (s[i][j]), end="")
        print()  
    print("-"*((len(n)+1)*7))


input = []
input = readFile("LCS1.txt")
str1 = input[0][0]
str2 = input[0][1]
str3 = input[1][0]
str4 = input[1][1]
str5 = input[2][0]
str6 = input[2][1]
str7 = input[3][0]
str8 = input[3][1]

matrix1, matrix2 = lengthOfLcs(str1,str2) 
lcs1 = printLcs(str1,str2,len(str1),len(str2),matrix1)
lcs_matrix1 = np.array(matrix1)
lcs_matrix2 = np.array(matrix2)
print("\n")
name1 = list("X"+str1)
name2 = list("Y"+str2)
# using str() to convert each element to string
res1 = [[str(ele) for ele in sub] for sub in lcs_matrix1]
res2 = [[str(ele) for ele in sub] for sub in lcs_matrix2]
results1 = [['0' if res1[i][j]=='0' and res2[i][j]=='0' else res2[i][j] + res1[i][j] for j in range(len(res1[0]))] for i in range(len(res1))]
print("X =\""+str1+"\"    Y=\""+str2+"\"")
printMatrix(results1,name1,name2)
print("Length of Longest Common Subsequence is : {}".format(matrix1[-1][-1]))
print("The Longest Common Subsequence of '"+ str1 + "' and '" + str2 + "' is "+str(lcs1)[1:-1])


matrix3, matrix4 = lengthOfLcs(str3,str4) 
lcs2 = printLcs(str3,str4,len(str3),len(str4),matrix3)
#lcs2  = sorted(lcs2)
lcs_matrix3 = np.array(matrix3)
lcs_matrix4 = np.array(matrix4)
print("\n")
#print(lcs_matrix2)
name3 = list("X"+str3)
name4 = list("Y"+str4)
# using str() to convert each element to string
res3 = [[str(ele) for ele in sub] for sub in lcs_matrix3]
res4 = [[str(ele) for ele in sub] for sub in lcs_matrix4]
results3 = [['0' if res3[i][j]=='0' and res4[i][j]=='0' else res4[i][j] + res3[i][j] for j in range(len(res3[0]))] for i in range(len(res3))]
print("X =\""+str3+"\"    Y=\""+str4+"\"")
printMatrix(results3,name3,name4)
print("Length of Longest Common Subsequence is : {}".format(matrix3[-1][-1]))
print("The Longest Common Subsequence of '"+ str3 + "' and '" + str4 + "' is "+str(lcs2)[1:-1])


matrix5, matrix6 = lengthOfLcs(str5,str6) 
lcs3 = printLcs(str5,str6,len(str5),len(str6),matrix5)
lcs_matrix5 = np.array(matrix5)
lcs_matrix6 = np.array(matrix6)
print("\n")
name5 = list("X"+str5)
name6 = list("Y"+str6)
# using str() to convert each element to string
res5 = [[str(ele) for ele in sub] for sub in lcs_matrix5]
res6 = [[str(ele) for ele in sub] for sub in lcs_matrix6]
results5 = [[' 0' if res5[i][j]=='0' and res6[i][j]=='0' else res6[i][j] + res5[i][j] for j in range(len(res5[0]))] for i in range(len(res5))]
print("X =\""+str5+"\"    Y=\""+str6+"\"")
printMatrix(results5,name5,name6)
print("Length of Longest Common Subsequence is : {}".format(matrix5[-1][-1]))
print("The Longest Common Subsequence of '"+ str5 + "' and '" + str6 + "' is "+str(lcs3)[1:-1])


matrix7, matrix8 = lengthOfLcs(str7,str8) 
lcs4 = printLcs(str7,str8,len(str7),len(str8),matrix7)
lcs_matrix7 = np.array(matrix7)
lcs_matrix8= np.array(matrix8)
print("\n")
name7 = list("X"+str7)
name8 = list("Y"+str8)
resultname8 = '   '.join(str(item) for item in name8)
# using str() to convert each element to string
res7 = [[str(ele) for ele in sub] for sub in lcs_matrix7]
res8 = [[str(ele) for ele in sub] for sub in lcs_matrix8]
results7 = [['  0' if res7[i][j]=='0' and res8[i][j]=='0' else res8[i][j] + res7[i][j] for j in range(len(res7[0]))] for i in range(len(res7))]
print("X =\""+str7+"\"    Y=\""+str8+"\"")
printMatrix(results7,name7,name8)
print("Length of Longest Common Subsequence is : {}".format(matrix7[-1][-1]))
print("The Longest Common Subsequence of '"+ str7 + "' and '" + str8 + "' is "+str(lcs4)[1:-1])









