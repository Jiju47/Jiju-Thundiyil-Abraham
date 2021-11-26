%Verzeichnisse Wählen für MM
clear all
tic
directory_name = uigetdir('D:\Promotion\PVAH_Paper\MM-Messung', 'Bitte Verzeichnis wählen');

filelistsruc = dir(directory_name);
fielelist = struct2cell(filelistsruc);
Name_Ordner = fielelist(1,:);
Name_path = fielelist(2,:);
%löscht ersten beiden Einträge
Name_Ordner(1:2)= [];
Name_path(1:2)= [];
%Anzahl der Einträge/Ordner welche eingelesen werden sollen
AnzahlderOrdnerarrray = size(Name_Ordner)-1;
AnzahlderOrdner = AnzahlderOrdnerarrray(2);

%%
answer1 = questdlg('Möchten Sie die Mueller Matrix aus 16 oder 36 Bildern berechnen?',...
	'Anzahl der zur Berechnung einbezogenen Bilder',...
	'16 Bilder','36 Bilder','36 Bilder');

answer = questdlg('Möchten Sie die Mueller Matrix als Textdatei Speichern?',...
	'Anzahl der zur Berechnung einbezogenen Bilder',...
	'Ja','Nein','Nein');

%erzeugt eine Figure
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
% 
if answer1 == '36 Bilder'
figure = figure('Name','36-Bilder MM Normiert');
colormap(color);
colorbar;
c = colorbar;
c.FontSize = 20;
ylabel('Mueller Matrix enties');

% Create xlabel
xlabel('Mueller Matrix enties');

set(gca,'CLim',[-1 1],'FontName','Arial','FontSize',16,'Layer','top','XTick',[1024 3072 5120 7168],'XTickLabel',...
    {'M [:,1]','M [:,2]','M [:,3]','M [:,4]'},'YTick',[768 2304 3840 5376],...
   'YTickLabel',{'M [1,:]','M [2,:]','M [3,:]','M [4,:]'});
else 
figrue = figure('Name','16-Bilder MM Normiert');
colormap(color);
colorbar;    
c.FontSize = 20;
ylabel('Mueller Matrix enties');

% Create xlabel
xlabel('Mueller Matrix enties');

set(gca,'CLim',[-1 1],'FontName','Arial','FontSize',16,'Layer','top','XTick',[1024 3072 5120 7168],'XTickLabel',...
    {'M [:,1]','M [:,2]','M [:,3]','M [:,4]'},'YTick',[768 2304 3840 5376],...
   'YTickLabel',{'M [1,:]','M [2,:]','M [3,:]','M [4,:]'});
end

%% Loop MuellerMatrix Berechnung 
for index = 1:AnzahlderOrdner
    Ordnerpfad = strcat(Name_path(index),'\',Name_Ordner(index));
   Ordnerpfadreadout = Ordnerpfad{1};
    [P] = MuellerMatrixfunction(Ordnerpfadreadout,answer1,answer);
  
end

toc
Berechnungszeit = toc;
Berechnungszeit;
fprintf Finished;
