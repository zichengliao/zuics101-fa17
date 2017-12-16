function Iu = img_upsample(I)
    I = im2double(I);   %converts values to 0-1
    [h, w, ~] = size(I);
    h2 = h*2 - 1;  %double the size of the input image
    w2 = w*2 - 1;
    Iu = zeros([h2, w2, size(I,3)]);
    
    %create the x/y coordinates for the new samples
    ys = linspace(1, h, h2);  
    xs = linspace(1, w, w2);
    for i = 1:h2
        for j = 1:w2
            y = ys(i); x = xs(j);
            Iu(i,j,:) = 0.25*I(floor(y),floor(x),:)+...
                        0.25*I(floor(y),ceil(x),:)+...
                        0.25*I(ceil(y),floor(x),:)+...
                        0.25*I(ceil(y),ceil(x),:);
        end
    end
        
end