clear;
f_x = @(theta, u, v) (u - cos(theta)) / ((u - cos(theta)).^2 + (v - sin(theta)).^2).^(3/2);
f_y = @(theta, u, v) (v - sin(theta)) / ((v - sin(theta)).^2 + (v - sin(theta)).^2).^(3/2);
epsilon = 8.854e-12;
[x, y] = meshgrid(-5:0.1:5, -5:0.1:5);
E_x = zeros(5/0.1+1, 5/0.1+1);
E_y = zeros(5/0.1+1, 5/0.1+1);
for i = 1:(5/0.01+1)
   for j = 1:(5/0.01+1)
      % ff_x = @(theta) f_x(x(i), y(j), theta);
      % ff_y = @(theta) f_y(x(i), y(j), theta);
      % f_x = @(theta) (x - cos(theta)) / ((x - cos(theta)).^2 + (y - sin(theta)).^2).^(3/2);
      % f_y = @(theta) (x - cos(theta)) / ((y - sin(theta)).^2 + (y - sin(theta)).^2).^(3/2);
      u = x(i);
      v = y(j);
      E_x(i,j) = quad(f_x, 0, 2*pi, [], [], u, v);
      E_y(i,j) = quad(f_y, 0, 2*pi, [], [], u, v);
   end
end
% E_x = arrayfun(@(u)arrayfun(@(v) quad(f_x, 0, 2*pi, [], [], u, v), y), x);

% E_x = integral(f_x, 0, 2*pi);
% E_y = integral(f_y, 0, 2*pi);