function dN = decay_chain(t,N0)
% We expect that N0 is a three-element vector.

% Half-lives / s
t_A = 1;
t_B = 20;

% Decay constants / s^-1
l_A = log(2)/t_A;
l_B = log(2)/t_B;

% Equation matrix
eqns = ...
    [-l_A 0 0;
     l_A -l_B 0;
     0 l_B 0];
 
 % Differential change from N0
 dN = eqns*N0;
 
 
 