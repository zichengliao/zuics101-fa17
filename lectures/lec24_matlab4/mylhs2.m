function [rhs] = mylhs2(x)
    rhs = x.^3 - x.^2 -14*x + 24;
end