%% set parameters
alpha = 0.1;
tmax = 0.5;     % maximum time (s)
length = 3.0;   % length of material
dx = 0.2;       % mesh spacing
dt = 0.01;      % time step (s)

%% data storage initialization
t = 0:dt:tmax;                  % (s)
x = 0:dx:length;                % (m)
u = zeros(numel(t), numel(x));  % Kelvin

%% set initial condition
% a sine wave:
%u(1,:) = (sin(pi*((1:numel(x))*dx)/length)).^2;
% a square wave:
u(1,x>=1&x<=2) = 353.15;         % Kelvin (= 80 deg C)

r = alpha * dt / (dx^2);
s = 1 - 2*r;

%% loop through time steps
for i = 2:1:numel(t)
    for j = 2:1:(numel(x)-1)
       u(i,j) = r*u(i-1,j-1) + s*u(i-1,j) + r*u(i-1,j+1);
    end
end

%% various results plots
plot( x,u );
plot( x(1,:), u(1,:) );
%contourf( x,t,u );
