# Write your code here
def greatest_sum(ns):
    
    """
    return (i,j) from ns = [-1,3,5,-10,2]
    [-1,3] [-1,3,5] [-1,3,5,-10] [-1,3,5,-10,2]
    [:2]   [:3]     [:4]         [:5]
    vanaf [:2] tot [len(ns)] 
    [3,5]  [3,5,-10] [3,5,-10,2]
    [1:3]  [1:4]     [1:5]
    vanaf [1:3] tot [1:len(ns-1)]
    
    result = []
    
    for l in range(len(ns))
        for i in range(0,len(ns))
            for j in range(2,len(ns)+1)
                result.append(ns[i:j])
                
                
        for q in range(1:len(ns))       
            for k in range(3,len(ns)+1)
                result.append(ns[q:k]) 
    """     
    result = {}            
    for l in range(len(ns)):
        for i in range(l,len(ns)):
            for j in range(l+2,len(ns)+1):
                result.update({(i,j):ns[i:j]})
    """
    result = {
        (i,j):[],
        (i,j):[],
        }
    """ 
    if(len(ns) == 1):
        return (0,1)
    else:
        return mode(result)

def secondSum(pair):
    return sum(pair[1])

def mode(result):
    return max(result.items(), key=secondSum)[0]          
                 
    

    
    
    
    
    