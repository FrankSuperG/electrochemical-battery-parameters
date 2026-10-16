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
% % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % %

% The MATLAB’s Signal Processing Toolbox plug-in is also required in order 
% to plot figures 5, 6, and 7. You can set the plot_differential to 0 
% to turn off the plotting of the aformentined figures.


%% MPM (Using ode15s DAE solver)
clear
clc
close all
global Vt
Vt = 3.2;

plot_differential = 1; % set to 0 to turn off


%% Input Current Magnitude
% Input cuurent can be set to any desired value, however, only the
% following inpute values will results in plots with data:
% Cover10 == -1/2
% Cover5  == -1
% Cover2  == -2.5
% Cover1  == -5
% 2C      == -10
CC.I = @(t) -5; % Amps

%% Parameter values

CC.cs_max_n =  28746;  % cs_max_n (mol/m^3)      Graphite
CC.cs_max_p =  35380;  % cs_max_p_0 (mol/m^3)    NMC
CC.Ds_n = 5.0e-15;     % Ds_n (m^2/s)      Graphite
CC.Ds_p = 8.0e-15;     % Ds_p (m^2/s)    NMC
CC.es_n = 0.610;       % es_n   Active material ration   Graphite
CC.es_p = 0.445;       % es_p   Active material ration   NMC
CC.k0_n = 1.1e-11;     % k0_n (mol/[m^2s(mol/m^3)]) reaction rate constant  Graphite
CC.k0_p = 5.0e-11;     % k0_p (mol/[m^2s(mol/m^3)]) reaction rate constant  NMC
CC.kt_n = 0;           % kt (omega.m^2) film resistence  Graphite
CC.kt_p = 0;           % kt (omega.m^2) film resistence  NMC

CC.ce_init = 1000;     % ce_initial (mol/m^3)
CC.tf = 1.34;          % Thermodynamic factor (averaged) (1-t_plus)*(1+d ln(f)/ d ln(c_e)) with c_e = 1 mol/l
CC.t_plus = 0.38;      % transference number
CC.kappa = 1.3;        % (S/m) electrolyte ionic conductivity (averaged)
CC.D_e = 5.35e-10;     % (m^2/s) Electrolyte Diffusion Coefficient
CC.brugg = 1.5;        % Bruggman exponent

CC.epsilon_e_n = 0.30;   % Volume fraction in electrolyte (porosity) for neg. electrode
CC.epsilon_e_s = 0.40;   % Volume fraction in electrolyte (porosity) for separator
CC.epsilon_e_p = 0.30;   % Volume fraction in electrolyte (porosity) for pos. electrode

CC.E = 10;  % Material modulus
CC.v = 0.3; % Poisson ratio


CC.F = 96485;       % Faraday Constant (C/mol)
CC.R = 8.3145;      % Gas constant
CC.T = 273.15+25;   % Temperature

%% Potential Functions

CC.Un_0 = @(x) 0.063+0.8*exp(-75*(x+0.007))+...
                    -0.0120*tanh((x-0.127)/0.016)+...
                    -0.0118*tanh((x-0.155)/0.016)+...
                    -0.0035*tanh((x-0.220)/0.020)+...
                    -0.0095*tanh((x-0.190)/0.013)+...
                    -0.0145*tanh((x-0.490)/0.020)+...
                    -0.0800*tanh((x-1.030)/0.055); % Graphite
                
                
CC.Up_0 = @(y) 4.3452-1.6518*(y)+1.6225*(y).^2-2.0843*(y).^3+3.5146*y.^4-2.2166*y.^5-0.5623e-4*exp(109.451*(y)-100.006); % NMC

%% Electrode Thickness $\delta$(m)

CC.del_n = 62e-6; % m Graphite
CC.del_s = 12e-6; % m Separator
CC.del_p = 67e-6; % m NMC

CC.del_c = CC.del_n+CC.del_s+CC.del_p; %cell length m

%% Particle radius R (m)
     
CC.Rn_0 = 1.50e-6;
CC.Rn_1 = 2.00e-6;
CC.Rn_2 = 2.50e-6;
CC.Rn_3 = 3.00e-6;
CC.Rn_4 = 3.70e-6; %Graphite


CC.Rp_0 = 3.50e-6; %NMC 

%% Fraction of active material for each particle

