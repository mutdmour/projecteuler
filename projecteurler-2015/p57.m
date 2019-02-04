%problems with exploring the den and num
format rat
n = 0;
v = 1;
c = 0;
for i = 1:8
    v = v - 1;
    while n ~= i
        n = n + 1;
        v = 1/(2 + v);
    end
    v = 1 + v
%    [n,d] = numden(sym(v))
 %   if length(num2str(n)) > length(num2str(d))
  %      c = c + 1;
   % end
    %m = c
end