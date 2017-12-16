function [rhs] = mylhs2(x)
    rhs = -2*x.^3 + 3*x.^2 -4*x - 5;
end