CC.zeta_n_0 = 0.10;
CC.zeta_n_1 = 0.22;
CC.zeta_n_2 = 0.30;
CC.zeta_n_3 = 0.25;
CC.zeta_n_4 = 0.13;

CC.zeta_p_0 = 1.00;

%% Active surface area per electrode unit volume (m^-1)
% $$a_{s,n}=\frac{3\zeta _{n}}{R_{n}}$$

CC.as_n_0 = 3*CC.es_n*CC.zeta_n_0/CC.Rn_0;
CC.as_n_1 = 3*CC.es_n*CC.zeta_n_1/CC.Rn_1;
CC.as_n_2 = 3*CC.es_n*CC.zeta_n_2/CC.Rn_2;
CC.as_n_3 = 3*CC.es_n*CC.zeta_n_3/CC.Rn_3;
CC.as_n_4 = 3*CC.es_n*CC.zeta_n_4/CC.Rn_4;

CC.as_p_0 = 3*CC.es_p*CC.zeta_p_0/CC.Rp_0;

%% Initial Particle SOC's

SOC_0 = 0.00;
y0_percent_p  = .8907;
y100_percent_p = .0335;
x0_percent_n = .0017;
x100_percent_n = .8332;

%% Area $\left(m^2 \right)$
% Adjust this value for changing the battery capacity

CC.A = 0.2050; % m^2 

%% Thermal properties
CC.th = 4.0; % cell thickness (mm)
CC.l = 132; % cell length (mm)
CC.w = 90; % cell width (mm)
CC.p_n_cell = 30; % number of parallel stacked cells in the pouch cell

CC.Ac = 2*(CC.th*(CC.l+CC.w)+CC.l*CC.w)*1e-6; % cell side area (m^2)

CC.Vol = CC.th*CC.l*CC.w*1e-9;     %cell volume (m^3)
CC.rho = 3100;              %cell lumped density (kg/m^3)
CC.Cp = 1100;               %cell lumped specific heat capacity (J/kg/K)
CC.h = 5;                   %The lumped convective coefficient (W/m^2/K)

CC.thermal_expan = 1.48; % (mu m/K)

Xrp = [-800.188839890836;779.024429422884;-284.191426454976;46.0455713779492;-2.79626039841497];
dUdTp =@(X,y) X(1)+X(2)*(y)+X(3)*(y).^2+X(4)*(y).^3+X(5)*(y).^4;        % NMC
CC.dUdTp_0 = @(y) dUdTp(Xrp,CC.Up_0(y))*1e-3;                           %partial molar entropy V/K NMC

Xrn = [-1571.24256569006,5251.50745693907,-6409.17384627168,3312.09434820777,-516.484224726484,-90.5107230814980,16.5771116346320];
dUdTn =@(X,y) X(7)+X(6)*(y)+X(5)*(y).^2+X(4)*(y).^3+X(3)*(y).^4+X(2)*(y).^5+X(1)*(y).^6; % graphite

CC.dUdTn_0 = @(x) dUdTn(Xrn,x)/CC.F; %partial molar entropy V/K graphite
CC.T_a = 24.8; %ambient temp. C

%% Spatial discretization slices

CC.nr = 10; % Number of elements in the solid particle
CC.nn = 10;  %number of elements in the negative electrode
CC.ns = 5;  %number of elements in the separator
CC.np = 10; %number of elements in the positive electrode

CC.drn_0 = CC.Rn_0/CC.nr;
CC.drn_1 = CC.Rn_1/CC.nr;
CC.drn_2 = CC.Rn_2/CC.nr;
CC.drn_3 = CC.Rn_3/CC.nr;
CC.drn_4 = CC.Rn_4/CC.nr;

CC.drp_0 = CC.Rp_0/CC.nr;


CC.dx_n = CC.del_n/CC.nn;
CC.dx_s = CC.del_s/CC.ns;
CC.dx_p = CC.del_p/CC.np;

%% Initial Concentration

x_init_p = (-SOC_0*(-y100_percent_p+y0_percent_p)+y0_percent_p); 
x_init_n = (SOC_0*(x100_percent_n-x0_percent_n)+x0_percent_n); 

%% A AND B Matrices
% Defining A and B matrices with 2nd order approximation for Boundary Conditions 

