function bool = pandigital(n)
n = num2str(n);
for i = 1:length(n)
    j = n(1);
    n = n(2:length(n));
    for k = length(n):-1:1
        if j == n(k)
            bool = 0;
            return
        end
    end
end 
bool = 1;
return

end
