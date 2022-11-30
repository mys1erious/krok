"""
    Fixing mutual exclusion, means that we are completely misunderstanding the problem. We
know that locks are utilized so that processes and threads can access the shared resources
in a program in a systematic, coordinated way, to avoid mishandling the data.
    Therefore, removing any locking mechanisms in a concurrent program means that the likelihood of
the shared resources, which are now free from access limitations, being manipulated in an
uncoordinated way (and therefore, becoming corrupted) increases significantly.
    So, by ignoring locks, it is relatively likely that we will need to completely redesign and
restructure our concurrent program.If the shared resources still need to be accessed and
manipulated in an organized way, other synchronization methods will need to be
implemented. The logic of our processes and threads might need to be altered to
appropriately interact with this new synchronization method, the execution time might be
negatively affected by this change in the structure of the program, and other potential
synchronization problems might also arise.

"""
