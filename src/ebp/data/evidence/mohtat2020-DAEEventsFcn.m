% % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % %  
% MPMe (c) by Peyman Mohtat, Jason B. Siegel, Anna G. Stefanopoulou       	%
%                                                                           %
% MPMe is licensed under a                                                  %
% Creative Commons Attribution 4.0 License.                                 %
% see <http://creativecommons.org/licenses/by/4.0/>,                        %
% which permits unrestricted reuse of the work in any medium, provided      %
% the original work is properly cited.                                      %
% [DOI: 10.1149/1945-7111/aba5d1]                                           %
%                                                                           %
% The modeling work in this material was funded by                          %
% the National Science Foundation under grant No. 1 762 247.                %
% The experimental work in this material was thanks to the support of       % 
% the Automotive Research Center (ARC) in accordance with                   %
% Cooperative Agreement W56HZV-14-2-0001 U.S. Army CCDC GVSC.               %
%                                                                           %
% % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % %

%%  SPMEvents Function
% This function is used to stop integration when the system states go out of 
% bounds. It is to be used with Events option in ode15s
% 
% 

function [position,isterminal,direction] = DAEEventsFcn(t,y,CC)
global Vt
%% Surface concentration
% $x_{0,s}$, $y_{0,s}$, $y_{1,s}$are the states we are restricting. 
% 
% The constraints are $0<y_{i,s} <1$ and $0<x_{0,s} <1$. These constraints 
% are given in *position* vector.
% 
% The *isterminal* vector gives the instruction to halt integration.
% 
% The *direction* vector is a zero vector (default) if all zeros are to located 
% i.e. the zero is approached in both directions.

x_0s=y(  (CC.nr+1) ); 
x_1s=y(2*(CC.nr+1) );
x_2s=y(3*(CC.nr+1) );
x_3s=y(4*(CC.nr+1) );
x_4s=y(5*(CC.nr+1) );

y_0s=y(6*(CC.nr+1) );

position = [x_0s;x_0s-1;x_1s;x_1s-1;x_2s;x_2s-1;x_3s;x_3s-1;x_4s;x_4s-1;y_0s-0.0335;y_0s-1;Vt-2.7;Vt-4.2];
isterminal = [1; 1; 1; 1; 1; 1; 1; 1; 1; 1; 1; 1;1 ;1];  % Halt integration 
direction = [0;0;0;0;0;0;0;0;0;0;0;0;0;0];   % The zero can be approached from either direction
end