function [ R2 ] = r_sqr( polycoefs, data )
  x = data(:,1);
  y = data(:,2);
  ym = polyval(polycoefs,x);
  resid = ym - y;
  svar = y - mean(y);
  sstot = sum(svar.^2);
  sserr = sum(resid.^2);
  R2 = 1 - sserr/sstot;
end