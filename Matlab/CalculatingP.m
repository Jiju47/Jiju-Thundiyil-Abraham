function [P,P_Vektor] = CalculatingP(MuellerMatrix)
%The Function calculates the polarisence and the polarisence vektor of a given retarder MM
%   Der Wert liegt zwischen 0 und 1

P = (1/(MuellerMatrix(1,1)))*(sqrt(MuellerMatrix(2,1)^2+MuellerMatrix(3,1)^2+MuellerMatrix(4,1)^2));

P_Vektor = 1/(MuellerMatrix(1,1))*[MuellerMatrix(2,1); MuellerMatrix(3,1); MuellerMatrix(4,1)];

end

