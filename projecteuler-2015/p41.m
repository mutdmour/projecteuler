p = primes(8507264931);
p = fliplr(p);
FID = fopen('p41_primes.txt', 'w');
fprintf(FID, '%d \n', p);
fclose(FID);
%for i = length(p):-1:1
%        if pandigital(i) == 1
%            i
%            break
%        end
%end