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

%% MPM DAE Solving Function
% This function solves the MPM equations in a Differential Algebraic Equation 
% Solver. 

function [dxdt,SOLNout] = Battery_MPM_Electrolyte_DAE(t,x,CC)
global Vt
%% State definition
% The first 5*(nr+1) states of the x vector are the negative particle SOC's$x_0$  
% at each spacial discretization of the particle. The nr+1th state is the surface 
% concentration.
% 
% The next nr+1 states are the NMC particle SOC's $$y_0$$.
% The next n_nodes are electrolyte concentration
% The next states are jn_0 , jn_1 , jn_2 , and jn_3.
% The next state is T 


x_0 = x(1:(CC.nr+1)); %normalized SOC
x_1 = x(1*(CC.nr+1)+(1:(CC.nr+1))); %normalized SOC
x_2 = x(2*(CC.nr+1)+(1:(CC.nr+1))); %normalized SOC
x_3 = x(3*(CC.nr+1)+(1:(CC.nr+1))); %normalized SOC
x_4 = x(4*(CC.nr+1)+(1:(CC.nr+1))); %normalized SOC

y_0 = x(5*(CC.nr+1)+(1:(CC.nr+1)));

dce = x(6*(CC.nr+1)+(1:(CC.n_nodes)));

jn_0 = x(6*(CC.nr+1)+CC.n_nodes+1);
jn_1 = x(6*(CC.nr+1)+CC.n_nodes+2);
jn_2 = x(6*(CC.nr+1)+CC.n_nodes+3);
jn_3 = x(6*(CC.nr+1)+CC.n_nodes+4);

T = x(6*(CC.nr+1)+CC.n_nodes+5);

ce_aver_n = sum(dce(1:2*CC.nn+1))/(2*CC.nn+1)+CC.ce_init;
ce_aver_p = sum(dce(2*(CC.nn+CC.ns)+1:end))/(2*CC.np+1)+CC.ce_init;
    
%% Input Current Profile

Iapplied=CC.I(t)./CC.A;

%% Charge Conservation
% This is a constraint. The sum of currents of the two particles should be equal 
% to the total current.
% 
% $$$$I\ =\ \sum_{i=1}^{N}{a_{s,i}\delta_nF}j_i$$$$

jn_4 = (Iapplied-jn_0*(CC.as_n_0*CC.del_n*CC.F)-jn_1*(CC.as_n_1*CC.del_n*CC.F)-jn_2*(CC.as_n_2*CC.del_n*CC.F)-jn_3*(CC.as_n_3*CC.del_n*CC.F))/(CC.as_n_4*CC.del_n*CC.F);

jp_0 = -Iapplied./(CC.as_p_0*CC.del_p*CC.F);

%% Exchange Current Density
% $$$$i_{0,i}=k_{0,i}\left(\bar{c_e}\right)^{0.5}\left(c_{s,max,i}-c_{se,i}\right)^{0.5}\left(c_{se,i}\right)^{0.5}$$$$

i0n_0 = CC.k0_n.*CC.F*ce_aver_n.^(0.5)*CC.cs_max_n*(1-x_0(end))^(0.5)*x_0(end)^(0.5);
i0n_1 = CC.k0_n.*CC.F*ce_aver_n.^(0.5)*CC.cs_max_n*(1-x_1(end))^(0.5)*x_1(end)^(0.5);
i0n_2 = CC.k0_n.*CC.F*ce_aver_n.^(0.5)*CC.cs_max_n*(1-x_2(end))^(0.5)*x_2(end)^(0.5);
i0n_3 = CC.k0_n.*CC.F*ce_aver_n.^(0.5)*CC.cs_max_n*(1-x_3(end))^(0.5)*x_3(end)^(0.5);
i0n_4 = CC.k0_n.*CC.F*ce_aver_n.^(0.5)*CC.cs_max_n*(1-x_4(end))^(0.5)*x_4(end)^(0.5);

i0p_0 = CC.k0_p.*CC.F*ce_aver_p.^(0.5)*CC.cs_max_p*(1-y_0(end))^(0.5)*y_0(end)^(0.5);

%% Butler-Volmer Equation
% $$$$j_i =\frac{i_{0,i} }{F}{\left(e^{\frac{\left(1-\alpha \right)F}{RT}\eta_i 
% } -e^{\frac{-\alpha F}{RT}\eta_i } \right)}$$$$
% 
% $$\eta_{p,i}=\frac{RT}{0.5F}\ast\ asinh\left(\frac{Fj_{p,i}}{2i_{0,i}}\right)$$
% 
% Inverting this equation we can solve for the overpotential.

