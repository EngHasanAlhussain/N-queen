from tkinter import *
import random
import time

#method for Stopping the program
def stop():
    print("program is terminated")
    exit(0)

def A_loop(list1):
    print("A_loop")
    j=0
    tic = time.perf_counter()  # To count time spent
    t = 0  # initial time
    while j<25:
        hit0 = Fitness_Function(list1)
        if hit0 == 0:
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            toc = time.perf_counter()
            t = toc - tic
            print_board(list1,j,t)
        i = 0
        if hit0 == 0:
            break
        while i < 8:
            list_copy1 = list1.copy()
            list_copy1[i]=1
            list_copy2 = list1.copy()
            list_copy2[i]=2
            list_copy3 = list1.copy()
            list_copy3[i]=3
            list_copy4 = list1.copy()
            list_copy4[i]=4
            list_copy5 = list1.copy()
            list_copy5[i]=5
            list_copy6 = list1.copy()
            list_copy6[i]=6
            list_copy7 = list1.copy()
            list_copy7[i]=7
            list_copy8 = list1.copy()
            list_copy8[i]=8

            hits = [None] * 8
            hits[0]= Fitness_Function(list_copy1)
            hits[1] = Fitness_Function(list_copy2)
            hits[2] = Fitness_Function(list_copy3)
            hits[3] = Fitness_Function(list_copy4)
            hits[4] = Fitness_Function(list_copy5)
            hits[5] = Fitness_Function(list_copy6)
            hits[6] = Fitness_Function(list_copy7)
            hits[7] = Fitness_Function(list_copy8)
            x=hits.index(min(hits))
            if x== 0:
                list1=list_copy1.copy()
            elif x==1:
                list1=list_copy2.copy()
            elif x == 2:
                list1 = list_copy3.copy()
            elif x == 3:
                list1 = list_copy4.copy()
            elif x == 4:
                list1 = list_copy5.copy()
            elif x == 5:
                list1 = list_copy6.copy()
            elif x == 6:
                list1 = list_copy7.copy()
            elif x == 7:
                list1 = list_copy8.copy()
            i = i + 1
        j=j+1
    print(j)


#If genetic algorithm is selected
def clicked_GA():

    lbl.configure(text="Okay, the puzzle will be solved using genetic algorithm\n Click Run!",fg="#000151")
    btn = Button(window, text="Run GA", font=("Arial Bold", 16), bg="yellow", fg="purple",command=GA_fun)
    btn.grid(column=66, row=8)
#Genetic function execution
def GA_fun():

    # Generate initial population of size 64
    list1=  []
    list2 = []
    list3 = []
    list4 = []
    list5=[]
    list6=[]
    list7 = []
    list8 = []
    i=0
    #list1 contains random 8 numbers
    while i<8:
        temp=random.randrange(1,9)
        list1.append(temp)
        i=i+1
    # list2 contains random 8 numbers
    i=0
    while i<8:
        temp=random.randrange(1,9)
        list2.append(temp)
        i=i+1
    # list3 contains random 8 numbers
    i = 0
    while i<8:
        temp=random.randrange(1,9)
        list3.append(temp)
        i=i+1
    # list4 contains random 8 numbers
    i=0
    while i<8:
        temp=random.randrange(1,9)
        list4.append(temp)
        i=i+1
    # list5 contains random 8 numbers
    i = 0
    while i < 8:
        temp = random.randrange(1, 9)
        list5.append(temp)
        i = i + 1
    # list6 contains random 8 numbers
    i = 0
    while i < 8:
        temp = random.randrange(1, 9)
        list6.append(temp)
        i = i + 1
    # list7 contains random 8 numbers
    i = 0
    while i < 8:
        temp = random.randrange(1, 9)
        list7.append(temp)
        i = i + 1
    # list8 contains random 8 numbers
    i = 0
    while i < 8:
        temp = random.randrange(1, 9)
        list8.append(temp)
        i = i + 1
    # Now I have 8 Gens which are the initial population
    #Call genetic loop and pass all population
    Genetic_loop(list1,list2,list3,list4,list5,list6,list7,list8)

