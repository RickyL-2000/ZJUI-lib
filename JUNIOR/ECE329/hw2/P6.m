[x, y] = meshgrid(-2:1:2, -2:1:2);
% u = x;
u = y;
v = ones(5);
quiver(x, y, u, v, 1);