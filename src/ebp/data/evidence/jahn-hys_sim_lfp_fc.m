%% Script Information
% Name           : hys_lfp_fc_sim
% Description    : Simulation of a full cell for the PD-ECM hysteresis model
% Version        : 1
% Original author: Leonard Jahn, EES @ University of Bayreuth
% Original date  : 13.11.2023

% Output:
% texp - time vector of the measurement
% Iexp - current vector of the measurement
% Qexp/SOCexp - amount of charge stored/state of charge from measurement
% Uexp - voltage vector of the measurement
%
% t - time vector if the simulation
% SOC - simulated state of charge of the full-cell
% U - simulated terminal voltage of the full-cell
% Uerr - deviation between simulation and measurement

%% Simulation of a full cell for the PD-ECM hysteresis model
clear all;
close all;
%chose the current profile that is supposed to be simulated
current_profile = 'hys_power'; %'full_cycle' / 'hys_power'

%% Load reference curve 
%folder with the stored reference data sets
pathname = 'Data\';

%reference measurement for capacity determination
pOCV = readtable([pathname '20230125_Hys_A123_01_25deg_pOCV.csv']);
[Q_max, idx_EOC] = max(pOCV.pQ);

%loading measurement data for the chosen current profile
if strcmp(current_profile, 'full_cycle')
    pOCV = readtable([pathname '20230125_Hys_A123_01_25deg_pOCV.csv']);
    Qexp = pOCV.pQ;
    SOCexp = Qexp./Q_max;
    Uexp = pOCV.pOCVAux;
    texp = pOCV.pt;
    Iexp = diff(Qexp*3600)./diff(texp);
    Iexp(end+1) = 0;
elseif strcmp(current_profile, 'hys_power')
    power_test_50 = readtable([pathname...
        '20230125_HysPowerTest_A123_01_25deg_SOC50.csv']);
    power_test_50 = power_test_50(1:275,:);
    power_test_100 = readtable([pathname...
        '20230125_HysPowerTest_A123_01_25deg_SOC100.csv']);
    Qexp_50 = power_test_50.Q_ch_power-power_test_50.Q_ch_power(1);
    Qexp_100 = power_test_100.Q_dc_power-power_test_100.Q_dc_power(1);
    
    SOCexp_50 = Qexp_50./Q_max;
    SOCexp_100 = Qexp_100./Q_max;
    
    Uexp_50 = power_test_50.U_ch_power;
    Uexp_100 = power_test_100.U_dc_power;
    Iexp_50 = power_test_50.I_ch_power;
    Iexp_100 = power_test_100.I_dc_power;
    texp_50 = power_test_50.t_ch_power;
    texp_100 = power_test_100.t_dc_power;
end

%% Define simulation parameter
%particle resistance distribution method
r_dis = "weibull_cap"; %"normal_cap" "weibull_cap"

%load RC parameter
data = readtable('Data\A123_parameter_posPulse.csv');

rc_param = table2array(data);
[~,idx_rcparam] = max(rc_param(:,1));
rc_param = rc_param(1:idx_rcparam,:);

R0_meas = min(rc_param(:,2));
%contact resistance and variation of contact resistance
ROCV_res = max(rc_param(:,2))*1.3;
rc_param(:,2) = 0;

ROCVdelta = 1; %variation of optimized ROCV_delta for half cells (max 1.25)
theta = [-1; ROCV_res; ROCVdelta];

%number of particles
n_particle = 50;

%cell capacity transformed into As
QGes = Q_max*3600; 

%% start simulation

if strcmp(current_profile, 'full_cycle')
    dt = 2; %time resolution
    SOC0 = 0; %starting SOC
    tI = texp; %input time vector for the current profile
    I = Iexp;  %input current profile
    
    %simulation
    [t, SOC_sim, ~, U_sim] = pdecm_fullcell(rc_param,...
        [ROCV_res ROCVdelta], r_dis, tI, I, QGes, SOC0, n_particle, dt);
    %error calculation
    Uint = interp1(t, U_sim, tI, 'pchip');
    Uerr = Uint-Uexp;
elseif strcmp(current_profile, 'hys_power')
    %define sim parameter
    dt = 0.5; %time resolution
    SOC0 = 0; %start SOC
    tI = texp_50; %input time vector for the current profile
    I = Iexp_50; %input current profile
    %simulation of path 1 of the path dependent rate capability test
    [t_50, SOC_50, ~, U_50] = pdecm_fullcell(rc_param,...
        [ROCV_res ROCVdelta], r_dis, tI, I, QGes, SOC0, n_particle, dt);
    %error calculation
    Uint_50 = interp1(t_50, U_50, tI, 'pchip');
    Uerr_50 = Uint_50(2:end)-Uexp_50(1:end-1);
    
    %define sim parameter
    tI = texp_100; %input time vector for the current profile
    I = Iexp_100; %input current profile
    %simulation of path 2 of the path dependent rate capability test
    [t_100, SOC_100, ~, U_100] = pdecm_fullcell(rc_param,...
        [ROCV_res ROCVdelta], r_dis, tI, I, QGes, SOC0, n_particle, dt);
    %error calculation
    Uint_100 = interp1(t_100, U_100, tI, 'pchip');
    Uerr_100 = Uint_100(2:end)-Uexp_100(1:end-1);
end
