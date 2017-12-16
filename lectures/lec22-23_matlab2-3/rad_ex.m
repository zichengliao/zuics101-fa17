function [N] = rad_ex(N0, dt, l_a, l_b)
%UNTITLED6 Summary of this function goes here
%   Detailed explanation goes here

lambda = [-l_a*dt+1,   0,     0;
           l_a*dt, -l_b*dt+1, 0;
           0,        l_b*dt,  1];

N = lambda*N0;

end

