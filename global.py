
      
import folium
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv("D:\\electrique.csv" ,encoding = "cp1252")
#print(data)
name=list(data["name"])
v=list(data["v"])
h=list(data["h"])
max_consomation=list(data["max_con"])
p=list(data["priority"])
som= sum(max_consomation)
print(som)
pp = p.copy()
#*********************************************************
'''for ss, s in enumerate(pp):
    if s==1:        
        pp[ss] = 'green'
    if s==2:
        pp[ss] = 'red'
    if s==3:
        pp[ss] = 'blue'
#print(p)
#print(pp)
map=folium.Map(location=[36.204692, 1.260199],zoom_start=10)
fgg=folium.FeatureGroup(name="my map")

for v,h,nm,mc,z in zip(v,h,name,max_consomation,pp):
    fgg.add_child(folium.Marker(location=[v,h],popup="<b>name  : </b>"+" poste " +str(nm)+"<br> <b>max_consomation : </b> "+str(mc)+" KW" ,icon=folium.Icon(color=z)))
    
map.add_child(fgg)
map.save("befor.html")'''
#*********************************************************
a=pd.DataFrame({'priority' : p, 'max_con' : max_consomation,'name':name,'v':v,'h':h}) 
print(a.sort_values(["priority"],ascending=True))
#-------------------------------------------------

#--------------------------------------------------
b=a.loc[a.priority==1]
dt=[i for i in range (len(b+1))]
b.sort_values("max_con", inplace = True)
b['i'] = dt
print(b)
bb = b['max_con'].tolist() 

c=a.loc[a.priority==2]
dt=[j for j in range (len(c+1))]
c.sort_values("max_con", inplace = True)
c['j'] = dt
print(c)
cc = c['max_con'].tolist() 

d=a.loc[a.priority==3]
dt=[k for k in range (len(d+1))]
d.sort_values("max_con", inplace = True)
d['k'] = dt
print(d)
dd = d['max_con'].tolist() 
#-------------------------------------------------
while True:
    try :
        n= input("give me total \n S =")
        n= int(n)
        break
    except:
        print("wrong format")
    finally :
        print("ok")
   
dif=som-n
print('diffrent is ',dif,'W')
if (dif==0)or(dif<0):
     print('every thing is ok')
else:
    print("we have some problem you should to turn on just those post")  
#------------------------------------------------
total=0
#******************************************************
list3=[]
for i in range (len(bb)):
    if total < n:
        total = total + bb[i]
        list3.append(i)
print('premier list des posts ',list3)
mini_table1=b.loc[b.i<len(list3)]
#print(mini_table1)
max_cons=list(mini_table1['max_con'])
#print(max_cons)
vv=list(mini_table1['v'])
#print(vv)
hh=list(mini_table1['h'])
#print(hh)
names=list(mini_table1['name'])
#print(names)

map=folium.Map(location=[36.204692, 1.260199],zoom_start=11)
fg=folium.FeatureGroup(name="mymap")

for vv,hh,nmm,mcc in zip(vv,hh,names,max_cons):
    fg.add_child(folium.Marker(location=[vv,hh],popup="<b>name  : </b>"+" poste " +str(nmm)+"<br> <b>max_consomation : </b> "+str(mcc)+" KW" ,icon=folium.Icon(color='pink')))
    
map.add_child(fg)


#********************************************************************
list4=[]
for j in range (len(cc)):
    if total < n:
        list4.append(j)
        total = total + cc[j] 
print('deuxiem list des posts' ,list4)
mini_table2=c.loc[c.j<len(list4)]
#print(mini_table2)
max_cons=list(mini_table2['max_con'])
#print(max_cons)
vv=list(mini_table2['v'])
#print(vv)
hh=list(mini_table2['h'])
#print(hh)
names=list(mini_table2['name'])
#print(names)

for v,h,nm,mc in zip(vv,hh,names,max_cons):
    fg.add_child(folium.Marker(location=[v,h],popup="<b>name  : </b>"+" poste " +str(nm)+"<br> <b>max_consomation : </b> "+str(mc)+" KW" ,icon=folium.Icon(color='purple')))
    
map.add_child(fg)


#*******************************************************************



list5=[]
for k in range (len(dd)):
    if total < n:
        list5.append(k)
        total = total + dd[k] 
print('troixiem list' ,list5)
mini_table3=d.loc[d.k<len(list5)]
#print(mini_table3)
max_cons=list(mini_table3['max_con'])
#print(max_cons)
vv=list(mini_table3['v'])
#print(vv)
hh=list(mini_table3['h'])
#print(hh)
names=list(mini_table3['name'])
#print(names)
for v,h,nm,mc in zip(vv,hh,names,max_cons):
    fg.add_child(folium.Marker(location=[v,h],popup="<b>name  : </b>"+" poste " +str(nm)+"<br> <b>max_consomation : </b> "+str(mc)+" KW" ,icon=folium.Icon(color='orange')))
    
map.add_child(fg)
map.save("after.html")


print('total consomation for this post is ',total,'W')