Asys = zeros(CC.nr+1,CC.nr+1);
Asys(1,1) = -6;
Asys(1,2) = 6;
for i = 1:CC.nr-1
    Asys(i+1,i) = (i-1)/i;
    Asys(i+1,i+1) = -2;
    Asys(i+1,i+2) = (i+1)/i;
end
Asys(CC.nr+1,CC.nr) = 2;
Asys(CC.nr+1,CC.nr+1) = -2;

Bsys = zeros(CC.nr+1,1);
Bsys(CC.nr+1,1) = -2*(CC.nr+1)/CC.nr;

% State_space electrolyte (FEM with Quadratic basis functions) M_a*ce_dot+K_a*ce = F_a*I(t)

% Elemental mass matrix
M_e = 1/15.*[4 -2 1;-2 16 2;1 2 4];
% Elemental diffusivity matrix
K_e = 1/6.*[7 -8 1;-8 16 -8;1 -8 7];
% Elemental flux vector
F_e = 1/3.*[1;4;1];

% Assembly 
CC.n_el = CC.nn+CC.ns+CC.np; %total number of elements
CC.n_nodes = 2*CC.n_el+1; %total number of nodes 


M_a = zeros(CC.n_nodes,CC.n_nodes); 
K_a = zeros(CC.n_nodes,CC.n_nodes);
F_a = zeros(CC.n_nodes,1);

for i = 1:CC.n_el
    if i <= CC.nn
        M_a(2*(i-1)+1:2*i+1,2*(i-1)+1:2*i+1) = M_a(2*(i-1)+1:2*i+1,2*(i-1)+1:2*i+1)+CC.dx_n*CC.epsilon_e_n/2.*M_e;
        K_a(2*(i-1)+1:2*i+1,2*(i-1)+1:2*i+1) = K_a(2*(i-1)+1:2*i+1,2*(i-1)+1:2*i+1)+2*CC.D_e*CC.epsilon_e_n^(CC.brugg)/CC.dx_n.*K_e;
        F_a(2*(i-1)+1:2*i+1,1) = F_a(2*(i-1)+1:2*i+1,1)+(1-CC.t_plus)/(CC.F*CC.del_n)*CC.dx_n/2.*F_e;
    elseif i > CC.nn && i <= CC.ns+CC.nn
        M_a(2*(i-1)+1:2*i+1,2*(i-1)+1:2*i+1) = M_a(2*(i-1)+1:2*i+1,2*(i-1)+1:2*i+1)+CC.dx_s*CC.epsilon_e_s/2.*M_e;
        K_a(2*(i-1)+1:2*i+1,2*(i-1)+1:2*i+1) = K_a(2*(i-1)+1:2*i+1,2*(i-1)+1:2*i+1)+2*CC.D_e*CC.epsilon_e_s^(CC.brugg)/CC.dx_s.*K_e;
%         F_a(2*(i-1)+1:2*i+1,1) = zeros(3,1); 
    else
        M_a(2*(i-1)+1:2*i+1,2*(i-1)+1:2*i+1) = M_a(2*(i-1)+1:2*i+1,2*(i-1)+1:2*i+1)+CC.dx_p*CC.epsilon_e_p/2.*M_e;
        K_a(2*(i-1)+1:2*i+1,2*(i-1)+1:2*i+1) = K_a(2*(i-1)+1:2*i+1,2*(i-1)+1:2*i+1)+2*CC.D_e*CC.epsilon_e_p^(CC.brugg)/CC.dx_p.*K_e;
        F_a(2*(i-1)+1:2*i+1,1) = F_a(2*(i-1)+1:2*i+1,1)-(1-CC.t_plus)/(CC.F*CC.del_p)*CC.dx_p/2.*F_e;
    end
end

%% USE ODE15S to solve DAE, ODE systems.

CC.Asys = Asys;
CC.Bsys = Bsys;
CC.M_a_inv = M_a^(-1);
CC.K_a = K_a;
CC.F_a = F_a;

%% Defining Initial States

X_i = [x_init_n*ones((CC.nr+1)*5,1); x_init_p*ones(CC.nr+1,1);zeros(CC.n_nodes,1);zeros(4,1);CC.T_a]; 

%% Time span

tspan = [0 3600*50/abs(CC.I(1)/CC.A)];


%% Mass Matrix

M = diag([ones(1,(CC.nr+1)*6+CC.n_nodes),0,0,0,0,1]);

