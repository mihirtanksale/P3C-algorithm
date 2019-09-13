arr=[12,33,15,20,27,37,42,13]
length= len(arr)
def print_Arr():
    for i in range(0,length):
        if arr[i]==-3:
            arr[i]="R"
        elif arr[i]==-2:
            arr[i]="G"
        elif arr[i]==-1:
            arr[i]="B"
#coloring rules
#red=-3 , green=-2 , blue=-1
def color_node(value):
    for p in range(0,length):
        if arr[p]==value:
            if p==0:
                if arr[p+1]!=-3:
                    arr[p]=-3
                    break
                elif arr[p+1]!=-2:
                    arr[p]=-2
                    break
                elif arr[p+1]!=-1:
                    arr[p]=-1
                    break
            elif p==length-1:
                if arr[p-1]!=-3:
                    arr[p]=-3
                    break
                elif arr[p-1]!=-2:
                    arr[p]=-2
                    break
                elif arr[p-1]!=-1:
                    arr[p]=-1
                    break
            else:
                if arr[p-1]!=-3 and arr[p+1]!=-3:
                    arr[p]=-3
                    break
                elif arr[p-1]!=-2 and arr[p+1]!=-2:
                    arr[p]=-2
                    break
                elif arr[p-1]!=-1 and arr[p+1]!=-1:
                    arr[p]=-1
                    break

def compare(a, b, c):
    if (a < b > c) :
        return 1
    else:
        return 0

def active_node():
    for i in range(0,length):
        if i==0:
            ret=compare(0,arr[i],arr[i+1])
            if ret==1:
                color_node(arr[i])
        elif i==length-1:
            re=compare(arr[i-1],arr[i],0)
            if re==1:
                color_node(arr[i])
        else:
            r=compare(arr[i-1],arr[i],arr[i+1])
            if r==1:
                color_node(arr[i])

def main():
    print arr
    active_node()
    print arr

    active_node()
    print arr

    active_node()
    print arr

    active_node()
    print arr

    active_node()
    print arr

    print_Arr()
    print arr
main()
