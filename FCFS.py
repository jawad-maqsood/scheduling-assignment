def execution(at,bt,n):
    avgwaiting=0
    avgturnarround=0
    wait=0
    finish=0
    turn=0
    for i in range(len(at)):
        if finish>=at[i]:
            wait=finish-at[i]
            finish=finish+bt[i]
            turn =finish-at[i]
            print()
            print ("process ",n[i])
            print("      finish time =",finish)
            print("      arrival time = ",at[i] )
            print("      turnarround time = ",turn )
            print("      waiting time = ",wait)
            avgwaiting=avgwaiting+wait
            avgturnarround=avgturnarround+turn
        else:
            wait=0
            finish=at[i]+bt[i]
            turn =finish-at[i]
            print()
            print ("process ",n[i])
            print("      finish time =",finish)
            print("      arrival time = ",at[i] )
            print("      turnarround time = ",turn )
            print("      waiting time = ",wait)

            avgwaiting=avgwaiting+wait
            avgturnarround=avgturnarround+turn
    count=len(at)
    print('average waiting time of this scheduler is = ',avgwaiting/count)
    print('average turnarround time of this scheduler is = ',avgturnarround/count)


def swap(min,inner,list):
    temp=list[min]
    list[min]=list[inner]
    list[inner]=temp
    return list

def sort(name,bt,at,count):
    for outer in range(count-1):
        min=outer
        for inner in range(outer+1,count):
            if at[inner]<at[min]:
                min=inner

        at = swap(min,outer,at)
        name = swap(min,outer,name)
        bt = swap(min,outer,bt)
    return at,name,bt


def inputprocesses(count,name,burstTime,arrivalTime):


    for index in range(count):
        print("please enter some information of process",index+1)
        pname=raw_input('enter name of process : ')
        pbt=int(input('enter burst time  of process : '))
        while pbt<-1:
            print("time can't be nagqtive")
            pbt=int(input('enter burst time  of process again : '))
        pat=int(input('enter arrival of process : '))
        while pat<-1:
            print("time can't be nagqtive")
            pat=int(input('enter arrival time  of process again : '))
        name.append(pname)
        burstTime.append(pbt)
        arrivalTime.append(pat)
    return name,burstTime,arrivalTime


def main():
    name=[]
    burstTime=[]
    arrivalTime=[]
    print ("          First Come First Serve ")
    processCount=int(input("\n Number of processs I want to add : "))
    if processCount>0:
        name,burstTime,arrivalTime=inputprocesses(processCount,name,arrivalTime,burstTime)
        arrivalTime,name,burstTime=sort(name,burstTime,arrivalTime,processCount)
        execution(arrivalTime,burstTime,name)
    else:
        print('bye')
main()
