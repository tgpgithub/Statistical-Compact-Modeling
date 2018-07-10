#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 06:29:47 2017

@author: user
"""

class Parameters(object):
    '''
    参数类
    '''
    def __init__(self):
        self.m = {}
        self.resetParameters()
        
    def resetParameters(self):           
        """初始化参数"""
        # mosfet参数card
        self.m[" binunit "] = 1;self.m[" diomod "] = 1;self.m[" igbmod "] = 0;self.m[" igcmod "] = 0;self.m[" level "] = 54;
        self.m[" mobmod "] = 0;self.m[" permod "] = 1;self.m[" rdsmod "] = 0;self.m[" stimod "] = 0;self.m[" wpemod "] = 0;
        self.m[" capmod "] = 2;self.m[" trnqsmod "] = 0;self.m[" xpart "] = 1;self.m[" fnoimod "] = 1;self.m[" tnoimod "] = 0;
        self.m[" dmcg "] = 0;self.m[" dmcgt "] = 0;self.m[" dmdg "] = 0;self.m[" ndep "] = 6.32e+18;self.m[" ngate "] = 0;
        self.m[" ngcon "] = 1;self.m[" nsd "] = 1e+20;self.m[" rsh "] = 0;self.m[" rshg "] = 0.1;self.m[" toxe "] = 8.5e-10;
        self.m[" xgl "] = 0;self.m[" xgw "] = 0;self.m[" xj "] = 1.75e-08;self.m[" nsub "] = 5e+18;self.m[" vbm "] = -3;
        self.m[" vfb "] = -1;self.m[" xt "] = 6e-08;self.m[" dwb "] = 0;self.m[" dwg "] = 0;self.m[" lint "] = 6.42065e-10;
        self.m[" ll "] = 0;self.m[" lln "] = 0.33;self.m[" lw "] = 0;self.m[" lwl "] = 0;self.m[" lwn "] = 0.33;
        self.m[" wint "] = 0;self.m[" wl "] = 0;self.m[" wln "] = 0.33;self.m[" ww "] = 0;self.m[" wwl "] = 0;
        self.m[" wwn "] = 0.33;self.m[" a0 "] = 0.812429;self.m[" a1 "] = 0;self.m[" a2 "] = 1;self.m[" agidl "] = 0;
        self.m[" ags "] = 2.13579e-55;self.m[" aigbacc "] = 0.43;self.m[" aigbinv "] = 0.35;self.m[" aigc "] = 0.054;self.m[" aigsd "] = 0.43;
        self.m[" alpha0 "] = 0;self.m[" alpha1 "] = 0;self.m[" b0 "] = 0;self.m[" b1 "] = 0;self.m[" beta0 "] = 30;
        self.m[" bgidl "] = 2.3e+09;self.m[" bigbacc "] = 0.054;self.m[" bigbinv "] = 0.03;self.m[" bigc "] = 0.054;self.m[" bigsd "] = 0.054;
        self.m[" cdsc "] = 0.0473886;self.m[" cdscb "] = -1.94116e-06;self.m[" cdscd "] = 0.00133942;self.m[" cgidl "] = 0.5;self.m[" cigbacc "] = 0.075;
        self.m[" cigbinv "] = 0.006;self.m[" cigc "] = 0.075;self.m[" cigsd "] = 0.075;self.m[" cit "] = 0;self.m[" delta "] = 0.0175878;
        self.m[" drout "] = 0.56;self.m[" dsub "] = 0.526083;self.m[" dvt0 "] = 5.36509;self.m[" dvt0w "] = 0;self.m[" dvt1 "] = 0.707995;
        self.m[" dvt1w "] = 0;self.m[" dvt2 "] = -0.00169479;self.m[" dvt2w "] = 0;self.m[" dvtp0 "] = 2.97429e-08;self.m[" dvtp1 "] = -0.367993;
        self.m[" egidl "] = 0.8;self.m[" eigbinv "] = 1.1;self.m[" eta0 "] = 0.31926;self.m[" etab "] = -0.117749;self.m[" eu "] = 1.67;
        self.m[" fprout "] = 0;self.m[" gbmin "] = 1e-12;self.m[" k1 "] = 0.464497;self.m[" k2 "] = -0.0785674;self.m[" k2we "] = 0;
        self.m[" k3 "] = 0;self.m[" k3b "] = 0;self.m[" keta "] = -0.047;self.m[" kvth0we "] = 0;self.m[" lambda "] = 0;
        self.m[" lc "] = 0;self.m[" lku0 "] = 0;self.m[" lkvth0 "] = 0;self.m[" llodku0 "] = 0;self.m[" llodvth "] = 0;
        self.m[" lodeta0 "] = 1;self.m[" lp "] = 1e-09;self.m[" lpe0 "] = 1.78671e-08;self.m[" lpeb "] = 1.84658e-08;self.m[" minv "] = -0.386689;
        self.m[" nfactor "] = 0.940901;self.m[" nigbacc "] = 1;self.m[" nigbinv "] = 3;self.m[" nigc "] = 1;self.m[" ntox "] = 1;
        self.m[" pclm "] = 1e-10;self.m[" pdiblc1 "] = 0;self.m[" pdiblc2 "] = 0.0479311;self.m[" pdiblcb "] = 0;self.m[" pdits "] = 0;
        self.m[" pditsd "] = 0;self.m[" pditsl "] = 0;self.m[" phin "] = 0;self.m[" pigcd "] = 1;self.m[" poxedge "] = 1;
        self.m[" prwb "] = 0.0140188;self.m[" prwg "] = 0;self.m[" pscbe1 "] = 4.24e+08;self.m[" pscbe2 "] = 1e-20;self.m[" pvag "] = 0.426307;
        self.m[" rdsw "] = 86.5462;self.m[" rdswmin "] = 0;self.m[" rdw "] = 0;self.m[" rdwmin "] = 0;self.m[" rsw "] = 0;
        self.m[" rswmin "] = 0;self.m[" toxref "] = 3e-09;self.m[" u0 "] = 0.0316446;self.m[" ua "] = 1.07729e-09;self.m[" ub "] = 0;
        self.m[" uc "] = -1.10233e-15;self.m[" up "] = 0;self.m["voff "] = -0.0836792;self.m[" voffl "] = -1.30743e-09;self.m[" vsat "] = 137323;
        self.m[" vth0 "] = 0.213313;self.m[" vtl "] = 205000;self.m[" w0 "] = 2.5e-06;self.m[" web "] = 0;self.m[" wec "] = 0;
        self.m[" wku0 "] = 0;self.m[" wkvth0 "] = 0;self.m[" wlod "] = 0;self.m[" wlodku0 "] = 0;self.m[" wlodvth "] = 0;
        self.m[" wr "] = 1;self.m[" xn "] = 3;self.m[" acde "] = 1;self.m[" cgdl "] = 0;self.m[" cgsl "] = 0;
        self.m[" ckappas "] = 0.6;self.m[" clc "] = 1e-07;self.m[" cle "] = 0.6;self.m[" moin "] = 15;self.m[" noff "] = 1;
        self.m[" vfbcv "] = -1;self.m[" voffcv "] = 0;self.m[" xrcrg1 "] = 12;self.m[" xrcrg2 "] = 1;self.m[" af "] = 1;
        self.m[" ef "] = 0;self.m[" kf "] = 1;self.m[" noia "] = 1e+20;self.m[" noib "] = 50000;self.m[" noic "] = -1.4e-12;
        self.m[" ntnoi "] = 1;self.m[" rnoia "] = 0.577;self.m[" rnoib "] = 0.37;self.m[" tnoia "] = 1.5;self.m[" tnoib "] = 3.5;
        self.m[" imax "] = 1000;self.m[" jsd "] = 0;self.m[" jss "] = 0;self.m[" jswd "] = 0;self.m[" jsws "] = 0;
        self.m[" njd "] = 1;self.m[" njs "] = 1;self.m[" vr "] = 0;self.m[" cjd "] = 0.000579;self.m[" cjs "] = 0.000579;
        self.m[" cjswd "] = 0;self.m[" cjswgd "] = 0;self.m[" cjswgs "] = 0;self.m[" cjsws "] = 0;self.m[" mjd "] = 0.5;
        self.m[" mjs "] = 0.5;self.m[" mjswd "] = 0.33;self.m[" mjswgd "] = 0.33;self.m[" mjswgs "] = 0.33;self.m[" mjsws "] = 0.33;
        self.m[" pb "] = 0.4;self.m[" pbd "] = 1;self.m[" pbs "] = 1;self.m[" pbswd "] = 1;self.m[" pbswgd "] = 1;
        self.m[" pbswgs "] = 1;self.m[" pbsws "] = 1;self.m[" tempmod "] = 0;self.m[" tnom "] = 27;self.m[" at "] = 33000;
        self.m[" kt1 "] = 0;self.m[" kt1l "] = 0;self.m[" kt2 "] = 0.022;self.m[" prt "] = 0;self.m[" ua1 "] = 4.31e-09;
        self.m[" ub1 "] = -7.61e-18;self.m[" uc1 "] = -5.69e-11;self.m[" ute "] = -1.5;self.m[" xtis "] = 3;self.m[" lmax "] = 1;
        self.m[" lmin "] = 0;self.m[" wmax "] = 1;self.m[" wmin "] = 0;self.m[" la0 "] = 0;self.m[" la1 "] = 0;
        self.m[" la2 "] = 0;self.m[" lags "] = 0;self.m[" lalpha0 "] = 0;self.m[" lalpha1 "] = 0;self.m[" lbeta0 "] = 0;
        self.m[" lcdsc "] = 0;self.m[" lcdscb "] = 0;self.m[" lcdscd "] = 0;self.m[" lcit "] = 0;self.m[" ldelta "] = -0.000302423;
        self.m[" ldrout "] = 0;self.m[" ldsub "] = 0;self.m[" ldvt0 "] = 0;self.m[" ldvt1 "] = 0;self.m[" leta0 "] = 0;
        self.m[" letab "] = 0;self.m[" lk1 "] = 0;self.m[" lk2 "] = 0;self.m[" lk2we "] = 0;self.m[" lk3 "] = 0;
        self.m[" lk3b "] = 0;self.m[" lketa "] = 0;self.m[" lku0we "] = 0;self.m[" lkvth0we "] = 0;self.m[" llpe0 "] = 0;
        self.m[" llpeb "] = 0;self.m[" lminv "] = 0;self.m[" lnfactor "] = 0.0259918;self.m[" lpclm "] = 0;self.m[" lpdiblc1 "] = 0;
        self.m[" lpdiblc2 "] = 0.000120817;self.m[" lpdiblcb "] = 0;self.m[" lprwb "] = 0;self.m[" lprwg "] = 0;self.m[" lpscbe1 "] = 0;
        self.m[" lpscbe2 "] = 0;self.m[" lpvag "] = 0;self.m[" lrdsw "] = 0.00199997;self.m[" lrdw "] = 0;self.m[" lrsw "] = 0;
        self.m[" lu0 "] = -0.00020478;self.m[" lua "] = 0;self.m[" lub "] = 0;self.m[" luc "] = 0;self.m[" lvoff "] = 0;
        self.m[" lvsat "] = -231.013;self.m[" lvth0 "] = 0;self.m[" lw0 "] = 0;self.m[" lwr "] = 0;self.m[" pa0 "] = 0;
        self.m[" pa1 "] = 0;self.m[" pa2 "] = 0;self.m[" pags "] = 0;self.m[" palpha0 "] = 0;self.m[" palpha1 "] = 0;
        self.m[" pbeta0 "] = 0;self.m[" pcdsc "] = 0;self.m[" pcdscb "] = 0;self.m[" pcdscd "] = 0;self.m[" pcit "] = 0;
        self.m[" pdelta "] = 0;self.m[" pdrout "] = 0;self.m[" pdsub "] = 0;self.m[" pdvt0 "] = 0;self.m[" pdvt1 "] = 0;
        self.m[" peta0 "] = 0;self.m[" petab "] = 0;self.m[" pk1 "] = 0;self.m[" pk2 "] = 0;self.m[" pk2we "] = 0;
        self.m[" pk3 "] = 0;self.m[" pk3b "] = 0;self.m[" pketa "] = 0;self.m[" pku0we "] = 0;self.m[" pkvth0we "] = 0;
        self.m[" plpe0 "] = 0;self.m[" plpeb "] = 0;self.m[" pminv "] = 0;self.m[" pnfactor "] = 0;self.m[" ppclm "] = 0;
        self.m[" ppdiblc1 "] = 0;self.m[" ppdiblc2 "] = 0;self.m[" ppdiblcb "] = 0;self.m[" pprwb "] = 0;self.m[" pprwg "] = 0;
        self.m[" ppscbe1 "] = 0;self.m[" ppscbe2 "] = 0;self.m[" ppvag "] = 0;self.m[" prdsw "] = 0;self.m[" prdw "] = 0;
        self.m[" prsw "] = 0;self.m[" pu0 "] = 0;self.m[" pua "] = 0;self.m[" pub "] = 0; 
    
    def updateCard(self):
        #输出读入的数据
		f = open("/home/user/Desktop/software1/ngspice-26/tests/bsim4/nmos/BSIM470_Benchmarking/nmodelcardpso","w");	
		f.write ("** Model: BSIM4.6.5**\n ") 
		f.write("** Berkeley SPICE3f5 Compatible\n ")
		f.write(".model n25 NMOS\n ")
		f.write("+ version = 4.6.5\n ")
		#遍历参数
		for (x,y) in self.m.iteritems():
			f.write(" + %s = %s \n"%(x,y))		
		f.close()
#para =Parameters()
#para.resetParameters()
#para.updateCard()
#print para.m