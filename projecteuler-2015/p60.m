p = primes(10000);
n = 5
for i = 1:length(p)
    l = [];
    for j = 1:i-1
    %    y = [p(i), p(j), p60_test(p(i),p(j))]
        if p60_test(p(i),p(j), p) == 1
            z = 1;
            for k = 1:length(l)
                if p60_test(p(j), l(k),p) == 0
                    z = 0;
                    break
                end
            end
            if z == 1
                l(length(l)+1) = p(j);
            end
        end
    end
    l(length(l)+1) = p(i);
    if length(l) == n
        l
        tot = 0;
        for j = 1:length(l)
            tot = tot + l(j);
        end
        tot
        break
    end
end

    
            