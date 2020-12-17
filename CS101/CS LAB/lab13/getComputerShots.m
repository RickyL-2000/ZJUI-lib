function [shotX,shotY] = getComputerShots(computerShots)
    if ismember(2,computerShots)
        [x,y] = find(computerShots == 2);
        ran1 = randi(numel(x));
        xc = x(ran1);
        yc = y(ran1);
        if xc == 1 && yc ~= 1 && yc ~= 5
            xchosen = [xc+1 xc xc];
            ychosen = [yc yc-1 yc+1];
        elseif xc == 5 && yc ~= 1 && yc ~= 5
            xchosen = [xc-1 xc xc];
            ychosen = [yc-1 yc+1 yc];
        elseif yc == 1 && xc ~= 1 && xc ~= 5
            xchosen = [xc-1 xc+1 xc];
            ychosen = [yc yc yc+1];
        elseif yc == 5 && xc ~=1 && xc ~= 5
            xchosen = [xc-1 xc+1 xc];
            ychosen = [yc yc yc-1];
        elseif xc == 1 && yc == 1
            xchosen = [2 1];
            ychosen = [1 2];
        elseif xc == 1 && yc == 5
            xchosen = [2 1];
            ychosen = [5 4];
        elseif xc == 5 && yc == 1
            xchosen = [4 5];
            ychosen = [1 2];
        elseif xc == 5 && yc == 5
            xchosen = [4 5];
            ychosen = [5 4];
        else
            xchosen = [xc-1 xc+1 xc xc];
            ychosen = [yc yc yc-1 yc+1];
        end
        xfinal = [];
        yfinal = [];
        for i = 1:1:numel(xchosen)
            for j = 1:1:numel(ychosen)
                if computerShots(xchosen(i),ychosen(j)) == 0
                    xfinal = [xfinal xchosen(i)];
                    yfinal = [yfinal ychosen(j)];
                end
            end
        end
        ran2 = randi(numel(xfinal));
        shotX = xfinal(ran2);
        shotY = yfinal(ran2);
    else
        xselected = randi(5);
        yselected = randi(5);
        while computerShots(xselected,yselected) ~= 0
            xselected = randi(5);
            yselected = randi(5);
        end
        shotX = xselected;
        shotY = yselected;
    end
end
       