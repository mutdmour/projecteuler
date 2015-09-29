s=1001;
A = zeros(s,s);
r = 1;
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
tot = 0;
for i = 1:s
    tot = tot + A(i,i);
end
j = s+1;
for i = 1:s
    j = j - 1;
    tot = tot + A(j,i);
end
tot = tot + 1;
tot