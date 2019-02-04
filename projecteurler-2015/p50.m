p = primes(997651);
m = 0;  
for i = length(p):-1:1
    for j = 1:length(p)-1
        n = p(i);
        k = j;
        l = [];
        c = 1;
        while n ~= 0 && k > 0 && n > -1
            n = n - p(k);
            l(c) = p(k);
            k = k + 1;
            c = c + 1;
        end
        if n == 0
            if length(l) > m
                m_v = p(i)
                m_l = l;
                m = length(l)
            end
            break
        end
    end
    break
end
m_v
%m_l   