#Genetic loop execurion
def  Genetic_loop(list1,list2,list3,list4,list5,list6,list7,list8):

    f=0     #to count number of Iterations
    tic = time.perf_counter() #To count time spent
    t=0   #initial time
    while f<7000: #Iterate for 7000 times
        # pass Gen 1 to fitness function
        hit1 = Fitness_Function(list1)
        # pass Gen 2 to fitness function
        hit2 = Fitness_Function(list2)
        # pass Gen 3 to fitness function
        hit3 = Fitness_Function(list3)
        # pass Gen 4 to fitness function
        hit4 = Fitness_Function(list4)
        # pass Gen 5 to fitness function
        hit5 = Fitness_Function(list5)
        # pass Gen 6 to fitness function
        hit6 = Fitness_Function(list6)
        # pass Gen 7 to fitness function
        hit7 = Fitness_Function(list7)
        # pass Gen 8 to fitness function
        hit8 = Fitness_Function(list8)
        # Calculate the total number of hits
        hits=hit1+hit2+hit3+hit4+hit5+hit6+hit7+hit8
        # NOw, check if one of the candidate solutions is fit and has zero hits(attacks)
        # if so, then solution is found, stop counting f and time and print the board
        if hit1 ==0:

            toc = time.perf_counter()
            t = toc - tic
            solution_found(list1,f,t)
            print_board(list1,f,t)
            break
        elif hit2==0:
            toc = time.perf_counter()
            t = toc - tic
            solution_found(list2,f,t)
            print_board(list2,f,t)
            break
        elif hit3==0:
            toc = time.perf_counter()
            t = toc - tic
            solution_found(list3,f,t)
            print_board(list3,f,t)
            break
        elif hit4==0:
            toc = time.perf_counter()
            t = toc - tic
            solution_found(list4,f,t)
            print_board(list4,f,t)
            break
        elif hit5==0:
            toc = time.perf_counter()
            t = toc - tic
            solution_found(list5,f,t)
            print_board(list5,f,t)
            break
        elif hit6==0:
            toc = time.perf_counter()
            t = toc - tic
            solution_found(list6,f,t)
            print_board(list6,f,t)
            break
        elif hit7==0:
            toc = time.perf_counter()
            t = toc - tic
            solution_found(list7,f,t)
            print_board(list7,f,t)
            break
        elif hit8==0:
            toc = time.perf_counter()
            t = toc - tic
            solution_found(list8,f,t)
            print_board(list8,f,t)
            break
        #Nowm Selection is executed
        fitness_values = [hit1, hit2, hit3, hit4,hit5,hit6,hit7,hit8]
        # Now we find the weakest gen, and eleminate it
        # and the strongest gen and duplicate it
        x=fitness_values.index(min(fitness_values))
        y=fitness_values.index(max(fitness_values))
        if y==0 and x==3:
            list1 = list4.copy()
        elif y==0 and x==2:
            list1 = list3.copy()
        elif y == 0 and x == 1:
            list1 = list2.copy()
        elif y == 0 and x == 4:
            list1 = list5.copy()
        elif y == 0 and x == 5:
            list1 = list6.copy()
        elif y == 0 and x == 6:
            list1 = list7.copy()
        elif y == 0 and x == 7:
            list1 = list8.copy()
        elif y == 1 and x == 3:
            list2 = list4.copy()
        elif y == 1 and x == 2:
            list2 = list3.copy()
        elif y == 1 and x == 0:
            list2 = list1.copy()
        elif y == 1 and x == 4:
            list2 = list5.copy()
        elif y == 1 and x == 5:
            list2 = list6.copy()
        elif y == 1 and x == 6:
            list2 = list7.copy()
        elif y == 1 and x == 7:
            list2 = list8.copy()
        elif y == 2 and x == 3:
            list3 = list4.copy()
        elif y == 2 and x == 1:
            list3 = list2.copy()
        elif y == 2 and x == 0:
            list3 = list1.copy()
        elif y == 2 and x == 4:
            list3 = list5.copy()
        elif y == 2 and x == 5:
            list3 = list6.copy()
        elif y == 2 and x == 6:
            list3 = list7.copy()
        elif y == 2 and x == 7:
            list3 = list8.copy()
        elif y == 3 and x == 2:
            list4 = list3.copy()
        elif y == 3 and x == 1:
            list4 = list2.copy()
        elif y == 3 and x == 0:
            list4 = list1.copy()
        elif y == 3 and x == 4:
            list4 = list5.copy()
        elif y == 3 and x == 5:
            list4 = list6.copy()
        elif y == 3 and x == 6:
            list4 = list7.copy()
        elif y == 3 and x == 7:
            list4 = list8.copy()
        elif y == 4 and x == 0:
            list5 = list1.copy()
        elif y == 4 and x == 1:
            list5 = list2.copy()
        elif y == 4 and x == 2:
            list5 = list3.copy()
        elif y == 4 and x == 3:
            list5 = list4.copy()
        elif y == 4 and x == 5:
            list5 = list6.copy()
        elif y == 4 and x == 6:
            list5 = list7.copy()
        elif y == 4 and x == 7:
            list5 = list8.copy()
        elif y == 5 and x == 0:
            list6 = list1.copy()
        elif y == 5 and x == 1:
            list6 = list2.copy()
        elif y == 5 and x == 2:
            list6 = list3.copy()
        elif y == 5 and x == 3:
            list6 = list4.copy()
        elif y == 5 and x == 4:
            list6 = list5.copy()
        elif y == 5 and x == 6:
            list6 = list7.copy()
        elif y == 5 and x == 7:
            list6 = list8.copy()
        elif y == 6 and x == 0:
            list7 = list1.copy()
        elif y == 6 and x == 1:
            list7 = list2.copy()
        elif y == 6 and x == 2:
            list7 = list3.copy()
        elif y == 6 and x == 3:
            list7 = list4.copy()
        elif y == 6 and x == 4:
            list7 = list5.copy()
        elif y == 6 and x == 5:
            list7 = list6.copy()
        elif y == 6 and x == 7:
            list7 = list8.copy()
        elif y == 7 and x == 0:
            list8 = list1.copy()
        elif y == 7 and x == 1:
            list8 = list2.copy()
        elif y == 7 and x == 2:
            list8 = list3.copy()
        elif y == 7 and x == 3:
            list8 = list4.copy()
        elif y == 7 and x == 4:
            list8 = list5.copy()
        elif y == 7 and x == 5:
            list8 = list6.copy()
        elif y == 7 and x == 6:
            list8 = list7.copy()

        fitness_values.remove(max(fitness_values))
        x = min(fitness_values)
        fitness_values.append(x)
        fitness_values.sort()

     #Crossover Execution
        #Here I'm tring to avoid cross over with identical gen
        if list1==list2:
            temp=list1
            list1=list3
            list3=temp
        if list3 == list4:
            temp = list3
            list3 = list2
            list2 = temp
        if list5 == list6:
            temp = list5
            list5 = list1
            list1 = temp
        if list7 == list8:
            temp = list7
            list7 = list4
            list4 = temp
        list1_copy=list1.copy()
        list2_copy=list2.copy()
        list3_copy=list3.copy()
        list4_copy=list4.copy()
        list5_copy = list5.copy()
        list6_copy = list6.copy()
        list7_copy = list7.copy()
        list8_copy = list8.copy()
        list1_copy[3:8]=list2[3:8]
        list2_copy[3:8]=list1[3:8]
        list3_copy[4:8] = list4[4:8]
        list4_copy[4:8] = list3[4:8]
        list5_copy[3:8] = list6[3:8]
        list6_copy[3:8] = list5[3:8]
        list7_copy[4:8] = list7[4:8]
        list8_copy[4:8] = list8[4:8]
        list1=list1_copy.copy()
        list2=list2_copy.copy()
        list3=list3_copy.copy()
        list4=list4_copy.copy()
        list5 = list5_copy.copy()
        list6 = list6_copy.copy()
        list7 = list7_copy.copy()
        list8 = list8_copy.copy()
        #random change in one number of each gen
        list1[1]=random.randrange(1,9)
        list2[3]=random.randrange(1,9)
        list3[5]=random.randrange(1,9)
        list4[7]=random.randrange(1,9)
        list5[4] = random.randrange(1, 9)
        list6[2] = random.randrange(1, 9)
        list7[0] = random.randrange(1, 9)
        list8[6] = random.randrange(1, 9)
        f=f+1
        #End of loop
    #If 7000 iteration is used, then the population is not efficient enough
    #Though, go and initalize a new population again
    if f==7000:
        GA_fun()
    #If iterations less than 7000, then solution is find, print the board
    if f<7000:
        toc = time.perf_counter()
        t=toc - tic
        print(f,t)

