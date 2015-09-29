%wrong due to imprecision issues
m = 0;
format compact
format long g
for a = 99
    for b = 95
        v = a.^b;
        v = num2str(v,1000);
        s = 0;
        for j = 1:length(v)
            s = s + str2num(v(j));
        if s > m
            m = s;
            m_a = a;
            m_b = b;
            m_v = str2num(v);
    %        l = [a, b, str2num(v), s]
        end
        end
    end
end
l = [m_a, m_b, m_v, m]