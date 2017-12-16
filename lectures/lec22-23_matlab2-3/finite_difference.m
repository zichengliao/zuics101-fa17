a = -9.8;
tmax = 0.5;     % maximum time (s)
dt = 0.01;      % time step (s)

%% data initialization
t = 0:dt:tmax;                % (s)
v = zeros(size(t));           % (m/s)
y = zeros(size(t));           % (m)
y(1) = 1;

%%
for i = 2:length(t)   %or numel
     v(i) = v(i-1) + a*dt;
     y(i) = y(i-1) + v(i-1)*dt;
end