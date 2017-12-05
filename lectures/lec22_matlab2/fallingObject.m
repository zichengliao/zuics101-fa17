function [ y ] = fallingObject( t, x0, y0 )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here

y = 0.5*(-9.81)*t.^2 + y0*t + x0;

y(y<0) = 0;

end