#Print board
def print_board(list1,f,t):
    # creat_board
    array = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]
    list5=list1.copy()
    i=0
    while i<8:
        array[list5[i]-1][i]=1
        i=i+1

    i = 0
    while i < 8:
        j = 0
        while j < 8:
            lbl = Label(window, text=array[j][i], font=("Arial Bold", 50), bg="black", fg="grey")
            lbl.grid(column=i, row=j)
            j = j + 1
        i = i + 1
    #number of iteration f
    lbl = Label(window, text='Solution is found, Number of Iterations is %d'%(f),font=("Arial Bold", 24),bg="#6b868e", fg="#febe00")
    lbl.grid(column=65, row=4)
    # time spent
    lbl = Label(window, text='Solution found in %.4f seconds' % (t), font=("Arial Bold", 24),bg="#6b868e", fg="#febe00")
    lbl.grid(column=65, row=5)
    return 0

#Fitness function
def    Fitness_Function(gen):
    #creat_board
    array = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]
    i=0
    hits=0
    x=0
    while i<8:
        x=gen[i]
        array[x-1][i]=1
        i=i+1

    #calculate row hits
    i=0
    while i<8:
        j=0
        rows_=0
        while j<8:
            if array[i][j]==1:
                rows_=rows_+1
            j=j+1
        if rows_>1:
            hits=hits+1
        i=i+1

    # calculate diagonal / hits
    diagonal=0
    i=0
    while i<8:
        if array[7-i][7-i]==1:
            diagonal=diagonal+1
        i=i+1
    if diagonal>2:
        hits=hits+1

    # calculate diagonal \ hits
    i = 0
    diagonal=0
    while i < 8:
        if array[7-i][i] == 1:
            diagonal = diagonal + 1
        i=i+1
    if diagonal > 2:
        hits = hits + 1

    diagonal=0
    k=0
    while k<=7:
        i=0
        diagonal = 0
        while i<=k:
            if array[k - i][i] == 1:
                diagonal = diagonal + 1
            i=i+1
        if diagonal>1:
            hits=hits+1
        k=k+1

    diagonal = 0
    k = 0
    while k <= 7:
        i = 0
        diagonal = 0
        while i <= k:
            if array[7-i][7-k+i] == 1:
                diagonal = diagonal + 1
            i = i + 1
        if diagonal > 1:
            hits = hits + 1
        k = k + 1

    diagonal = 0
    k = 0
    while k <= 7:
        i = 0
        diagonal = 0
        while i <= k:
            if array[i][7 - k + i] == 1:
                diagonal = diagonal + 1
            i = i + 1
        if diagonal > 1:
            hits = hits + 1
        k = k + 1

    diagonal = 0
    k = 0
    while k <= 7:
        i = 0
        diagonal = 0
        while i <= k:
            if array[7-k+i][i] == 1:
                diagonal = diagonal + 1
            i = i + 1
        if diagonal > 1:
            hits = hits + 1
        k = k + 1

    return hits
