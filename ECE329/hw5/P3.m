clear;
[x, z] = meshgrid(-5:0.1:5, -5:0.1:5);
Bx = zeros(101, 101);
Bz = zeros(101, 101);
delta_l = 2 / 20;

for yy = -1.0 : delta_l : (1.0 - delta_l)
    Bx = Bx + delta_l .* z ./ ((x - 1).^2 + yy.^2 + z.^2).^1.5;
    Bz = Bz - delta_l .* (x - 1) ./ ((x - 1).^2 + yy.^2 + z.^2).^1.5;
    Bx = Bx - delta_l .* z ./ ((x + 1).^2 + yy.^2 + z.^2).^1.5;
    Bz = Bz + delta_l .* (x + 1) ./ ((x + 1).^2 + yy.^2 + z.^2).^1.5;
end

for xx = -1.0 : delta_l : (1.0 - delta_l)
    Bz = Bz + delta_l ./ ((xx - x).^2 + 1 + z.^2).^1.5;
    Bz = Bz + delta_l ./ ((xx - x).^2 + 1 + z.^2).^1.5;
end

Bx(51, 41) = 0.0;
Bx(51, 61) = 0.0;
Bz(51, 41) = 0.0;
Bz(51, 61) = 0.0;

quiver(x, z, Bx, Bz, 3)