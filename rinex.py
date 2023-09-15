import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

obs = "base.23O"
NaviFile = "base.23N"

def read_nav(nav):    
    
    IONALPHA, IONBETA, DELTA_UTC = [], [], []
    PRN, Epoch, a_f0, a_f1, a_f2 = [], [], [], [], []
    IODE, Crs, Delta_n, Mo = [], [], [], []
    Cuc, Eccentricity, Cus, sqrt_A = [], [], [], []
    TOE, Cic, OMEGA, CIS = [], [], [], []
    Io, Crc, Omega, OMEGA_dot = [], [], [], []
    IDOT, L2_codes_chan, GNSS_week, L2P_DataFlag = [], [], [], []
    SV_Accuracy, SV_Health, TGD, IODC = [], [], [], []
    TransTime, FitInterval = [], []

    headlines_counter = 0

    # Opening File for Reading
    File = open(nav,mode="r")

    # Parsing Header of the Navigation File
    while True:
        headlines_counter += 1
        line = File.readline()
        if "RINEX VERSION / TYPE" in line:
            RinexVersion, rem = line.split(None,1)
        elif "ION ALPHA" in line:
            ionalpha1, rem = line.split(None,1)
            ionalpha2, rem = rem.split(None, 1)
            ionalpha3, rem = rem.split(None, 1)
            ionalpha4, rem = rem.split(None, 1)
            IONALPHA.append([float(ionalpha1), float(ionalpha2), float(ionalpha3), float(ionalpha4)])
        elif "ION BETA" in line:
            ionbeta1, rem = line.split(None,1)
            ionbeta2, rem = rem.split(None, 1)
            ionbeta3, rem = rem.split(None, 1)
            ionbeta4, rem = rem.split(None, 1)
            IONBETA.append([float(ionbeta1), float(ionbeta2), float(ionbeta3), float(ionbeta4)])
        elif "DELTA-UTC:" in line:
            a0, rem = line.split(None,1)
            a1, rem = rem.split(None, 1)
            T,rem = rem.split(None, 1)
            W, rem = rem.split(None, 1)  
            DELTA_UTC.append([float(a0), float(a1), int(T), int(W)])    
        elif "END OF HEADER" in line:
            print("Header Section Parsed Successfully!\nThe total number of headlines in the file are {}".format(headlines_counter))
            head = File.tell()
            break
    File.seek(head)

    # Parsing Navigation Messages From Tracked Satellites
    File.seek(head)
    while True:
        Line = File.readline()
        if not Line: 
            break
        # Extracting Satellite Number from the Ephemeris Data
        svprn,rem = Line.split(None,1)
            
        # Extracting Epochs of Ephemeris Data
        yy,rem = rem.split(None,1)
        mm,rem = rem.split(None,1)
        dd,rem = rem.split(None,1)
        hour,rem = rem.split(None,1)
        min,rem = rem.split(None,1)
        sec,rem = rem.split(None,1)
    
        time = yy + "/" + mm + "/" + dd + "::" + hour + ":" + min + ":" + sec
        
        af0,rem = rem.split(None,1)
        af1,rem = rem.split(None,1)
        af2 = float(rem)
            
        # Broadcast Orbit 1
        Line = File.readline()
        iode, rem = Line.split(None,1)
        crs, rem = rem.split(None,1)
        deltan, rem = rem.split(None,1)
        m0 = float(rem)
        
        # Broadcast Orbit 2
        Line = File.readline()
        c_uc, rem = Line.split(None,1)
        ecc, rem = rem.split(None,1)
        c_us, rem = rem.split(None,1)
        roota = float(rem)
        
        # Broadcast Orbit 3
        Line = File.readline()
        t0e,rem = Line.split(None,1)
        c_ic, rem = rem.split(None,1)
        omega0, rem = rem.split(None,1)
        c_is = float(rem)
        
        # Broadcast Orbit 4
        Line = File.readline()
        i0,rem = Line.split(None,1)
        c_rc, rem = rem.split(None,1)
        omega, rem = rem.split(None,1)
        omega_dot = float(rem)
        
        # Broadcast Orbit 5 
        Line = File.readline()
        i_dot, rem = Line.split(None,1)
        codes, rem = rem.split(None,1)
        weekno,rem = rem.split(None,1)
        l2_flag = float(rem)
        
        # Broadcast Orbit 6
        Line = File.readline()
        sv_acc, rem = Line.split(None,1)
        sv_health,rem = rem.split(None,1)
        tgd,rem = rem.split(None)
        iodc = float(rem)
        
        # Broadcast Orbit 7
        Line = File.readline()
        tom,rem = Line.split(None,1)
        fit_inter = float(rem)
        
        # Storing the Data into Containers
        PRN.append(int(svprn)); Epoch.append(time); a_f0.append(float(af0))
        a_f1.append(float(af1)); a_f2.append(af2); IODE.append(float(iode))
        Crs.append(float(crs)); Delta_n.append(float(deltan)); Mo.append(float(m0))
        Cuc.append(float(c_uc)); Eccentricity.append(float(ecc)); Cus.append(float(c_us))
        sqrt_A.append(float(roota)); TOE.append(float(t0e)); CIS.append(float(c_is))
        Io.append(float(i0)); Crc.append(float(c_rc)); Omega.append(float(omega)); OMEGA_dot.append(float(omega_dot))
        IDOT.append(float(i_dot)); L2_codes_chan.append(float(codes)); GNSS_week.append(float(weekno)); L2P_DataFlag.append(float(l2_flag))
        SV_Accuracy.append(float(sv_acc)); SV_Health.append(float(sv_health)); TGD.append(float(tgd)); IODC.append(float(iodc))
        TransTime.append(float(tom)); FitInterval.append(float(fit_inter))
        
        print("Satellite PRN {} Data Decoded Successfully!".format(svprn))

    # Storing the Extracted Data into Pandas DataFrame
    ephemeris = {"Epoch":Epoch, "PRN": PRN, "a_f0": af0, "a_f1": a_f1,
                "a_f2": a_f2, "IODE": IODE, "Crs": Crs, "Delta_n": Delta_n,
                "Mo": Mo, "Cuc": Cuc, "Eccentricity": Eccentricity, "Cus": Cus,
                "sqrt_A":sqrt_A, "TOE": TOE, "CIS": CIS, "Io": Io, "Crs": Crs, "Omega": Omega,
                "OMEGA_dot": OMEGA_dot, "IDOT": IDOT, "L2_codes_chan": L2_codes_chan, 
                "GNSS_Week": GNSS_week, "L2P_DataFlag": L2P_DataFlag, "SV_Accuracy": SV_Accuracy,
                "SV_Health": SV_Health, "TGD":TGD, "IODC": IODC, "TransTime": TransTime,
                "FitInterval":FitInterval}

    Ephemeris = pd.DataFrame(ephemeris)
    Ephemeris.to_csv(nav + "NavFile.csv")
                
    File.close()

