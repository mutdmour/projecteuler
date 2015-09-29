function z = p60_test(a,b,p)
r = str2double(strcat(num2str(a),num2str(b)));
s = str2double(strcat(num2str(b),num2str(a)));
if r > p(length(p))
    if isprime(r) == 0
        z = 0;
        return
    end
elseif ismember(r, p) == 0
    z = 0;
    return
end
if s > p(length(p))
    if isprime(s) == 0
        z = 0;
        return
    end
elseif ismember(s,p) == 0
    z = 0;
    return
end
z = 1;
end
