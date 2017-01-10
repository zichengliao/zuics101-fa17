%% Compose a function `quake` which accepts as parameters a list of time
%  lengths `spans` and a list of corresponding standard deviations `stds`.
%
%  The function should return an array of random earthquake data as a row
%  of time points and a row of generated measurements.
%
function [ quakedata ] = quake( spans, stds )
    % expand spans and stds into an array of standard deviations
    stdev = [];
    for i = 1:size(spans,2)
        new_array = ones(1,spans(i)) * stds(i);
        stdev = cat(2, stdev, new_array);
    end
    
    % generate random data by specified standard deviations
    quakedata = zeros(2, sum(spans));
    % YOU WRITE THIS CODE
    % set the first row to the range, [1 2 3 ... sum(spans)] using MATLAB
    quakedata(1,:) = 1:sum(spans); %YOU WRITE THIS CODE
    
    % generate the quake data based on standard deviation
    for j = 1:size(data,2)
        quakedata(2,j) = stdev(j) * randn();
    end
end