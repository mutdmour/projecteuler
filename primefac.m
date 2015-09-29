function n = primefac(k, p)
    n = 0;
    for j = 1:length(p)
        f = p(j);
        if f > k
            break
        end
        if rem(k, f) == 0
            k = k / f;
            n = n + 1;
            while rem(k,f) == 0
                k = k / f;
            end
        end
        if k == 1
            break
        end
    end
end

            