eta_n_0 = (CC.R*CC.T/0.5/CC.F)*asinh(jn_0*CC.F/2/i0n_0);
eta_n_1 = (CC.R*CC.T/0.5/CC.F)*asinh(jn_1*CC.F/2/i0n_1);
eta_n_2 = (CC.R*CC.T/0.5/CC.F)*asinh(jn_2*CC.F/2/i0n_2);
eta_n_3 = (CC.R*CC.T/0.5/CC.F)*asinh(jn_3*CC.F/2/i0n_3);
eta_n_4 = (CC.R*CC.T/0.5/CC.F)*asinh(jn_4*CC.F/2/i0n_4);

eta_p_0 = (CC.R*CC.T/0.5/CC.F)*asinh(jp_0*CC.F/2/i0p_0);

%% Voltage due to Resistance
% $$$$V_{R,i} =k_{t,p} *A*F*j_{p,i}$$$$

Vr_n_0 = (CC.kt_n)*jn_0*CC.F;
Vr_n_1 = (CC.kt_n)*jn_1*CC.F;
Vr_n_2 = (CC.kt_n)*jn_2*CC.F;
Vr_n_3 = (CC.kt_n)*jn_3*CC.F;
Vr_n_4 = (CC.kt_n)*jn_4*CC.F;

Vr_p_0 = (CC.kt_p)*jp_0*CC.F;

SOLNout.Un_0=CC.Un_0(x_0(end));
SOLNout.Un_1=CC.Un_0(x_1(end));
SOLNout.Un_2=CC.Un_0(x_2(end));
SOLNout.Un_3=CC.Un_0(x_3(end));
SOLNout.Un_4=CC.Un_0(x_4(end));

SOLNout.Up_0=CC.Up_0(y_0(end));

SOLNout.Ve_o = -(CC.del_n/(CC.epsilon_e_n^CC.brugg)+2*CC.del_s/(CC.epsilon_e_s^CC.brugg)+CC.del_p/(CC.epsilon_e_p^CC.brugg))*Iapplied/(2*CC.kappa);
SOLNout.Ve_ce = 2*CC.R*CC.T/CC.F*CC.tf*(log(dce(end)+CC.ce_init)-log(dce(1)+CC.ce_init));
    

SOLNout.dUdTn_0=CC.dUdTn_0(x_0(end));
SOLNout.dUdTn_1=CC.dUdTn_0(x_1(end));
SOLNout.dUdTn_2=CC.dUdTn_0(x_2(end));
SOLNout.dUdTn_3=CC.dUdTn_0(x_3(end));
SOLNout.dUdTn_4=CC.dUdTn_0(x_4(end));

SOLNout.dUdTp_0=CC.dUdTp_0(y_0(end));

SOLNout.sumEnergy_n = jn_0*(CC.as_n_0)*(SOLNout.Un_0+Vr_n_0-(T+273.15)*SOLNout.dUdTn_0)+...
                      jn_1*(CC.as_n_1)*(SOLNout.Un_1+Vr_n_1-(T+273.15)*SOLNout.dUdTn_1)+...
                      jn_2*(CC.as_n_2)*(SOLNout.Un_2+Vr_n_2-(T+273.15)*SOLNout.dUdTn_2)+...
                      jn_3*(CC.as_n_3)*(SOLNout.Un_3+Vr_n_3-(T+273.15)*SOLNout.dUdTn_3)+...
                      jn_4*(CC.as_n_4)*(SOLNout.Un_4+Vr_n_4-(T+273.15)*SOLNout.dUdTn_4);
                  
SOLNout.sumEnergy_p = jp_0*(CC.as_p_0)*(SOLNout.Up_0+Vr_p_0-(T+273.15)*SOLNout.dUdTp_0);
                      
%% Terminal Voltage
% $$$$V{\left(t\right)}=\phi_{s,i}^+ {\left(t\right)}-\phi_s^- {\left(t\right)}$$$$   

Vt = (eta_p_0+SOLNout.Up_0+Vr_p_0)-(eta_n_0+SOLNout.Un_0+Vr_n_0)+SOLNout.Ve_o+SOLNout.Ve_ce;

