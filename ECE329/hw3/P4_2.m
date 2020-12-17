clear;
epsilon = 8.854e-12;
[x, y] = meshgrid(-5:0.01:5, -5:0.01:5);
V_i = @ (theta, x, y) 1 ./ ((x-cos(theta)).^2 + (y-sin(theta)).^2).^0.5 / (2 * pi * 4 * pi * epsilon);
V = integral(@(theta) V_i(theta, x, y), 0, 2*pi, 'RelTol', 1e-10, 'ArrayValued', true);
contour(x, y, V*1e-9, 'ShowText', 'on');

clear;
epsilon = 8.854e-12;
[x, z] = meshgrid(-5:0.01:5, -5:0.01:5);
V_i = @ (theta, x, z) 1 ./ ((x-cos(theta)).^2 + (sin(theta)).^2 + z.^2).^0.5 / (2 * pi * 4 * pi * epsilon);
V = integral(@(theta) V_i(theta, x, z), 0, 2*pi, 'RelTol', 1e-10, 'ArrayValued', true);
contour(x, z, V*1e-9, 'ShowText', 'on');