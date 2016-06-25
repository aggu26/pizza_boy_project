import sys
import time
import os
from math import sin,cos,sqrt,atan2,radians,pow
global choice,logs,f_read_counter;
f_read_counter=0;
int(f_read_counter);
date_list=[];
date_lat_list=[];
date_lat_list=[];
s="";
dd="";
mm="";
yy="";
date="";
dist=0.0;
distance=0.0;
lat1=0.0;lat2=0.0;long1=0.0;long2=0.0;
v_counter=0;
date_is_der_counter=0;
fl_temp=[];
fl=[];
fl_sub=[];
lat_list=[];
lon_list=[];
'''**********************************************************************************'''
def processing(n,m):
    for i in range(0,m):
        if i%10==0:
            print('.',end='');
            time.sleep(n);
'''**********************************************************************************'''
def back_to_main():
    print("\nGoing Back To Main Menu",end='');
    processing(0.25,50);
'''**********************************************************************************'''
def print_report(distace):
    pass;
'''**********************************************************************************'''
def file_read(str1):
    global fl_temp,fl_sub;
    fl_sub=[];
    logs=os.getcwd();
    f_read_counter=0;
    logs+='\\logs\\';
    try:
        fle=open(logs+str1+".txt","r");
        print("Opening File",end='');
        processing(0.25,50);
        print("\nFile Opened");
        print("Processing File",end='');
        pos=fle.tell();
        fle.seek(pos+29);
        data=fle.read();
        fl=data.split();
        for obs in fl:
            fl_temp.append(obs);
            if len(fl_temp)==4:
                date_list=list(fl_temp[0]);
                date_list[0:2]=[''.join(date_list[0:2])]
                date_list[2:4]=[''.join(date_list[2:4])]
                date_list[4:]=[''.join(date_list[4:])]
                for obs2 in date_list:
                    if obs2=='/':
                        date_list.remove('/');
                    else:
                        pass;
                for i in range(len(date_list)):
                    fl_temp.insert(i,date_list[i])
                del fl_temp[3];
                fl_sub.append(fl_temp);
                fl_temp=[];
        processing(0.25,100);
        print("\nFile Processed");
        f_read_counter+=1;
    except IOError as ioarg:
        print(ioarg);
        f_read_counter+=1;
        back_to_main();
        main();
'''**********************************************************************************'''
def file_read1(str1):
    global fl_temp,fl_sub;
    fl_sub=[];
    logs=os.getcwd();
    f_read_counter=0;
    logs+='\\logs\\';
    try:
        fle=open(logs+str1+".txt","r");
        print("Opening File",end='');
        processing(0.25,50);
        print("\nFile Opened");
        print("Processing File",end='');
        pos=fle.tell();
        fle.seek(pos+29);
        data=fle.read();
        fl=data.split();
        for obs in fl:
            fl_temp.append(obs);
            if len(fl_temp)==4:
                fl_sub.append(fl_temp);
                fl_temp=[];
        processing(0.25,100);
        print("\nFile Processed");
        f_read_counter=0;
    except IOError as ioarg:
        print(ioarg);
        f_read_counter+=1;
        back_to_main();
        main();
