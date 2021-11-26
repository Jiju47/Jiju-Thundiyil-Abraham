function [R] = CalculatingR(M_R)
%The Function calculates the retardance of a given retarder MM
% Der Wert ist zwischen 1 und Pi
R = acos((trace(M_R)/2)-1);
end

