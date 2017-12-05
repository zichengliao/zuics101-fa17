t = 1:0.01:10;
N0 = 100;
l = 1;

N = rad_analytic(t,N0,l);

plot(t,N);
