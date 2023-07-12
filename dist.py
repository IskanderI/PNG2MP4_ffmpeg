#------------------------------------------------------------------------------

def get_start_end(size, rank, N, start) :
    
    """
    
    Distribute N consecutive items as evenly as possible over processors
    Uneven workload (differs by 1 at most) is on the initial ranks

    Parameters
    ----------
    size  : communicator size
    rank  : processor rank
    N     : total number of items to be distributed
    start : index of the first item

    Output
    ----------
    rstart: index of first local row
    rend: 1 + index of last row
    
    """

    rstart = 0
    rend   = N
    if size >= N:
        if rank < N:
            rstart = rank
            rend   = rank + 1
        else:
            rstart = 0
            rend   = 0
    else:
        n = N//size # Integer division PEP-238
        remainder = N%size
        rstart    = n * rank
        rend      = n * (rank+1)
        if remainder:
            if rank >= remainder:
                rstart += remainder
                rend   += remainder
            else:
                rstart += rank
                rend   += rank + 1
                
    return rstart + start, rend + start

#------------------------------------------------------------------------------