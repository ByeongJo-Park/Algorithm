S = input()
T ='abcdefghijklmnopqrstuvwxyz'
K = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
A = len(S)
for i in range(len(S)):
    if S[i] == '=':
        if S[i-1] == 'z' and S[i-2] == 'd':
                A -= 1      
        A -= 1
    
    if S[i] == 'j':
        if S[i-1] == 'n' or S[i-1] == 'l':
            A -= 1
            
    if S[i] == '-':
        A -= 1
        
print(A)