'''**********************************************************************************'''
def report_gen():
    try:
        global lat_list,lon_list,v_counter,date_is_der_counter,year,date_sep;
        global dist,distance,lat1,lat2,long1,long2,s,dd,mm,yy,date,date_lat_list,date_lat_list;
        date_list=[];
        date_sep=[];
        print("\n********Allowance Calculation********\n");
        print("\n\t1. Monthly Report");
        print("\n\t2. Yearly Report");
        print("\n\t3. Any Key TO Exit");
        choice=input("\nEnter Your Choice:");
        if choice=='1':
            file_name_ac=input("\nEnter the name of the file:");
            file_read1(file_name_ac);
            if f_read_counter<=0:
                month=input("\nEnter the Month say (JAN-01,FEB-02..):");
                year=input("\nEnter the Year of the Month say(2016-16):");
                year1="20"+year;
                if(month!="" and year!=""):
                    if month=="1" or month=="3" or month=="5" or month=="7" or month=="8" or month=="10" or month=="12" or month=="01" or month=="03" or month=="05" or month=="07" or month=="08":
                        for i in range(1,32):
                            if len(month)==1:
                                if len(str(i))==1:
                                    date_list.append(str("0"+str(i)+"/"+"0"+month+"/"+year));
                                else:   
                                    date_list.append(str(str(i)+"/"+"0"+month+"/"+year));
                            else:
                                if len(str(i))==1:
                                    date_list.append(str("0"+str(i)+"/"+month+"/"+year));
                                else:
                                    date_list.append(str(str(i)+"/"+month+"/"+year));
                    elif month=='2' or month=='02':
                        if int(year1)%4==0:
                            if int(year1)%100==0:
                                if int(year1)%400==0:
                                    count=1;
                                else:
                                    count=0;
                            else:
                                count=1;
                        else:
                            count=0;
                        if count==0:
                            for j in range(1,29):
                                if len(month)==1:
                                    if len(str(j))==1:
                                        date_list.append(str("0"+str(j)+"/"+"0"+month+"/"+year));
                                    else:   
                                        date_list.append(str(str(j)+"/"+"0"+month+"/"+year));
                                else:
                                    if len(str(j))==1:
                                        date_list.append(str("0"+str(j)+"/"+month+"/"+year));
                                    else:   
                                        date_list.append(str(str(j)+"/"+month+"/"+year));
                                    
                        else:            
                            for j in range(1,30):
                                if len(month)==1:
                                    if len(str(j))==1:
                                        date_list.append(str("0"+str(j)+"/"+"0"+month+"/"+year));
                                    else:   
                                        date_list.append(str(str(j)+"/"+"0"+month+"/"+year));
                                else:
                                    if len(str(j))==1:
                                        date_list.append(str("0"+str(j)+"/"+month+"/"+year));
                                    else:   
                                        date_list.append(str(str(j)+"/"+month+"/"+year));
                    else:
                        for j in range(1,31):
                            if len(month)==1:
                                if len(str(j))==1:
                                    date_list.append(str("0"+str(j)+"/"+"0"+month+"/"+year));
                                else:   
                                    date_list.append(str(str(j)+"/"+"0"+month+"/"+year));
                            else:
                                if len(str(j))==1:
                                    date_list.append(str("0"+str(j)+"/"+month+"/"+year));
                                else:
                                    date_list.append(str(str(j)+"/"+month+"/"+year));

                    for dates in date_list:
                        for obs in fl_sub:
                            if obs[0]==dates:
                                lat_list.append(obs[2]);
                                lon_list.append(obs[3]);
                        lat_list_len=len(lat_list);
                        lon_list_len=len(lon_list);
                        if lat_list_len==lon_list_len:
                            for i in range(len(lat_list)):
                                a=i+1;
                                if a<len(lat_list):
                                    latt1=float(lat_list[i]);
                                    latt2=float(lat_list[i+1]);
                                    long1=float(lon_list[i]);
                                    long2=float(lon_list[i+1]);
                                    r=6373.0;
                                    lat1=radians(latt1);
                                    lon1=radians(long1);
                                    lat2=radians(latt2);
                                    lon2=radians(long2);
                                    dlon=lon2-lon1;
                                    dlat=lat2-lat1;
                                    a = pow(sin(dlat/2),2) + (cos(lat1) * cos(lat2)) * ((pow(sin(dlon / 2),2)));
                                    c = 2 * atan2(sqrt(a), sqrt(1 - a));
                                    d=r*c;
                                    dist+=d;
                                else:
                                    pass;
                            lat_list=[];
                            lon_list=[];
                            print(dates,"\t",dist);
                            dist=0.0;
                        else:
                            print("\nThe Data Available is in correct!!");
                    
        elif choice=='2':
            file_name_ac=input("\nEnter the name of the file:");
            file_read1(file_name_ac);
            if f_read_counter<=0:
                year=input("\nEnter the Year say(2016-16):");
                year1="20"+year;
                if(year!=""):
                    for i in range(1,13):
                        if i==2:
                            if int(year1)%4==0:
                                if int(year1)%100==0:
                                    if int(year1)%400==0:
                                        count=1;
                                    else:
                                        count=0;
                                else:
                                    count=1;
                            else:
                                count=0;
                            if count==0:
                                for j in range(1,29):
                                    if len(str(j))==1:
                                        date_list.append(str("0"+str(j)+"/"+"0"+str(i)+"/"+year));
                                    else:   
                                        date_list.append(str(str(j)+"/"+"0"+str(i)+"/"+year));
                            else:            
                                for j in range(1,30):
                                    if len(str(j))==1:
                                        date_list.append(str("0"+str(j)+"/"+"0"+str(i)+"/"+year));
                                    else:   
                                        date_list.append(str(str(j)+"/"+"0"+str(i)+"/"+year));
                        elif i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
                            for j in range(1,32):
                                if len(str(i))==1:
                                    if len(str(j))==1:
                                        date_list.append(str("0"+str(j)+"/"+"0"+str(i)+"/"+year));
                                    else:   
                                        date_list.append(str(str(j)+"/"+"0"+str(i)+"/"+year));
                                else:
                                    if len(str(j))==1:
                                        date_list.append(str("0"+str(j)+"/"+str(i)+"/"+year));
                                    else:
                                        date_list.append(str(str(j)+"/"+str(i)+"/"+year));           
                        else:
                            for j in range(1,31):
                                if len(str(i))==1:
                                    if len(str(j))==1:
                                        date_list.append(str("0"+str(j)+"/"+"0"+str(i)+"/"+year));
                                    else:   
                                        date_list.append(str(str(j)+"/"+"0"+str(i)+"/"+year));
                                else:
                                    if len(str(j))==1:
                                        date_list.append(str("0"+str(j)+"/"+str(i)+"/"+year));
                                    else:
                                        date_list.append(str(str(j)+"/"+str(i)+"/"+year));            
                    for dates in date_list:
                        for obs in fl_sub:
                            if obs[0]==dates:
                                lat_list.append(obs[2]);
                                lon_list.append(obs[3]);
                        lat_list_len=len(lat_list);
                        lon_list_len=len(lon_list);
                        if lat_list_len==lon_list_len:
                            for i in range(len(lat_list)):
                                a=i+1;
                                if a<len(lat_list):
                                    latt1=float(lat_list[i]);
                                    latt2=float(lat_list[i+1]);
                                    long1=float(lon_list[i]);
                                    long2=float(lon_list[i+1]);
                                    r=6373.0;
                                    lat1=radians(latt1);
                                    lon1=radians(long1);
                                    lat2=radians(latt2);
                                    lon2=radians(long2);
                                    dlon=lon2-lon1;
                                    dlat=lat2-lat1;
                                    a = pow(sin(dlat/2),2) + (cos(lat1) * cos(lat2)) * ((pow(sin(dlon / 2),2)));
                                    c = 2 * atan2(sqrt(a), sqrt(1 - a));
                                    d=r*c;
                                    dist+=d;
                                else:
                                    pass;
                            lat_list=[];
                            lon_list=[];
                            print(dates,"\t",dist);             
                            dist=0.0;
                        else:
                            print("\nThe Data Available is in correct!!");
            else:
                back_to_main();
    except Exception as earg:
        print("\n"+earg);
        back_to_main();
        sys.exit(0);
        main();
