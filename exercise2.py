def overlap(x1,y1,x2,y2):
    interval1 = []
    for i in range(x1,y1):
        interval1.append(i)
    interval2 = []
    for i in range (x2,y2):
        interval2.append(i)
    interval_overlap = []
    end = 0
    for i in range(x1,y2):
        end+=1
        if i in interval1 and i in interval2:
            interval_overlap.append(i)
        elif i == len(range(x1,y2)):
            interval_overlap.append(0)
    return interval_overlap
print(overlap(1,6,7,10))