#solution_found
def solution_found(list1,f,t):

    print(list1)
    y=print_board(list1,f,t)
    print("Congratulation!")
#####################################################################
#####################################################################
#########            Backtravking            ########################
#####################################################################
#####################################################################


#####################################################################
########To check if a position is attacked or not ###################
#####################################################################
def is_attack(board,i, j):
    #To check if there is a queen on the row or a column
    for k in range(0, N.get()):
        if board[i][k] == 1 or board[k][j] == 1:
             return True
    #Checks diagonals if there is an attack
    for k in range(0, N.get()):
        for l in range(0, N.get()):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False

#####################################################################
#This function for all Backtracking choices
#Based on the input it will do the search
#####################################################################
def MRV_MCV_LCV():

    ##Time start counting
    tic = time.perf_counter()  # To count time spent
    t = 0  # initial time
    # Build a chessboard NxN matrix with all elements 0
    board = [[0] * N.get() for _ in range(N.get())]
    #put the 1st queen in a random place in the 1st column
    board[random.randrange(N.get())][0]=1
    sum = [0]*N.get()           #This is a sum array that count how many positions that are not attacked and free
    count=0                     #Count number if Iterations
    while count<40:            #Loop starts the search
        ##################################
        #######Forward checking ##########
        ##################################
        if FC.get()==1:         #Based on the choices, if forward checking is selected, then do forward checking
            available=[1]*N.get() #This array used to check a step forward in the next column
                                  #Each time we assign a queen, and forward checking is selected, then do the checking

        j = 0              #Here we try to find the column with MRV and MCV
                           #MRV will start with the column with minimum remaining non-attack
        while j < N.get():
            i = 0
            while i < N.get():
                if not is_attack(board, i, j):
                    sum[j] = sum[j] + 1
                i=i+1
            j = j + 1
        prev_row=[0]*N.get() #initialze a prev_row array, this array will be used for backtracking, so I backtrack with prev. rows
        prev_col=[0]*N.get() #Same thing above with columns
        sum[sum.index(min(sum))]=N.get()-1  #Initially, ignore the first one because it is already has a queen

        if var_order1.get()==1 and var_order2.get()==0:
            x=min(sum)  #if MRV is selected and MCV is not, choose the col. with low non-attack
        elif var_order2.get()==1:
            if FC.get()==1:
                x=min(sum)
            else  :
                x=max(sum)  #if MCV is selected, choose the col. with high non-attack
        elif var_order2.get()==1 and var_order1.get()==1:
            x = max(sum)  #if both MRV &  MCV are selected, choose the maximum
        elif value.get()==1 or ARC.get()==1 or FC.get()==1:
            x=random.randrange(1,N.get()) #ELSE let it be random, because the ordering is not specified
        else:
            x = random.randrange(1, N.get())

        i = 0
        prev_i = 0  #To save the previous values indexes, in case we needed to for backtracking
        prev_j = 0
        flag = 0
        while i < N.get():
            ##########################################################
            ##If FC is selected, check before searching, to save time#
            ##########################################################
            if FC.get() == 1 and available[i]==0:
                i=i+1
                continue
            flag=0
            if not is_attack(board, i, x):
                #if the postion is not attacked, then assign 1 immediately, but if LCV is selected, this means that we need to be aware such
                #that we put the queen in a place that make flexibilty for other queens
                if value.get()==1:
                    l=0
                    next_col=[0]*N.get()
                    while l<N.get():
                        if not is_attack(board, l, x):
                           board[l][x] = 1
                           u=0
                           while u<N.get():
                              if not is_attack(board,u,(x+1)%N.get())==1:
                                 next_col[u]=next_col[u]+1
                              u=u+1
                        l=l+1
                    c=0
                    while c<N.get():
                        board[c][x]=0
                        c=c+1
                    d=next_col.index(max(next_col))
                    board[d][x]
                else:
                   board[i][x] = 1  #If LCV is not selected, we assign immediatly, based on the X value that is attained before from the MRV and MCV, etc.

                if ARC.get() == 1:  #if ARC is selected, do arc consistenty
                    ARC_check(board,int(i),int(x))
                #Save the position if we need to backtrack
                prev_i = i
                prev_j = x
                prev_row.append(i)
                prev_col.append(x)
                flag = 1 #a queen is assigned
            ################
            #######FC#######
            ################
            if FC.get() == 1 and flag==1:
                available[i] = 0  #becuase we assign we make the column unavaialbe

            if flag == 0:#If no place is avaialbe, then we backtrack using the previous saved arrays!
                a=0
                while a<len(prev_col):
                    if flag==1:
                        break
                    board[prev_row[a]][prev_col[a]]=0
                    p=0
                    while p<N.get():
                        if not is_attack(board, p, prev_col[a]):
                            if not p == prev_row[a]:
                                board[p][prev_col[a]] = 1
                                if ARC.get() == 1:
                                    ARC_check(board,p,prev_col[a])
                        p = p + 1
                    c = 0
                    while c < N.get():
                        if not is_attack(board, c, x):
                            board[c][x] = 1
                            if ARC.get() == 1:
                                ARC_check(board,c,x)
                            prev_row.append(c)
                            prev_col.append(x)
                            flag = 1
                        c=c+1
                    a = a + 1
                    if flag==0:
                        continue
            i = i + 1
        #After bakctracking, we go throghout the column and assign 1 to an avaialble place
        i=0
        while i<N.get():
            j=0
            while j<N.get():
                if board[i][j]==1:
                    break
                j=j+1

            k=0
            while k<N.get():
                m=0
                #################
                #####FC##########
                ###############
                if FC.get()==1 and available[m]==0:
                    k=k+1
                    continue

                while m<N.get():
                    if not is_attack(board,k,m):
                        board[k][m]=1
                        if ARC.get()==1:
                            #############
                            ####ARC######
                            #############
                          ARC_check(board,k,m)            ####After each assign. we do FC and ARC if selected
                            ############
                            ####FC#####
                            ###########
                        if FC.get()==1:
                            available[k]=0
                    m=m+1
                k=k+1
            i = i + 1
        #########################
        #now, we chack if all the queens are assigned and solution is found###
        ones=0
        i=0
        while i<N.get():
            j=0
            while j<N.get():
                if board[i][j]==1:
                    ones=ones+1
                j=j+1
            i=i+1
        if ones==N.get():  #If N queens are there, then the search is finished break!!
            count=count+1
            break
        if ones<N.get() and count==39:
            board = [[0] * N.get() for _ in range(N.get())]
            board[random.randrange(N.get())][0] = 1
            sum = [0] * N.get()
            count=0
            continue

        count=count+1

        toc = time.perf_counter()  #Time counter stops
        t = toc - tic
        x = sum.index(min(sum))
    #########################
    #####print the board#####
    #########################
    for i in board:
        print(i)
    print_board_2(board,t,count)

