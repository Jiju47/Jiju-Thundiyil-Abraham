function [Delta,Delta_Vektor] = CalculatingDelta(M_delta)
%The Function calculates the average of the principal depolarization
%factors of a depolarizer Matrix
%   Der Wert liegt zwischen 0 und 1
Delta = 1 - ((abs(M_delta(2,2))+abs(M_delta(3,3))+abs(M_delta(4,4)))/3);

Delta_Vektor = 1/(M_delta(1,1))*[M_delta(1,2); M_delta(1,3); M_delta(1,4)];

end

