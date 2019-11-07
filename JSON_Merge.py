from json import load,dump
import os



def merger(path,infile,outfile,Maxsize):
    json_files=[pos_json for pos_json in os.listdir(path) for i in range(10) if pos_json.endswith(infile+str(i)+'.json')]     #Get all the .json file with prefix of infile value
    with open(infile+"1.json") as f1:
        second_list=load(f1)
    counter=1
    size=0
    for k in range(2,len(json_files)+1):
        with  open(infile+str(k)+".json") as f2:
            first_list = load(f2)

        for i, v in enumerate(second_list):
            for i in first_list[v]:
                second_list[v].append(i)
        
        
        if Maxsize>size:
            with open(outfile+str(counter)+".json", "w") as fout:
                dump(second_list, fout)
                
        else:
            counter=counter+1
            with open(outfile+str(counter)+".json", "w") as fout:
                dump(second_list, fout)
                
        size=os.path.getsize(path+outfile+str(counter)+".json")
                
    print(second_list) #print a final merge result



#path="C:/Users/Rishi/Desktop/JSON/"    
#merger(path,"data","merged",10)



