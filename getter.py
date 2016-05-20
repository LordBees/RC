##nc
import os,sys#,#sockets
cwd = os.getcwd()
class socket:
    pass

class fileops:##controls fileops
    EXISTS_TABLE = []##stores files that should exist
    FILE_TABLE=[]##stores filenames of files##could dict
    LOADED_PATHS = [] ## stores cfg data for later
    def __init__(self):
        pass
    def resolve_fname(arraydat , INTEGER  = False):##if the position is a number return position instead
        if INTEGER:
            return str(self.LOADED_PATHS[arraydat])+str(self.FILE_TABLE[arraydat])
        else:
            return str(self.LOADED_PATHS[self.FILE_TABLE.index(arraydat)])+str(self.FILE_TABLE[self.FILE_TABLE.index(arraydat)])##uses filetables index of the file in question to work out he path name
    def RAW_load(fname):#reads each line and retns as array
        f = open(fname,'r')
        returner = f.readlines()
        f,close()
        return returner
    
    def RAW_save(fname,dat,ARRAY = False,TRUNCATE = False):##saves each line
        if TRUNCATE:
            f = open(fname,'w')
        else:
            f = open(fname,'a')

        if ARRAY:
            for x in dat:
                f.write(str(x)+'\n')
        else:
            f.write(dat+'\n')
        f.close()
    
    def F_load(fname):##load and uncsv names
        f = open(fname,'r')
        returner = f.readlines()
        f.close()
        return returner
    
    def F_save(fname,dat,ARRAY = False,TRUNCATE = False): #'if array csvs items linebyline
        if TRUNCATE:
            f = open(fname,'w')
        else:
            f = open(fname,'a')
    
        if ARRAY:
            for x in dat:
                line_csv_string =''
                for entry in range(len(x)):
                    if ',' in x[entry]: #if comma detected ##converts commas to full stops for subcsving data 
                        temp = ''
                        for char in range(len(x[entry])):
                            if char == ',':
                                temp += '.'
                            else:
                                temp+=x[entry][char]
                        x[entry] = temp
                
                line_csv_string += str(x[entry])+','#append string with csv
            f.write(line_csv_string+'\n') #finally write compiled string ##can be indented once for multiple line support and need to add some extra for it 
                #line_csv_string = ''##nullify
            f.write('LEN:'+str(len(dat)))
            
        else:##if just one line to write
            
            #if ',' in dat:
            #    for x in range(len(dat)):
            #        if dat[x] == ',':
            #            dat[x] = '.'
            f.write(dat+'\n')##write line
        f.close()
            
    def save_cfg():##polymorph controller script to change the variable path
        pass
    def load_cfg():
        pass
    def polymorph_PC():
        pass
        #polymorph payload conroller code
        ##backup code and secret it
        
        ##copy and  edit variables at start of code
        
    def integrity_check():
        ITERATION = 0
        FAILEDLOAD = 0
        for x in self.EXISTS_TABLE:#range(len(self.EXISTS_TABLE)):
            if x:#EXISTS_TABLE
                if  not os.isfile(str(self.LOADED_PATHS[ITERATION])+str(self.FILE_TABLE[ITERATION])):##does the not file exist with the specified path when it should
                    print('Attempting repair...    '+str(self.FILE_TABLE[ITERATION]))
                    ##REPAIR
                    ##END REPAIR
                else:
                    print('found .. '+str(self.FILE_TABLE[ITERATION]))
            ITERATION +=1
        print('Load check complete:  LOADED|'+(len(self.EXISTS_TABLE)- FAILEDLOAD)+'    Failed|'+str(FAILEDLOAD))

    
class payload_controller:
    payload_meta = []#[ [names] , [exists] ]
    def __init__(self):
        pass
    def get_payload(self,ip_tuple,saveloc = None):
        if saveloc == None:
            saveloc = cwd
            
        ##establish network connection to host
        #ask the server for the payload file
        #request check
            #if true
            #get payload

            #if false
            #return error to user

        #check payload is good
        #update files to show payload metadata
            
    def run_payload(self,Payload = None,Stealth = False):
        if payload == None:
            execpath = 'configfile'##temp so compiles
        ##read data
        ##confirm execution from host controller unless stealth
        #do os.system to run
    def nul_payload(self,name = None,Stealth = False):
        pass
        ##check payload name in array
        ## if not stealth prompt host for nullification req
        ##if none do nothing
        ##if all truncate all
        ##else null name
    def proc_req(procnam,metadatarr):##need try/except loop in here
        if procnam.lower() == 'get_payload':
            self.get_payload(metadataarr[0],metadataarr[1],metadataarr[2])
        elif procnam.lower() == 'run_payload':
            run_payload(metadataarr[0],metadataarr[1])
        elif procnam.lower() == 'nul_payload':
            nul_payload(metadataarr[0],metadataarr[1])

            
class payload:
    name = ''##currently test for holding data about payloads
    meta = []
    version = 0
    def __init__(self,controller):##controller = instanced payload_controller
        pass
    def exec_payload(self):
        controller.run_payload(run_payload(meta[0],meta[1]))
    def updt_payload(self,Stealth = False):
        pass
        ##connect to server
        ##if version != serverversion:
            ##grab new file if not stealth else ask host and retn versioninfo
##            if Stealth:
##                controller.get_payload(meta[0],meta[1])
##            else:
##                ###req from host
##                controller.get_payload(meta[0],meta[1])
    
##code
##init network listener
##if request then do what asked
