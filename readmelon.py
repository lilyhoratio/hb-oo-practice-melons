import harvest 

with open("harvest_log.txt") as f: 
    ## don't need readline(f) - python2
    i = 1
    for line in f:
        line = f.split(" ")
        melon_obj_name = "melon"+str(i)
        i +=1
        globals()[melon_obj_name] = Melon()