'''**********************************************************************************'''
def allowance_calc():
    try:
        global lat_list,lon_list,v_counter,date_is_der_counter;
        global date_list,km_list,dist,distance,lat1,lat2,long1,long2,s,dd,mm,yy,tkm;
        date_list=[];km_list=[];
        lat_list=[];lon_list=[];v_counter=0;date_is_der_counter=0;
        print("\n********Allowance Calculation********\n");
        print("\n\t1. Daily Allowance");
        print("\n\t2. Monthly Allowance");
        print("\n\t3. Any Key To Exit");
        choice=input("\nEnter Your Choice:");
        if choice=='2':
            date_is_der_counter=0;
            dist=0;
            file_name_ac=input("\nEnter the name of the file:");
            file_read1(file_name_ac);
            month=input("\nEnter the month say (JAN-01,FEB-02..):");
            year=input("\nEnter the Year of the Month say(2016-16):");
            if(month!="" and year!=""):
                for i in range(1,32):
                    date_list.append(str(i)+"/"+month+"/"+year);
                for dates in date_list:
                    for obs in fl_sub:
                        if obs[0]==dates:
                            lat_list.append(obs[2]);
                            lon_list.append(obs[3]);
                    lat_list_len=len(lat_list);
                    lon_list_len=len(lon_list);
                    if lat_list_len==lon_list_len:
                        for i in range(len(lat_list)):
                            a=i+1;
                            if a<len(lat_list):
                                latt1=float(lat_list[i]);
                                latt2=float(lat_list[i+1]);
                                long1=float(lon_list[i]);
                                long2=float(lon_list[i+1]);
                                r=6373.0;
                                lat1=radians(latt1);
                                lon1=radians(long1);
                                lat2=radians(latt2);
                                lon2=radians(long2);
                                dlon=lon2-lon1;
                                dlat=lat2-lat1;
                                a = pow(sin(dlat/2),2) + (cos(lat1) * cos(lat2)) * ((pow(sin(dlon / 2),2)));
                                c = 2 * atan2(sqrt(a), sqrt(1 - a));
                                d=r*c;
                                dist+=d;
                            else:
                                pass;
                        lat_list=[];
                        lon_list=[];
                        km_list.append(float(dist));
                        dist=0.0;
                    else:
                        print("\nThe Data Available is in correct!!");
            tkm=sum(km_list);
            print("\nProcessing",end='');
            processing(0.25,50);
            print("\nTotal Distance Travelled for the given Month:",tkm,"Km");
            print("\nProcessing",end='');
            processing(0.25,30);
            print("\nTotal Allowance To be paid for The given Month:Rs.",float(round(tkm*3)));
            back_to_main();
        elif choice=='1':
            date_is_der_counter=0;
            dist=0;
            file_name_ac=input("\nEnter the name of the file:");
            file_read(file_name_ac);
            ip_date=str(input('Enter Some date (DD/MM/YY):'));
            s=list(ip_date);
            s[0:2]=[''.join(s[0:2])];
            s[2:4]=[''.join(s[2:4])];
            s[4:]=[''.join(s[4:])];
            for obs2 in s:
                    if obs2=='/':
                        s.remove('/');
                    else:
                        pass;
            dd=s[0];mm=s[1];yy=s[2];
            for obs_in_fl_sub in fl_sub:
                    if obs_in_fl_sub[0]==dd and obs_in_fl_sub[1]==mm and obs_in_fl_sub[2]==yy:
                        lat_list.append(obs_in_fl_sub[4]);
                        lon_list.append(obs_in_fl_sub[5]);
            if date_is_der_counter>0:
                print("Processing",end='');
                processing(0.25,50);
                print("\nThere is no data for Entered Date!!");
                back_to_main();
            else:
                lat_list_len=len(lat_list);
                lon_list_len=len(lon_list);
                if lat_list_len==lon_list_len:
                    for i in range(len(lat_list)):
                        a=i+1;
                        if a<len(lat_list):
                            latt1=float(lat_list[i]);
                            latt2=float(lat_list[i+1]);
                            long1=float(lon_list[i]);
                            long2=float(lon_list[i+1]);
                            r=6373.0;
                            lat1=radians(latt1);
                            lon1=radians(long1);
                            lat2=radians(latt2);
                            lon2=radians(long2);
                            dlon=lon2-lon1;
                            dlat=lat2-lat1;
                            a = pow(sin(dlat/2),2) + (cos(lat1) * cos(lat2)) * ((pow(sin(dlon / 2),2)));
                            c = 2 * atan2(sqrt(a), sqrt(1 - a));
                            d=r*c;
                            dist+=d;
                        else:
                            pass;
                else:
                    print("\nThe Data Available is in correct!!");
                print("Processing",end='');
                processing(0.25,50);
                print("\nTotal Distance Travelled for the given Month:",dist,"Km");
                print("Processing",end='');
                processing(0.25,30);
                print("\nTotal Allowance To be paid for The given Month:Rs.",float(round(dist*3)));
                back_to_main();
        else:
            back_to_main();
    except Exception as e:
        print(e);
