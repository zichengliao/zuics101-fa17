function [N, N0] = rad_analytic(t, N0, lambda)

    N = N0 * exp(-lambda * t);

end

