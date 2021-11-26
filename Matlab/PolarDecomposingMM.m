function [M_delta,M_R,M_D] = PolarDecomposingMM(Matrix)
%DecomposingMM: gibt die Decomposing Matrizen für die Input "Matrix" aus.
%   Berechnet für eine Mueller Matrix die zusammensetzung der Matrix "M"
%   aus "M = M_delta * M_R * M_D". Also einer Depolarisierenden Matrix (M_delta)
%   einer Verzögernden Matrix(M_R) und einer Polarisationsdrehenden Matrix (M_D)

%% Polarianze
P_firstcolumn = transpose(Matrix(2:4,1));

%% Transmittance for unpolarized light
T_u_stokes = Matrix*[1;0;0;0];
T_u = norm(T_u_stokes);

%% M_D
D_firstraw = transpose(Matrix(1,2:4));
D = 1/(Matrix(1,1)) * D_firstraw;
D_betrag = norm(D); %nur D
D_norm = D/D_betrag; %mit dach
m_D = sqrt(1-(D_betrag^2))*eye(3)+ (1-sqrt(1-(D_betrag^2)))*D_norm*transpose(D_norm);
M_D =     [Matrix(1,1) D(1) D(2) D(3); 
           D(1) m_D(1,1) m_D(1,2) m_D(1,3);
           D(2) m_D(2,1) m_D(2,2) m_D(2,3);
           D(3) m_D(3,1) m_D(3,2) m_D(3,3)];
% Eigentlich muss M_D mit der Transmissivität für unpolarisiertes Licht
% multipliziert werden:
% M_D =     T_u*[Matrix(1,1) D(1) D(2) D(3); 
%            D(1) m_D(1,1) m_D(1,2) m_D(1,3);
%            D(2) m_D(2,1) m_D(2,2) m_D(2,3);
%            D(3) m_D(3,1) m_D(3,2) m_D(3,3)];
       
%% M_strich
%M_strich ist M= M*M^-1
%M_strich = Matrix*inv(M_D);
M_strich = Matrix/M_D; %soll effizienter sein
%Verzögerungsmatrix und Depolarisationsmatrix( M_R= M * M_D^-1)
%Berechne M_strich und m_strich (untermatrix)
%P_delta= transpose(M_strich(1,2:4));
P_delta= M_strich(2:4,1);
%P_delta = (P-m*D)/(1-D_betrag^2);

m_strich = [M_strich(2,2) M_strich(2,3) M_strich(2,4);
            M_strich(3,2) M_strich(3,3) M_strich(3,4);
            M_strich(4,2) M_strich(4,3) M_strich(4,4)];
%Eigenwerte von m_strich
Eigenwerte_m_strich = eig(m_strich*transpose(m_strich));
Eigen0 = Eigenwerte_m_strich(1);
Eigen1 = Eigenwerte_m_strich(2);
Eigen2 = Eigenwerte_m_strich(3);


%% M_delta
A = transpose(m_strich*transpose(m_strich)+(sqrt(Eigen0*Eigen1)+sqrt(Eigen1*Eigen2)+sqrt(Eigen2*Eigen0))*eye(3));
B = (sqrt(Eigen0)+sqrt(Eigen1)+sqrt(Eigen2))*(m_strich*transpose(m_strich))+sqrt(Eigen0*Eigen1*Eigen2)*eye(3);
if det(m_strich)<0
m_delta = -mtimes(inv(A),B);
                 
else
m_delta = mtimes(inv(A),B);   
end

M_delta =[1 0 0 0;
          P_delta(1) m_delta(1,1) m_delta(1,2) m_delta(1,3);
          P_delta(2) m_delta(2,1) m_delta(2,2) m_delta(2,3)
          P_delta(3) m_delta(3,1) m_delta(3,2) m_delta(3,3)];
%% M_R
M_R = M_delta\M_strich; % eigentlich M_R = (M_delta^-1)\(M_strich)



end

