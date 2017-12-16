function [Tc, Tt] = CelsiusFromFahrenheit(Tf)
    Tc = (Tf-32)*(5/9);
    Tt = 2*Tc;
end