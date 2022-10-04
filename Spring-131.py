from time import time
cvf=0
import os
import binascii
self="'"

namez = input("for compression c or e for extract: ")
#@Author Jurijus pacalovas
class encypthion_class:

    def encypthion1(self):

                 
                
                self.name = "Author: Jurijus Pacalovas"

                print(self.name)

                if namez!="c" and namez!="e":
                    print("Your enter incorrect letter")
                
                if namez=="c":


                    
                   
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                   
                    long_block=100
                        
                    namea=""
                    namem=""
                    namema="?"
                    Portal=2
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)

                    long=len(name)
                   
                    Times_compression=1
                    
                    name_cut=len(".bin")
                    
                    nameas=name+".bin"
                    name_bofore=len(nameas)
                    F=0
                    
                    

                    	 
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                 
                    size_data3=""
                    size_data2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
                        
                
                        size_after2=len(data)
                        #print(size_after2)  
                        
                        if len(data)==0 or len(data)>2**40:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                            
                      
                         

                  
                        s=str(data)
                        
                        
                        lenf1=len(data)
                          
                    
                            
  
                            
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countraz==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    qqwslenf=len(size_data2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    lenf3=len(size_data2)
                                lenf2=len(size_data2)

                                
                                    
                                
                                size_data3=size_data2
                                long_B=len(size_data3)
                                long=len(size_data3)
                                
                                info_hex=size_data3
                                times10=0
                                
                                while long>=400:
                                    #print(long)
                                
                                    size_data3=info_hex
                                    
                                    long=len(size_data3)
                                    #print(long)
                                   
                                   
                                    block=0
                                    
                                    blocks=8*4
                                    #print(blocks)
                                    
                                    Calculus=""
                                    Caculus_oct=0
                                    res=""
                                    res3=0
                                    res6=""
                                    file=0
                                    resf=0
                                    
    
                                    
                                    
                                    while block<long:
                                        Calculus=size_data3[block:block+blocks]
                                        block=block+blocks
                                        Calculus8=size_data3[block:block+blocks]
                                        block=block+blocks
                                        
                                        if file==0:
                                                
                                            long2=len(Calculus)
                                            #print(long2)
                                            block2=0
                                            blocks2=0
                                            Times=0
                                            Times2=0
                                            res1=0
                                            res2=0
                                            res5=0
                                            
                                            while Times2!=32:
                                                Times2+=4
                                                Times=0
                                                #print(Times2)
                                                while Times!=32:
                                                    Times+=4
                                                    #print(Times)
                                                    block2=0
        
                                                    if Calculus[Times:Times+4]==Calculus[Times2:Times2+4] and res1==0 and Times!=Times2: 
                                                        Caculus_oct=format(Times//4,'03b')
                                                        Caculus_oct2=format((Times2//4)-1,'03b')
                                                        #print(Caculus_oct2)
                                                        #print(Caculus_oct)
                                                        if Times<Times2:
                                                            res7=Caculus_oct+Caculus_oct2+Calculus[:Times]+Calculus[Times+4:Times2]+Calculus[Times2+4:]
                                                            
                                                        if Times2<Times:
                                                            res7=Caculus_oct+Caculus_oct2+Calculus[:Times2]+Calculus[Times2+4:Times]+Calculus[Times+4:]
                                                        #print(Times)
                                                        #print(Times2)
                                                        #print(len(res7))
                                                        res1=1
                                                        
                                                        res5=1
                                                        
                                                        
    
                                        if file==0: 
                                            long2=len(Calculus)                                                                                                                            
                                            #print(long2)
                                            block2=0
                                            blocks2=0
                                            Times3=Times
                                            Times4=Times2
                                            Times=0
                                            
                                            Times2=0
                                            res1=0
                                            res2=0
                                            
                                            
                                            while Times2!=32:
                                                Times2+=4
                                                Times=0
                                                #print(Times2)
                                                while Times!=32:
                                                    Times+=4
                                                    #print(Times)
                                                    block2=0
        
                                                    if Calculus[Times3:Times3+4]==Calculus8[Times2:Times2+4] and Calculus8[Times3:Times3+4]==Calculus8[Times2:Times2+4] and res2==0 and Times!=Times2: 
                                                        Caculus_oct=format(Times//4,'03b')
                                                        Caculus_oct2=format((Times2//4)-1,'03b')
                                                        #print(Caculus_oct2)
                                                        #print(Caculus_oct)
                                                        if Times<Times2:
                                                            res10= Calculus8[Times2:Times2+4]+Caculus_oct2+Calculus8[:Times]+Calculus8[Times+4:Times2]+Calculus8[Times2+4:]
                                                            
                                                        if Times2<Times:
                                                            res10= Calculus8[Times:Times+4]+Caculus_oct2+Calculus8[:Times2]+Calculus8[Times2+4:Times]+Calculus8[Times+4:]                          
                                                            #print(Times)
                                                        #print(Times2)
                                                        #print(len(res7))
                                                        res2=1
                                                        if   res5==1:
                                                            res5=2
                                                        
                                                        
                                                                                                                                                                                     
                                            if   res5==2:
                                                res3+=1
                                                #print(res3)
                                                res+="0"+res7+res10
                                            else:
                                                res+="1"+Calculus+Calculus8
                                                
                                            resf+=1
                                            
                                        
                                        #print(block)                                        
                                        
                                    
     
                                                
                                                
                                                
                                     
               
                                    

                                        
                                    
                                    times10+=1
                                    info_hex=res 
                                                                   
                                
                                encypthion=info_hex
                                
                               
                                
                                #print(res3)
                                
                
                                    
                                b=bin(times10)[2:]
                                long_T=len(b)

                                b1=format(long_T,'08b')   
                          
                                size_data12=b1+b+encypthion

                                size_data12="1"+size_data12
                            
                                lenf=len(size_data12)
                                        
                                add_bits118=""
                                count_bits=8-lenf%8
                                z=0
                                    
                                if count_bits!=8:
                                    while z<count_bits:
                                                    add_bits118="0"+add_bits118
                                                    z=z+1
                                                                    
                                                                    
                                size_data12=add_bits118+size_data12
                                
                                
                                    
                                size_data11=size_data12 
                                  
                               
             
                                                                                
                                n = int(size_data11, 2)
                                
                                qqwslenf=len(size_data11)
                                qqwslenf=(qqwslenf/8)*2
                                qqwslenf=str(qqwslenf)
                                qqwslenf="%0"+qqwslenf+"x"
                             
                                jl=binascii.unhexlify(qqwslenf % n)
                                
                             
                                
                                #import paq
                                #jl= paq.compress(jl)
                                
                                    
                                size_after=len(jl)

                                size_after=len(jl)
                                
                                   
                                qqqwz=qqqwz+1
                                szxzzza=""
                                szxzs=""
                            
                                assxw=assxw+1
                                if assxw==1:
                                    assx=10
                                    if assx==10:

                                        f2.write(jl)
                                        x2 = time()
                                        x3=x2-x
                                        return print(x3)

    def encypthion2(self):

                 
                 if namez=="e":
                    
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                    Portal=2
                    namea=""
                    namem=""
                    namema="?"
                    Deep=0
                 
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
                    name_cut=""
                    name_cut=len(".bin")
                    nameas=name
                    
                    name_long=len(nameas)
                    nameSS=name[name_long-name_cut:]
                    if nameSS!=".bin":
                        x3=0.0
                        return print(x3)
                        
                    nameas=name[:name_long-name_cut]
                    nac=len(nameas)
                    
                  
                    
                    long=len(nameas)

                    nac=len(nameas)
                   
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                 
                    size_data3=""
                    size_data2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        
                        data = binary_file.read()
                        import paq
                        data= paq.decompress(data)

                        

                    
                        if len(data)==0:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                     	

                        s=str(data)
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countraz==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    qqwslenf=len(size_data2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    lenf3=len(size_data2)
                                lenf2=len(size_data2)  
                                x4=1
                                if x4==1:

                                    

                                    size_data3=size_data2
                                    
                                    if size_data3[0:9]=="000000001":
                                        size_data3=size_data3[9:]
                                    elif size_data3[0:8]=="00000001":
                                        size_data3=size_data3[8:]
                                    elif size_data3[0:7]=="0000001":
                                        size_data3=size_data3[7:]
                                    elif size_data3[0:6]=="000001":
                                        size_data3=size_data3[6:]
                                    elif size_data3[0:5]=="00001":
                                        size_data3=size_data3[5:]
                                    elif size_data3[0:4]=="0001":
                                        size_data3=size_data3[4:]
                                    elif size_data3[0:3]=="001":
                                        size_data3=size_data3[3:]
                                    elif size_data3[0:2]=="01":
                                        size_data3=size_data3[2:]
                                    elif size_data3[0:1]=="1":
                                        size_data3=size_data3[1:]                                    
                                    
                                   
                                        
                                      
                                    n = int(size_data3, 2)
                                    
                                    
                                    qqwslenf=len(size_data3)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                  
                                    sssssw=len(jl) 
                                  
                                   

                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                                    
                            
                                    assxw=assxw+1
                                    if assxw==1:
                                        assx=10
                                        if assx==10:
                                        	
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)  
                  
self=""                                
d=encypthion_class()
    
xw=d.encypthion1()
print(xw)

xw1=d.encypthion2()
print(xw1)
