Xr = [0,pi*5];
Yr = [0,1];
nx = 1000;
ny = 500;

xs = linspace(Xr(1), Xr(2), nx);
ys = linspace(Yr(1), Yr(2), ny);
[X,Y] = meshgrid(xs,ys);

%%
I = zeros(size(X));
% for r = 1:size(X,1)
%     for c = 1:size(X,2)
%         I(r,c) = sin(X(r,c));
%     end
% end



%% render image
figure(1);
colormap(jet);
pcolor(I);
shading interp;
axis image;
axis off;