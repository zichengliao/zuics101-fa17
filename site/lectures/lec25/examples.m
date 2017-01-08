x = linspace( -1,1,11 );
y = [ 0.038 0.058 0.1 0.2 0.5 1 0.5 0.2 0.1 0.058 0.038 ];

coefs = polyfit( x,y,2 );
yfit = polyval( coefs,x );

plot( x,y,'.', x,yfit,'-' );

%%

x = linspace( -1,1,11 );
y = [ 0.038 0.058 0.1 0.2 0.5 1 0.5 0.2 0.1 0.058 0.038 ];

coefs = polyfit( x,y,8 );
xfit = linspace( -1.5,1.5,101 );
yfit = polyval( coefs,xfit );

plot( x,y,'.', xfit,yfit,'-' );
ylim( [-1 1] );

%%

x = linspace( 0,1,6 );
y = [ 1 0.5 0.2 0.1 0.058 0.038 ];

coefs = polyfit( x,y,3 );
yfit = polyval( coefs,x );

plot( x,y,'.', x,yfit,'-' );

%%

poll = csvread('brexit.csv');
% poll is a matrix. 
% In matlab, you can use poll = importdata(’brexit.csv’);
% Then change below poll to be poll.data

n = numel(poll(:,3));
mean_l = rolling_mean( poll(:,3)', 25 );

fit_poly_l = polyfit( 13:167,mean_l(13:167),19 );  %why?
poly_l = polyval( fit_poly_l,1:n );

hold on
plot( poll(:,3), 'ro' );
plot( 1:n,mean_l, 'r-' );
plot( 1:n,poly_l, 'r:' );

%%

x = linspace( -2*pi,2*pi,21 );
y = sin( x );

figure; hold on;
plot( x,y,'.' );
for i = 2:9
    coefs = polyfit( x,y,i );
    xfit = linspace( -2*pi,2*pi,101 );
    yfit = polyval( coefs,xfit );
    plot( xfit,yfit,'-' );
end

