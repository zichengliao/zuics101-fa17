x = 0:0.001:1;
y = x;
figure; plot(x,y, 'linewidth', 3)
hold on; plot(x,y.^0.75, '--', 'linewidth', 3)
hold on; plot(x,y.^0.5, '--', 'linewidth', 3)
hold on; plot(x,y.^0.25, '--', 'linewidth', 3)
hold on; plot(x,y.^2, '--', 'linewidth', 3)
hold on; plot(x,y.^3, '--', 'linewidth', 3)
hold on; plot(x,y.^5, '--', 'linewidth', 3)

title('y = pow(x,n)');
xlabel('X');
ylabel('Y');