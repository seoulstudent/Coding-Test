import os 

PATH = os.path.dirname(os.path.realpath(__file__))

f = open(PATH+"/pond_initial_state.txt", 'r')
lines = f.readlines()

pond_initial_state = []
max_rows, max_cols = 0, 0


for line in lines:
    
    line = line.rstrip('\n')
    line = line.split(' ') 
    
    cols = len(line)
    if(max_cols < cols) : max_cols = cols
       
    temp = [0]*cols    
    for i in range(cols) :
        temp[i] = int(line[i])
    
    pond_initial_state.append(temp)
    max_rows+=1

f.close()

#----------------- Start ------------# 

pond_result_state = [[0 for j in range(max_cols)] for i in range(max_rows)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
pre_max_depth = 0
max_depth = 0 

while True : 

    for y in range(max_rows) :
        for x in range(max_cols) : 

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
        
            
                if nx < 0 or ny < 0 or nx > max_cols or ny > max_rows :
                    break
                    
                if pond_initial_state[y][x] > pond_initial_state[ny][nx]:
                    break
                
                if pond_initial_state[y][x] == 0 or pond_initial_state[ny][nx] == 0 :
                    break

                count += 1
            
                if count == 4 :
                    pond_initial_state[y][x] = pond_initial_state[y][x] + 1
                    if max_depth < pond_initial_state[y][x] :
                        max_depth = pond_initial_state[y][x] 
                            
            count = 0 

    if pre_max_depth != max_depth :
        pre_max_depth = max_depth
    elif pre_max_depth == max_depth :
        break


#------------------ Make a txt file-------------------#
f = open(PATH+"/pond_result_state.txt", 'w')
for row in range(len(pond_initial_state)):
  f.writelines(str(pond_initial_state[row]) + '\n')

f.close() 


