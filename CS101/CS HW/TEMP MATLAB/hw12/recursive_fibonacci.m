function [F] = recursive_fibonacci(N) 
  if N == 1
      F = 1;
      save recursion_check.dat F -ascii -append;
  elseif N == 2
      F = 1;
      save recursion_check.dat F -ascii -append;
      %save recursion_check.dat F -ascii -append
  else
      F = recursive_fibonacci(N-1) + recursive_fibonacci(N-2)
      save recursion_check.dat F -ascii -append;
  end
end