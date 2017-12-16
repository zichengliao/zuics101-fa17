function [rhs] = mylhs(x)
    b = 1.0;
    rhs = exp(-sin(b.*x).^2) - 2 + x.^2;
end