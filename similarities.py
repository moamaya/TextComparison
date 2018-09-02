#path = '/Users/MarloAmaya/Library/Mobile Documents/com~apple~CloudDocs/Summer 2017/COSC 1306/HW/Additional Files/ICW11_Project/file_names.txt'
files = open('file_names.txt', 'r')
lines = files.readlines()
dictlist = []
matrix = []
total_files = len(lines)
files.close()


def generate_vocabulary(content):
    mydict = {}
    with open(content) as f:
        words = f.read().split()
        for w in words:
            if w not in mydict:
                mydict[w] = 1
            else:
                mydict[w] = mydict[w] + 1
        f.close()
    return (mydict)


def compute_similarity(a,b):
    matches = 0
    for key, value in a.items():
        if key in b:
            matches=matches + 1
    #print(matches)
    uniquedicts=a.copy()

    for key, value in b.items():
        if key not in uniquedicts:
            uniquedicts[key]=value
        else :
            uniquedicts[key] = uniquedicts[key] + b[key]
    #print(len(uniquedicts))
    return (round (100*matches/len(uniquedicts),2))

def compute_matrix(dictlist):
    unique_matrix = []
    all_to_all_matrix = []
    for i in dictlist:
        rowa=[]
        rowb=[]
        for j in dictlist:
            a=compute_similarity(i,j)
            b=compute_similarity(i,j)
            rowa.append(a)
            rowb.append(b)
        unique_matrix.append(rowa)
        all_to_all_matrix.append(rowb)
    return (unique_matrix,all_to_all_matrix)

def print_matrix(m,l):
    print("%-*s" %(40," "),end="")
    for i in l:
        print(i[:-1],end="\t")
    print()
    for i in range(len(m[0])):
        print("%-*s" %(40,l[i][:-1]),end="")
        for j in range(len(m[0])):
            print("%*.2f" %(15,m[i][j]),end="")
        print()
    return

for i in lines:
    print("Processing file: %s" % i.split())
    dictlist.append(generate_vocabulary(i.split()[0]))

for i in range(total_files):
    matrix.append([0] * total_files)
    for j in range(total_files):
        matrix[i][j] = compute_similarity(dictlist[i], dictlist[j])



a,b = compute_matrix(dictlist)

print_matrix(matrix,lines)