SOLNout.Iapplied=Iapplied;
SOLNout.jn_0=jn_0;
SOLNout.jn_1=jn_1;
SOLNout.jn_2=jn_2;
SOLNout.jn_3=jn_3;
SOLNout.jn_4=jn_4;

SOLNout.jp_0=jp_0;
SOLNout.Vt =Vt;


SOLNout.eta_n_0=eta_n_0;
SOLNout.eta_p_0=eta_p_0;
SOLNout.Vr_n_0=Vr_n_0;
SOLNout.Vr_p_0=Vr_p_0;

SOLNout.T=T;


%% DAE Setup
% Here the first three equations solve for the SOC's of three particles.
% 
% $$\frac{dc_{p,i}}{dt}=D_{s,p,i}d_{r,p,i}^2\ast A_{sys}\ast c_{p,i}+\frac{1}{d_{r,p,i}}\ast 
% B_{sys}\ast j_{p,i}$$
% 
% Introducing dce = ce-ce_init variable in order to remove the singularity
% dce_dot = -M_a^(-1)*K_a*dce-M_a^(-1)*K_a*ce_init+M_a^(-1)*F_a*I(t)
%
% The last equations are not a differential equation. It is a linear equation 
% which is our constraint.
% 
% $$$$\phi_{s,1} -\phi_{s,1} =0$$$$
% 
% The DAE solver solves for the last state $$j_{p,0}$$ such that the linear 
% equation is satisfied. 
% 
% The M matrix defined in the parent m code defines the mass matrix $$M\left(t,y\right)y^{'} 
% =f\left(t,y\right)$$.
% 
% In our case all diagonal elements except the last one are 1. This says 
% that they are all differential equations $$y^{'} =f\left(t,y\right)$$.
% 
% The last element is 0. This says it it is an algebraic (linear) equation 
% $$f\left(t,y\right)=0$$.


dxdt = [(CC.Ds_n/(CC.drn_0)^2*CC.Asys*x_0+1/CC.drn_0*CC.Bsys*(jn_0)/CC.cs_max_n);...% negative current here for negative electrode
        (CC.Ds_n/(CC.drn_1)^2*CC.Asys*x_1+1/CC.drn_1*CC.Bsys*(jn_1)/CC.cs_max_n);...% negative current here for negative electrode
        (CC.Ds_n/(CC.drn_2)^2*CC.Asys*x_2+1/CC.drn_2*CC.Bsys*(jn_2)/CC.cs_max_n);...% negative current here for negative electrode
        (CC.Ds_n/(CC.drn_3)^2*CC.Asys*x_3+1/CC.drn_3*CC.Bsys*(jn_3)/CC.cs_max_n);...% negative current here for negative electrode
        (CC.Ds_n/(CC.drn_4)^2*CC.Asys*x_4+1/CC.drn_4*CC.Bsys*(jn_4)/CC.cs_max_n);...% negative current here for negative electrode
        (CC.Ds_p/(CC.drp_0)^2*CC.Asys*y_0+1/CC.drp_0*CC.Bsys*(jp_0)/CC.cs_max_p);...% positive current here for negative electrode
        (-CC.M_a_inv*CC.K_a*dce-CC.M_a_inv*CC.K_a*CC.ce_init*ones(CC.n_nodes,1)+CC.M_a_inv*CC.F_a*Iapplied);...% electrolyte
        (SOLNout.Un_0+eta_n_0+Vr_n_0)-(SOLNout.Un_1+eta_n_1+Vr_n_1);... % voltage balance on anode
        (SOLNout.Un_0+eta_n_0+Vr_n_0)-(SOLNout.Un_2+eta_n_2+Vr_n_2);... % voltage balance on anode
        (SOLNout.Un_0+eta_n_0+Vr_n_0)-(SOLNout.Un_3+eta_n_3+Vr_n_3);... % voltage balance on anode
        (SOLNout.Un_0+eta_n_0+Vr_n_0)-(SOLNout.Un_4+eta_n_4+Vr_n_4);... % voltage balance on anode
        ((-CC.h*(T-CC.T_a)))*CC.Ac/CC.Vol/CC.rho/CC.Cp*2+... 
            ((-SOLNout.sumEnergy_n*CC.F*CC.del_n-SOLNout.sumEnergy_p*CC.F*CC.del_p-Iapplied*Vt))/CC.del_c/CC.rho/CC.Cp]; % energy balance 

end