##############################
#####print board method#######
##############################
def print_board_2(array,t,f):
    i = 0
    while i < N.get():
        j = 0
        while j < N.get():
            lbl = Label(window, text=array[j][i], font=("Arial Bold", 50), bg="black", fg="grey")
            lbl.grid(column=i, row=j)
            j = j + 1
        i = i + 1
        # number of iteration f
    lbl = Label(window, text='Solution is found, Number of Iterations is %d' % (f), font=("Arial Bold", 24),
                bg="#6b868e", fg="#febe00")
    lbl.grid(column=65, row=4)
    # time spent
    lbl = Label(window, text='Solution found in %.4f seconds' % (t), font=("Arial Bold", 24), bg="#6b868e",
                fg="#febe00")
    lbl.grid(column=65, row=5)

#########################
#####ARC method##########
#########################
def ARC_check(board,row,col):
    i=0
    attack=0
    if col==N.get()-1:
        return 0
    while i<N.get():
        if is_attack(board,i,col+1)==1:
            attack=attack+1
        i=i+1
    print("ARC")
    if attack == N:
        board[row][col]=0

#####A method to check the validity of the entered choices, before execution
def selection():

    if var_order1.get() == 1 or var_order2.get() == 1 or value.get() == 1 or ARC.get() == 1 or FC.get()==1 :
        btn = Button(window, text="Run backtrack", font=("Arial Bold", 18), bg="yellow", fg="purple", command=MRV_MCV_LCV)
        btn.grid(column=66, row=6)
