C = 3;
center = rand(C,2)*10;
sigma = abs(randn(C,1)) + 0.5;

Xs = [];
Ys = [];
for i = 1:C
    Xs = [Xs; center(i,1) + sigma(i)*randn(1000,1)];
    Ys = [Ys; center(i,2) + sigma(i)*randn(1000,1)];
end
figure;hold on;
scatter(Xs(1:1000), Ys(1:1000), 'r');
scatter(Xs(1001:2000), Ys(1001:2000), 'g');
scatter(Xs(2001:3000), Ys(2001:3000), 'b');