'''**********************************************************************************'''
def visit_counter():
    try:
        print("\n********Visit Counter********\n");
        global lat_list,lon_list,v_counter,date_is_der_counter;
        lat_list=[];lon_list=[];v_counter=0;date_is_der_counter=0;
        file_name_vc=input("Enter the name of the file:");
        file_read(file_name_vc);
        month=input("\nEnter the month say (JAN-01,FEB-02..):");
        lat=input("\nPlease Enter The Lattitude Of The Location:");
        lon=input("\nPlease Enter The Longitude Of The Location:");
        if(month!="" and lat!="" and lon!="" ):
            for obs_in_fl_sub in fl_sub:
                if obs_in_fl_sub[1]==month:
                    lat_list.append(obs_in_fl_sub[4]);
                    lon_list.append(obs_in_fl_sub[5]);
                else:
                    date_is_der_counter+=1;
            if date_is_der_counter==0:
                print("Processing",end='');
                processing(0.25,50);
                print("\nThere is no data for Entered Month!!");
                back_to_main();
            else:
                for i in range(len(lat_list)):
                    if lat_list[i]==lat and lon_list[i]==lon:
                        v_counter=v_counter+1;
                print("Processing",end='');
                processing(0.25,50);
                print("\nHe/She Visited This Location for ",v_counter,"times!");
                back_to_main();
        else:
            print("Processing",end='');
            processing(0.25,30);
            print("\nValues Should Not Be Empty!!");
            back_to_main();
    except Exception as e:
        print("\n",e);
        back_to_main();
'''**********************************************************************************'''
def display_main():
    print("\n\n********Pizza Boy Project********\n");
    print("\t OPERATION MENU\n");
    print("\t1. Generate Report\n");
    print("\t2. Allowance Calculation\n");
    print("\t3. Visit Counter\n");
    print("\t4. Exit");
    choice=input("\nEnter Your Choice:");
    return choice;
'''**********************************************************************************'''
def main():
    while 1:
        choice=display_main();
        if choice=='1':
            report_gen();
        elif choice=='2':
            allowance_calc();
        elif choice=='3':
            visit_counter();
        elif choice=='4':
            time.sleep(0.15);
            print("Exiting",end='');
            processing(0.25,50);
            sys.exit(0);
        elif choice==None or choice=='':
            print("\nPlease Select an option!!");
        else:
            print("\nChoose Correct Option!!");
'''**********************************************************************************'''
main();
