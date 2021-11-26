tic
clear all
close all
%Variablen:
%%
color = [0 0 1
    0 0 0.975
    0 0 0.95
    0 0 0.925
    0 0 0.9
    0 0 0.875
    0 0 0.85
    0 0 0.825
    0 0 0.8
    0 0 0.75
    0 0 0.7
    0 0 0.65
    0 0 0.6
    0 0 0.55
    0 0 0.5
    0 0 0.45
    0 0 0.4
    0 0 0.35
    0 0 0.3
    0 0 0.25
    0 0 0.2
    0 0 0
    0.2 0 0
    0.25 0 0
    0.3 0 0
    0.35 0 0
    0.4 0 0
    0.45 0 0
    0.5 0 0
    0.55 0 0
    0.6 0 0
    0.65 0 0
    0.7 0 0
    0.75 0 0
    0.8 0 0
    0.825 0 0
    0.85 0 0
    0.875 0 0
    0.9 0 0
    0.925 0 0
    0.95 0 0
    0.975 0 0
    1 0 0];
%%
            %------------------------------------------
            %Messordner wird ausgewählt
            directory_name = uigetdir('C:\Users\dierk\ownCloud\Messdaten\MM', 'Bitte Verzeichnis wählen');
            %Useraufforderung1 = 'Bitte geben Sie den Ornernamen an, aus dem die Messdaten verrechnet werden sollen: \n';
%OrdernName = input(Useraufforderung1,'s');
%------------------------------------------
%%
%Bilder Werden geladen
%%
%Dateipfade für die Bilder werden Benannt:
pathimgHH = strcat(directory_name,'\HH.tiff');
pathimgHL = strcat(directory_name,'\HL.tiff');
pathimgHM = strcat(directory_name,'\HM.tiff');
pathimgHP = strcat(directory_name,'\HP.tiff');
pathimgHR = strcat(directory_name,'\HR.tiff');
pathimgHV = strcat(directory_name,'\HV.tiff');

pathimgLH = strcat(directory_name,'\LH.tiff');
pathimgLL = strcat(directory_name,'\LL.tiff');
pathimgLM = strcat(directory_name,'\LM.tiff');
pathimgLP = strcat(directory_name,'\LP.tiff');
pathimgLR = strcat(directory_name,'\LR.tiff');
pathimgLV = strcat(directory_name,'\LV.tiff');

pathimgMH = strcat(directory_name,'\MH.tiff');
pathimgML = strcat(directory_name,'\ML.tiff');
pathimgMM = strcat(directory_name,'\MM.tiff');
pathimgMP = strcat(directory_name,'\MP.tiff');
pathimgMR = strcat(directory_name,'\MR.tiff');
pathimgMV = strcat(directory_name,'\MV.tiff');

pathimgPH = strcat(directory_name,'\PH.tiff');
pathimgPL = strcat(directory_name,'\PL.tiff');
pathimgPM = strcat(directory_name,'\PM.tiff');
pathimgPP = strcat(directory_name,'\PP.tiff');
pathimgPR = strcat(directory_name,'\PR.tiff');
pathimgPV = strcat(directory_name,'\PV.tiff');

pathimgRH = strcat(directory_name,'\RH.tiff');
pathimgRL = strcat(directory_name,'\RL.tiff');
pathimgRM = strcat(directory_name,'\RM.tiff');
pathimgRP = strcat(directory_name,'\RP.tiff');
pathimgRR = strcat(directory_name,'\RR.tiff');
pathimgRV = strcat(directory_name,'\RV.tiff');

pathimgVH = strcat(directory_name,'\VH.tiff');
pathimgVL = strcat(directory_name,'\VL.tiff');
pathimgVM = strcat(directory_name,'\VM.tiff');
pathimgVP = strcat(directory_name,'\VP.tiff');
pathimgVR = strcat(directory_name,'\VR.tiff');
pathimgVV = strcat(directory_name,'\VV.tiff');

%Bilder Werden geladen
imgHH = imread(pathimgHH);
imgHL = imread(pathimgHL);
imgHM = imread(pathimgHM);
imgHP = imread(pathimgHP);
imgHR = imread(pathimgHR);
imgHV = imread(pathimgHV);

