function G = p96_sudoku(G)
    w = 0;
    temp = zeros(size(G));
    while ismember(0, G) == 1
        for x = 1:9
            for y = 1:9
                z = 0;
                if G(x,y) == 0
                    l = [];
                    for j = 1:9
                        if length(l) > 2
                            break
                            end
                        if ismember(j, G(x, 1:9)) == 0
                            if ismember(j, G(1:9, y)) == 0
                                if x >= 1 && x <= 3
                                    if y >= 1 && y <= 3
                                        if ismember(j, G(1:3, 1:3))==0
                                            l(length(l)+1) = j;
                                        end
                                    elseif y >= 4 && y <= 6
                                        if ismember(j, G(1:3, 4:6))==0
                                            l(length(l)+1) = j;
                                        end
                                    elseif y >= 7 && y <= 9
                                        if ismember(j, G(1:3, 7:9))==0
                                            l(length(l)+1) = j;
                                        end
                                    end
                                elseif x >= 4 && x <= 6
                                    if y >= 1 && y <= 3
                                        if ismember(j, G(4:6, 1:3))==0
                                            l(length(l)+1) = j;
                                        end
                                    elseif y >= 4 && y <= 6
                                        if ismember(j, G(4:6, 4:6))==0
                                            l(length(l)+1) = j;
                                        end
                                    elseif y >= 7 && y <= 9
                                        if ismember(j, G(4:6, 7:9))==0
                                            l(length(l)+1) = j;
                                        end
                                    end
                                elseif x >= 7 && x <= 9
                                    if y >= 1 && y <= 3
                                        if ismember(j, G(7:9, 1:3))==0
                                            l(length(l)+1) = j;
                                        end
                                    elseif y >= 4 && y <= 6
                                        if ismember(j, G(7:9, 4:6))==0
                                            l(length(l)+1) = j;
                                        end
                                    elseif y >= 7 && y <= 9
                                        if ismember(j, G(7:9, 7:9))==0
                                            l(length(l)+1) = j;
                                        end
                                    end
                                end
                            end
                        end
                    end
                    if isempty(l) == 1
                        return
                    end
                    if length(l) == 1
                        G(x,y) = l(1);
                    end
                    if w == 1 && length(l) == 2
                        rep = G;
                        rep(x,y) = l(1);
                        got = p96_sudoku(rep);
                        if ismember(0, got) == 1
                            rep = G;
                            rep(x,y) = l(2);
                            got = p96_sudoku(rep);  
                            if ismember(0,got) == 1
                                return
                            end
                        end
                        if ismember(0, got) == 0
                            G = got;
                            w = 0;
                        end
                    end
                end
            end
        end
        if temp == G
            w = 1;
        end
        temp = G;
    end
end