import subprocess
import os

ip1 = '192.168.19.254'
ip2 = '192.168.20.254'
ip3 = '192.168.30.254'
ip4 = '192.168.49.254'
ip5 = '192.168.50.254'
# ip6 = '192.168.60.254'
ip7 = '192.168.70.254'
ip8 = '192.168.80.254'
ip9 = '192.168.90.254'
ip10 = '192.168.100.254'
ip11 = '192.168.119.254'
# ip12 = '192.168.120.254'

#//---------------65001------------------
#//---------------MUSHROOM------------------
trenbirmushroom = "192.168.10.253"
#//------------TEPE EKRANLAR---------------
t1tp1 = '192.168.19.50'
t1tp2 = '192.168.19.51'
t1tp3 = '192.168.19.52'
t1tp4 = '192.168.19.53'
t1tp5 = '192.168.19.54'
t1tp6 = '192.168.19.55'
#//------------SES ISLEMCI---------------
t1ses1 = '192.168.19.121'
t1ses2 = '192.168.19.122'
t1ses3 = '192.168.19.123'
t1ses4 = '192.168.19.124'
t1ses5 = '192.168.19.125'
t1ses6 = '192.168.19.126'
#//-------------GPS-------------------
t1gps1 = "192.168.19.227"
t1gps2 = "192.168.19.228"
#//------------LEDLER---------------
t1tcbs1led1   =      '192.168.19.80'
t1tcbs1led2   =      '192.168.19.81'
t1tcbs2led1   =      '192.168.19.82'
t1tcbs2led2   =      '192.168.19.83'
t1mifcs1led1  =      '192.168.19.84'
t1mifcs2led1  =      '192.168.19.85'
t1mifcs2led2  =      '192.168.19.86'
t1mif1as1led1 =      '192.168.19.87'
t1mif1as1led2 =      '192.168.19.88'
t1mif1as2led1 =      '192.168.19.89'
t1mif1as2led2 =      '192.168.19.90'
t1mif1bs1led1 =      '192.168.19.91'
t1mif1bs1led2 =      '192.168.19.92'
t1mif1bs2led1 =      '192.168.19.93'
t1mif1bs2led2 =      '192.168.19.94'
t1mif2s1led1  =      '192.168.19.95'
t1mif2s1led2  =      '192.168.19.96'
t1mif2s2led1  =      '192.168.19.97'
t1mif2s2led2  =      '192.168.19.98'
t1tcfs1led1   =      '192.168.19.99'
t1tcfs1led2   =      '192.168.19.100'
t1tcfs2led1   =      '192.168.19.101'
t1tcfs2led2   =      '192.168.19.102'
t1mif1asoldisled =   '192.168.19.108'
t1mif1bsoldisled =   '192.168.19.109'
t1mif1bsagdisled =   '192.168.19.110'
t1mif2soldisled  =   '192.168.19.111'
t1mif2sagdisled  =   '192.168.19.112'
t1tcfsoldisled   =   '192.168.19.113'
t1tcfsagdisled   =   '192.168.19.114'
              

#//------------KAMERALAR--------------
t1tcbsoldis =   '192.168.19.9'
t1tcbd1     =   '192.168.19.10'
t1tcbsagdis =   '192.168.19.11'
t1tcbmakinist = '192.168.19.12'
t1tcbs1 =       '192.168.19.13'
t1tcbs2 =       '192.168.19.14'
t1mifcs1 =      '192.168.19.15'
t1mifcs2 =      '192.168.19.16'
t1mif1as1 =     '192.168.19.17'
t1mif1as2 =     '192.168.19.18'
t1mif1bs1 =     '192.168.19.19'
t1mif1bs2 =     '192.168.19.20'
t1mif2s1 =      '192.168.19.21'
t1mif2s2 =      '192.168.19.22'
t1tcfs1 =       '192.168.19.23'
t1tcfs2 =       '192.168.19.24'
t1tcfmakinist = '192.168.19.25'
t1tcfsoldis   = '192.168.19.26'
t1tcfsagdis =   '192.168.19.27'
t1tcfd1 =       '192.168.19.28'
#//---------------65002------------------
#//---------------MUSHROOM------------------
trenikimushroom = "192.168.20.253"
#//------------ACCESSPOINTLER-------- 
t2v1accs = '192.168.20.241'
t2v2accs = '192.168.20.242'
t2v3accs = '192.168.20.243'
t2v4accs = '192.168.20.244'
t2v5accs = '192.168.20.245'
t2v6accs = '192.168.20.246'
#-----------------------------------
#//-----------------65003-------------------
#//---------------MUSHROOM------------------
trenucmushroom = "192.168.30.253"
#//------------ACCESSPOINTLER-------- 
t3v1accs = '192.168.30.241'
t3v2accs = '192.168.30.242'
t3v3accs = '192.168.30.243'
t3v4accs = '192.168.30.244'
t3v5accs = '192.168.30.245'
t3v6accs = '192.168.30.246'
#//---------------------------------------------
#//---------------65004------------------
#//---------------MUSHROOM------------------
trendortmushroom = "192.168.40.253"
#//------------TEPE EKRANLAR---------------
t4tp1 = '192.168.49.50'
t4tp2 = '192.168.49.51'
t4tp3 = '192.168.49.52'
t4tp4 = '192.168.49.53'
t4tp5 = '192.168.49.54'
t4tp6 = '192.168.49.55'
#//------------SES ISLEMCI------------
t4ses1 = '192.168.49.121'
t4ses2 = '192.168.49.122'
t4ses3 = '192.168.49.123'
t4ses4 = '192.168.49.124'
t4ses5 = '192.168.49.125'
t4ses6 = '192.168.49.126'
#//-------------GPS--------------------
t4gps1 = "192.168.49.227"
t4gps2 = "192.168.49.228"
#//------------LEDLER---------------
t4tcbs1led1   =      '192.168.49.80'
t4tcbs1led2   =      '192.168.49.81'
t4tcbs2led1   =      '192.168.49.82'
t4tcbs2led2   =      '192.168.49.83'
t4mifcs1led1  =      '192.168.49.84'
t4mifcs2led1  =      '192.168.49.85'
t4mifcs2led2  =      '192.168.49.86'
t4mif1as1led1 =      '192.168.49.87'
t4mif1as1led2 =      '192.168.49.88'
t4mif1as2led1 =      '192.168.49.89'
t4mif1as2led2 =      '192.168.49.90'
t4mif1bs1led1 =      '192.168.49.91'
t4mif1bs1led2 =      '192.168.49.92'
t4mif1bs2led1 =      '192.168.49.93'
t4mif1bs2led2 =      '192.168.49.94'
t4mif2s1led1  =      '192.168.49.95'
t4mif2s1led2  =      '192.168.49.96'
t4mif2s2led1  =      '192.168.49.97'
t4mif2s2led2  =      '192.168.49.98'
t4tcfs1led1   =      '192.168.49.99'
t4tcfs1led2   =      '192.168.49.100'
t4tcfs2led1   =      '192.168.49.101'
t4tcfs2led2   =      '192.168.49.102'
t4mif1asoldisled =   '192.168.49.108'
t4mif1bsoldisled =   '192.168.49.109'
t4mif1bsagdisled =   '192.168.49.110'
t4mif2soldisled  =   '192.168.49.111'
t4mif2sagdisled  =   '192.168.49.112'
t4tcfsoldisled   =   '192.168.49.113'
t4tcfsagdisled   =   '192.168.49.114'
              

#//------------KAMERALAR--------------
t4tcbsoldis =   '192.168.49.9'
t4tcbd1     =   '192.168.49.10'
t4tcbsagdis =   '192.168.49.11'
t4tcbmakinist = '192.168.49.12'
t4tcbs1 =       '192.168.49.13'
t4tcbs2 =       '192.168.49.14'
t4mifcs1 =      '192.168.49.15'
t4mifcs2 =      '192.168.49.16'
t4mif1as1 =     '192.168.49.17'
t4mif1as2 =     '192.168.49.18'
t4mif1bs1 =     '192.168.49.19'
t4mif1bs2 =     '192.168.49.20'
t4mif2s1 =      '192.168.49.21'
t4mif2s2 =      '192.168.49.22'
t4tcfs1 =       '192.168.49.23'
t4tcfs2 =       '192.168.49.24'
t4tcfmakinist = '192.168.49.25'
t4tcfsoldis   = '192.168.49.26'
t4tcfsagdis =   '192.168.49.27'
t4tcfd1 =       '192.168.49.28'
#//---------------65005------------------
#//---------------MUSHROOM------------------
trenbesmushroom = "192.168.50.253"
#//------------ACCESSPOINTLER---------------
t5v1accs = '192.168.50.241'
t5v2accs = '192.168.50.242'
t5v3accs = '192.168.50.243'
t5v4accs = '192.168.50.244'
t5v5accs = '192.168.50.245'
t5v6accs = '192.168.50.246'
#--------------------------------------------
#//---------------65006------------------
#//---------------MUSHROOM------------------
trenaltiv1mushroom = "192.168.21.253"
trenaltiv2mushroom = "192.168.22.253"
trenaltiv3mushroom = "192.168.23.253"
trenaltiv4mushroom = "192.168.24.253"
trenaltiv5mushroom = "192.168.25.253"
trenaltiv6mushroom = "192.168.26.253"
#//------------ACCESSPOINTLER---------------
t6v1accs = '192.168.21.254'
t6v2accs = '192.168.22.254'
t6v3accs = '192.168.23.254'
t6v4accs = '192.168.24.254'
t6v5accs = '192.168.25.254'
t6v6accs = '192.168.26.254'
#//---------------65007------------------
#//---------------MUSHROOM------------------
trenyedimushroom = "192.168.70.253"
#//------------ACCESSPOINTLER---------------
t7v1accs = '192.168.70.241'
t7v2accs = '192.168.70.242'
t7v3accs = '192.168.70.243'
t7v4accs = '192.168.70.244'
t7v5accs = '192.168.70.245'
t7v6accs = '192.168.70.246'
#--------------------------------------------
#//---------------65008------------------
#//---------------MUSHROOM------------------
trensekizmushroom = "192.168.80.253"
#//------------ACCESSPOINTLER---------------
t8v1accs = '192.168.80.241'
t8v2accs = '192.168.80.242'
t8v3accs = '192.168.80.243'
t8v4accs = '192.168.80.244'
t8v5accs = '192.168.80.245'
t8v6accs = '192.168.80.246'
#--------------------------------------------
#//---------------65009------------------
#//---------------MUSHROOM------------------
trendokuzmushroom = "192.168.90.253"
#//------------ACCESSPOINTLER---------------
t9v1accs = '192.168.90.241'
t9v2accs = '192.168.90.242'
t9v3accs = '192.168.90.243'
t9v4accs = '192.168.90.244'
t9v5accs = '192.168.90.245'
t9v6accs = '192.168.90.246'
#--------------------------------------------
#//---------------65010------------------
#//---------------MUSHROOM------------------
trenonmushroom = "192.168.100.253"
#//------------ACCESSPOINTLER---------------
t10v1accs = '192.168.100.241'
t10v2accs = '192.168.100.242'
t10v3accs = '192.168.100.243'
t10v4accs = '192.168.100.244'
t10v5accs = '192.168.100.245'
t10v6accs = '192.168.100.246'
#--------------------------------------------
#//---------------65011------------------
#//---------------MUSHROOM------------------
trenonbirmushroom = "192.168.110.253"
#//------------TEPE EKRANLAR---------------
t11tp1 = '192.168.119.50'
t11tp2 = '192.168.119.51'
t11tp3 = '192.168.119.52'
t11tp4 = '192.168.119.53'
t11tp5 = '192.168.119.54'
t11tp6 = '192.168.119.55'
#//------------SES ISLEMCI------------
t11ses1 = '192.168.119.121'
t11ses2 = '192.168.119.122'
t11ses3 = '192.168.119.123'
t11ses4 = '192.168.119.124'
t11ses5 = '192.168.119.125'
t11ses6 = '192.168.119.126'
#//-------------GPS--------------------
t11gps1 = "192.168.119.227"
t11gps2 = "192.168.119.228"
#//------------LEDLER---------------
t11tcbs1led1   =      '192.168.119.80'
t11tcbs1led2   =      '192.168.119.81'
t11tcbs2led1   =      '192.168.119.82'
t11tcbs2led2   =      '192.168.119.83'
t11mifcs1led1  =      '192.168.119.84'
t11mifcs2led1  =      '192.168.119.85'
t11mifcs2led2  =      '192.168.119.86'
t11mif1as1led1 =      '192.168.119.87'
t11mif1as1led2 =      '192.168.119.88'
t11mif1as2led1 =      '192.168.119.89'
t11mif1as2led2 =      '192.168.119.90'
t11mif1bs1led1 =      '192.168.119.91'
t11mif1bs1led2 =      '192.168.119.92'
t11mif1bs2led1 =      '192.168.119.93'
t11mif1bs2led2 =      '192.168.119.94'
t11mif2s1led1  =      '192.168.119.95'
t11mif2s1led2  =      '192.168.119.96'
t11mif2s2led1  =      '192.168.119.97'
t11mif2s2led2  =      '192.168.119.98'
t11tcfs1led1   =      '192.168.119.99'
t11tcfs1led2   =      '192.168.119.100'
t11tcfs2led1   =      '192.168.119.101'
t11tcfs2led2   =      '192.168.119.102'
t11mif1asoldisled =   '192.168.119.108'
t11mif1bsoldisled =   '192.168.119.109'
t11mif1bsagdisled =   '192.168.119.110'
t11mif2soldisled  =   '192.168.119.111'
t11mif2sagdisled  =   '192.168.119.112'
t11tcfsoldisled   =   '192.168.119.113'
t11tcfsagdisled   =   '192.168.119.114'
#//------------KAMERALAR--------------
t11tcbsoldis =   '192.168.119.9'
t11tcbd1     =   '192.168.119.10'
t11tcbsagdis =   '192.168.119.11'
t11tcbmakinist = '192.168.119.12'
t11tcbs1 =       '192.168.119.13'
t11tcbs2 =       '192.168.119.14'
t11mifcs1 =      '192.168.119.15'
t11mifcs2 =      '192.168.119.16'
t11mif1as1 =     '192.168.119.17'
t11mif1as2 =     '192.168.119.18'
t11mif1bs1 =     '192.168.119.19'
t11mif1bs2 =     '192.168.119.20'
t11mif2s1 =      '192.168.119.21'
t11mif2s2 =      '192.168.119.22'
t11tcfs1 =       '192.168.119.23'
t11tcfs2 =       '192.168.119.24'
t11tcfmakinist = '192.168.119.25'
t11tcfsoldis   = '192.168.119.26'
t11tcfsagdis =   '192.168.119.27'
t11tcfd1 =       '192.168.119.28'
#//---------------65012------------------
#//---------------MUSHROOM------------------
trenonikiv1mushroom = "192.168.41.253"
trenonikiv2mushroom = "192.168.42.253"
trenonikiv3mushroom = "192.168.43.253"
trenonikiv4mushroom = "192.168.44.253"
trenonikiv5mushroom = "192.168.45.253"
trenonikiv6mushroom = "192.168.46.253"
#//------------ACCESSPOINTLER---------------
t12v1accs = '192.168.41.254'
t12v2accs = '192.168.42.254'
t12v3accs = '192.168.43.254'
t12v4accs = '192.168.44.254'
t12v5accs = '192.168.45.254'
t12v6accs = '192.168.46.254'

