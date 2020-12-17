function [zSorted] = complexSort(z)
  zSorted = [];
  Z = [z;(real(z).*real(z) + imag(z).*imag(z))];
  Z = sortrows(Z',2)';
  for i = size(Z,2):-1:1
      zSorted = [zSorted,Z(1,i)];
  end
end