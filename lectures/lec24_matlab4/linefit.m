load('xy.mat');

%prepare the maxtrix A and rhs vector
A = [x ones(numel(x),1)];
rhs = y;

k = A\rhs;		%backslash again!

%compute fitted values
yfit = A*k;

figure; plot(x,y,'bx', 'linewidth', 2);
hold on;
plot(x, yfit, 'r-', 'linewidth',2);
plot(x, yfit, 'ms', 'linewidth',2); 	%as scattered points
