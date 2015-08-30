#!/usr/bin/python

from snack import *

def askForm(uWinText,askText,uForm):
  screen=SnackScreen()
  try:
    ret = EntryWindow(screen, uWinText, askText, uForm, allowCancel = 0, width = 40, entryWidth = 20, buttons = [ 'Ok' ], help = None)
  except:
    print 'poh'
  screen.finish()
  return(ret)

def errorWindow(userMessage):
  screen=SnackScreen()
  ret = ButtonChoiceWindow(screen, 'Error', userMessage, buttons = [ 'Ok' ]);
  screen.finish()

def writeEthFile(path,uIpAddr,uNetMask,uGW,uDNS):
  if uIpAddr=='DHCP':
    proto='dhcp'
  else:
    proto='static'
  str2file='\
  DEVICE=eth0\n\
  TYPE=Ethernet\n\
  ONBOOT=yes\n\
  NM_CONTROLLED=yes\n\
  DEFROUTE=yes\n\
  PEERDNS=yes\n\
  PEERROUTES=yes\n\
  IPV4_FAILURE_FATAL=yes\n\
  IPV6INIT=no\n\
  NAME="System eth0"\n\
  BOOTPROTO='+proto+'\n\
  DNS1='+uDNS[0]+'\n\
  DNS2='+uDNS[1]+'\n ';
  if uIpAddr != 'DHCP':
    str2file=str2file+'\
    IPADDR='+uIpAddr+'\n\
    NETMASK='+uNetMask+'\n\
    GATEWAY='+uGW+'\n '
  writeFile(path,str2file)

def writeFile(uFile,uStr):
  fHandle=open(uFile,'w')
  fHandle.write(uStr);
  fHandle.close;

def askUser():
  goodData=False
  username=""
  while goodData==False:
    goodData=True;
    uMessage=None; 
    status,values=askForm('User settings','Please enter desired system user and password',[('Username',username), 'password', 'password again']);
    if username=='exit':
      quit();
    username,passwd1,passwd2=values;
    if len(username)<5:
      goodData=False;
      uMessage='The user name must contain 5 or more characters';
      if len(username)==0:
        uMessage='Error! You must enter username!';
    else:
      if len(passwd1)<6:
        goodData=False
        uMessage='The password must be 6 or more characters';
      else:
        if passwd1!=passwd2:
          goodData=False;
          uMessage='The passwords do not match'
    if uMessage!=None: 
      errorWindow(uMessage);

  print username,passwd1
  writeFile('/tmp/username',username+':'+passwd1+':'+passwd2)

def askNetwork():
  def checkIp(tup):
    key,uIP=tup
    dig=uIP.split('.')
    if len(dig) == 4:
      for digits in dig:
        if digits.isdigit() == True:
          if int(digits)<0  or int(digits)>255:
            return(key+' is entred incorrectly');
        else:  
          return(key+' is entered incorrectly.\nNecessary to enter only numbers');
    else:
      return(key+' is entred incorrectly');
    return('ok')

  goodData=False
  ipAddr='DHCP';
  netMask='255.255.255.0'
  uGW=''
  dnses=('8.8.8.8','8.8.4.4')

  while goodData==False:
    iStatus=None;
    goodData=True;
    status,values=askForm('Network settings','Please enter network settings',[('IP address',ipAddr), ('Netmask',netMask), ('Gateway',uGW), ('First DNS',dnses[0]),('Second DNS',dnses[1])]);
    if ipAddr=='exit':
      quit();
    ipAddr,netMask,uGW,dns1,dns2=values;
    dnses=(dns1,dns2)
    if ipAddr!='DHCP':
      if len(ipAddr)!=0:
        addresses=(['IP address',ipAddr],['Netmask',netMask],['Gateway',uGW])
        for key,address in addresses:
          if len(address) != 0:
            iStatus=checkIp([key,address])
            if iStatus != 'ok':
              errorWindow(iStatus);
              goodData=False
              break;
          else:
            errorWindow('You must enter '+key)
            goodData=False
            break;
      else:
        errorWindow('You must enter IP address or "DHCP"')
        goodData=False
        break;
    index=0;
    for dns in dnses:
      if len(dns) != 0:
        iStatus=checkIp(['DNS',dns])
        if iStatus != 'ok':
          errorWindow(iStatus);
          goodData=False
          break;
      index=index+1    
    if goodData == True:
      writeEthFile('/tmp/ifcfg-eth0',ipAddr,netMask,uGW,[dnses[0],dnses[1]])

askUser();
askNetwork(); 


