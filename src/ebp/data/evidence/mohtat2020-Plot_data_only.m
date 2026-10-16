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

%% Plot all the experimental data
clear
clc
close all

%%
load Cover10.mat

figure(1)
yyaxis left
plot(Qd_data,dVdQ_data,'linewidth',1.5)
xlabel('Q [Ah]','Interpreter','LaTex');ylabel('$dV/dQ$ [V/Ah]','Interpreter','LaTex')
set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
xlim([0 5]);
ylim([0 0.5]);
hold on


yyaxis right
plot(Qdf_data,derv_dis,'linewidth',1.5)
xlabel('Q [Ah]','Interpreter','LaTex');ylabel('$d^{2}\delta /dQ^{2}~[\mu m/Ah^2]$','Interpreter','LaTex')
set(gca,'fontsize',16)
xlim([0 5]);
% ylim([-100 60])
hold on

figure(2)
plot(Q_data,Vt_data,'linewidth',1.5)
set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
xlabel('Q [Ah]','Interpreter','LaTex');
ylabel('Voltage [V]','Interpreter','LaTex');

hold on


figure(3)
plot(Qf_data,Dis_data,'linewidth',1.5)
set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
xlabel('Q [Ah]','Interpreter','LaTex');
ylabel('Displacement [$\mu m$]','Interpreter','LaTex');

hold on

figure(4)
plot(Q_data,Temp_data,'linewidth',1.5)
set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
xlabel('Q [Ah]','Interpreter','LaTex');
ylabel('Temperature [C]','Interpreter','LaTex');

hold on

%%
load Cover5.mat

figure(1)
yyaxis left
plot(Qd_data,dVdQ_data,'linewidth',1.5)
xlabel('Q [Ah]','Interpreter','LaTex');ylabel('$dV/dQ$ [V/Ah]','Interpreter','LaTex')
set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
xlim([0 5]);
ylim([0 0.5]);
hold on


yyaxis right
plot(Qdf_data,derv_dis,'linewidth',1.5)
xlabel('Q [Ah]','Interpreter','LaTex');ylabel('$d^{2}\delta /dQ^{2}~[\mu m/Ah^2]$','Interpreter','LaTex')
set(gca,'fontsize',16)
xlim([0 5]);
% ylim([-100 60])
hold on

figure(2)
plot(Q_data,Vt_data,'linewidth',1.5)
set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
xlabel('Q [Ah]','Interpreter','LaTex');
ylabel('Voltage [V]','Interpreter','LaTex');

hold on


figure(3)
plot(Qf_data,Dis_data,'linewidth',1.5)
set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
xlabel('Q [Ah]','Interpreter','LaTex');
ylabel('Displacement [$\mu m$]','Interpreter','LaTex');

hold on

figure(4)
plot(Q_data,Temp_data,'linewidth',1.5)
set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
xlabel('Q [Ah]','Interpreter','LaTex');
ylabel('Temperature [C]','Interpreter','LaTex');

hold on

%%
load Cover2.mat

figure(1)
yyaxis left
plot(Qd_data,dVdQ_data,'linewidth',1.5)
xlabel('Q [Ah]','Interpreter','LaTex');ylabel('$dV/dQ$ [V/Ah]','Interpreter','LaTex')
set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
xlim([0 5]);
ylim([0 0.5]);
hold on


yyaxis right
plot(Qdf_data,derv_dis,'linewidth',1.5)
xlabel('Q [Ah]','Interpreter','LaTex');ylabel('$d^{2}\delta /dQ^{2}~[\mu m/Ah^2]$','Interpreter','LaTex')
set(gca,'fontsize',16)
xlim([0 5]);
% ylim([-100 60])
hold on

figure(2)
plot(Q_data,Vt_data,'linewidth',1.5)
set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
xlabel('Q [Ah]','Interpreter','LaTex');
ylabel('Voltage [V]','Interpreter','LaTex');

hold on


