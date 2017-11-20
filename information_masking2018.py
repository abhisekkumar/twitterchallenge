import sys
import re
for line in sys.stdin.readlines(): #readline from STDIN.
    #print ("----------")
    #print line
    if line[0] == 'E':      #Check if it relates with the initial condition email or phone
        newmask = line.replace(" ","").rstrip(' \t\n\r')      #mask the input with the appropriate condition
        print ("E:"+ newmask.split(":")[1].split("@")[0][0]+"*****"+newmask.split(":")[1].split("@")[0][-1]+"@"+newmask.split("@")[-1])
    else:
        newmask0=line[2:].strip(' \t\n\r')
        if (newmask0[0]=='+'):
            newmask0='+'+newmask0.split("+")[1].strip(' \t\n\r')
        #print (newmask0)
        p_out=re.sub("\d", "*", newmask0.replace(")","(").replace(" ","(").replace("((","(").replace("(","-")[0:-4])+newmask0[-4:] #it will check for brackets, space and replace all with single hyphen
        #print (p_out)
        cnt=2
        if (p_out[0]=='+'):        #if international number
            cnt=3
        if (p_out.count('-')==cnt-1 and p_out[-5]!='-'):
            p_out=p_out[0:-4]+'-'+p_out[-4:]
            #print (p_out)
        if (p_out.count('-')>0):
            #print (" L1")
            if p_out[0] == '-':
                print ('P:'+p_out[1:])
            else:
                 print ('P:'+p_out)
        else:                    #check the phone number and mask it with asterisk
            #print (p_out)
            if p_out[0] == '+':
                num_len=len(p_out)-1
                str2="*****"
                print ("P:+"+str2[0:num_len-10]+'-***'+'-***-'+p_out[-4:])
            else:
                print ("P:"+'***'+'-***-'+p_out[-4:])
         