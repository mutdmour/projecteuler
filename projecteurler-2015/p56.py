m = 0
for a in range(1,100):
    for b in range(1,100):
        v = a**b
        v = str(v)
        s = 0
        for j in v:
            s = s + int(j)
        if s > m:
            m = s
            m_a, m_b, m_v = a, b, int(v)
print(m_a, m_b, m_v, m)