figure(3)
plot(Qf_data,Dis_data,'linewidth',1.5)
set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
xlabel('Q [Ah]','Interpreter','LaTex');
ylabel('Displacement [$\mu m$]','Interpreter','LaTex');

hold on

figure(4)
plot(Q_data,Temp_data,'linewidth',1.5)
set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
xlabel('Q [Ah]','Interpreter','LaTex');
ylabel('Temperature [C]','Interpreter','LaTex');

hold on

%%
load Cover1.mat

figure(1)
yyaxis left
plot(Qd_data,dVdQ_data,'linewidth',1.5)
xlabel('Q [Ah]','Interpreter','LaTex');ylabel('$dV/dQ$ [V/Ah]','Interpreter','LaTex')
set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
% h = legend('C/10','C/5','C/2','1C');
% set(h,'Interpreter','latex','Location','best')
xlim([0 5]);
ylim([0 0.5]);
hold on


yyaxis right
plot(Qdf_data,derv_dis,'linewidth',1.5)
xlabel('Q [Ah]','Interpreter','LaTex');ylabel('$d^{2}\delta /dQ^{2}~[\mu m/Ah^2]$','Interpreter','LaTex')
set(gca,'fontsize',16)
h = legend('C/10','C/5','C/2','1C','C/10','C/5','C/2','1C');
set(h,'Interpreter','latex','Location','best')
xlim([0 5]);
% ylim([-100 60])
hold on

figure(2)
plot(Q_data,Vt_data,'linewidth',1.5)
set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
xlabel('Q [Ah]','Interpreter','LaTex');
ylabel('Voltage [V]','Interpreter','LaTex');

hold on


figure(3)
plot(Qf_data,Dis_data,'linewidth',1.5)
set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
xlabel('Q [Ah]','Interpreter','LaTex');
ylabel('Displacement [$\mu m$]','Interpreter','LaTex');

hold on

figure(4)
plot(Q_data,Temp_data,'linewidth',1.5)
set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
xlabel('Q [Ah]','Interpreter','LaTex');
ylabel('Temperature [C]','Interpreter','LaTex');

hold on

%%
load 2C.mat

% figure(1)
% yyaxis left
% plot(Qd_data,dVdQ_data,'linewidth',1.5)
% xlabel('Q [Ah]','Interpreter','LaTex');ylabel('$dV/dQ$ [V/Ah]','Interpreter','LaTex')
% set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
% xlim([0 5]);
% ylim([0 0.5]);
% hold on
% 
% 
% yyaxis right
% plot(Qdf_data,derv_dis,'linewidth',1.5)
% xlabel('Q [Ah]','Interpreter','LaTex');ylabel('$d^{2}\delta /dQ^{2}~[\mu m/Ah^2]$','Interpreter','LaTex')
% set(gca,'fontsize',16)
% xlim([0 5]);
% % ylim([-100 60])
% hold on

figure(2)
plot(Q_data,Vt_data,'linewidth',1.5)
set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
xlabel('Q [Ah]','Interpreter','LaTex');
ylabel('Voltage [V]','Interpreter','LaTex');
h = legend('C/10','C/5','C/2','1C','2C');
set(h,'Interpreter','latex','Location','best')

hold on


figure(3)
plot(Qf_data,Dis_data,'linewidth',1.5)
set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
xlabel('Q [Ah]','Interpreter','LaTex');
ylabel('Displacement [$\mu m$]','Interpreter','LaTex');
h = legend('C/10','C/5','C/2','1C','2C');
set(h,'Interpreter','latex','Location','best')

hold on

figure(4)
plot(Q_data,Temp_data,'linewidth',1.5)
set(gca,'fontsize',16,'TickLabelInterpreter','LaTex')
xlabel('Q [Ah]','Interpreter','LaTex');
ylabel('Temperature [C]','Interpreter','LaTex');
h = legend('C/10','C/5','C/2','1C','2C');
set(h,'Interpreter','latex','Location','best')

hold on