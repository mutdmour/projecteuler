%too damn slow
format short
per = 100;
s = 5;
while s<10
    A
    s=s+2;
    A = zeros(s,s);
    r = s;
    c = s;
    k = s^2;
    i = 0;
    while k ~= 1
        for i = k:-1:1
            if c > 0
                if A(r,c) == 0
                    A(r,c) = i;
                    c = c - 1;
                else
                    k = i;
                    break
                end
            else
                k = i;
                break
            end
        end
        c = c + 1;
        r = r + 1;
        for i = k:-1:1
            if r < s+1
                if A(r,c) == 0
                    A(r,c) = i;
                    r = r + 1;
                else
                    k = i;
                    break
                end
            else
                k = i;
                break
            end
        end
        r = r - 1;
        c = c + 1;
        for i = k:-1:1
            if c < s+1
                if A(r,c) == 0
                    A(r,c) = i;
                    c = c + 1;
                else
                    k = i;
                    break
                end
            else
                k = i;
                break
            end
        end
        c = c - 1;
        r = r - 1;
        for i = k:-1:1
            if r > 0
                if A(r,c) == 0
                    A(r,c) = i;
                    r = r - 1;
                else
                    k = i;
                    break
                end
            else
                k = i;
                break
            end
        end
        r = r + 1;
        c = c - 1;
    end
    A(find(A==0))=1;

   % n = 0;
   % for i = 1:s
    %    if isprime(A(i,i))==1
     %       n = n + 1;
      %  end
  %  end
  %  j = s+1;
  %  for i = 1:s
   %     j = j-1;
    %    if isprime(A(j,i))==1
     %       n = n + 1;
 %       end
  %  end

 %   per = n / (s*2-1) * 100;
%    l = [s per]
end
s
