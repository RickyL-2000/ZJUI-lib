function [mgrid,hit] = evaluateShot(grid,shotX,shotY)
    if grid(shotX,shotY) > 0
        hit = 1;
    else
        hit = 0;
    end
    grid(shotX,shotY) = -1;
    mgrid = grid;
end