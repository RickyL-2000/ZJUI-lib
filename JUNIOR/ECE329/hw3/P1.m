[x, y] = meshgrid(-2:1:2, -2:1:2);
u = x / 4 / pi ./ (x.*x + y.*y);
u(3, 3) = 0;
v = y / 4 / pi ./ (x.*x + y.*y);
v(3, 3) = 0;
quiver(x, y, u, v, 0.6);
