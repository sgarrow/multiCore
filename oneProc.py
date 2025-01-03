import time
import worker as wk
##############################################################

def oneProc( flatIterableIn, numProc, q, wrkF ):

    kStart       = time.time()
    chunkedIterable = wk.chunkify( flatIterableIn, 1 )
    results      = []

    for el in chunkedIterable: # Only 1 chunk here.
        rtnLst = wrkF( 'f0',   # Process Name (hard coded).
                       q,      # Queue.
                       el )    # Element.
        results.append(rtnLst) # [procName, el, np] 
    #print(results)

    return time.time() - kStart
##############################################################