while True:

    print("""\033[1;32m
---------------------------------------------------------------------------------------
██  ██  ██████   █████████ ████  ████  █████████  ████████  █████████  ████        ████  █████████
██  ██    ██     ██          ██  ██    ██            ██     ██         ██ ██      ██ ██  ██
██  ██    ██     █████████     ██      █████████     ██     ███████    ██  ██    ██  ██  █████████
██  ██    ██            ██     ██             ██     ██     ██         ██   ██  ██   ██         ██
██  ██    ██     █████████     ██      █████████     ██     █████████  ██     ██     ██  █████████ █ █ █
        
 """)
    print("\nYapılacak İşlemi Seçin.\n")
    print("=======================") 
    print("\n1. 65001\n")
    print("2.  65002\n")
    print("3.  65003\n")
    print("4.  65004\n")
    print("5.  65005\n")
    print("6.  65006\n")
    print("7.  65007\n")
    print("8.  65008\n")
    print("9.  65009\n")
    print("10. 65010\n")
    print("11. 65011\n")
    print("12. 65012\n")
    print("0.  ÇIKIŞ")

    print("\n=======================")
    
    secim = input("\nSeçiminiz :")
    if secim == '1':
        output = subprocess.Popen(["ping.exe",ip1],stdout = subprocess.PIPE).communicate()[0]
        response = os.system("ping " + ip1)
        output = str(output)
        if ('unreachable' in output):
            print("65001 UNREACHABLE")
        if response == 0:
            os.system("CLS")
            print ("65001 ON")
            output = subprocess.Popen(["ping.exe",trenbirmushroom],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + trenbirmushroom)
            output = str(output)
            if ('unreachable' in output):
                print("\nMUSHROOM UNREACHABLE")
            elif response == 0:           
                print("\nMUSHROOM ON")
            else:
                print("\nMUSHROOM OFF")
#//-------------------TEPE EKRAN--------------------------        
            output = subprocess.Popen(["ping.exe",t1tp1],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t1tp1)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCB TEPE EKRAN UNREACHABLE")
            elif response == 0:
                print("\nTCB TEPE EKRAN ON")
            else:
                print("\nTCB TEPE EKRAN OFF")
            output = subprocess.Popen(["ping.exe",t1tp2],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t1tp2)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIFC TEPE EKRAN UNREACHABLE")
            elif response == 0:
                print("\nMIFC TEPE EKRAN ON")
            else:         
                print("\nMIFC TEPE EKRAN OFF")
            output = subprocess.Popen(["ping.exe",t1tp3],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t1tp3)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1A TEPE EKRAN UNREACHABLE")
            elif response == 0:
                print("\nMIF1A TEPE EKRAN ON")
            else:         
                print("\nMI1A TEPE EKRAN OFF")
            output = subprocess.Popen(["ping.exe",t1tp4],stdout = subprocess.PIPE).communicate()[0]                 
            response = os.system("ping " + t1tp4)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1B TEPE EKRAN UNREACHABLE")
            elif response == 0:
                print("\nMIF1B TEPE EKRAN ON")
            else:         
                print("\nMIF1B TEPE EKRAN OFF")
            output = subprocess.Popen(["ping.exe",t1tp5],stdout = subprocess.PIPE).communicate()[0]                             
            response = os.system("ping " + t1tp5)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF2 TEPE EKRAN UNREACHABLE")
            elif response == 0:
                print("\nMIF2 TEPE EKRAN ON")
            else:         
                print("\nMIF2 TEPE EKRAN OFF")
            output = subprocess.Popen(["ping.exe",t1tp6],stdout = subprocess.PIPE).communicate()[0]                             
            response = os.system("ping " + t1tp6)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCF TEPE EKRAN UNREACHABLE")
            elif response == 0:
                print("\nTCF TEPE EKRAN ON")
            else:         
                print("\nTCF TEPE EKRAN OFF")
##--------------------SES ISLEMCI----------------------------------------
            output = subprocess.Popen(["ping.exe",t1ses1],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t1ses1)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCB SES ISLEMCI UNREACHABLE")
            elif response == 0:
                print("\nTCB SES ISLEMCI ON")
            else:
                print("\nTCB SES ISLEMCI OFF")
            output = subprocess.Popen(["ping.exe",t1ses2],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t1ses2)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIFC SES ISLEMCI UNREACHABLE")
            elif response == 0:
                print("\nMIFC SES ISLEMCI ON")
            else:         
                print("\nMIFC SES ISLEMCI OFF")  
            output = subprocess.Popen(["ping.exe",t1ses3],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t1ses3)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1A SES ISLEMCI UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SES ISLEMCI ON")
            else:         
                print("\nMI1A SES ISLEMCI OFF")     
            output = subprocess.Popen(["ping.exe",t1ses4],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t1ses4)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1B SES ISLEMCI UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SES ISLEMCI ON")
            else:         
                print("\nMIF1B SES ISLEMCI OFF")
            output = subprocess.Popen(["ping.exe",t1ses5],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t1ses5)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF2 SES ISLEMCI UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SES ISLEMCI ON")
            else:         
                print("\nMIF2 SES ISLEMCI OFF")
            output = subprocess.Popen(["ping.exe",t1ses6],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t1ses6)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCF SES ISLEMCI UNREACHABLE")
            elif response == 0:
                print("\nTCF SES ISLEMCI ON")
            else:         
                print("\nTCF SES ISLEMCI OFF")
#//----------------------GPS--------------------------
            t1gps1 = "192.168.49.227"
            output = subprocess.Popen(["ping.exe",t1gps1],stdout = subprocess.PIPE).communicate()[0]                                         
            unreachable = os.system("ping " + t1gps1)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCB GPS UNREACHABLE")
            elif unreachable == 0:
                    print("\nTCB GPS ON")
            else:
                print("\nTCB GPS OFF")
            output = subprocess.Popen(["ping.exe",t1gps2],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t1gps2)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCF GPS UNREACHABLE")
            elif response == 0:
                print("\nTCF GPS ON")
            else:
                print("\nTCF GPS OFF")    