imgLH = imread(pathimgLH);
imgLL = imread(pathimgLL);
imgLM = imread(pathimgLM);
imgLP = imread(pathimgLP);
imgLR = imread(pathimgLR);
imgLV = imread(pathimgLV);

imgMH = imread(pathimgMH);
imgML = imread(pathimgML);
imgMM = imread(pathimgMM);
imgMP = imread(pathimgMP);
imgMR = imread(pathimgMR);
imgMV = imread(pathimgMV);

imgPH = imread(pathimgPH);
imgPL = imread(pathimgPL);
imgPM = imread(pathimgPM);
imgPP = imread(pathimgPP);
imgPR = imread(pathimgPR);
imgPV = imread(pathimgPV);

imgRH = imread(pathimgRH);
imgRL = imread(pathimgRL);
imgRM = imread(pathimgRM);
imgRP = imread(pathimgRP);
imgRR = imread(pathimgRR);
imgRV = imread(pathimgRV);

imgVH = imread(pathimgVH);
imgVL = imread(pathimgVL);
imgVM = imread(pathimgVM);
imgVP = imread(pathimgVP);
imgVR = imread(pathimgVR);
imgVV = imread(pathimgVV);
%%
%Nur roter Farbkanal der einzelnen Bilder wird ausgewählt
%%
redHH = imgHH(:,:,1);
redHL = imgHL(:,:,1);
redHM = imgHM(:,:,1);
redHP = imgHP(:,:,1);
redHR = imgHR(:,:,1);
redHV = imgHV(:,:,1);

redLH = imgLH(:,:,1);
redLL = imgLL(:,:,1);
redLM = imgLM(:,:,1);
redLP = imgLP(:,:,1);
redLR = imgLR(:,:,1);
redLV = imgLV(:,:,1);

redMH = imgMH(:,:,1);
redML = imgML(:,:,1);
redMM = imgMM(:,:,1);
redMP = imgMP(:,:,1);
redMR = imgMR(:,:,1);
redMV = imgMV(:,:,1);

redPH = imgPH(:,:,1);
redPL = imgPL(:,:,1);
redPM = imgPM(:,:,1);
redPP = imgPP(:,:,1);
redPR = imgPR(:,:,1);
redPV = imgPV(:,:,1);

redRH = imgRH(:,:,1);
redRL = imgRL(:,:,1);
redRM = imgRM(:,:,1);
redRP = imgRP(:,:,1);
redRR = imgRR(:,:,1);
redRV = imgRV(:,:,1);

redVH = imgVH(:,:,1);
redVL = imgVL(:,:,1);
redVM = imgVM(:,:,1);
redVP = imgVP(:,:,1);
redVR = imgVR(:,:,1);
redVV = imgVV(:,:,1);
%------------------------------------------
%Bilder in Double umwandeln für eine Bessere Rechnung
HH = double(redHH+1);
HL = double(redHL+1);
HM = double(redHM+1);
HP = double(redHP+1);
HR = double(redHR+1);
HV = double(redHV+1);

LH = double(redLH+1);
LL = double(redLL+1);
LM = double(redLM+1);
LP = double(redLP+1);
LR = double(redLR+1);
LV = double(redLV+1);

MH = double(redMH+1);
ML = double(redML+1);
MM = double(redMM+1);
MP = double(redMP+1);
MR = double(redMR+1);
MV = double(redMV+1);

PH = double(redPH+1);
PL = double(redPL+1);
PM = double(redPM+1);
PP = double(redPP+1);
PR = double(redPR+1);
PV = double(redPV+1);

RH = double(redRH+1);
RL = double(redRL+1);
RM = double(redRM+1);
RP = double(redRP+1);
RR = double(redRR+1);
RV = double(redRV+1);

VH = double(redVH+1);
VL = double(redVL+1);
VM = double(redVM+1);
VP = double(redVP+1);
VR = double(redVR+1);
VV = double(redVV+1);
%%
%Berechnung der einzelnen Einträge der Mueller Matrix für 16 und 36 Bilder
%%
% Abfrage ob 16 oder 36 Einträge für MM
%%
answer1 = questdlg('Möchten Sie die Mueller Matrix aus 16 oder 36 Bildern berechnen?',...
	'Anzahl der zur Berechnung einbezogenen Bilder',...
	'16 Bilder','36 Bilder','36 Bilder');
