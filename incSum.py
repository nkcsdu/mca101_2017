def incSum(nA, nB):
    '''
    objective: to print the sum of two numbers

    input parameters:
    nA: number A
    nB: number B

    output: sum of two numbers

    approach: using inc(nA, nB) function

    return value: Sum of numbers nA and nB
    '''

    return inc(nA, nB)

def inc(nA, nB):
    '''
    objective: to print the sum of two numbers

    input parameters:
    nA: number A
    nB: number B

    approach: incremental approach
     incrementing number nA, nB times

    return value: sum of numbers nA and nB
    '''

    if(nB==0):
        return nA
    else:
        if(nB>0):
            return inc(nA+1, nB-1)
        else:
            return inc(nA-1, nB+1)
        
    
    

    

    
    
