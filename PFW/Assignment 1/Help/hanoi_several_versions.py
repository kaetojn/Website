from TOAHModel import TOAHModel, MoveSequence

def hanoi(num_cheeses: int) -> None:
    M = MoveSequence([])

    def move_cheeses(n: int, source: int, intermediate: int, 
                     destination: int) -> None:
        """Populate the MoveSequence M with the 3-stool strategy to get n 
        cheeses from source to destination, possibly using intermediate"""
        if n > 1:   
            move_cheeses(n - 1, source, destination, intermediate)        
            move_cheeses(1, source, None, destination)
            move_cheeses(n - 1, intermediate, source, destination)
        else: 
            M.add_move(source,destination)
    
    def move_cheeses_verbose(n: int, source: int, intermediate: int, 
                     destination: int) -> None:
        """Construct a MoveSequence to get n cheeses from source
           to destination, possibly using intermediate"""
        if n > 1: 
            # we want to temporarily put n-1 cheeses on the intermediate stool, so
            # the intermediate stool is the subcase destination stool        
            subcase_dest = intermediate  
            # the remaining stool (besides the origin) is used as the subcase 
            # intermediate stool
            subcase_interm = destination  
            move_cheeses_verbose(n - 1, source, subcase_interm, subcase_dest)        
            move_cheeses_verbose(1, source, None, destination)
            subcase_source = intermediate
            subcase_dest = destination 
            subcase_interm = source 
            move_cheeses_verbose(n - 1, subcase_source, subcase_interm, subcase_dest)
        else: 
            M.add_move(source,destination)
            
    # move_cheeses(n=num_cheeses, source=0, intermediate=1, destination=2)        
    move_cheeses_verbose(n=num_cheeses, source=0, intermediate=1, destination=2)
    return M
        



def hanoi_mutual_recursive(n:int):
    """Construct a MoveSequence of the 3-stool strategy to get n 
    cheeses from stool 0 to stool 2"""

    M = MoveSequence([])
    
    def hanoi0to2(n:int) -> None:
        """Construct a MoveSequence to get n cheeses from stool 0
        to stool 2, possibly using stool 1 also."""        
        if n > 1:
            hanoi0to1(n-1)
            hanoi0to2(1)
            hanoi1to2(n-1)
        else:
            M.add_move(0,2)
                   
    def hanoi0to1(n:int) -> None:
        if n > 1:
            hanoi0to2(n-1)
            hanoi0to1(1)
            hanoi2to1(n-1)
        else:
            M.add_move(0,1)
                   
    def hanoi1to2(n:int) -> None:
        if n > 1:
            hanoi1to0(n-1)
            hanoi1to2(1)
            hanoi0to2(n-1)
        else:
            M.add_move(1,2)
                   
    def hanoi1to0(n:int) -> None:
        if n > 1:
            hanoi1to2(n-1)
            hanoi1to0(1)
            hanoi2to0(n-1)
        else:
            M.add_move(1,0)
            
    def hanoi2to0(n:int) -> None:
        if n > 1:
            hanoi2to1(n-1)
            hanoi2to0(1)
            hanoi1to0(n-1)
        else:
            M.add_move(2,0)
            
    def hanoi2to1(n:int) -> None:
        if n > 1:
            hanoi2to0(n-1)
            hanoi2to1(1)
            hanoi0to1(n-1)
        else:
            M.add_move(2,1)
             
    hanoi0to2(n)    
    return M
    
