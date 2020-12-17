clear;
epsilon = 8.854e-12;
[x, y] = meshgrid(-5:0.01:5, -5:0.01:5);
V = -log(sqrt(x.*x + y.*y)) / 2 / pi;
S = -10:0.01:0;
contour(x, y, V, S)