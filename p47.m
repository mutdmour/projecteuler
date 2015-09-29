p = primes(200000);
i = 1;
z = 0;
while z == 0
    i = i + 1;
    if primefac(i, p) == 4
        if primefac(i+1, p) == 4
            if primefac(i+2, p) == 4
                if primefac(i+3, p) == 4
                    z = 1;
                    i
                end
            end
        end
    end
end

   