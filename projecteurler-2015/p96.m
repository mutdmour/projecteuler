file = load('p96_sudoku_modified.txt');
n = -8;
tot = 0;
for i = 1:50
    n = n+9;
    G = file(n:n+8, 1:9);
    G = p96_sudoku(G);
    v = str2double(strcat(num2str(G(1,1)), num2str(G(1,2)), num2str(G(1,3))));
    tot = tot + v;
end
tot