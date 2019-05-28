function [mgrid] = evaluateGuess(grid,shotX,shotY,hit)
    if hit == 1
        grid(shotX,shotY) = 2;
        mgrid = grid;
    elseif hit == 0
        grid(shotX,shotY) = 1;
        mgrid = grid;
    end
end