poll = csvread('brexit.csv');
% poll is a matrix. 
% In matlab, you can use poll = importdata(’brexit.csv’);
% Then change below poll to be poll.data

n = numel(poll(:,3));
mean_l = rolling_mean( poll(:,3)', 25 );
stdev_l = rolling_std( poll(:,3)', 25 );
std_lp = mean_l+stdev_l;
std_lm = mean_l-stdev_l;
hold on
plot( poll(:,3), 'ro' );
plot( 0:n-1,mean_l, 'r-' );
plot( 0:n-1,std_lp, 'r--' );
plot( 0:n-1,std_lm, 'r--' );

mean_r = rolling_mean( poll(:,2)', 25 );
stdev_r = rolling_std( poll(:,2)', 25 );
std_rp = mean_r+stdev_r;
std_rm = mean_r-stdev_r;
plot( poll(:,2), 'bo' );
plot( 0:n-1,mean_r, 'b-' );
plot( 0:n-1,std_rp, 'b--' );
plot( 0:n-1,std_rm, 'b--' );

mean_u = rolling_mean( poll(:,4)', 25 );
stdev_u = rolling_std( poll(:,4)', 25 );
std_up = mean_u+stdev_u;
std_um = mean_u-stdev_u;
plot( poll(:,4), 'ko' );
plot( 0:n-1,mean_u, 'k-' );
plot( 0:n-1,std_up, 'k--' );
plot( 0:n-1,std_um, 'k--' );
