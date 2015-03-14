top = 0;
bottom = 600;
x = 400;
for i = top:bottom
  y(i+1) = i;
  test(i+1) = 8*sin(y(i+1)*0.1);
  x(i+2) = test((i+1))+x(i+1);
end

plot(x(1:end-1),y)
axis([0 800 0 600]) 