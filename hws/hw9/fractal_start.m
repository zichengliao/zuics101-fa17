function fractal_start
    hm = figure(1);
    title('Mandelbrot set (pick a point to initialize Julia set)');
    axis off;
    hold on;
    hj = figure(2);
    title('Julia set (pick two corners to zoom in; double click to return to Mandelbrot set)');
    axis off;
    hold on;
    
    set(hm, 'Position', [100,100, 800,800]);
    set(hj, 'Position', [900,100, 800,800]);

    mXr = [-2.0,.5];
    mYr = [-1.25,1.25];
    n = 400;
    flag = true;
    set(hm, 'visible', 'on');
    Mandelbrot_plot(mXr, mYr, n);
    while true
        if flag
            c = 0.2826 + 0.0103*1i;
            flag = false;
        else
            [x,y] = ginput(1);
            c =  mXr(1) + x/400*(mXr(2)-mXr(1)) +(mYr(1)+y/400*(mYr(2)-mYr(1)))*1i;
        end
        
        jXr = [-2,2];
        jYr = [-2,2];    
        set(hj, 'visible', 'on');
        while true
            Julia_plot(c, jXr, jYr, n);
            [x, y] = ginput(2);
            if max(x) - min(x) < 1e-7
                break
            end
            jXr = [jXr(1) + x(1)/400*(jXr(2)-jXr(1)), jXr(1) + x(2)/400*(jXr(2)-jXr(1))];
            jYr = [jYr(1) + y(1)/400*(jYr(2)-jYr(1)), jYr(1) + y(2)/400*(jYr(2)-jYr(1))];
            jXr = sort(jXr);
            jYr = sort(jYr);
        end
        set(hm, 'visible', 'on');
    end
end

function Mandelbrot_plot(Xr, Yr, n)
    xs = linspace(Xr(1,1),Xr(1,2),n);
    ys = linspace(Yr(1,1),Yr(1,2),n);
    [X,Y] = meshgrid(xs,ys);
    W = zeros(size(X));
    for i = 1:size(X,1)
        for j = 1:size(X,2)
            W(i,j) = Mandelbrot(X(i,j)+Y(i,j)*1i);
        end
    end
    
    %render Mandelbrot set
    colormap(jet);
    pcolor(W);
    shading interp;
    axis image;
    axis off;
end

function it = Mandelbrot(c)
    it = 0;
    z = c;
    while it < 100
        if abs(z) > 2
            return;
        end
        z = z^2 + c;
        it = it + 1;
    end
end

function Julia_plot(c, jXr, jYr, n)
    xs = linspace(jXr(1,1),jXr(1,2),n);
    ys = linspace(jYr(1,1),jYr(1,2),n);
    [X,Y] = meshgrid(xs,ys);
    W = zeros(size(X));
    for i = 1:size(X,1)
        for j = 1:size(X,2)
            W(i,j) = Julia(X(i,j)+Y(i,j)*1i,c); 
        end
    end
    
    %render Julia set
    colormap(jet);
    pcolor(W);
    shading interp;
    axis image;
    axis off;
end

function it = Julia(z,c)
    it = 0;
    while it < 100
        if abs(z) > 2
            return;
        end
        z = z^2 + c;
        it = it + 1;
    end
end