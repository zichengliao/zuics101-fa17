%% Compose a function rolling_mean which accepts as parameters an array
%  called `data` containing a row of time values and a row of rolling_mean 
%  values
%
%  The function should return the resulting array of time points and
%  calculated rolling-window means.
%
function [ means ] = rolling_mean( data, n )
    % test that the input is valid
    assert(n > 0,         'n should be positive.');
    assert(~mod(n,1),     'n should be an integer.');
    assert(~(mod(n,2)-1), 'n should be odd.');
    
    % get "stencil"---how far forward and back to include values
    rng = floor(n/2);
    
    % calculate the rolling mean
    means = zeros(size(data));
    means(1,:) = data(1,:);  % copy the x-values
    for i = 1:size(data,2)  % loop over all values in the array
        % If the stencil doesn't apply, then set the mean value to NaN.
        if i < rng+1 || i > (size(data,2)-rng)
            means(2,i) = NaN;
        else
            %% YOU WRITE THIS CODE
            means(2,i) = mean(data(2, i-rng:i+rng));
        end
    end
end