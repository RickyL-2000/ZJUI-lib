function [ result ] = isclose(a, b)
    rel_tol = 1e-6;
    result = abs(a - b) <= max(rel_tol * max(abs(a), abs(b)));
end