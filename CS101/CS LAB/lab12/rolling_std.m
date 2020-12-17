%% Compose a function rolling_std which accepts as parameters an array
%  called `data` containing a row of time values and a row of measurements
%  and a window size `n`.
%
%  The function should return the resulting array of time points and
%  calculated rolling-window standard deviations.
%
function [ stds ] = rolling_std( data, n )
    % test that the input is valid
    assert(n > 0,         'n should be positive.');
    assert(~mod(n,1),     'n should be an integer.');
    assert(~(mod(n,2)-1), 'n should be odd.');
    
    % YOU WRITE THIS CODE
    % It should be a straightforward modification of `rolling_mean`, using
    % the MATLAB standard deviation function.  To find this, use the `f_x`
    % button at the left of the prompt in the Command Window in MATLAB.
    % get range "stencil"---how far forward and back to include values
    rng = floor(n/2);
    
    % calculate the rolling std
    stds = zeros(size(data));
    stds(1,:) = data(1,:);  % copy the x-values which is the time values
    for i = 1:size(data,2)  % loop over all values in the array
        % If the stencil doesn't apply, then set the value to NaN.
        if i < rng+1 || i > (size(data,2)-rng)
            stds(2,i) = NaN;
            continue;
        end
        
        stds(2,i) = std(data(2,(i-rng):(i+rng)));
    end
end