#//------------------LEDLER---------------------------
            output = subprocess.Popen(["ping.exe",t1tcbs1led1],stdout = subprocess.PIPE).communicate()[0]                                                     
            response = os.system("ping " + t1tcbs1led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCB SALON 1 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nTCB SALON 1 LED 1 ON")
            else:
                print("\nTCB SALON 1 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t1tcbs1led2],stdout = subprocess.PIPE).communicate()[0]                                                     
            response = os.system("ping " + t1tcbs1led2)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCB SALON 1 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nTCB SALON 1 LED 2 ON")
            else:
                print("\nTCB SALON 1 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t1tcbs2led1],stdout = subprocess.PIPE).communicate()[0]                                                     
            response = os.system("ping " + t1tcbs2led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCB SALON 2 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nTCB SALON 2 LED 1 ON")
            else:
                print("\nTCB SALON 2 LED 1 OFF")
            unreachable = os.system("ping " + t1tcbs2led2)
            output = subprocess.Popen(["ping.exe",t1tcbs2led2],stdout = subprocess.PIPE).communicate()[0]                                                     
            output = str(output) 
            if ('unreachable' in output):
                print("TCB SALON 2 LED 2 UNREACHABLE")
            elif unreachable == 0:
                print("\nTCB SALON 2 LED 2 ON")
            else:
                print("\nTCB SALON 2 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t1mifcs1led1],stdout = subprocess.PIPE).communicate()[0]                                                                 
            response = os.system("ping " + t1mifcs1led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIFC SALON 1 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIFC SALON 1 LED 1 ON")
            else:
                print("\nMIFC SALON 1 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t1mifcs2led1],stdout = subprocess.PIPE).communicate()[0]                                                                 
            response = os.system("ping " + t1mifcs2led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIFC SALON 2 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIFC SALON 2 LED 1 ON")
            else:
                print("\nMIFC SALON 2 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t1mifcs2led2],stdout = subprocess.PIPE).communicate()[0]                                                                 
            response = os.system("ping " + t1mifcs2led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIFC SALON 2 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nMIFC SALON 2 LED 2 ON")
            else:
                print("\nMIFC SALON 2 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t1mif1as1led1],stdout = subprocess.PIPE).communicate()[0]                                                                             
            response = os.system("ping " + t1mif1as1led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1A SALON 1 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SALON 1 LED 1 ON")
            else:
                print("\nMIF1A SALON 1 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t1mif1as1led2],stdout = subprocess.PIPE).communicate()[0]                                                                                          
            response = os.system("ping " + t1mif1as1led2)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1A SALON 1 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SALON 1 LED 2 ON")
            else:
                print("\nMIF1A SALON 1 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t1mif1as2led1],stdout = subprocess.PIPE).communicate()[0]                                                                                         
            response = os.system("ping " + t1mif1as2led1),
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF1A SALON 2 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SALON 2 LED 1 ON")
            else:
                print("\nMIF1A SALON 2 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t1mif1as2led2],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t1mif1as2led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF1A SALON 2 LED 2 UNREACHABLE")                                                                                                      
            elif response == 0:
                print("\nMIF1A SALON 2 LED 2 ON")
            else:
                print("\nMIF1A SALON 2 LED 2 OFF")
#/-----------------------------------------------------------
            output = subprocess.Popen(["ping.exe",t1mif1bs1led1],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t1mif1bs1led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1B SALON 1 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SALON 1 LED 1 ON") 
            else:
                print("\nMIF1B SALON 1 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t1mif1bs1led2],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t1mif1bs1led2)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1B SALON 1 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SALON 1 LED 2 ON")
            else:
                print("\nMIF1B SALON 1 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t1mif1bs2led1],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t1mif1bs2led1)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF1B SALON 2 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SALON 2 LED 1 ON")
            else:
                print("\nMIF1B SALON 2 LED 1 OFF") 
            output = subprocess.Popen(["ping.exe",t1mif1bs2led2],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t1mif1bs2led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF1B SALON 2 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SALON 2 LED 2 ON")
            else:
                print("\nMIF1B SALON 2 LED 2 OFF")
#//---------------------------------------------------------------
            output = subprocess.Popen(["ping.exe",t1mif2s1led1],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t1mif2s1led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF2 SALON 1 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SALON 1 LED 1 ON")
            else:
                print("\nMIF2 SALON 1 LED 1 OFF") 
            output = subprocess.Popen(["ping.exe",t1mif2s1led2],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t1mif2s1led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF2 SALON 1 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SALON 1 LED 2 ON")
            else:
                print("\nMIF2 SALON 1 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t1mif2s2led1],stdout = subprocess.PIPE).communicate()[0]            
            response = os.system("ping " + t1mif2s2led1)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF2 SALON 2 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SALON 2 LED 1 ON")
            else:
                print("\nMIF2 SALON 2 LED 1 OFF") 
            output = subprocess.Popen(["ping.exe",t1mif2s2led2],stdout = subprocess.PIPE).communicate()[0]                        
            response = os.system("ping " + t1mif2s2led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF2 SALON 2 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SALON 2 LED 2 ON")
            else:
                print("\nMIF2 SALON 2 LED 2 OFF")
#//-----------------------------------------------------------
            output = subprocess.Popen(["ping.exe",t1tcfs1led1],stdout = subprocess.PIPE).communicate()[0]                        
            response = os.system("ping " + t1tcfs1led1)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCF SALON 1 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nTCF SALON 1 LED 1 ON")
            else:
                print("\nTCF SALON 1 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t1tcfs1led2],stdout = subprocess.PIPE).communicate()[0]                        
            response = os.system("ping " + t1tcfs1led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCF SALON 1 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nTCF SALON 1 LED 2 ON")
            else:
                print("\nTCF SALON 1 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t1tcfs2led1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1tcfs2led1)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCF SALON 2 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nTCF SALON 2 LED 1 ON")
            else:
                print("\nTCF SALON 2 LED 1 OFF") 
            output = subprocess.Popen(["ping.exe",t1tcfs2led2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1tcfs2led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCF SALON 2 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nTCF SALON 2 LED 2 ON")
            else:
                print("\nTCF SALON 2 LED 2 OFF")                          
#//--------------------------------------------------------
            output = subprocess.Popen(["ping.exe",t1mif1asoldisled],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1mif1asoldisled)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF1A SOL DIS LED UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SOL DIS LED ON")
            else:
                print("\nMIF1A SOL DIS LED OFF")
            output = subprocess.Popen(["ping.exe",t1mif1bsoldisled],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1mif1bsoldisled)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF1B SOL DIS LED UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SOL DIS LED ON")
            else:
                print("\nMIF1B SOL DIS LED OFF")
            output = subprocess.Popen(["ping.exe",t1mif2soldisled],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1mif2soldisled)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF2 SOL DIS LED UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SOL DIS LED ON")
            else:
                print("\nMIF2 SOL DIS LED OFF")
            output = subprocess.Popen(["ping.exe",t1mif2sagdisled],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1mif2sagdisled)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF2 SAG DIS LED UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SAĞ DIS LED ON")
            else:
                print("\nMIF2 SAĞ DIS LED OFF")
            output = subprocess.Popen(["ping.exe",t1tcfsoldisled],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1tcfsoldisled)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCF SOL DIS LED UNREACHABLE")
            elif response == 0:
                print("\nTCF SOL DIŞ LED ON")
            else:
                print("\nTCF SOL DIŞ LED OFF")
            output = subprocess.Popen(["ping.exe",t1tcfsagdisled],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1tcfsagdisled)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCF SAG DIS LED UNREACHABLE")
            elif response == 0:
                print("\nTCF SAG DIŞ LED ON")
            else:
                print("\nTCF SAĞ DIŞ LED OFF")
#/------------------------KAMERALAR-----------------------------
            output = subprocess.Popen(["ping.exe",t1tcbsoldis],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1tcbsoldis)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCB SOL DIS KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCB SOL DIS KAMERA ON")
            else:
                print("\nTCB SOL DIŞ KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t1tcbd1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1tcbd1)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCB ÖN KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCB ÖN KAMERA ON")
            else:
                print("\nTCB ÖN KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t1tcbsagdis],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1tcbsagdis)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCB SAG KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCB SAG DIS KAMERA ON")
            else:
                print("\nTCB SAS DIS KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t1tcbmakinist],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1tcbmakinist)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCB MAKİNİST KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCB MAKİNİST KAMERA ON")
            else:
                print("\nTCB MAKİNİST KAMERA OFF") 
            output = subprocess.Popen(["ping.exe",t1tcbs1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1tcbs1)
            output = str(output) 
            if('unreachable' in output):
                print("\nTCB SALON 1 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCB SALON 1 KAMERA ON")
            else:
                print("\nTCB SALON 1 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t1tcbs2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1tcbs2)
            output = str(output)
            if('unreachable' in output):
                print("\nTCB SALON 2 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCB SALON 2 KAMERA ON")
            else:
                print("\nTCB SALON 2 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t1mifcs1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1mifcs1)
            output = str(output)
            if('unreachable' in output):
                print("\nMIFC SALON 1 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIFC SALON 1 KAMERA ON")
            else:
                print("\nMIFC SALON 1 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t1mifcs2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1mifcs2)
            output = str(output)
            if('unreachable' in output):
                print("\nMIFC SALON 2 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIFC SALON 2 KAMERA ON")
            else:
                print("\nMIFC SALON 2 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t1mif1as1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1mif1as1)
            output = str(output)
            if('unreachable' in output):
                print("\nMIF1A SALON 1 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SALON 1 KAMERA ON")
            else:
                print("\nMIF1A SALON 1 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t1mif1as2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1mif1as2)
            output = str(output)
            if('unreachable' in output):
                print("\nMIF1A SALON 2 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SALON 2 KAMERA ON")
            else:
                print("\nMIF1A SALON 2 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t1mif1bs1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1mif1bs1)
            output = str(output)
            if('unreachable' in output):
                print("\nMIF1B SALON 1 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SALON 1 KAMERA ON")
            else:
                print("\nMIF1B SALON 1 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t1mif1bs2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1mif1bs2)
            output = str(output)
            if('unreachable' in output):
                print("\nMIF1B SALON 2 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SALON 2 KAMERA ON")
            else:
                print("\nMIF1B SALON 2 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t1mif2s1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1mif2s1)
            output = str(output)
            if('unreachable' in output):
                print("\nMIF2 SALON 1 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SALON 1 KAMERA ON")
            else:
                print("\nMIF2 SALON 1 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t1mif2s2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1mif2s2)
            output = str(output)
            if('unreachable' in output):
                print("\nMIF2 SALON 2 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SALON 2 KAMERA ON")
            else:
                print("\nMIF2 SALON 2 KAMERA OFF")
            #//------------------------------------------------
            output = subprocess.Popen(["ping.exe",t1tcfs1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1tcfs1)
            output = str(output)
            if('unreachable' in output):
                print("\nTCF SALON 1 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCF SALON 1 KAMERA ON")
            else:
                print("\nTCF SALON 1 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t1tcfs2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1tcfs2)
            output = str(output)
            if('unreachable' in output):
                print("\nTCF SALON 2 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCF SALON 2 KAMERA ON")
            else:
                print("\nTCF SALON 2 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t1tcfmakinist],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t1tcfmakinist)
            output = str(output)
            if('unreachable' in output):
                print("\nTCF MAKİNİST KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCF MAKİNİST KAMERA ON")
            else:
                print("\nTCF MAKİNİST KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t1tcfsoldis],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t1tcfsoldis)
            output = str(output)
            if('unreachable' in output):
                print("\nTCF SOL DIŞ KAMERA UNREACHABLE")
            elif response ==  0:
                print("\nTCF SOL DIŞ KAMERA ON")
            else:
                print("\nTCF SOL DIŞ KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t1tcfsagdis],stdout = subprocess.PIPE).communicate()[0]    
            response = os.system("ping " + t1tcfsagdis)
            output = str(output)
            if('unreachable' in output):
                print("\nTCF SAĞ DIŞ KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCF SAĞ DIŞ KAMERA ON")
            else:
                print("\nTCF SAĞ DIŞ KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t1tcfd1],stdout = subprocess.PIPE).communicate()[0]    
            response = os.system("ping " + t1tcfd1)
            output = str(output)
            if('unreachable' in output):
                print("\nTCF ÖN KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCF ÖN KAMERA ON")
            else:
                print("\nTCF ÖN DIŞ KAMERA OFF")        
        else:
            print ("\n65001 OFF")
    if secim == '2':
        output = subprocess.Popen(["ping.exe",ip2],stdout = subprocess.PIPE).communicate()[0]    
        response = os.system("ping " + ip2)
        output = str(output)
        if('unreachable' in output):
                print("\n65002 UNREACHABLE")
        if response == 0:
            os.system("CLS")
            print ("65002 ON")
            output = subprocess.Popen(["ping.exe",trenikimushroom],stdout = subprocess.PIPE).communicate()[0]    
            response = os.system("ping " + trenikimushroom)
            output = str(output)
            if('unreachable' in output):
                print("\nMUSHROOM UNREACHABLE")
            elif response == 0:           
                print("\nMUSHROOM ON")
            else:
                print("\nMUSHROOM OFF")
            output = subprocess.Popen(["ping.exe",t2v1accs],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t2v1accs)
            output = str(output)
            if('unreachable' in output):
                print("\nTCB ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nTCB ACCESSPOINT ON")
            else:
                print("\nTCB ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t2v2accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t2v2accs)
            output = str(output)
            if('unreachable' in output):
                print("\nMIFC ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIFC ACCESSPOINT ON")
            else:         
                print("\nMIFC ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t2v3accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t2v3accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF1A ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF1A ACCESSPOINT ON")
            else:         
                print("\nMI1A ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t2v4accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t2v4accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF1B ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF1B ACCESSPOINT ON")
            else:         
                print("\nMI1B ACCESSPOINT OFF") 
            output = subprocess.Popen(["ping.exe",t2v5accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t2v5accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF2 ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF2 ACCESSPOINT ON")
            else:         
                print("\nMIF2 ACCESSPOINT OFF")     

            output = subprocess.Popen(["ping.exe",t2v6accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t2v6accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nTCF ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nTCF ACCESSPOINT ON")
            else:         
                print("\nTCF ACCESSPOINT OFF")                
        else:         
            print ("65002 OFF")
#//---------------------------------------------------------------------
    if secim == '3':
        output = subprocess.Popen(["ping.exe",ip3],stdout = subprocess.PIPE).communicate()[0]    
        response = os.system("ping " + ip3)
        output = str(output)
        if('unreachable' in output):
                print("\n65003 UNREACHABLE")
        if response == 0:
            os.system("CLS")
            print ("65003 ON")
            output = subprocess.Popen(["ping.exe",trenucmushroom],stdout = subprocess.PIPE).communicate()[0]    
            response = os.system("ping " + trenucmushroom)
            output = str(output)
            if('unreachable' in output):
                print("\nMUSHROOM UNREACHABLE")
            elif response == 0:           
                print("\nMUSHROOM ON")
            else:
                print("\nMUSHROOM OFF")
            output = subprocess.Popen(["ping.exe",t3v1accs],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t3v1accs)
            output = str(output)
            if('unreachable' in output):
                print("\nTCB ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nTCB ACCESSPOINT ON")
            else:
                print("\nTCB ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t3v2accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t3v2accs)
            output = str(output)
            if('unreachable' in output):
                print("\nMIFC ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIFC ACCESSPOINT ON")
            else:         
                print("\nMIFC ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t3v3accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t3v3accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF1A ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF1A ACCESSPOINT ON")
            else:         
                print("\nMI1A ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t3v4accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t3v4accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF1B ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF1B ACCESSPOINT ON")
            else:         
                print("\nMI1B ACCESSPOINT OFF") 
            output = subprocess.Popen(["ping.exe",t3v5accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t3v5accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF2 ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF2 ACCESSPOINT ON")
            else:         
                print("\nMIF2 ACCESSPOINT OFF")     

            output = subprocess.Popen(["ping.exe",t3v6accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t3v6accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nTCF ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nTCF ACCESSPOINT ON")
            else:         
                print("\nTCF ACCESSPOINT OFF")    
        else:
            print ("\n65003 OFF")
#/-----------------------------------------------------------------------------
    if secim == '4':
        output = subprocess.Popen(["ping.exe",ip4],stdout = subprocess.PIPE).communicate()[0]
        response = os.system("ping " + ip4)
        output = str(output)
        if ('unreachable' in output):
            print("65004 UNREACHABLE")
        if response == 0:
            os.system("CLS")
            print ("65004 ON")
            output = subprocess.Popen(["ping.exe",trendortmushroom],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + trendortmushroom)
            output = str(output)
            if ('unreachable' in output):
                print("\nMUSHROOM UNREACHABLE")
            elif response == 0:           
                print("\nMUSHROOM ON")
            else:
                print("\nMUSHROOM OFF")
#//-------------------TEPE EKRAN--------------------------        
            output = subprocess.Popen(["ping.exe",t4tp1],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t4tp1)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCB TEPE EKRAN UNREACHABLE")
            elif response == 0:
                print("\nTCB TEPE EKRAN ON")
            else:
                print("\nTCB TEPE EKRAN OFF")
            output = subprocess.Popen(["ping.exe",t4tp2],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t4tp2)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIFC TEPE EKRAN UNREACHABLE")
            elif response == 0:
                print("\nMIFC TEPE EKRAN ON")
            else:         
                print("\nMIFC TEPE EKRAN OFF")
            output = subprocess.Popen(["ping.exe",t4tp3],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t4tp3)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1A TEPE EKRAN UNREACHABLE")
            elif response == 0:
                print("\nMIF1A TEPE EKRAN ON")
            else:         
                print("\nMI1A TEPE EKRAN OFF")
            output = subprocess.Popen(["ping.exe",t4tp4],stdout = subprocess.PIPE).communicate()[0]                 
            response = os.system("ping " + t4tp4)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1B TEPE EKRAN UNREACHABLE")
            elif response == 0:
                print("\nMIF1B TEPE EKRAN ON")
            else:         
                print("\nMIF1B TEPE EKRAN OFF")
            output = subprocess.Popen(["ping.exe",t4tp5],stdout = subprocess.PIPE).communicate()[0]                             
            response = os.system("ping " + t4tp5)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF2 TEPE EKRAN UNREACHABLE")
            elif response == 0:
                print("\nMIF2 TEPE EKRAN ON")
            else:         
                print("\nMIF2 TEPE EKRAN OFF")
            output = subprocess.Popen(["ping.exe",t4tp6],stdout = subprocess.PIPE).communicate()[0]                             
            response = os.system("ping " + t4tp6)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCF TEPE EKRAN UNREACHABLE")
            elif response == 0:
                print("\nTCF TEPE EKRAN ON")
            else:         
                print("\nTCF TEPE EKRAN OFF")
##--------------------SES ISLEMCI----------------------------------------
            output = subprocess.Popen(["ping.exe",t4ses1],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t4ses1)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCB SES ISLEMCI UNREACHABLE")
            elif response == 0:
                print("\nTCB SES ISLEMCI ON")
            else:
                print("\nTCB SES ISLEMCI OFF")
            output = subprocess.Popen(["ping.exe",t4ses2],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t4ses2)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIFC SES ISLEMCI UNREACHABLE")
            elif response == 0:
                print("\nMIFC SES ISLEMCI ON")
            else:         
                print("\nMIFC SES ISLEMCI OFF")  
            output = subprocess.Popen(["ping.exe",t4ses3],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t4ses3)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1A SES ISLEMCI UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SES ISLEMCI ON")
            else:         
                print("\nMI1A SES ISLEMCI OFF")     
            output = subprocess.Popen(["ping.exe",t4ses4],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t4ses4)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1B SES ISLEMCI UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SES ISLEMCI ON")
            else:         
                print("\nMIF1B SES ISLEMCI OFF")
            output = subprocess.Popen(["ping.exe",t4ses5],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t4ses5)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF2 SES ISLEMCI UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SES ISLEMCI ON")
            else:         
                print("\nMIF2 SES ISLEMCI OFF")
            output = subprocess.Popen(["ping.exe",t4ses6],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t4ses6)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCF SES ISLEMCI UNREACHABLE")
            elif response == 0:
                print("\nTCF SES ISLEMCI ON")
            else:         
                print("\nTCF SES ISLEMCI OFF")
#//----------------------GPS--------------------------
            t1gps1 = "192.168.49.227"
            output = subprocess.Popen(["ping.exe",t4gps1],stdout = subprocess.PIPE).communicate()[0]                                         
            unreachable = os.system("ping " + t4gps1)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCB GPS UNREACHABLE")
            elif unreachable == 0:
                    print("\nTCB GPS ON")
            else:
                print("\nTCB GPS OFF")
            output = subprocess.Popen(["ping.exe",t4gps2],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t4gps2)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCF GPS UNREACHABLE")
            elif response == 0:
                print("\nTCF GPS ON")
            else:
                print("\nTCF GPS OFF")    
#//------------------LEDLER---------------------------
            output = subprocess.Popen(["ping.exe",t4tcbs1led1],stdout = subprocess.PIPE).communicate()[0]                                                     
            response = os.system("ping " + t4tcbs1led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCB SALON 1 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nTCB SALON 1 LED 1 ON")
            else:
                print("\nTCB SALON 1 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t4tcbs1led2],stdout = subprocess.PIPE).communicate()[0]                                                     
            response = os.system("ping " + t4tcbs1led2)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCB SALON 1 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nTCB SALON 1 LED 2 ON")
            else:
                print("\nTCB SALON 1 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t4tcbs2led1],stdout = subprocess.PIPE).communicate()[0]                                                     
            response = os.system("ping " + t4tcbs2led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCB SALON 2 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nTCB SALON 2 LED 1 ON")
            else:
                print("\nTCB SALON 2 LED 1 OFF")
            unreachable = os.system("ping " + t4tcbs2led2)
            output = subprocess.Popen(["ping.exe",t4tcbs2led2],stdout = subprocess.PIPE).communicate()[0]                                                     
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCB SALON 2 LED 2 UNREACHABLE")
            elif unreachable == 0:
                print("\nTCB SALON 2 LED 2 ON")
            else:
                print("\nTCB SALON 2 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t4mifcs1led1],stdout = subprocess.PIPE).communicate()[0]                                                                 
            response = os.system("ping " + t4mifcs1led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIFC SALON 1 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIFC SALON 1 LED 1 ON")
            else:
                print("\nMIFC SALON 1 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t4mifcs2led1],stdout = subprocess.PIPE).communicate()[0]                                                                 
            response = os.system("ping " + t4mifcs2led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIFC SALON 2 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIFC SALON 2 LED 1 ON")
            else:
                print("\nMIFC SALON 2 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t4mifcs2led2],stdout = subprocess.PIPE).communicate()[0]                                                                 
            response = os.system("ping " + t4mifcs2led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIFC SALON 2 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nMIFC SALON 2 LED 2 ON")
            else:
                print("\nMIFC SALON 2 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t4mif1as1led1],stdout = subprocess.PIPE).communicate()[0]                                                                             
            response = os.system("ping " + t4mif1as1led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1A SALON 1 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SALON 1 LED 1 ON")
            else:
                print("\nMIF1A SALON 1 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t4mif1as1led2],stdout = subprocess.PIPE).communicate()[0]                                                                                          
            response = os.system("ping " + t4mif1as1led2)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1A SALON 1 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SALON 1 LED 2 ON")
            else:
                print("\nMIF1A SALON 1 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t4mif1as2led1],stdout = subprocess.PIPE).communicate()[0]                                                                                         
            response = os.system("ping " + t4mif1as2led1)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF1A SALON 2 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SALON 2 LED 1 ON")
            else:
                print("\nMIF1A SALON 2 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t4mif1as2led2],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t4mif1as2led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF1A SALON 2 LED 2 UNREACHABLE")                                                                                                      
            elif response == 0:
                print("\nMIF1A SALON 2 LED 2 ON")
            else:
                print("\nMIF1A SALON 2 LED 2 OFF")
#/-----------------------------------------------------------
            output = subprocess.Popen(["ping.exe",t4mif1bs1led1],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t4mif1bs1led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1B SALON 1 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SALON 1 LED 1 ON") 
            else:
                print("\nMIF1B SALON 1 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t4mif1bs1led2],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t4mif1bs1led2)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1B SALON 1 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SALON 1 LED 2 ON")
            else:
                print("\nMIF1B SALON 1 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t4mif1bs2led1],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t4mif1bs2led1)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF1B SALON 2 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SALON 2 LED 1 ON")
            else:
                print("\nMIF1B SALON 2 LED 1 OFF") 
            output = subprocess.Popen(["ping.exe",t4mif1bs2led2],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t4mif1bs2led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF1B SALON 2 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SALON 2 LED 2 ON")
            else:
                print("\nMIF1B SALON 2 LED 2 OFF")
#//---------------------------------------------------------------
            output = subprocess.Popen(["ping.exe",t4mif2s1led1],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t4mif2s1led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF2 SALON 1 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SALON 1 LED 1 ON")
            else:
                print("\nMIF2 SALON 1 LED 1 OFF") 
            output = subprocess.Popen(["ping.exe",t4mif2s1led2],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t4mif2s1led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF2 SALON 1 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SALON 1 LED 2 ON")
            else:
                print("\nMIF2 SALON 1 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t4mif2s2led1],stdout = subprocess.PIPE).communicate()[0]            
            response = os.system("ping " + t4mif2s2led1)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF2 SALON 2 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SALON 2 LED 1 ON")
            else:
                print("\nMIF2 SALON 2 LED 1 OFF") 
            output = subprocess.Popen(["ping.exe",t4mif2s2led2],stdout = subprocess.PIPE).communicate()[0]                        
            response = os.system("ping " + t4mif2s2led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF2 SALON 2 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SALON 2 LED 2 ON")
            else:
                print("\nMIF2 SALON 2 LED 2 OFF")
#//-----------------------------------------------------------
            output = subprocess.Popen(["ping.exe",t4tcfs1led1],stdout = subprocess.PIPE).communicate()[0]                        
            response = os.system("ping " + t4tcfs1led1)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCF SALON 1 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nTCF SALON 1 LED 1 ON")
            else:
                print("\nTCF SALON 1 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t4tcfs1led2],stdout = subprocess.PIPE).communicate()[0]                        
            response = os.system("ping " + t4tcfs1led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCF SALON 1 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nTCF SALON 1 LED 2 ON")
            else:
                print("\nTCF SALON 1 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t4tcfs2led1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4tcfs2led1)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCF SALON 2 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nTCF SALON 2 LED 1 ON")
            else:
                print("\nTCF SALON 2 LED 1 OFF") 
            output = subprocess.Popen(["ping.exe",t4tcfs2led2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4tcfs2led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCF SALON 2 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nTCF SALON 2 LED 2 ON")
            else:
                print("\nTCF SALON 2 LED 2 OFF")                          
#//--------------------------------------------------------
            output = subprocess.Popen(["ping.exe",t4mif1asoldisled],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4mif1asoldisled)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF1A SOL DIS LED UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SOL DIS LED ON")
            else:
                print("\nMIF1A SOL DIS LED OFF")
            output = subprocess.Popen(["ping.exe",t4mif1bsoldisled],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4mif1bsoldisled)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF1B SOL DIS LED UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SOL DIS LED ON")
            else:
                print("\nMIF1B SOL DIS LED OFF")
            output = subprocess.Popen(["ping.exe",t4mif2soldisled],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4mif2soldisled)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF2 SOL DIS LED UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SOL DIS LED ON")
            else:
                print("\nMIF2 SOL DIS LED OFF")
            output = subprocess.Popen(["ping.exe",t4mif2sagdisled],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4mif2sagdisled)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF2 SAG DIS LED UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SAĞ DIS LED ON")
            else:
                print("\nMIF2 SAĞ DIS LED OFF")
            output = subprocess.Popen(["ping.exe",t4tcfsoldisled],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4tcfsoldisled)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCF SOL DIS LED UNREACHABLE")
            elif response == 0:
                print("\nTCF SOL DIŞ LED ON")
            else:
                print("\nTCF SOL DIŞ LED OFF")
            output = subprocess.Popen(["ping.exe",t4tcfsagdisled],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4tcfsagdisled)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCF SAG DIS LED UNREACHABLE")
            elif response == 0:
                print("\nTCF SAG DIŞ LED ON")
            else:
                print("\nTCF SAĞ DIŞ LED OFF")
#/------------------------KAMERALAR-----------------------------
            output = subprocess.Popen(["ping.exe",t4tcbsoldis],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4tcbsoldis)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCB SOL DIS KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCB SOL DIS KAMERA ON")
            else:
                print("\nTCB SOL DIŞ KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t4tcbd1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4tcbd1)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCB ÖN KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCB ÖN KAMERA ON")
            else:
                print("\nTCB ÖN KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t4tcbsagdis],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4tcbsagdis)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCB SAG KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCB SAG DIS KAMERA ON")
            else:
                print("\nTCB SAS DIS KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t4tcbmakinist],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4tcbmakinist)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCB MAKİNİST KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCB MAKİNİST KAMERA ON")
            else:
                print("\nTCB MAKİNİST KAMERA OFF") 
            output = subprocess.Popen(["ping.exe",t4tcbs1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4tcbs1)
            output = str(output) 
            if('unreachable' in output):
                print("\nTCB SALON 1 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCB SALON 1 KAMERA ON")
            else:
                print("\nTCB SALON 1 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t4tcbs2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4tcbs2)
            output = str(output)
            if('unreachable' in output):
                print("\nTCB SALON 2 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCB SALON 2 KAMERA ON")
            else:
                print("\nTCB SALON 2 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t4mifcs1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4mifcs1)
            output = str(output)
            if('unreachable' in output):
                print("\nMIFC SALON 1 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIFC SALON 1 KAMERA ON")
            else:
                print("\nMIFC SALON 1 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t4mifcs2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4mifcs2)
            output = str(output)
            if('unreachable' in output):
                print("\nMIFC SALON 2 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIFC SALON 2 KAMERA ON")
            else:
                print("\nMIFC SALON 2 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t4mif1as1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4mif1as1)
            output = str(output)
            if('unreachable' in output):
                print("\nMIF1A SALON 1 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SALON 1 KAMERA ON")
            else:
                print("\nMIF1A SALON 1 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t4mif1as2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4mif1as2)
            output = str(output)
            if('unreachable' in output):
                print("\nMIF1A SALON 2 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SALON 2 KAMERA ON")
            else:
                print("\nMIF1A SALON 2 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t4mif1bs1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4mif1bs1)
            output = str(output)
            if('unreachable' in output):
                print("\nMIF1B SALON 1 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SALON 1 KAMERA ON")
            else:
                print("\nMIF1B SALON 1 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t4mif1bs2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4mif1bs2)
            output = str(output)
            if('unreachable' in output):
                print("\nMIF1B SALON 2 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SALON 2 KAMERA ON")
            else:
                print("\nMIF1B SALON 2 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t4mif2s1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4mif2s1)
            output = str(output)
            if('unreachable' in output):
                print("\nMIF2 SALON 1 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SALON 1 KAMERA ON")
            else:
                print("\nMIF2 SALON 1 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t4mif2s2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4mif2s2)
            output = str(output)
            if('unreachable' in output):
                print("\nMIF2 SALON 2 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SALON 2 KAMERA ON")
            else:
                print("\nMIF2 SALON 2 KAMERA OFF")
            #//------------------------------------------------
            output = subprocess.Popen(["ping.exe",t4tcfs1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4tcfs1)
            output = str(output)
            if('unreachable' in output):
                print("\nTCF SALON 1 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCF SALON 1 KAMERA ON")
            else:
                print("\nTCF SALON 1 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t4tcfs2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t4tcfs2)
            output = str(output)
            if('unreachable' in output):
                print("\nTCF SALON 2 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCF SALON 2 KAMERA ON")
            else:
                print("\nTCF SALON 2 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t4tcfmakinist],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t4tcfmakinist)
            output = str(output)
            if('unreachable' in output):
                print("\nTCF MAKİNİST KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCF MAKİNİST KAMERA ON")
            else:
                print("\nTCF MAKİNİST KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t4tcfsoldis],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t4tcfsoldis)
            output = str(output)
            if('unreachable' in output):
                print("\nTCF SOL DIŞ KAMERA UNREACHABLE")
            elif response ==  0:
                print("\nTCF SOL DIŞ KAMERA ON")
            else:
                print("\nTCF SOL DIŞ KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t4tcfsagdis],stdout = subprocess.PIPE).communicate()[0]    
            response = os.system("ping " + t4tcfsagdis)
            output = str(output)
            if('unreachable' in output):
                print("\nTCF SAĞ DIŞ KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCF SAĞ DIŞ KAMERA ON")
            else:
                print("\nTCF SAĞ DIŞ KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t4tcfd1],stdout = subprocess.PIPE).communicate()[0]    
            response = os.system("ping " + t4tcfd1)
            output = str(output)
            if('unreachable' in output):
                print("\nTCF ÖN KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCF ÖN KAMERA ON")
            else:
                print("\nTCF ÖN DIŞ KAMERA OFF")               
        else:
            print ("65004 OFF")

    #//------------------------------------------------
    if secim == '5':   
        output = subprocess.Popen(["ping.exe",ip5],stdout = subprocess.PIPE).communicate()[0]    
        response = os.system("ping " + ip5)
        output = str(output)
        if('unreachable' in output):
                print("\n65005 UNREACHABLE")
        if response == 0:
            os.system("CLS")
            print ("65005 ON")
            output = subprocess.Popen(["ping.exe",trenbesmushroom],stdout = subprocess.PIPE).communicate()[0]    
            response = os.system("ping " + trenbesmushroom)
            output = str(output)
            if('unreachable' in output):
                print("\nMUSHROOM UNREACHABLE")
            elif response == 0:           
                print("\nMUSHROOM ON")
            else:
                print("\nMUSHROOM OFF")
            output = subprocess.Popen(["ping.exe",t5v1accs],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t5v1accs)
            output = str(output)
            if('unreachable' in output):
                print("\nTCB ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nTCB ACCESSPOINT ON")
            else:
                print("\nTCB ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t5v2accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t5v2accs)
            output = str(output)
            if('unreachable' in output):
                print("\nMIFC ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIFC ACCESSPOINT ON")
            else:         
                print("\nMIFC ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t5v3accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t5v3accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF1A ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF1A ACCESSPOINT ON")
            else:         
                print("\nMI1A ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t5v4accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t5v4accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF1B ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF1B ACCESSPOINT ON")
            else:         
                print("\nMI1B ACCESSPOINT OFF") 
            output = subprocess.Popen(["ping.exe",t5v5accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t5v5accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF2 ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF2 ACCESSPOINT ON")
            else:         
                print("\nMIF2 ACCESSPOINT OFF")     
            output = subprocess.Popen(["ping.exe",t5v6accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t5v6accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nTCF ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nTCF ACCESSPOINT ON")
            else:         
                print("\nTCF ACCESSPOINT OFF")                
        else:
            print ("65005 OFF")
    #//------------------------------------------------------------
    if secim == '6':
        output = subprocess.Popen(["ping.exe",trenaltiv1mushroom],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + trenaltiv1mushroom)
        output = str(output)
        if('unreachable' in output):
            print("\nTCB MUSHROOM UNREACHABLE")
        elif response == 0:  
            print ("\nTCB MUSHROOM ON")
        else:
            print("\nTCB MUSHROOM OFF")
        output = subprocess.Popen(["ping.exe",t6v1accs],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + t6v1accs)
        output = str(output)
        if('unreachable' in output):
            print("\nTCB ACCESSPOINT UNREACHABLE")
        elif response == 0:  
            print ("\nTCB ACCESSPOINT ON")
        else:
            print("\nTCB ACCESSPOINT OFF")         
        output = subprocess.Popen(["ping.exe",trenaltiv2mushroom],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + trenaltiv2mushroom)
        output = str(output)
        if('unreachable' in output):
            print("\nMIFC MUSHROOM UNREACHABLE")
        elif response == 0:  
            print ("\nMIFC MUSHROOM ON")
        else:
            print("\nMIFC MUSHROOM OFF")
        output = subprocess.Popen(["ping.exe",t6v2accs],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + t6v2accs)
        output = str(output)
        if('unreachable' in output):
            print("\nMIFC ACCESSPOINT UNREACHABLE")
        elif response == 0:  
            print ("\nMIFC ACCESSPOINT ON")
        else:
            print("\nMIFC ACCESSPOINT OFF")
        output = subprocess.Popen(["ping.exe",trenaltiv3mushroom],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + trenaltiv3mushroom)
        output = str(output)
        if('unreachable' in output):
            print("\nMIF1A MUSHROOM UNREACHABLE")
        elif response == 0:  
            print ("\nMIF1A MUSHROOM ON")
        else:
            print("\nMIF1A MUSHROOM OFF")
        output = subprocess.Popen(["ping.exe",t6v3accs],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + t6v3accs)
        output = str(output)
        if('unreachable' in output):
            print("\nMIF1A ACCESSPOINT UNREACHABLE")
        elif response == 0:  
            print ("\nMIF1A ACCESSPOINT ON")
        else:
            print("\nMIF1A ACCESSPOINT OFF")
        #/------      
        output = subprocess.Popen(["ping.exe",trenaltiv4mushroom],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + trenaltiv4mushroom)
        output = str(output)
        if('unreachable' in output):
            print("\nMIF1B MUSHROOM UNREACHABLE")
        elif response == 0:  
            print ("\nMIF1B MUSHROOM ON")
        else:
            print("\nMIF1B MUSHROOM OFF")
        output = subprocess.Popen(["ping.exe",t6v4accs],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + t6v4accs)
        output = str(output)
        if('unreachable' in output):
            print("\nMIF1B ACCESSPOINT UNREACHABLE")
        elif response == 0:  
            print ("\nMIF1B ACCESSPOINT ON")
        else:
            print("\nMIF1B ACCESSPOINT OFF")               
       #//////-----------------------------------------------
        output = subprocess.Popen(["ping.exe",trenaltiv5mushroom],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + trenaltiv5mushroom)
        output = str(output)
        if('unreachable' in output):
            print("\nMIF2 MUSHROOM UNREACHABLE")
        elif response == 0:  
            print ("\nMIF2 MUSHROOM ON")
        else:
            print("\nMIF2 MUSHROOM OFF")
        output = subprocess.Popen(["ping.exe",t6v5accs],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + t6v5accs)
        output = str(output)
        if('unreachable' in output):
            print("\nMIF2 ACCESSPOINT UNREACHABLE")
        elif response == 0:  
            print ("\nMIF2 ACCESSPOINT ON")
        else:
            print("\nMIF2 ACCESSPOINT OFF")
    #//-------------------------------------------
        output = subprocess.Popen(["ping.exe",trenaltiv6mushroom],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + trenaltiv6mushroom)
        output = str(output)
        if('unreachable' in output):
            print("\nTCF MUSHROOM UNREACHABLE")
        elif response == 0:  
            print ("\nTCF MUSHROOM ON")
        else:
            print("\nTCF MUSHROOM OFF")
        output = subprocess.Popen(["ping.exe",t6v6accs],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + t6v6accs)
        output = str(output)
        if('unreachable' in output):
            print("\nTCF ACCESSPOINT UNREACHABLE")
        elif response == 0:  
            print ("\nTCF ACCESSPOINT ON")
        else:
            print("\nTCF ACCESSPOINT OFF")
    if secim == '7':   
        output = subprocess.Popen(["ping.exe",ip7],stdout = subprocess.PIPE).communicate()[0]    
        response = os.system("ping " + ip7)
        output = str(output)
        if('unreachable' in output):
                print("\n65007 UNREACHABLE")
        if response == 0:
            os.system("CLS")
            print ("\n65007 ON")
            output = subprocess.Popen(["ping.exe",trenyedimushroom],stdout = subprocess.PIPE).communicate()[0]    
            response = os.system("ping " + trenyedimushroom)
            output = str(output)
            if('unreachable' in output):
                print("\nMUSHROOM UNREACHABLE")
            elif response == 0:           
                print("\nMUSHROOM ON")
            else:
                print("\nMUSHROOM OFF")
            output = subprocess.Popen(["ping.exe",t7v1accs],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t7v1accs)
            output = str(output)
            if('unreachable' in output):
                print("\nTCB ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nTCB ACCESSPOINT ON")
            else:
                print("\nTCB ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t7v2accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t7v2accs)
            output = str(output)
            if('unreachable' in output):
                print("\nMIFC ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIFC ACCESSPOINT ON")
            else:         
                print("\nMIFC ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t7v3accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t7v3accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF1A ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF1A ACCESSPOINT ON")
            else:         
                print("\nMI1A ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t7v4accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t7v4accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF1B ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF1B ACCESSPOINT ON")
            else:         
                print("\nMI1B ACCESSPOINT OFF") 
            output = subprocess.Popen(["ping.exe",t7v5accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t7v5accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF2 ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF2 ACCESSPOINT ON")
            else:         
                print("\nMIF2 ACCESSPOINT OFF")     

            output = subprocess.Popen(["ping.exe",t7v6accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t7v6accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nTCF ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nTCF ACCESSPOINT ON")
            else:         
                print("\nTCF ACCESSPOINT OFF")            
        else:
            print ("65007 OFF")
    #//------------------------------------------------------------
    if secim == '8':   
        output = subprocess.Popen(["ping.exe",ip8],stdout = subprocess.PIPE).communicate()[0]    
        response = os.system("ping " + ip8)
        output = str(output)
        if('unreachable' in output):
                print("\n65008 UNREACHABLE")
        if response == 0:
            os.system("CLS")
            print ("\n65008 ON")
            output = subprocess.Popen(["ping.exe",trensekizmushroom],stdout = subprocess.PIPE).communicate()[0]    
            response = os.system("ping " + trensekizmushroom)
            output = str(output)
            if('unreachable' in output):
                print("\nMUSHROOM UNREACHABLE")
            elif response == 0:           
                print("\nMUSHROOM ON")
            else:
                print("\nMUSHROOM OFF")
            output = subprocess.Popen(["ping.exe",t8v1accs],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t8v1accs)
            output = str(output)
            if('unreachable' in output):
                print("\nTCB ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nTCB ACCESSPOINT ON")
            else:
                print("\nTCB ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t8v2accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t8v2accs)
            output = str(output)
            if('unreachable' in output):
                print("\nMIFC ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIFC ACCESSPOINT ON")
            else:         
                print("\nMIFC ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t8v3accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t8v3accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF1A ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF1A ACCESSPOINT ON")
            else:         
                print("\nMI1A ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t8v4accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t8v4accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF1B ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF1B ACCESSPOINT ON")
            else:         
                print("\nMI1B ACCESSPOINT OFF") 
            output = subprocess.Popen(["ping.exe",t8v5accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t8v5accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF2 ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF2 ACCESSPOINT ON")
            else:         
                print("\nMIF2 ACCESSPOINT OFF")     

            output = subprocess.Popen(["ping.exe",t8v6accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t8v6accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nTCF ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nTCF ACCESSPOINT ON")
            else:         
                print("\nTCF ACCESSPOINT OFF")                
        else:
            print ("65008 OFF")
    #//-----------------------------------------------------------
    if secim == '9':   
        output = subprocess.Popen(["ping.exe",ip9],stdout = subprocess.PIPE).communicate()[0]    
        response = os.system("ping " + ip9)
        output = str(output)
        if('unreachable' in output):
                print("\n65009 UNREACHABLE")
        if response == 0:
            os.system("CLS")
            print ("\n65009 ON")
            output = subprocess.Popen(["ping.exe",trendokuzmushroom],stdout = subprocess.PIPE).communicate()[0]    
            response = os.system("ping " + trendokuzmushroom)
            output = str(output)
            if('unreachable' in output):
                print("\nMUSHROOM UNREACHABLE")
            elif response == 0:           
                print("\nMUSHROOM ON")
            else:
                print("\nMUSHROOM OFF")
            output = subprocess.Popen(["ping.exe",t9v1accs],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t9v1accs)
            output = str(output)
            if('unreachable' in output):
                print("\nTCB ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nTCB ACCESSPOINT ON")
            else:
                print("\nTCB ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t9v2accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t9v2accs)
            output = str(output)
            if('unreachable' in output):
                print("\nMIFC ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIFC ACCESSPOINT ON")
            else:         
                print("\nMIFC ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t9v3accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t9v3accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF1A ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF1A ACCESSPOINT ON")
            else:         
                print("\nMI1A ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t9v4accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t9v4accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF1B ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF1B ACCESSPOINT ON")
            else:         
                print("\nMI1B ACCESSPOINT OFF") 
            output = subprocess.Popen(["ping.exe",t9v5accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t9v5accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF2 ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF2 ACCESSPOINT ON")
            else:         
                print("\nMIF2 ACCESSPOINT OFF")     

            output = subprocess.Popen(["ping.exe",t9v6accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t9v6accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nTCF ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nTCF ACCESSPOINT ON")
            else:         
                print("\nTCF ACCESSPOINT OFF")          
        else:
            print ("65009 OFF")
    #//---------------------------------------------------------------------------
    if secim == '10':   
        output = subprocess.Popen(["ping.exe",ip10],stdout = subprocess.PIPE).communicate()[0]    
        response = os.system("ping " + ip10)
        output = str(output)
        if('unreachable' in output):
                print("\n65010 UNREACHABLE")
        if response == 0:
            os.system("CLS")
            print ("\n65010 ON")
            output = subprocess.Popen(["ping.exe",trenonmushroom],stdout = subprocess.PIPE).communicate()[0]    
            response = os.system("ping " + trenonmushroom)
            output = str(output)
            if('unreachable' in output):
                print("\nMUSHROOM UNREACHABLE")
            elif response == 0:           
                print("\nMUSHROOM ON")
            else:
                print("\nMUSHROOM OFF")
            output = subprocess.Popen(["ping.exe",t10v1accs],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t10v1accs)
            output = str(output)
            if('unreachable' in output):
                print("\nTCB ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nTCB ACCESSPOINT ON")
            else:
                print("\nTCB ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t10v2accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t10v2accs)
            output = str(output)
            if('unreachable' in output):
                print("\nMIFC ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIFC ACCESSPOINT ON")
            else:         
                print("\nMIFC ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t10v3accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t10v3accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF1A ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF1A ACCESSPOINT ON")
            else:         
                print("\nMI1A ACCESSPOINT OFF")
            output = subprocess.Popen(["ping.exe",t10v4accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t10v4accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF1B ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF1B ACCESSPOINT ON")
            else:         
                print("\nMI1B ACCESSPOINT OFF") 
            output = subprocess.Popen(["ping.exe",t10v5accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t10v5accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nMIF2 ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nMIF2 ACCESSPOINT ON")
            else:         
                print("\nMIF2 ACCESSPOINT OFF")     

            output = subprocess.Popen(["ping.exe",t10v6accs],stdout = subprocess.PIPE).communicate()[0]                
            response = os.system("ping " + t10v6accs)
            output = str(output)   
            if('unreachable' in output):
                print("\nTCF ACCESSPOINT UNREACHABLE")
            elif response == 0:
                print("\nTCF ACCESSPOINT ON")
            else:         
                print("\nTCF ACCESSPOINT OFF")       
        else:
            print ("65010 OFF")
    #//---------------------------------------------------------
    if secim == '11':
        output = subprocess.Popen(["ping.exe",ip11],stdout = subprocess.PIPE).communicate()[0]
        response = os.system("ping " + ip11)
        output = str(output)
        if ('unreachable' in output):
            print("65011 UNREACHABLE")
        if response == 0:
            os.system("CLS")
            print ("65011 ON")
            output = subprocess.Popen(["ping.exe",trenonbirmushroom],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + trenonbirmushroom)
            output = str(output)
            if ('unreachable' in output):
                print("\nMUSHROOM UNREACHABLE")
            elif response == 0:           
                print("\nMUSHROOM ON")
            else:
                print("\nMUSHROOM OFF")
#//-------------------TEPE EKRAN--------------------------        
            output = subprocess.Popen(["ping.exe",t11tp1],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t11tp1)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCB TEPE EKRAN UNREACHABLE")
            elif response == 0:
                print("\nTCB TEPE EKRAN ON")
            else:
                print("\nTCB TEPE EKRAN OFF")
            output = subprocess.Popen(["ping.exe",t11tp2],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t11tp2)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIFC TEPE EKRAN UNREACHABLE")
            elif response == 0:
                print("\nMIFC TEPE EKRAN ON")
            else:         
                print("\nMIFC TEPE EKRAN OFF")
            output = subprocess.Popen(["ping.exe",t11tp3],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t11tp3)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1A TEPE EKRAN UNREACHABLE")
            elif response == 0:
                print("\nMIF1A TEPE EKRAN ON")
            else:         
                print("\nMI1A TEPE EKRAN OFF")
            output = subprocess.Popen(["ping.exe",t11tp4],stdout = subprocess.PIPE).communicate()[0]                 
            response = os.system("ping " + t11tp4)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1B TEPE EKRAN UNREACHABLE")
            elif response == 0:
                print("\nMIF1B TEPE EKRAN ON")
            else:         
                print("\nMIF1B TEPE EKRAN OFF")
            output = subprocess.Popen(["ping.exe",t11tp5],stdout = subprocess.PIPE).communicate()[0]                             
            response = os.system("ping " + t11tp5)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF2 TEPE EKRAN UNREACHABLE")
            elif response == 0:
                print("\nMIF2 TEPE EKRAN ON")
            else:         
                print("\nMIF2 TEPE EKRAN OFF")
            output = subprocess.Popen(["ping.exe",t11tp6],stdout = subprocess.PIPE).communicate()[0]                             
            response = os.system("ping " + t11tp6)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCF TEPE EKRAN UNREACHABLE")
            elif response == 0:
                print("\nTCF TEPE EKRAN ON")
            else:         
                print("\nTCF TEPE EKRAN OFF")
##--------------------SES ISLEMCI----------------------------------------
            output = subprocess.Popen(["ping.exe",t11ses1],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t11ses1)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCB SES ISLEMCI UNREACHABLE")
            elif response == 0:
                print("\nTCB SES ISLEMCI ON")
            else:
                print("\nTCB SES ISLEMCI OFF")
            output = subprocess.Popen(["ping.exe",t1ses2],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t11ses2)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIFC SES ISLEMCI UNREACHABLE")
            elif response == 0:
                print("\nMIFC SES ISLEMCI ON")
            else:         
                print("\nMIFC SES ISLEMCI OFF")  
            output = subprocess.Popen(["ping.exe",t11ses3],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t11ses3)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1A SES ISLEMCI UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SES ISLEMCI ON")
            else:         
                print("\nMI1A SES ISLEMCI OFF")     
            output = subprocess.Popen(["ping.exe",t11ses4],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t11ses4)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1B SES ISLEMCI UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SES ISLEMCI ON")
            else:         
                print("\nMIF1B SES ISLEMCI OFF")
            output = subprocess.Popen(["ping.exe",t11ses5],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t11ses5)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF2 SES ISLEMCI UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SES ISLEMCI ON")
            else:         
                print("\nMIF2 SES ISLEMCI OFF")
            output = subprocess.Popen(["ping.exe",t11ses6],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t11ses6)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCF SES ISLEMCI UNREACHABLE")
            elif response == 0:
                print("\nTCF SES ISLEMCI ON")
            else:         
                print("\nTCF SES ISLEMCI OFF")
#//----------------------GPS--------------------------
            t1gps1 = "192.168.49.227"
            output = subprocess.Popen(["ping.exe",t11gps1],stdout = subprocess.PIPE).communicate()[0]                                         
            unreachable = os.system("ping " + t11gps1)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCB GPS UNREACHABLE")
            elif unreachable == 0:
                    print("\nTCB GPS ON")
            else:
                print("\nTCB GPS OFF")
            output = subprocess.Popen(["ping.exe",t11gps2],stdout = subprocess.PIPE).communicate()[0]                                         
            response = os.system("ping " + t11gps2)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCF GPS UNREACHABLE")
            elif response == 0:
                print("\nTCF GPS ON")
            else:
                print("\nTCF GPS OFF")    
#//------------------LEDLER---------------------------
            output = subprocess.Popen(["ping.exe",t11tcbs1led1],stdout = subprocess.PIPE).communicate()[0]                                                     
            response = os.system("ping " + t11tcbs1led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCB SALON 1 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nTCB SALON 1 LED 1 ON")
            else:
                print("\nTCB SALON 1 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t11tcbs1led2],stdout = subprocess.PIPE).communicate()[0]                                                     
            response = os.system("ping " + t11tcbs1led2)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCB SALON 1 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nTCB SALON 1 LED 2 ON")
            else:
                print("\nTCB SALON 1 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t11tcbs2led1],stdout = subprocess.PIPE).communicate()[0]                                                     
            response = os.system("ping " + t11tcbs2led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nTCB SALON 2 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nTCB SALON 2 LED 1 ON")
            else:
                print("\nTCB SALON 2 LED 1 OFF")
            unreachable = os.system("ping " + t11tcbs2led2)
            output = subprocess.Popen(["ping.exe",t11tcbs2led2],stdout = subprocess.PIPE).communicate()[0]                                                     
            output = str(output) 
            if ('unreachable' in output):
                print("TCB SALON 2 LED 2 UNREACHABLE")
            elif unreachable == 0:
                print("\nTCB SALON 2 LED 2 ON")
            else:
                print("\nTCB SALON 2 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t11mifcs1led1],stdout = subprocess.PIPE).communicate()[0]                                                                 
            response = os.system("ping " + t11mifcs1led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIFC SALON 1 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIFC SALON 1 LED 1 ON")
            else:
                print("\nMIFC SALON 1 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t11mifcs2led1],stdout = subprocess.PIPE).communicate()[0]                                                                 
            response = os.system("ping " + t11mifcs2led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIFC SALON 2 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIFC SALON 2 LED 1 ON")
            else:
                print("\nMIFC SALON 2 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t11mifcs2led2],stdout = subprocess.PIPE).communicate()[0]                                                                 
            response = os.system("ping " + t11mifcs2led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIFC SALON 2 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nMIFC SALON 2 LED 2 ON")
            else:
                print("\nMIFC SALON 2 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t11mif1as1led1],stdout = subprocess.PIPE).communicate()[0]                                                                             
            response = os.system("ping " + t11mif1as1led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1A SALON 1 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SALON 1 LED 1 ON")
            else:
                print("\nMIF1A SALON 1 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t11mif1as1led2],stdout = subprocess.PIPE).communicate()[0]                                                                                          
            response = os.system("ping " + t11mif1as1led2)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1A SALON 1 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SALON 1 LED 2 ON")
            else:
                print("\nMIF1A SALON 1 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t11mif1as2led1],stdout = subprocess.PIPE).communicate()[0]                                                                                         
            response = os.system("ping " + t11mif1as2led1),
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF1A SALON 2 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SALON 2 LED 1 ON")
            else:
                print("\nMIF1A SALON 2 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t11mif1as2led2],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t11mif1as2led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF1A SALON 2 LED 2 UNREACHABLE")                                                                                                      
            elif response == 0:
                print("\nMIF1A SALON 2 LED 2 ON")
            else:
                print("\nMIF1A SALON 2 LED 2 OFF")
#/-----------------------------------------------------------
            output = subprocess.Popen(["ping.exe",t11mif1bs1led1],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t11mif1bs1led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1B SALON 1 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SALON 1 LED 1 ON") 
            else:
                print("\nMIF1B SALON 1 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t11mif1bs1led2],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t11mif1bs1led2)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF1B SALON 1 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SALON 1 LED 2 ON")
            else:
                print("\nMIF1B SALON 1 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t11mif1bs2led1],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t11mif1bs2led1)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF1B SALON 2 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SALON 2 LED 1 ON")
            else:
                print("\nMIF1B SALON 2 LED 1 OFF") 
            output = subprocess.Popen(["ping.exe",t11mif1bs2led2],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t11mif1bs2led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF1B SALON 2 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SALON 2 LED 2 ON")
            else:
                print("\nMIF1B SALON 2 LED 2 OFF")
#//---------------------------------------------------------------
            output = subprocess.Popen(["ping.exe",t11mif2s1led1],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t11mif2s1led1)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF2 SALON 1 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SALON 1 LED 1 ON")
            else:
                print("\nMIF2 SALON 1 LED 1 OFF") 
            output = subprocess.Popen(["ping.exe",t11mif2s1led2],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t11mif2s1led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF2 SALON 1 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SALON 1 LED 2 ON")
            else:
                print("\nMIF2 SALON 1 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t11mif2s2led1],stdout = subprocess.PIPE).communicate()[0]            
            response = os.system("ping " + t11mif2s2led1)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF2 SALON 2 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SALON 2 LED 1 ON")
            else:
                print("\nMIF2 SALON 2 LED 1 OFF") 
            output = subprocess.Popen(["ping.exe",t11mif2s2led2],stdout = subprocess.PIPE).communicate()[0]                        
            response = os.system("ping " + t11mif2s2led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF2 SALON 2 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SALON 2 LED 2 ON")
            else:
                print("\nMIF2 SALON 2 LED 2 OFF")
#//-----------------------------------------------------------
            output = subprocess.Popen(["ping.exe",t11tcfs1led1],stdout = subprocess.PIPE).communicate()[0]                        
            response = os.system("ping " + t11tcfs1led1)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCF SALON 1 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nTCF SALON 1 LED 1 ON")
            else:
                print("\nTCF SALON 1 LED 1 OFF")
            output = subprocess.Popen(["ping.exe",t11tcfs1led2],stdout = subprocess.PIPE).communicate()[0]                        
            response = os.system("ping " + t11tcfs1led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCF SALON 1 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nTCF SALON 1 LED 2 ON")
            else:
                print("\nTCF SALON 1 LED 2 OFF")
            output = subprocess.Popen(["ping.exe",t11tcfs2led1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11tcfs2led1)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCF SALON 2 LED 1 UNREACHABLE")
            elif response == 0:
                print("\nTCF SALON 2 LED 1 ON")
            else:
                print("\nTCF SALON 2 LED 1 OFF") 
            output = subprocess.Popen(["ping.exe",t11tcfs2led2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11tcfs2led2)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCF SALON 2 LED 2 UNREACHABLE")
            elif response == 0:
                print("\nTCF SALON 2 LED 2 ON")
            else:
                print("\nTCF SALON 2 LED 2 OFF")                          
#//--------------------------------------------------------
            output = subprocess.Popen(["ping.exe",t11mif1asoldisled],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11mif1asoldisled)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF1A SOL DIS LED UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SOL DIS LED ON")
            else:
                print("\nMIF1A SOL DIS LED OFF")
            output = subprocess.Popen(["ping.exe",t11mif1bsoldisled],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11mif1bsoldisled)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF1B SOL DIS LED UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SOL DIS LED ON")
            else:
                print("\nMIF1B SOL DIS LED OFF")
            output = subprocess.Popen(["ping.exe",t11mif2soldisled],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11mif2soldisled)
            output = str(output) 
            if ('unreachable' in output):
                print("\nMIF2 SOL DIS LED UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SOL DIS LED ON")
            else:
                print("\nMIF2 SOL DIS LED OFF")
            output = subprocess.Popen(["ping.exe",t11mif2sagdisled],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11mif2sagdisled)
            output = str(output)
            if ('unreachable' in output):
                print("\nMIF2 SAG DIS LED UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SAĞ DIS LED ON")
            else:
                print("\nMIF2 SAĞ DIS LED OFF")
            output = subprocess.Popen(["ping.exe",t11tcfsoldisled],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11tcfsoldisled)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCF SOL DIS LED UNREACHABLE")
            elif response == 0:
                print("\nTCF SOL DIŞ LED ON")
            else:
                print("\nTCF SOL DIŞ LED OFF")
            output = subprocess.Popen(["ping.exe",t11tcfsagdisled],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11tcfsagdisled)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCF SAG DIS LED UNREACHABLE")
            elif response == 0:
                print("\nTCF SAG DIŞ LED ON")
            else:
                print("\nTCF SAĞ DIŞ LED OFF")
#/------------------------KAMERALAR-----------------------------
            output = subprocess.Popen(["ping.exe",t11tcbsoldis],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11tcbsoldis)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCB SOL DIS KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCB SOL DIS KAMERA ON")
            else:
                print("\nTCB SOL DIŞ KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t11tcbd1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11tcbd1)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCB ÖN KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCB ÖN KAMERA ON")
            else:
                print("\nTCB ÖN KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t11tcbsagdis],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11tcbsagdis)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCB SAG KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCB SAG DIS KAMERA ON")
            else:
                print("\nTCB SAS DIS KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t11tcbmakinist],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11tcbmakinist)
            output = str(output) 
            if ('unreachable' in output):
                print("\nTCB MAKİNİST KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCB MAKİNİST KAMERA ON")
            else:
                print("\nTCB MAKİNİST KAMERA OFF") 
            output = subprocess.Popen(["ping.exe",t11tcbs1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11tcbs1)
            output = str(output) 
            if('unreachable' in output):
                print("\nTCB SALON 1 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCB SALON 1 KAMERA ON")
            else:
                print("\nTCB SALON 1 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t11tcbs2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11tcbs2)
            output = str(output)
            if('unreachable' in output):
                print("\nTCB SALON 2 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCB SALON 2 KAMERA ON")
            else:
                print("\nTCB SALON 2 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t11mifcs1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11mifcs1)
            output = str(output)
            if('unreachable' in output):
                print("\nMIFC SALON 1 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIFC SALON 1 KAMERA ON")
            else:
                print("\nMIFC SALON 1 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t11mifcs2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11mifcs2)
            output = str(output)
            if('unreachable' in output):
                print("\nMIFC SALON 2 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIFC SALON 2 KAMERA ON")
            else:
                print("\nMIFC SALON 2 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t11mif1as1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11mif1as1)
            output = str(output)
            if('unreachable' in output):
                print("\nMIF1A SALON 1 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SALON 1 KAMERA ON")
            else:
                print("\nMIF1A SALON 1 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t11mif1as2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11mif1as2)
            output = str(output)
            if('unreachable' in output):
                print("\nMIF1A SALON 2 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIF1A SALON 2 KAMERA ON")
            else:
                print("\nMIF1A SALON 2 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t11mif1bs1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11mif1bs1)
            output = str(output)
            if('unreachable' in output):
                print("\nMIF1B SALON 1 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SALON 1 KAMERA ON")
            else:
                print("\nMIF1B SALON 1 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t11mif1bs2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11mif1bs2)
            output = str(output)
            if('unreachable' in output):
                print("\nMIF1B SALON 2 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIF1B SALON 2 KAMERA ON")
            else:
                print("\nMIF1B SALON 2 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t11mif2s1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11mif2s1)
            output = str(output)
            if('unreachable' in output):
                print("\nMIF2 SALON 1 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SALON 1 KAMERA ON")
            else:
                print("\nMIF2 SALON 1 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t11mif2s2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11mif2s2)
            output = str(output)
            if('unreachable' in output):
                print("\nMIF2 SALON 2 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nMIF2 SALON 2 KAMERA ON")
            else:
                print("\nMIF2 SALON 2 KAMERA OFF")
            #//------------------------------------------------
            output = subprocess.Popen(["ping.exe",t11tcfs1],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t1tcfs1)
            output = str(output)
            if('unreachable' in output):
                print("\nTCF SALON 1 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCF SALON 1 KAMERA ON")
            else:
                print("\nTCF SALON 1 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t11tcfs2],stdout = subprocess.PIPE).communicate()[0]                                       
            response = os.system("ping " + t11tcfs2)
            output = str(output)
            if('unreachable' in output):
                print("\nTCF SALON 2 KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCF SALON 2 KAMERA ON")
            else:
                print("\nTCF SALON 2 KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t11tcfmakinist],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t11tcfmakinist)
            output = str(output)
            if('unreachable' in output):
                print("\nTCF MAKİNİST KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCF MAKİNİST KAMERA ON")
            else:
                print("\nTCF MAKİNİST KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t11tcfsoldis],stdout = subprocess.PIPE).communicate()[0]
            response = os.system("ping " + t11tcfsoldis)
            output = str(output)
            if('unreachable' in output):
                print("\nTCF SOL DIŞ KAMERA UNREACHABLE")
            elif response ==  0:
                print("\nTCF SOL DIŞ KAMERA ON")
            else:
                print("\nTCF SOL DIŞ KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t11tcfsagdis],stdout = subprocess.PIPE).communicate()[0]    
            response = os.system("ping " + t11tcfsagdis)
            output = str(output)
            if('unreachable' in output):
                print("\nTCF SAĞ DIŞ KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCF SAĞ DIŞ KAMERA ON")
            else:
                print("\nTCF SAĞ DIŞ KAMERA OFF")
            output = subprocess.Popen(["ping.exe",t11tcfd1],stdout = subprocess.PIPE).communicate()[0]    
            response = os.system("ping " + t11tcfd1)
            output = str(output)
            if('unreachable' in output):
                print("\nTCF ÖN KAMERA UNREACHABLE")
            elif response == 0:
                print("\nTCF ÖN KAMERA ON")
            else:
                print("\nTCF ÖN DIŞ KAMERA OFF")         
        else:
            print ("65011 OFF")
    #*//*----------------------------------------------------------------------
    if secim == '12':   
        output = subprocess.Popen(["ping.exe",trenonikiv1mushroom],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + trenonikiv1mushroom)
        output = str(output)
        if('unreachable' in output):
            print("\n65012 TCB MUSHROOM UNREACHABLE")
        elif response == 0:  
            print ("\n65012 TCB MUSHROOM ON")
        else:
            print("\n65012 TCB MUSHROOM OFF")
        output = subprocess.Popen(["ping.exe",t12v1accs],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + t12v1accs)
        output = str(output)
        if('unreachable' in output):
            print("\n65012 TCB ACCESSPOINT UNREACHABLE")
        elif response == 0:  
            print ("\n65012 TCB ACCESSPOINT ON")
        else:
            print("\n65012 TCB ACCESSPOINT OFF")         
        output = subprocess.Popen(["ping.exe",trenonikiv2mushroom],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + trenonikiv2mushroom)
        output = str(output)
        if('unreachable' in output):
            print("\n65012 MIFC MUSHROOM UNREACHABLE")
        elif response == 0:  
            print ("\n65012 MIFC MUSHROOM ON")
        else:
            print("\n65012 MIFC MUSHROOM OFF")
        output = subprocess.Popen(["ping.exe",t12v2accs],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + t12v2accs)
        output = str(output)
        if('unreachable' in output):
            print("\n65012 MIFC ACCESSPOINT UNREACHABLE")
        elif response == 0:  
            print ("\n65012 MIFC ACCESSPOINT ON")
        else:
            print("\n65012 MIFC ACCESSPOINT OFF")
        output = subprocess.Popen(["ping.exe",trenonikiv3mushroom],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + trenonikiv3mushroom)
        output = str(output)
        if('unreachable' in output):
            print("\n65012 MIF1A MUSHROOM UNREACHABLE")
        elif response == 0:  
            print ("\n65012 MIF1A MUSHROOM ON")
        else:
            print("\n65012 MIF1A MUSHROOM OFF")
        output = subprocess.Popen(["ping.exe",t12v3accs],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + t12v3accs)
        output = str(output)
        if('unreachable' in output):
            print("\n65012 MIF1A ACCESSPOINT UNREACHABLE")
        elif response == 0:  
            print ("\n65012 MIF1A ACCESSPOINT ON")
        else:
            print("\n65012 MIF1A ACCESSPOINT OFF")
        #/------      
        output = subprocess.Popen(["ping.exe",trenonikiv4mushroom],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + trenonikiv4mushroom)
        output = str(output)
        if('unreachable' in output):
            print("\n65012 MIF1B MUSHROOM UNREACHABLE")
        elif response == 0:  
            print ("\n65012 MIF1B MUSHROOM ON")
        else:
            print("\n65012 MIF1B MUSHROOM OFF")
        output = subprocess.Popen(["ping.exe",t12v4accs],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + t12v4accs)
        output = str(output)
        if('unreachable' in output):
            print("\n65012 MIF1B ACCESSPOINT UNREACHABLE")
        elif response == 0:  
            print ("\n65012 MIF1B ACCESSPOINT ON")
        else:
            print("\n65012 MIF1B ACCESSPOINT OFF")               
       #//////-----------------------------------------------
        output = subprocess.Popen(["ping.exe",trenonikiv5mushroom],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + trenonikiv5mushroom)
        output = str(output)
        if('unreachable' in output):
            print("\n65012 MIF2 MUSHROOM UNREACHABLE")
        elif response == 0:  
            print ("\n65012 MIF2 MUSHROOM ON")
        else:
            print("\n65012 MIF2 MUSHROOM OFF")
        output = subprocess.Popen(["ping.exe",t12v5accs],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + t12v5accs)
        output = str(output)
        if('unreachable' in output):
            print("\n65012 MIF2 ACCESSPOINT UNREACHABLE")
        elif response == 0:  
            print ("\n65012 MIF2 ACCESSPOINT ON")
        else:
            print("\n65012 MIF2 ACCESSPOINT OFF")
    #//-------------------------------------------
        output = subprocess.Popen(["ping.exe",trenonikiv6mushroom],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + trenonikiv6mushroom)
        output = str(output)
        if('unreachable' in output):
            print("\n65012 TCF MUSHROOM UNREACHABLE")
        elif response == 0:  
            print ("\n65012 TCF MUSHROOM ON")
        else:
            print("\n65012 TCF MUSHROOM OFF")
        output = subprocess.Popen(["ping.exe",t12v6accs],stdout = subprocess.PIPE).communicate()[0]   
        response = os.system("ping " + t12v6accs)
        output = str(output)
        if('unreachable' in output):
            print("\nTCF ACCESSPOINT UNREACHABLE")
        elif response == 0:  
            print ("\nTCF ACCESSPOINT ON")
        else:
            print("\nTCF ACCESSPOINT OFF")
    else:
        break