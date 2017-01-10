%% Compose a function distance which accepts as parameters an array called
%  data containing a row of time values and a row of measurements
%
%  The function should return the calculated distance in miles.
%
function [ dist ] = distance( data )
    % calculate the rolling-window standard deviations
    %% YOU WRITE THIS CODE
    % store the result of the five-point rolling standard deviation in
    % the array `stds`
    stds = rolling_std(data, 5);
    
    % find the point P
    threshold_values = stds(2,:)>5;  % you should look at the form of std>10
    P = find(threshold_values,1);
    
    % find the point S
    % by visual inspection, the plot goes to zero between indexes 120 to
    % 150, so use 150 as the starting point to search forward for S
    %% YOU WRITE THIS CODE
    S = find(threshold_values(150:end),1) + 149;
    
    % calculate the difference between P and S (in seconds)
    dist = 5.7*(S-P); % YOU WRITE THIS CODE
end