############################################################
#####If bakcktracking is selected, then show its menue#####
############################################################
def back_tracking():
    lbl = Label(window, text="            choose one or more options of heuristics below            ", bg="#6b868e", font=("Arial Bold", 24),fg="#f60b86")
    lbl.grid(column=65, row=0)
    global N
    N = IntVar()
    lbl3 = Label(window, text='Enter N',font=("Arial Bold", 24), bg="#708090", fg="#371e86").grid(column=66, row=4)
    Entry(window,textvariable=N,font=("Arial Bold", 20), bg="black", fg="white").grid(column=66, row=5)

    #####Defigning the variables for selected choices##########

    global var_order1 #####MRV
    var_order1 = IntVar()
    global var_order2 #####MCV
    var_order2= IntVar()
    global value    ########LCV
    value= IntVar()
    global ARC ##########ARC
    ARC= IntVar()
    global FC ##########FC
    FC= IntVar()
    lbl = Label(window, text="        Choose the Variable Ordering          ", bg="#6b868e",font=("Arial Bold", 24), fg="#f60b86")
    lbl.grid(column=65, row=3)

    Checkbutton(window, text='Minimum Remaining Values (MRV)',font=("Arial Bold", 18), bg="#478e2c", fg="#371e86",variable=var_order1, onvalue=1, offvalue=0,command=selection).grid(column=65, row=4)
    Checkbutton(window, text=' Most Constraining Variable (MCV)', font=("Arial Bold", 18), bg="#478e2c",fg="#371e86", variable=var_order2, onvalue=1, offvalue=0,command=selection).grid(column=65, row=5)
    lbl = Label(window, text="        Choose the Value Ordering          ", bg="#6b868e", font=("Arial Bold", 24),fg="#f60b86")
    lbl.grid(column=65, row=6)
    Checkbutton(window, text='  Least Constraining Value (LCV) ', font=("Arial Bold", 18), bg="#478e2c",fg="#371e86", variable=value, onvalue=1, offvalue=0,command=selection).grid(column=65, row=7)
    Checkbutton(window, text='  Arc Consistency (ARC) ', font=("Arial Bold", 18), bg="#478e2c",fg="#371e86", variable=ARC, onvalue=1, offvalue=0,command=selection).grid(column=65, row=8)
    Checkbutton(window, text='  Forward Checking (FC) ', font=("Arial Bold", 18), bg="#478e2c",fg="#371e86", variable=FC, onvalue=1, offvalue=0,command=selection).grid(column=65, row=9)



########Window display###################

window = Tk()

window.title("8-Queen solver")
window.geometry('1720x1880')
window.configure(bg='#6b868e')

lbl = Label(window, text="Hello! Choose which algorithm to solve the puzzle, please :)",bg="#6b868e",font=("Arial Bold", 24),fg="#f60b86")
lbl.grid(column=65, row=0)

btn = Button(window, text="Genetic algorithm",font=("Arial Bold", 18),bg="#478e2c",fg="#371e86",command=clicked_GA)
btn.grid(column=65, row=2)
btn = Button(window, text="backtracking",font=("Arial Bold", 18),bg="#478e2c",fg="#371e86",command=back_tracking)
btn.grid(column=65, row=1)

Button(window, text="Stop & exit",font=("Arial", 16),bg="black",fg="#cc0100",command=stop).grid(column=65, row=12)

window.mainloop()

####################################
#####End of Code####################
####################################
