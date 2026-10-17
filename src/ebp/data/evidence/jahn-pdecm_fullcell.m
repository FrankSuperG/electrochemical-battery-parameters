%% Script Information
% Name           : hys_sim_fullcell
% Description    : Simulates anode and cathode half cell and combines these
%                  to the full cell voltage
% Version        : 1
% Original author: Leonard Jahn, EES @ University of Bayreuth
% Original date  : 13.11.2023

function [T, SOC_cell, SOC_loc, U_cell] = pdecm_fullcell(rc_param,...
    ROCV_res, r_dis, tI, I, QGes, SOC0, n_particle, dt)
    
    Q_oh = 0.02;
    
    % load opt parameter
    anode = load('.\Data\20230221_graphite_opt_parameter_man.mat');
    cathode = load('.\Data\20230221_lfp_opt_parameter_man.mat');

    n2p = 0.7/0.5;
    if isscalar(SOC0)
        SOC0_cathode = (SOC0*QGes+QGes*Q_oh)/(QGes+(QGes*Q_oh));
        SOC0_anode = SOC0/n2p;
    else
        SOC0_anode = SOC0(:,1);
        SOC0_cathode = SOC0(:,2);
    end
    
    %anode simulation
    theta_anode(1) = -1;
    theta_anode(2) = anode.optP(1)/(cathode.optP(1)...
        +anode.optP(1))*ROCV_res(1);
    theta_anode(3) = anode.optP(2)*ROCV_res(2);
    theta_anode(4) = anode.optP(3); %optional
    
    rc_param_anode = [rc_param(:,1)/n2p rc_param(:,2:end)];
    %energy curve
    ocpn_anode_param = load('.\Data\param_ocpn_graphite.mat');
    ocpn_anode = @(DOL)ocp_function_anode(DOL, ocpn_anode_param);
    
    [T_anode, U_cell_anode, ~, ~, ~, ~, SOC_loc_anode, ~]...
        = pdecm_lr_solver(ocpn_anode, rc_param_anode,...
        theta_anode, r_dis, tI, I, QGes*n2p, SOC0_anode, n_particle, dt);

    %cathode simulation
    theta_cathode(1) = 0;
    theta_cathode(2) = cathode.optP(1)/(cathode.optP(1)...
        +anode.optP(1))*ROCV_res(1);
    theta_cathode(3) = cathode.optP(2)*ROCV_res(2);
    theta_cathode(4) = cathode.optP(3)*1.3; %optional
    
    if theta_cathode(3)>1 || theta_anode(3)>1
        disp('Error: ROCVdelta larger than 1')
        return 
    end
    %energy curve
    ocpn_cathode_param = load('.\Data\param_ocpn_lfp.mat');
    ocpn_cathode = @(DOL)ocp_function_cathode(DOL, ocpn_cathode_param);

    [~, U_cell_cathode, ~, SOC_cell_cathode, ~, ~, SOC_loc_cathode, ~]...
        = pdecm_lr_solver(ocpn_cathode, rc_param, theta_cathode,...
        r_dis, tI, I, QGes+(QGes*Q_oh), SOC0_cathode, n_particle, dt);

    %% full cell
    T = T_anode;
    U_cell = U_cell_cathode+U_cell_anode;
    SOC_cell = SOC_cell_cathode*(1+Q_oh)-Q_oh;
    SOC_loc = [SOC_loc_anode(:,end) SOC_loc_cathode(:,end)];
end

%functions for the interpolation between grid points of the open circuit
%potentials of graphite and lfp
function ocpn_anode = ocp_function_anode(DOL, param)
    pot = param.pot;
    pot_dol = param.pot_dol;
    ocpn_anode = interp1(pot_dol, -pot, DOL, 'spline', -pot(1));
    ocpn_anode(DOL>1) = 0;
end

function ocpn_cathode = ocp_function_cathode(DOL, param)
    pot = param.pot;
    pot_dol = param.pot_dol;
    ocpn_cathode = interp1(pot_dol, pot, DOL, 'pchip', 'extrap');
end
