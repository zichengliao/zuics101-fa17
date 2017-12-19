%% import data
poll = importdata('brexit.csv');


%% population who choose to leave
n = numel(poll.data(:,3));
mean_l = rolling_mean( poll.data(:,3)', 25 );
stdev_l = rolling_std( poll.data(:,3)', 25 );
std_lp = mean_l+stdev_l;
std_lm = mean_l-stdev_l;
figure; hold on;
plot( poll.data(:,3), 'rx' );
plot( 0:n-1,mean_l, 'r-', 'linewidth',3 );
plot( 0:n-1,std_lp, 'r--', 'linewidth',2 );
plot( 0:n-1,std_lm, 'r--', 'linewidth',2 );

%% population who choose to stay
mean_r = rolling_mean( poll.data(:,2)', 25 );
stdev_r = rolling_std( poll.data(:,2)', 25 );
std_rp = mean_r+stdev_r;
std_rm = mean_r-stdev_r;
plot( poll.data(:,2), 'bo' );
plot( 0:n-1,mean_r, 'b-', 'linewidth',3 );
plot( 0:n-1,std_rp, 'b--', 'linewidth',2 );
plot( 0:n-1,std_rm, 'b--', 'linewidth',2 );

%% plot the rest of the data (undecided)
plot( poll.data(:,4), 'ks');
