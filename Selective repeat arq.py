import time
import random
print(&quot;Enter the number of frames to send&quot;)
k=int(input())
print(&quot;Enter the number of frames per window&quot;)
n=int(input())
print(&quot;1.Perfect\n2.Not recieved\n3.Time out&quot;)
l=int(input())
def transmit(frame
global l
k=int(random.random()*10)
if(k&gt;=8 and l==2):
return &quot;Not recieved&quot;
elif(k&gt;=8 and l==3):
time.sleep(5)
else:
return &quot;Recieved&quot;
tosend=[x%(2**n) for x in range(k)]
Start=0
End=n
j=0
resend=[]
print(tosend)
flag=1
while(End&lt;=len(tosend) or len(tosend1)!=0):
flag=0
while(Start&lt;len(tosend)):
print(&quot; Sending frame &quot;,tosend[Start])
t=time.time()
start=int(time.time()-t)
ack=transmit(tosend[Start]) #
end=int(time.time()-t)
if(end&gt;3):
print(&quot; Timeout error&quot;)
resend.append(tosend[Start])
flag=1
elif ack==&quot;Not recieved&quot;:
print(&quot; N-ack &quot;,tosend[Start])
resend.append(tosend[Start])
flag=1
else:
if len(resend)==0:
print(&quot; ack &quot;,(tosend[Start]+1)%(2**n))
Start=Start+1
End=End+1

if flag==1:
break
j=Start+1
while j&lt;End and j&lt;len(tosend) and len(resend)!=0:
print(&quot; Sending frame &quot;,tosend[j])
t=time.time()
start=int(time.time()-t)
ack=transmit(tosend[start])
end=int(time.time()-t)
if(end&gt;3):
print(&quot; Timeout error&quot;)
resend.append(tosend[j])
flag=1
elif ack==&quot;Not recieved&quot;:
print(&quot; N-ack &quot;,tosend[j])
resend.append(tosend[j])
flag=1
else:
print(&quot; N-ack&quot; ,resend[-1])
j=j+1

i=0

while len(resend)!=0:
print(&quot; Sending frame &quot;,resend[0])
if len(resend)&gt;1:
del(resend[i])
print(&quot; N-ack&quot;,resend[0])
else:
k=End
if(End&gt;=len(tosend)):
k=-1
print(&quot; ack &quot;,(tosend[k])%(2**n))
del(resend[i])
tosend1=tosend[End:End+n]
Start=End
End=End+n
flag=1
