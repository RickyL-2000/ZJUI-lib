%%% problem 1 %%%
tspan1 = [0:-0.0001:-2.12];
y0 = 1;
[t1,y1] = ode113(@(t,y) y^2+y*t+t^2, tspan1, y0);
k=flipud([t1,y1]);
tspan2 = [0:0.001: 0.858];
[t2,y2] = ode113(@(t,y) y^2+y*t+t^2, tspan2, y0);
j=[t2,y2];
j(1,:)=[];
n=[k;j];
result_table=table(n(:,1),n(:,2));
writetable(result_table, 'prb_1.csv')

%%%% problem 2 %%%
tspan3 = [0:-0.001:-25];
y0 = 1;
[t3,y3] = ode113(@(t,y) y^3+y*t^2+t*y^2+t^3, tspan3, y0);
kk=flipud([t3,y3]);
tspan4 = [0:0.0001: 0.439];
[t4,y4] = ode113(@(t,y) y^3+y*t^2+t*y^2+t^3, tspan4, y0);
jj=[t4,y4];
jj(1,:)=[];
nn=[kk;jj];
result_table=table(nn(:,1),nn(:,2));
writetable(result_table, 'prb_2.csv')