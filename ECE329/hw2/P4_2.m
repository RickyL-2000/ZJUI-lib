epsilon = 8.854e-12;
[x, y] = meshgrid(-2.5:0.1:2.5, -2.5:0.1:2.5);
u = (1 ./ (x.*x + (y+1).*(y+1)) + 1 ./ (x.*x + (y-1).*(y-1))) .* x / 4 / pi / epsilon;
v = ((y+1) ./ (x.*x+(y+1).*(y+1)) + (y-1) ./ (x.*x+(y-1).*(y-1))) / 4 / pi / epsilon;
quiver(x, y, u, v, 2)