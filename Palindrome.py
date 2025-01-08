def palindrome(a):
 
    c = 0       #initializing a counter variable
    l = len(a)  
    z = (l//2)  #storing the midpoint in a variable
    if (len(a) % 2 != 0):
        z = z+1     #increasing value of midpoint by 1 if the length of the array is odd
    
    for i in range(z):  #running a loop from i till the midpoint

        if (a[0] != a[l-1]): #Basis condition
            break;

        elif (a[i] == a[l-i-1]):  #checking if ith term from the 
                                #beginning is equal to the ith term from the end
            c=c+1       #increasing the value of the counter

    if (c == z):            #check if the value of the counter equals that of the midpoint
                            #print appropriate message
        print("Palindrome");
    else:
        print("Not Palindrome");
 
# Driver code.
p = [3,4,5,4,3]
q = [1,2,1,1,2,1]
r = [0,3,6]
palindrome(p)
palindrome(q)
palindrome(r)
