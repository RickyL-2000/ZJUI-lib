function [check] = checkLoss(grid)
    if max(max(grid)) <= 0
        check = 1;
    else
        check = 0;
    end
end