% Handle response
switch answer1
%%
    case '16 Bilder'
M11 = HH+HV+VH+VV;
M12 = HH+HV-VH-VV;
M13 = 2*PH+2*PV-M11;
M14 = 2*RH+2*RV-M11;

M21 = HH-HV+VH-VV;
M22 = HH-HV-VH+VV;
M23 = 2*PH-2*PV-M21;
M24 = 2*RH-2*RV-M21;

M31 = 2*HP+2*VP-M11;
M32 = 2*HP-2*VP-M12;
M33 = 4*PP-2*PH-2*PV-M31;
M34 = 4*RP-2*RH-2*RV-M31;

M41 = 2*HR+2*VR-M11;
M42 = 2*HR-2*VR-M12;
M43 = 4*PR-2*PH-2*PV-M41;
M44 = 4*RR-2*RH-2*RV-M41;  
%%
%Zuschneiden der Bilder
figure('Name','Bitte Klicken Sie zunächst auf den oberen linken punkt und dann auf den unteren rechten Punkt welchen Sie auswählen möchten') 
M11uint = uint8(M11);
imshow(M11uint);
[uperleftcorner,lowerrightcorner] = ginput(2);
roundeduperleftcorner = round(uperleftcorner);
roundetlowerrightcorner = round(lowerrightcorner);

