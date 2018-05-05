def execution(at,bt,n,it,quant):
    timer=0
    turn=[]
    qtime=[]
    preAt=[]
    waitQ=[]
    for i in range(len(at)):
        qtime.append(quant)
    for i in range(len(at)):
        preAt.append(at[0])
    while not(len(at)==0) or not(len(waitQ)==0):
        if not(len(waitQ)==0):

                if timer>=waitQ[1]:
                    bt.append(waitQ[1+1])
                    at.append(waitQ[1])
                    n.append(waitQ[0])
                    it.append(waitQ[3])
                    preAt.append(waitQ[4])
                    qtime.append(waitQ[5])
                    for j in range(6):
                        del waitQ[0]

        if   not(len(at)==0) and timer>=at[0]:
            if bt[0]<=quant and (it[0]==0 or bt[0]==it[0]):
                for i in range(bt[0]):
                    timer+=1
                trn=timer-preAt[0]
                turn.append(trn)
                print("process : ",n[0],"completed at ",timer)
                del at[0]
                del it[0]
                del bt[0]
                del n[0]
                del preAt[0]
                del qtime[0]
            elif bt[0]>quant and (it[0]==0 or bt[0]==it[0]):
                for i in range(qtime[0]):
                    timer+=1
                    bt[0]-=i
                    it[0]=0
                qtime[0]=quant
                print("process : ",n[0],"executing",bt[0])
                bt.append(bt[0])
                at.append(at[0])
                n.append(n[0])
                it.append(it[0])
                preAt.append(preAt[0])
                qtime.append(qtime[0])
                del at[0]
                del it[0]
                del bt[0]
                del n[0]
                del preAt[0]
                del qtime[0]
            elif it[0]>0 :                    #input case6
                  if it[0]>qtime[0]:
                    for i in range(qtime[0]):
                        timer+=1
                    bt[0]-=qtime[0]
                    it[0]-=qtime[0]
                    bt.append(bt[0])
                    at.append(at[0])
                    n.append(n[0])
                    it.append(it[0])
                    preAt.append(preAt[0])
                    qtime.append(qtime[0])
                    del at[0]
                    del it[0]
                    del bt[0]
                    del n[0]
                    del preAt[0]
                    del qtime[0]
                  elif it[0]<=qtime[0]:
                    at[0]+=10
                    for i in range(it[0]):
                         timer+=1
                         qtime[0]-=i
                         bt[0]-=i
                    it[0]=0

                    print("process : ",n[0]," I/O at",timer)
                    waitQ.append(n[0])
                    waitQ.append(at[0])
                    waitQ.append(bt[0])


                    waitQ.append(it[0])
                    waitQ.append(preAt[0])
                    waitQ.append(qtime[0])

                    del at[0]
                    del it[0]
                    del bt[0]
                    del n[0]
                    del preAt[0]
                    del qtime[0]
        else:
            timer+=1

def swap(min,inner,list):
    temp=list[min]
    list[min]=list[inner]
    list[inner]=temp
    return list

def sort(name,bt,at,count,it):
    for outer in range(count-1):
        min=outer
        for inner in range(outer+1,count):
            if at[inner]<at[min]:
                min=inner

        at = swap(min,outer,at)
        name = swap(min,outer,name)
        bt = swap(min,outer,bt)
        it=swap(min,outer,it)
    return at,name,bt,it


def inputprocesses(count,name,burstTime,arrivalTime,inputtime):


    for index in range(count):
        print("please enter some information of process",index+1)
        pname=raw_input('enter name of process : ')
        pbt=int(input('enter burst time  of process : '))
        while pbt<=-1:
            print("time can't be nagqtive")
            pbt=int(input('enter burst time  of process again : '))
        pat=int(input('enter arrival of process : '))
        while pat<=-1:
            print("time can't be nagqtive")
            pat=int(input('enter arrival time  of process again : '))
        pit=int(input('enter input time of process : '))
        while pit<=-1:
            print("time can't be nagqtive")
            pit=int(input('enter input time  of process again : '))
        name.append(pname)
        burstTime.append(pbt)
        arrivalTime.append(pat)
        inputtime.append(pit)
    return name,burstTime,arrivalTime,inputtime


def main():
    name=[]
    burstTime=[]
    arrivalTime=[]
    inputtime=[]
    quantumtime=0
    print ("          Round Robin ")
    processCount=int(input("\n Number of processs I want to add : "))
    if processCount>0:
        quantumtime=int(input('Enter quantum time : '))
        name,burstTime,arrivalTime,inputtime=inputprocesses(processCount,name,arrivalTime,burstTime,inputtime)
        arrivalTime,name,burstTime,inputtime=sort(name,burstTime,arrivalTime,processCount,inputtime)
        execution(arrivalTime,burstTime,name,inputtime,quantumtime)
    else:
        print('bye')
main()
