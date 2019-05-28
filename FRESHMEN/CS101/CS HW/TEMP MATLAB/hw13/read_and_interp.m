function [ t ] = read_and_interp( s )
    t = [];
    a = size(s);
    for i = 1:a(1)
        if s(i,2:end) == '9999'
            t = [t;(str2num(s(i-1,2:end))+str2num(s(i+1,2:end)))/2];
        else
            t = [t;str2num(s(i,2:end))];
        end
    end
end