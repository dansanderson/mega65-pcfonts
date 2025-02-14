10 dim t$(88),f$(88)
20 for i=0 to 87:read t$(i),f$(i):next i
30 i=0
40 clrbit $d054,5:setbit $d07a,4
100 gosub 500
105 bload (f$(i)),p($ff7e000)
107 gosub 200
110 getkey a$:a=asc(a$)
120 if a=85 then 190 : rem use
130 if a=81 then 180 : rem quit
130 if a=157 then i=i-1 : rem left
140 if a=29 or a=43 then i=i+1 : rem right or space
150 if i<0 then i=87
160 if i>87 then i=0
170 goto 100
180 clrbit $d07a,4:font c
190 end
200 background 6:border 6
210 print chr$(147) + chr$(5)
220 print chr$(2) + "PC fonts on the MEGA65" + chr$(130) + chr$(13)
230 print "This text is being displayed using a classic PC font from"
240 print "the Oldschool PC Font Resource, using the MEGA65's 8x16 high"
250 print "resolution text mode."+chr$(13)
260 print "The current font: " +chr$(158) + t$(i) + chr$(5) + chr$(13)
270 print "Select a new font with left/right cursor keys."
280 print "(U)se the current font, or (Q)uit and disable high resolution text mode."
290 print chr$(17)+chr$(17)+chr$(17)+chr$(17)+chr$(17)+chr$(17)
300 for x=0 to 255:poke $0800+80*13+x,x:next x
310 return
500 print chr$(19)+chr$(17)+chr$(17)+chr$(17)+chr$(17)+chr$(17)+chr$(17)+chr$(17);
510 print chr$(29)+chr$(29)+chr$(29)+chr$(29)+chr$(29)+chr$(29)+chr$(29)+chr$(29);
520 print chr$(29)+chr$(29)+chr$(29)+chr$(29)+chr$(29)+chr$(29)+chr$(29)+chr$(29);
530 print chr$(29)+chr$(29)+"                                          ";
540 return
9000 data "ACM VGA","acmvga.tcr"
9010 data "ACM VGA (all)","acmvga-a.tcr"
9020 data "ATI","ati.tcr"
9030 data "ATI (all)","ati-a.tcr"
9040 data "AT&T PC6300","attpc6300.tcr"
9050 data "AT&T PC6300 (all)","attpc6300-a.tcr"
9060 data "CL Eagle II","cleagleii.tcr"
9070 data "CL Eagle II (all)","cleagleii-a.tcr"
9080 data "CL Eagle III","cleagleiii.tcr"
9090 data "CL Eagle III (all)","cleagleiii-a.tcr"
9100 data "CL Stingray 0","clstingry0.tcr"
9110 data "CL Stingray 0 (all)","clstingry0-a.tcr"
9120 data "CL Stingray 1","clstingry1.tcr"
9130 data "CL Stingray 1 (all)","clstingry1-a.tcr"
9140 data "CompaqThin","compaqthin.tcr"
9150 data "CompaqThin (all)","compaqthin-a.tcr"
9160 data "Compaq Port3","compaqprt3.tcr"
9170 data "Compaq Port3 (all)","compaqprt3-a.tcr"
9180 data "Compis","compis.tcr"
9190 data "Compis (all)","compis-a.tcr"
9200 data "DOS/V TWN16","dosvtwn16.tcr"
9210 data "DOS/V TWN16 (all)","dosvtwn16-a.tcr"
9220 data "DOS/V re. ANK16","dosvrank16.tcr"
9230 data "DOS/V re. ANK16 (all)","dosvrank16-a.tcr"
9240 data "DOS/V re. JPN16","dosvrjpn16.tcr"
9250 data "DOS/V re. JPN16 (all)","dosvrjpn16-a.tcr"
9260 data "DOS/V re. PRC16","dosvrprc16.tcr"
9270 data "DOS/V re. PRC16 (all)","dosvrprc16-a.tcr"
9280 data "EverexME","everexme.tcr"
9290 data "EverexME (all)","everexme-a.tcr"
9300 data "FMTowns","fmtownsre.tcr"
9310 data "FMTowns (all)","fmtownsre-a.tcr"
9320 data "IBM DOS ISO8","ibmdosiso8.tcr"
9330 data "IBM DOS ISO8 (all)","ibmdosiso8-a.tcr"
9340 data "IBM Model30r0","ibmmod30r0.tcr"
9350 data "IBM Model30r0 (all)","ibmmod30r0-a.tcr"
9360 data "IBM Model3x alt 1","ibmmod3xa1.tcr"
9370 data "IBM Model3x alt 1 (all)","ibmmod3xa1-a.tcr"
9380 data "IBM Model3x alt 2","ibmmod3xa2.tcr"
9390 data "IBM Model3x alt 2 (all)","ibmmod3xa2-a.tcr"
9400 data "IBM Model3x alt 3","ibmmod3xa3.tcr"
9410 data "IBM Model3x alt 3 (all)","ibmmod3xa3-a.tcr"
9420 data "IBM Model3x alt 4","ibmmod3xa4.tcr"
9430 data "IBM Model3x alt 4 (all)","ibmmod3xa4-a.tcr"
9440 data "IBM PGC","ibmpgc.tcr"
9450 data "IBM PGC (all)","ibmpgc-a.tcr"
9460 data "IBM VGA","ibmvga.tcr"
9470 data "IBM VGA (all)","ibmvga-a.tcr"
9480 data "IGS VGA","igsvga.tcr"
9490 data "IGS VGA (all)","igsvga-a.tcr"
9500 data "MBytePC230","mbytepc230.tcr"
9510 data "MBytePC230 (all)","mbytepc230-a.tcr"
9520 data "NEC APC3","necapc3.tcr"
9530 data "NEC APC3 (all)","necapc3-a.tcr"
9540 data "Nix8810 M15","nix8810m15.tcr"
9550 data "Nix8810 M15 (all)","nix8810m15-a.tcr"
9560 data "Nix8810 M16","nix8810m16.tcr"
9570 data "Nix8810 M16 (all)","nix8810m16-a.tcr"
9580 data "OlivettiThin","olivettthn.tcr"
9590 data "OlivettiThin (all)","olivettthn-a.tcr"
9600 data "PhoenixEGA","phoenixega.tcr"
9610 data "PhoenixEGA (all)","phoenixega-a.tcr"
9620 data "PhoenixVGA","phoenixvga.tcr"
9630 data "PhoenixVGA (all)","phoenixvga-a.tcr"
9640 data "Robotron A7100","rbtrna7100.tcr"
9650 data "Robotron A7100 (all)","rbtrna7100-a.tcr"
9660 data "Sigma RM","sigmarm.tcr"
9670 data "Sigma RM (all)","sigmarm-a.tcr"
9680 data "SperryPC","sperrypc.tcr"
9690 data "SperryPC (all)","sperrypc-a.tcr"
9700 data "Tandy2K","tandy2k.tcr"
9710 data "Tandy2K (all)","tandy2k-a.tcr"
9720 data "Tandy2K G","tandy2kg.tcr"
9730 data "Tandy2K G (all)","tandy2kg-a.tcr"
9740 data "ToshibaSat","toshibasat.tcr"
9750 data "ToshibaSat (all)","toshibasat-a.tcr"
9760 data "ToshibaT300","toshibt300.tcr"
9770 data "ToshibaT300 (all)","toshibt300-a.tcr"
9780 data "ToshibaTxL1","toshibtxl1.tcr"
9790 data "ToshibaTxL1 (all)","toshibtxl1-a.tcr"
9800 data "ToshibaTxL2","toshibtxl2.tcr"
9810 data "ToshibaTxL2 (all)","toshibtxl2-a.tcr"
9820 data "Trident","trident.tcr"
9830 data "Trident (all)","trident-a.tcr"
9840 data "TridentEarly","tridntearl.tcr"
9850 data "TridentEarly (all)","tridntearl-a.tcr"
9860 data "Verite","verite.tcr"
9870 data "Verite (all)","verite-a.tcr"