%% ODE15s setup and solutions

options = odeset('Mass',M,'RelTol',1e-6,'AbsTol',1e-7,'Events',@(t,X)DAEEventsFcn(t,X,CC),'MaxStep',0.5);

[t,X,te,ye,ie] = ode15s(@(t,X) Battery_MPM_Electrolyte_DAE(t,X,CC),tspan,X_i,options);

[dxdy,SolnCC] = Battery_MPM_Electrolyte_DAE(t(1),X(1,:).',CC);

for ii=2:length(t)
    [dxdy,SolnCC(ii)]=Battery_MPM_Electrolyte_DAE(t(ii),X(ii,:).',CC);
end

%% Mechanical response
% en(x) expansion function of the graphite 
% ep(y) expansion function of the NMC
dr_norm = 1/CC.nr;
r_norm = 0:dr_norm:1;

int_1 = r_norm.^2;

Mn_0 = arrayfun(@en, X(:,1:CC.nr+1))*diag(int_1);
Mn_1 = arrayfun(@en, X(:,1*(CC.nr+1)+(1:(CC.nr+1))))*diag(int_1);
Mn_2 = arrayfun(@en, X(:,2*(CC.nr+1)+(1:(CC.nr+1))))*diag(int_1);
Mn_3 = arrayfun(@en, X(:,3*(CC.nr+1)+(1:(CC.nr+1))))*diag(int_1);
Mn_4 = arrayfun(@en, X(:,4*(CC.nr+1)+(1:(CC.nr+1))))*diag(int_1);
Mp_0 = arrayfun(@ep, X(:,5*(CC.nr+1)+(1:(CC.nr+1))))*diag(int_1);

un_0 = (CC.Rn_0).*( sum(Mn_0(:,2:end) + Mn_0(:,1:end-1) ,2)./2.*dr_norm );
un_1 = (CC.Rn_1).*( sum(Mn_1(:,2:end) + Mn_1(:,1:end-1) ,2)./2.*dr_norm );
un_2 = (CC.Rn_2).*( sum(Mn_2(:,2:end) + Mn_2(:,1:end-1) ,2)./2.*dr_norm );
un_3 = (CC.Rn_3).*( sum(Mn_3(:,2:end) + Mn_3(:,1:end-1) ,2)./2.*dr_norm );
un_4 = (CC.Rn_4).*( sum(Mn_4(:,2:end) + Mn_4(:,1:end-1) ,2)./2.*dr_norm );
up_0 = (CC.Rp_0).*( sum(Mp_0(:,2:end) + Mp_0(:,1:end-1) ,2)./2.*dr_norm );

% Electrode Expansion
de_t_n = (un_0*CC.as_n_0+un_1*CC.as_n_1+un_2*CC.as_n_2+un_3*CC.as_n_3+un_4*CC.as_n_4)*CC.del_n;
de_t_p = up_0*CC.as_p_0*CC.del_p;

% Thermal Expansion

det_t_therm = CC.thermal_expan*([SolnCC.T]'-CC.T_a);

% Total Expasion
de_t_t = CC.p_n_cell*1*(de_t_n+de_t_p)*1e6+det_t_therm;
de_t_t = (de_t_t - de_t_t(1));

%% Plotting
plot_data = 1;

if CC.I(1) == -0.5
    load Cover10
    temp = movmean(Temp_data,[200 20]);
    nred = 40;
elseif CC.I(1) == -1
    load Cover5
    temp = movmean(Temp_data,[100 5]);
    nred = 40;
elseif CC.I(1) == -2.5
    load Cover2
    temp = movmean(Temp_data,[40 0]);
    nred = 40;
elseif CC.I(1) == -5
    load Cover1
    temp = movmean(Temp_data,[20 0]);
    nred = 20;
elseif CC.I(1) == -10
    load 2C
    temp = movmean(Temp_data,[15 1]);
    nred = 10;
else
    derv_dis=[];Dis_data=[];dVdQ_data=[];Q_data=[];Qd_data=[];Qdf_data=[];
    Qf_data=[];Temp_data=[];delta_Dis_data=[];plot_data = 0;
    warning('No equivalent dataset was found for the selected input current')
end

Q = [0;-(cumsum(CC.I(1)*(t(2:end)-t(1:end-1)))*1/3600)];
Vt = [SolnCC.Vt];
T = [SolnCC.T];

if plot_data == 1
    
    time_data = linspace(0,t(end),length(Temp_data));
    time_data_dis = linspace(0,t(end),length(Dis_data));
    delta_Dis_data = Dis_data-Dis_data(1);


    figure(1)
    plot(t,Vt,'-k',time_data(1:nred:end),Vt_data(1:nred:end),'s','MarkerSize',8,'color','k','LineWidth',1.5)
    set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
    xlabel('t [s]','Interpreter','LaTex');
    ylabel('$V_t$ [V]','Interpreter','LaTex');
%     ylim([2.8 4.4]);
    h = legend('Model','Data');
    set(h,'Interpreter','latex','Location','best')
    hold on

    interpV = interp1(t,Vt,time_data)';
    RMSE_V = sqrt((interpV-Vt_data)'*(interpV-Vt_data)/length(Vt_data)); 

    figure(2)
    plot(t,de_t_t,'-k',time_data_dis(1:nred:end),Dis_data(1:nred:end)-Dis_data(1),'s','MarkerSize',8,'color','k','LineWidth',1.5)
    set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
    xlabel('t [s]','Interpreter','LaTex');
    ylabel('$\Delta t_t~[\mu m]$','Interpreter','LaTex');
%     ylim([0 120]);
    h = legend('Model','Data');
    set(h,'Interpreter','latex','Location','best')
    hold on

    interpE = interp1(t,de_t_t,time_data_dis)';
    RMSE_E = sqrt((interpE-Dis_data+Dis_data(1))'*(interpE-Dis_data+Dis_data(1))/length(Dis_data)); 

    figure(3)
    plot(t,T-T(1),'-k',time_data(1:nred:end),temp(1:nred:end)-temp(1),'s','MarkerSize',10,'color','k','LineWidth',1.5)
    set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
    xlabel('t [s]','Interpreter','LaTex');
    ylabel('$\Delta T$ [C]','Interpreter','LaTex');
%     ylim([-1 7]);
    h = legend('Model','Data');
    set(h,'Interpreter','latex','Location','best')
    hold on

    interpT = interp1(t,T-T(1),time_data)';
    RMSE_T = sqrt((interpT-temp+temp(1))'*(interpT-temp+temp(1))/length(temp)); 

else

    figure(1)
    plot(t,Vt,'-k','LineWidth',1.5)
    set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
    xlabel('t [s]','Interpreter','LaTex');
    ylabel('$V_t$ [V]','Interpreter','LaTex');
    h = legend('Model');
    set(h,'Interpreter','latex','Location','best')
    hold on

    figure(2)
    plot(t,de_t_t,'-k','LineWidth',1.5)
    set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
    xlabel('t [s]','Interpreter','LaTex');
    ylabel('$\Delta t_t~[\mu m]$','Interpreter','LaTex');
    h = legend('Model');
    set(h,'Interpreter','latex','Location','best')
    hold on

    figure(3)
    plot(t,T-T(1),'-k','LineWidth',1.5)
    set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
    xlabel('t [s]','Interpreter','LaTex');
    ylabel('$\Delta T$ [C]','Interpreter','LaTex');
    h = legend('Model');
    set(h,'Interpreter','latex','Location','best')
    hold on

end

figure(4)
plot(Q,X(:,CC.nr+1),Q,X(:,2*(CC.nr+1)),Q,X(:,3*(CC.nr+1)),Q,X(:,4*(CC.nr+1)),Q,X(:,5*(CC.nr+1)),'LineWidth',1.5)
set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
xlabel('Q [Ah]','Interpreter','LaTex');
ylabel('Lithiation state $x$ [-]','Interpreter','LaTex');
h = legend('$R_{p,1}$','$R_{p,2}$','$R_{p,3}$','$R_{p,4}$','$R_{p,5}$');
set(h,'Interpreter','latex','Location','best')


if plot_differential == 1

    dV = Vt(2:end)-Vt(1:end-1);
    dQ = Q(2:end)-Q(1:end-1);
    Qd = Q(1:end-1)+(Q(2:end)-Q(1:end-1))./2;

    dVdQ = dV./dQ';              

    N = 3;                 % Order of polynomial fit
    F = 2500/abs(CC.I(1))*1.8+1;                % Window length
    [b,g] = sgolay(N,F);   % Calculate S-G coefficients


    HalfWinf  = ((F+1)/2) -1;

    yf = de_t_t;
    dxf = mean(dQ);


    for n = (F+1)/2:length(yf)-(F+1)/2
      % Zeroth derivative (smoothing only)
      SG0f(n) = dot(g(:,1),yf(n - HalfWinf:n + HalfWinf));


      % 1st differential
      SG1f(n) = dot(g(:,2),yf(n - HalfWinf:n + HalfWinf));

      % 2nd differential
      SG2f(n) = 2*dot(g(:,3)',yf(n - HalfWinf:n + HalfWinf))';
    end

    SG1f = SG1f./dxf;         % Turn differential into derivative
    SG2f = SG2f./(dxf.*dxf);    % and into 2nd derivative


    figure(5)
    subplot(2,1,1)
    plot(Q,Vt,Q_data,Vt_data,'--','linewidth',1.5)
    set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
    xlabel('Q [Ah]','Interpreter','LaTex');
    ylabel('$V_t$ [V]','Interpreter','LaTex');
    h = legend('Model','data');
    set(h,'Interpreter','latex','Location','best')

    subplot(2,1,2)
    plot(Qd,abs(dVdQ),Qd_data,dVdQ_data,'--','linewidth',1.5)
    set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
    xlabel('Q [Ah]','Interpreter','LaTex');
    ylabel('$dV/dQ$ [V/Ah]','Interpreter','LaTex');
    h = legend('Model','data');
    set(h,'Interpreter','latex','Location','best')
    ylim([0 0.5])


    figure(6)
    subplot(2,1,1)
    plot(Q,de_t_t,Qf_data,delta_Dis_data,'--','linewidth',1.5)
    set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
    xlabel('Q [Ah]','Interpreter','LaTex');
    ylabel('$\Delta t_t~[\mu m]$','Interpreter','LaTex');
    xlim([0 5])
    h = legend('Model','data');
    set(h,'Interpreter','latex','Location','best')

    subplot(2,1,2)
    plot(Q(HalfWinf+1:length(SG0f)),SG2f(HalfWinf+1:end),Qdf_data,derv_dis,'--','linewidth',1.5)
    set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
    xlabel('Q [Ah]','Interpreter','LaTex')
    ylabel('$d^{2}\delta /dQ^{2}~[\mu m/Ah^2]$','Interpreter','LaTex')
    set(gca,'fontsize',16)
    xlim([0 5])
    ylim([-150 150])
    h = legend('Model','data');
    set(h,'Interpreter','latex','Location','best')


    figure(7)
    subplot(2,1,1)
    plot(Qd,abs(dVdQ),'k',Qd_data,dVdQ_data,'k--','linewidth',1.5)
    set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
    xlabel('Q [Ah]','Interpreter','LaTex');
    ylabel('$dV/dQ$ [V/Ah]','Interpreter','LaTex');
    h = legend('Model','data');
    set(h,'Interpreter','latex','Location','best')
    ylim([0 0.5])


    subplot(2,1,2)
    plot(Q(HalfWinf+1:length(SG0f)),SG2f(HalfWinf+1:end),'k',Qdf_data,derv_dis,'k--','linewidth',1.5)
    set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
    xlabel('Q [Ah]','Interpreter','LaTex')
    ylabel('$d^{2}\delta /dQ^{2}~[\mu m/Ah^2]$','Interpreter','LaTex')
    set(gca,'fontsize',16)
    xlim([0 5])
    ylim([-80 80])
    h = legend('Model','data');
    set(h,'Interpreter','latex','Location','best')

end

%% Expansion functions

function e = en(x)

if x < 0.12
    e = 2.4060/0.12*x;
elseif 0.12 <= x && x < 0.18
    e = -(2.4060-3.3568)/0.06*(x-0.12)+2.4060;
elseif 0.18 <= x && x < 0.24
    e = -(3.3568-4.3668)/0.06*(x-0.18)+3.3568;
elseif 0.24 <= x && x < 0.50
    e = -(4.3668-5.583)/0.26*(x-0.24)+4.3668;
elseif 0.50 <= x 
    e = -(5.583-13.0635)/0.50*(x-0.50)+5.583;
end
     e = e/100;
end

function e = ep(y)

e = -1.10/100*(1-y);

end



