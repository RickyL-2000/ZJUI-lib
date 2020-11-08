%% geometry
A = [0 0];
B = [1 0];
C = [1 .5];
D = [0 0.5];

E = [0.3 0.2];
F = [0.7 0.2];
G = [0.7 0.3];
H = [0.3 0.3];

figure; hold on;
plot([A(1) B(1) C(1) D(1) A(1)],[A(2) B(2) C(2) D(2) A(2)],'k-','linewidth',2);
plot([E(1) F(1) G(1) H(1) E(1)],[E(2) F(2) G(2) H(2) E(2)],'b-','linewidth',2);
xlabel('x (m)'); ylabel('y (m)'); axis tight equal; grid on;

%% meshes 
xg = linspace(A(1), B(1), 101);
yg = linspace(A(2), D(2), 51);

Nx = length(xg); dx = (B(1) - A(1))/(Nx - 1);
Ny = length(yg); dy = (D(2) - A(2))/(Ny - 1);

Eid = [round((E(1) - A(1))/dx) + 1, round((E(2) - A(2))/dy) + 1];
Fid = [round((F(1) - A(1))/dx) + 1, round((F(2) - A(2))/dy) + 1];
Gid = [round((G(1) - A(1))/dx) + 1, round((G(2) - A(2))/dy) + 1];
Hid = [round((H(1) - A(1))/dx) + 1, round((H(2) - A(2))/dy) + 1];

%% assign boundary and initial values
V = zeros(Nx,Ny);
V(Eid(1):Fid(1),Eid(2):Hid(2)) = 1; % rectangular region EFGH
% V(1:Nx,1) = -1; % AB edge

% plot out the initial value
figure; imagesc(xg,yg,V'); axis xy tight equal; colorbar;
xlabel('x (m)'); ylabel('y (m)');

%% Solve V using the iterative solution