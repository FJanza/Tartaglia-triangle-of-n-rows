
def sumador_de_i(i):
    sum_i = 0 

    for sum in range(0,i):
        sum_i = sum_i + sum

    return(sum_i)


#--------------------------------------------------
def print_terminal_1():

    rows = input("ingrese cuantas filas tendra el triangulo de tartaglia/pascal: ")

    for i in range(0,int(rows)):
        print(i, end="  ")

        for j in range(0,i+1):
            

            if j == 0 or j == i: 
                print("1",end="")

            elif j == 1 or j == i-1:
                print(i, end="")

            elif j == 2 or j == i-2:
                print( sumador_de_i(i) , end="")
            
            elif i%2==0:
                print(sumador_de_i(i-1)+sumador_de_i(i-1), end="")
            elif i%2==1:
                print(sumador_de_i(i-1)+sumador_de_i(i-2), end="")
            
             
        print("")
#--------------------------------------------------
def print_terminal_2():

    rows = input("ingrese cuantas filas tendra el triangulo de tartaglia/pascal: ")


    triangulo=[]
    m=int(rows)
    n=m+1

    for f in range (m):
        triangulo.append([])
        for c in range(n):
            triangulo[f].append(0)

    triangulo[0][0] = 1

    for i in range(1,m):

        for j in range(0,n): 

            triangulo[i][j] = triangulo[i-1][j] + triangulo[i-1][j-1]
        
    for i in range (m):

        print(i,end="   ")

        
        for k in range(0,(m-i)):
            print(" ",end="")

        for j in range (n):
            if triangulo[i][j] != 0:
                
                print(triangulo[i][j],end=' ')

        print()
        

        
        

        
#--------------------------------------------------
def main():
    print_terminal_2()


#--------------------------------------------------
if __name__ == '__main__':
    main()  