M11= M11(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M12= M12(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M13= M13(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M14= M14(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));

M21= M21(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M22= M22(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M23= M23(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M24= M24(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));

M31= M31(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M32= M32(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M33= M33(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M34= M34(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));

M41= M41(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M42= M42(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M43= M43(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M44= M44(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));

%%
%%
%Bestimme Mittelwerte der Matrizen (16 Bilder)
%%

meanM11=mean(M11(:));
meanM12=mean(M12(:));
meanM13=mean(M13(:));
meanM14=mean(M14(:));

meanM21=mean(M21(:));
meanM22=mean(M22(:));
meanM23=mean(M23(:));
meanM24=mean(M24(:));

meanM31=mean(M31(:));
meanM32=mean(M32(:));
meanM33=mean(M33(:));
meanM34=mean(M34(:));

meanM41=mean(M41(:));
meanM42=mean(M42(:));
meanM43=mean(M43(:));
meanM44=mean(M44(:));
%------------------------------------------

%%
%Berechung der MM und Auswertung (16 Bilder)
%%

MuellerMatrix = [meanM11 meanM12 meanM13 meanM14; meanM21 meanM22 meanM23 meanM24; meanM31 meanM32 meanM33 meanM34; meanM41 meanM42 meanM43 meanM44]/meanM11; % Normiert auf M11 um Werte zwischen 0 und 1 zu erhalten.
% display (MuellerMatrix)
% figure('Name','16-Bilder MM');
% image ([M11 M12 M13 M14; M21 M22 M23 M24; M31 M32 M33 M34; M41 M42 M43 M44]);
% BetragMuellerMatrix = abs(([M11 M12 M13 M14; M21 M22 M23 M24; M31 M32 M33 M34; M41 M42 M43 M44]));
% figure('Name','16-Bilder MM Betrag')
% imagesc(BetragMuellerMatrix,[0 100]);

%Alle Elementer der MM durch die erste geteilt:
nM11 = M11./M11;
nM12 = M12./M11;
nM13 = M13./M11;
nM14 = M14./M11;

nM21 = M21./M11;
nM22 = M22./M11;
nM23 = M23./M11;
nM24 = M24./M11;

nM31 = M31./M11;
nM32 = M32./M11;
nM33 = M33./M11;
nM34 = M34./M11;

nM41 = M41./M11;
nM42 = M42./M11;
nM43 = M43./M11;
nM44 = M44./M11;
%Element M11 auf den Wert 1 Normieren
normM11 = M11/max(max(M11)); 
%Bild der Normierten Matrix
figure('Name','16-Bilder MM Normiert')
imagesc ([nM11 nM12 nM13 nM14; nM21 nM22 nM23 nM24; nM31 nM32 nM33 nM34; nM41 nM42 nM43 nM44],[-1 1]);
colormap(color);
colorbar;
% BetragMuellerMatrixnormiert = abs(([normM11 nM12 nM13 nM14; nM21 nM22 nM23 nM24; nM31 nM32 nM33 nM34; nM41 nM42 nM43 nM44]));
% figure('Name','16-Bilder MM Normiert und Betrag')
% colormap(gray);
% colorbar;
% imagesc(BetragMuellerMatrixnormiert, [0 1]);
% set(gca,'XTick',[],'YTick',[]);

    case '36 Bilder'
%%
M11 = HH+HV+VH+VV;
M12 = HH+HV-VH-VV;
M13 = PH+PV-MH-MV;
M14 = RH+RV-LH-LV;

M21 = HH-HV+VH-VV;
M22 = HH-HV-VH+VV;
M23 = PH-PV-MH+MV;
M24 = RH-RV-LH+LV;

M31 = HP-HM+VP-VM;
M32 = HP-HM-VP+VM;
M33 = PP-PM-MP+MM;
M34 = RP-RM-LP+LM;

M41 = HR-HL+VR-VL;
M42 = HR-HL-VR+VL;
M43 = PR-PL-MR+ML;
M44 = RR-RL-LR+LL;

%Zuschneiden der Bilder variabler Bildausschnitt
figure('Name','Bitte Klicken Sie zunächst auf den oberen linken punkt und dann auf den unteren rechten Punkt welchen Sie auswählen möchten') 
M11uint = uint8(M11);
imshow(M11uint);
[uperleftcorner,lowerrightcorner] = ginput(2);
roundeduperleftcorner = round(uperleftcorner);
roundetlowerrightcorner = round(lowerrightcorner);
% %Zuschneiden der Bilder fester Bildausschnitt
% roundeduperleftcorner =[1054;1634];%refl 0
% roundetlowerrightcorner =[675;1175];%refl 0
% roundeduperleftcorner =[1150;1690];%refl 90
% roundetlowerrightcorner =[373;1275];%refl 90
% roundeduperleftcorner =[392;1332];
% roundetlowerrightcorner =[447;1313];

% % Für Bereich B
% roundeduperleftcorner = [268 744];
% roundetlowerrightcorner = [661 1115];

M11= M11(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M12= M12(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M13= M13(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M14= M14(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));

M21= M21(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M22= M22(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M23= M23(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M24= M24(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));

M31= M31(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M32= M32(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M33= M33(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M34= M34(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));

M41= M41(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M42= M42(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M43= M43(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
M44= M44(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));

% 
% M11= M11(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
% M12= M12(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
% M13= M13(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
% M14= M14(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
% 
% M21= M21(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
% M22= M22(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
% M23= M23(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
% M24= M24(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
% 
% M31= M31(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
% M32= M32(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
% M33= M33(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
% M34= M34(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
% 
% M41= M41(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
% M42= M42(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
% M43= M43(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));
% M44= M44(roundetlowerrightcorner(1):roundetlowerrightcorner(2),roundeduperleftcorner(1):roundeduperleftcorner(2));


%%
%------------------------------------------
%%
%Bestimme Mittelwerte der Matrizen (36 Bilder)
%%
meanM11=mean(M11(:));
meanM12=mean(M12(:));
meanM13=mean(M13(:));
meanM14=mean(M14(:));

meanM21=mean(M21(:));
meanM22=mean(M22(:));
meanM23=mean(M23(:));
meanM24=mean(M24(:));

meanM31=mean(M31(:));
meanM32=mean(M32(:));
meanM33=mean(M33(:));
meanM34=mean(M34(:));

meanM41=mean(M41(:));
meanM42=mean(M42(:));
meanM43=mean(M43(:));
meanM44=mean(M44(:));
%------------------------------------------
%%
%Berechung der MM und Auswertung (36 Bilder)
%%

MuellerMatrix = [meanM11 meanM12 meanM13 meanM14; meanM21 meanM22 meanM23 meanM24; meanM31 meanM32 meanM33 meanM34; meanM41 meanM42 meanM43 meanM44]/meanM11; % Normiert auf M11 um Werte zwischen 0 und 1 zu erhalten.
% display (MuellerMatrix)
% figure('Name','36-Bilder MM');
% image ([M11 M12 M13 M14; M21 M22 M23 M24; M31 M32 M33 M34; M41 M42 M43 M44]);
% BetragMuellerMatrix = abs(([M11 M12 M13 M14; M21 M22 M23 M24; M31 M32 M33 M34; M41 M42 M43 M44]));
% figure('Name','36-Bilder MM Betrag');
% imagesc(BetragMuellerMatrix,[0 100]);

%Alle Elementer der MM durch die erste geteilt:
nM11 = M11./M11;
nM12 = M12./M11;
nM13 = M13./M11;
nM14 = M14./M11;

nM21 = M21./M11;
nM22 = M22./M11;
nM23 = M23./M11;
nM24 = M24./M11;

nM31 = M31./M11;
nM32 = M32./M11;
nM33 = M33./M11;
nM34 = M34./M11;

nM41 = M41./M11;
nM42 = M42./M11;
nM43 = M43./M11;
nM44 = M44./M11;

%Element M11 auf den Wert 1 Normieren
normM11 = M11/max(max(M11)); 
%Bild der Normierten Matrix (alle Bilder mit M11 normiert 
figure('Name','36-Bilder MM Normiert');
imagesc ([nM11 nM12 nM13 nM14; nM21 nM22 nM23 nM24; nM31 nM32 nM33 nM34; nM41 nM42 nM43 nM44],[-1 1]);
colormap(color);
colorbar;
c = colorbar;
c.FontSize = 20;
%alle Bilder normiert außer M11
% BetragMuellerMatrixnormiert = abs(([nM11 nM12 nM13 nM14; nM21 nM22 nM23 nM24; nM31 nM32 nM33 nM34; nM41 nM42 nM43 nM44]));
% figure('Name','36-Bilder MM Normiert und Betrag');
% colormap(gray);
% imagesc(BetragMuellerMatrixnormiert, [0 1]);
% colorbar;
% set(gca,'XTick',[],'YTick',[]);
end
%%Decomposing 
[M_delta,M_R,M_D] = PolarDecomposingMM(MuellerMatrix);

[Delta,Delta_Vektor] = CalculatingDelta(M_delta);
[R] = CalculatingR(M_R);
[P,P_Vektor] = CalculatingP(MuellerMatrix);
[a1,a2,a3] = CalculatingA(M_R,R);
a_vector=[1, a1, a2, a3];
%%
%Speichert die Matrix als txt datei im Bildordner falls gewünscht
answer = questdlg('Möchten Sie die Mueller Matrix als Textdatei Speichern?',...
	'Anzahl der zur Berechnung einbezogenen Bilder',...
	'Ja','Nein','Nein');
switch answer
    case 'Ja'
       MMsavepath = strcat(directory_name,'\MuellerMatrixausschnitt',answer1,'.txt');
        %dlmwrite(MMsavepath,MuellerMatrix,'delimiter','\t','precision',6);
         dlmwrite(MMsavepath,MuellerMatrix,'delimiter','\t','precision','%.6f','newline','pc');
         
         M_deltasavepath = strcat(directory_name,'\M_deltaausschnit',answer1,'.txt');
         dlmwrite(M_deltasavepath,M_delta,'delimiter','\t','precision','%.6f','newline','pc');
         
         M_Rsavepath = strcat(directory_name,'\M_Rausschnit',answer1,'.txt');
         dlmwrite(M_Rsavepath,M_R,'delimiter','\t','precision','%.6f','newline','pc');
         
         M_Dsavepath = strcat(directory_name,'\M_Dausschnit',answer1,'.txt');
         dlmwrite(M_Dsavepath,M_D,'delimiter','\t','precision','%.6f','newline','pc');
    
         Kennzahlen = [R,P,Delta];

         Kennzahlensavepath = strcat(directory_name,'\R-P-Deltaausschnit',answer1,'.txt');
         dlmwrite(Kennzahlensavepath,Kennzahlen,'delimiter','\t','precision','%.6f');
         
         a_vectorsavepath = strcat(directory_name,'\a-vector',answer1,'.txt');
         dlmwrite(a_vectorsavepath,a_vector,'delimiter','\t','precision','%.6f');
    case 'Nein'
    
end
%Speichern des Bildes
MMsavepath = strcat(directory_name,'\BildMM',answer1,'Ausschnitt','.tiff');
print('-r300',MMsavepath,'-dtiff')

directory_name

Berechnungszeit = toc;
