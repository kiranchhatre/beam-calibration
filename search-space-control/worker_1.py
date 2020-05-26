# Author: Kiran Chhatre
from relativeFactoredNudges import getNudges
import pandas as pd 
import subprocess, os, shutil, glob, time

# paths
shared = '/home/berkeleylab/Model/storage'
beam = '/home/berkeleylab/Repository/beam'

# iterator
total_rel_nudge_trials = 36
rel_nudge_stages = list(range(8,total_rel_nudge_trials+1,4))
counter = list(range(len(rel_nudge_stages)+1))

# constants
finaliteration = '0'
p = 25 # intercepts
q = 13 # last iterations
time_now = time.ctime()

# Methods

def create_conf_copies(no_iters):
    for num in range(no_iters): 
        shutil.copy(beam+'/test/input/sf-light/urbansim-10k.conf',beam+'/test/input/sf-light/urbansim-10k_'+str(num+1)+'.conf')

def ext_change(param):
if param == 'edit':
    os.rename(picked_conf_file, picked_conf_file[:-4] + 'txt')
elif param == 'save':  
    os.rename(filename, filename[:-3] + 'conf')

def del_conf_copies():
    for filename in glob.glob(beam+'/test/input/sf-light/urbansim-10k_*.conf'):  
        os.remove(filename)

def change_conf(input_vector):
    with open(filename, 'r') as fin: 
        file_text=fin.readlines()

    # Adding the intercepts values

    for i in range(p,p+8,1):               
        file_text[i] = file_text[i].split('=',1)[0]+'= '

    file_text[p]   = file_text[p]  +str(input_vector[1]) #car_intercept
    file_text[p+1] = file_text[p+1]+str(input_vector[8]) #walk_transit_intercept
    file_text[p+2] = file_text[p+2]+str(input_vector[3]) #drive_transit_intercept
    file_text[p+3] = file_text[p+3]+str(input_vector[6]) #ride_hail_transit_intercept
    file_text[p+4] = file_text[p+4]+str(input_vector[4]) #ride_hail_intercept
    file_text[p+5] = file_text[p+5]+str(input_vector[5]) #ride_hail_pooled_intercept
    file_text[p+6] = file_text[p+6]+str(input_vector[7]) #walk_intercept
    file_text[p+7] = file_text[p+7]+str(input_vector[0]) #bike_intercept
        
    for j in range(p,p+8,1):
        file_text[j] = file_text[j]+' \n'

    # Repairing the lastiteration value of the conf file

    for i in range(q,q+1,1):                
        file_text[i] = file_text[i].split('=',1)[0]+'= '

    file_text[q] = file_text[q]+finaliteration
            
    for j in range(q,q+1,1):
        file_text[j] = file_text[j]+' \n'
        
    with open(filename, 'w') as fini:
        for i in file_text:
            fini.write(i)

def vector(whichCounter):
    input_vector = getNudges()
    if len(input_vector) == whichCounter + 1:
        return input_vector
    else:
        return vector(whichCounter)  

def find_op_folder(time_now, parallel_passes):
    output_folders = []
    for i in range(len(glob.glob(beam+'/output/sf-light/*'))):
        if time.ctime(os.path.getctime(glob.glob(beam+'/output/sf-light/*')[i])) < time_now:
            pass 
        elif time.ctime(os.path.getctime(glob.glob(beam+'/output/sf-light/*')[i])) > time_now: 
            output_folders.append(glob.glob(beam+'/sf-light/*')[i]) if glob.glob(beam+'/sf-light/*')[i] not in output_folders else output_folders
    if any( [not output_folders, len(output_folders) < parallel_passes] ):
        return find_op_folder(time_now)
    else:
        return output_folders 


# Recipe

for i in range(len(counter)):
    input_vector = vector(whichCounter=counter[i])
    if len(input_vector) == 1:
        parallel_passes = 7
    else:
        parallel_passes = 4
    create_conf_copies(no_iters=parallel_passes)

    # BEAM run (Start new process for these)
    for i in range(len(parallel_passes)):
        picked_conf_file = beam+'/test/input/sf-light/urbansim-10k_'+str(i)+'.conf'
        ext_change('edit')
        filename = beam+'/test/input/sf-light/urbansim-10k_'+str(i)+'.txt'
        change_conf(input_vector=input_vector[i])    
        ext_change('save')
        with open(beam+"/instanceconfpath.txt", "w") as text_file: 
            text_file.write(picked_conf_file)
        subprocess.call([beam+'/runme.sh'])

    # bookkeeping (Start new process for these) 
    output_folders = find_op_folder(time_now=time_now, parallel_passes=parallel_passes)
    for j in range(len(output_folders)):
        out_file = output_folders[j] + '/referenceRealizedModeChoice.csv'
        while not os.path.exists(out_file):
            time.sleep(1) 
        if os.path.isfile(out_file):
            df =  pd.read_csv(out_file)
        else:
            raise ValueError("%s isn't a file!" % file_path)

        df['iterations'][1] = 'modeshare_now'
        df.loc[-1] = ['intercepts_now'] + input_vector_base[i] 
        df.index = df.index+1 
        df.sort_index(inplace=True)
        df.set_index('iterations', inplace=True)
        df.loc['L1'] = df.loc['benchmark'] - df.loc['modeshare_now']
        df.loc['L1_rank'] = df.loc['L1'].abs().rank(ascending=False)
        df.loc['Positive_Directionality'] =  df.loc['L1'].ge(0) 
        #df.loc['v_dIntercept'] = [0,0,0,0,0,0,0,0,0]
        total_L1 = df.loc['L1'].abs().sum()
        df.to_csv(shared+'/'+str(j)+'_'+total_L1+'.csv', sep='\t', encoding='utf-8')  

    del_conf_copies()





