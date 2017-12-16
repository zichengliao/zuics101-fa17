function myfractal_plot   
    % a simple UI for Mandelbrot/Julia fractal set plot
    hm = figure(1);
    title('Mandelbrot set (pick a point to initialize a Julia set)');
    axis off;
    hold on;
    hj = figure(2);
    title('Julia set (pick two corners to zoom in; or double click to stop)');
    axis off;
    hold on;
    
    set(hm, 'Position', [100,100, 400,400]);
    set(hj, 'Position', [500,100, 400,400]);
    mXr = [-2.0, .5];
    mYr = [-1.25, 1.25];
    k = 400;
    figure(1);
    Mandelbrot_plot(mXr, mYr, k);
    while true
        disp('pick a point to initialize a Julia set');
        [x,y] = ginput(1);
        c =  mXr(1) + x/400*(mXr(2)-mXr(1)) +(mYr(1)+y/400*(mYr(2)-mYr(1)))*1i

        jXr = [-2,2];
        jYr = [-2,2];    
        figure(2);
        while true
            Julia_plot(c, jXr, jYr, k);
            disp('zoom-in by choosing two corners of a bounding box\or double-click to stop');
            [x, y] = ginput(2);
            if max(x) - min(x) < 1e-7
                break
            end
            jXr = [jXr(1) + x(1)/k*(jXr(2)-jXr(1)), jXr(1) + x(2)/k*(jXr(2)-jXr(1))];
            jYr = [jYr(1) + y(1)/k*(jYr(2)-jYr(1)), jYr(1) + y(2)/k*(jYr(2)-jYr(1))];
            jXr = sort(jXr);
            jYr = sort(jYr);
            disp([jXr, jYr]);
        end
        figure(1);
    end
end

%%
function Mandelbrot_plot(Xr, Yr, k)
    xs = linspace(Xr(1,1),Xr(1,2),k);
    ys = linspace(Yr(1,1),Yr(1,2),k);
    [X, Y] = meshgrid(xs,ys);
    I = zeros(size(X));  %an image of all gray, nothing in it yet
    
    % create the image for the Mandelbrot set
    %fill in your code here
    %
    %
    %
    %fill in your code here
    for i = 1:size(X,1)
        for j = 1:size(X,2)
            I(i,j) = Mandelbrot(X(i,j)+Y(i,j)*1i);
        end
    end
    
    % plot the Mandelbrot set
    colormap(jet);
    pcolor(I);
    shading interp;
    axis image;
    axis off;
end

function n = Mandelbrot(c)
    n = 0;
    z = 0;
    while n < 100
        if abs(z) > 2
            return;
        end
        z = z^2 + c;
        n = n + 1;
    end
end

%%
function Julia_plot(c, Xr, Yr, k)
    xs = linspace(Xr(1,1),Xr(1,2),k);
    ys = linspace(Yr(1,1),Yr(1,2),k);
    [X,Y] = meshgrid(xs,ys);
    I = zeros(size(X));  %an image of all gray, nothing in it yet
    
    % create the image for the Julia set
    %fill in your code here
    %
    %
    %
    %fill in your code here
    for i = 1:size(X,1)
        for j = 1:size(X,2)
            I(i,j) = Julia(X(i,j)+Y(i,j)*1i,c); 
        end
    end
    
    % plot the Julia set
    colormap(jet);
    pcolor(I);
    shading interp;
    axis image;
    axis off;
end


function n = Julia(z,c)
    n = 0;
    while n < 100
        if abs(z) > 2
            return;
        end
        z = z^2 + c;
        n = n + 1;
    end
end