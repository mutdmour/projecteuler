tot = 0
for i = 1:2
    k = sqrt(i)
    if floor(k) ~= k
        k = num2str(k,200)
        k = k(3:length(k))
        for j = 1:100
            tot = tot + str2double(k(j));
        end
    end
end