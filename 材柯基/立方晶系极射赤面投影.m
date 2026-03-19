%% 立方晶系极射赤面投影（最终完整版：删除机制可视化）

clear; clc; close all;

%% ===== 输入 uvw =====
disp('输入示例: [1 1 1]')
uvw = input('[uvw] = ');

if length(uvw)~=3 || norm(uvw)==0
    error('uvw 输入错误')
end
uvw = uvw / norm(uvw);

%% ===== 输入 hkl =====
disp('逐个输入 (hkl)，如 [1 1 1]，回车结束')

hkl_list = [];

while true
    str = input('输入 (hkl)：','s');
    if isempty(str), break; end

    hkl = str2num(str); %#ok<ST2NM>

    if length(hkl)~=3 || norm(hkl)==0
        disp('输入错误')
        continue;
    end

    hkl_list = [hkl_list; hkl];
end

if isempty(hkl_list)
    error('至少输入一个 (hkl)')
end

%% ===== 对称 =====
ops = cubic_symmetry_ops();
n = size(hkl_list,1);
colors = lines(n);

%% ================= 2D =================
figure; hold on; axis equal; grid on;
theta = linspace(0,2*pi,200);
plot(cos(theta),sin(theta),'k','LineWidth',2);

legend_h = [];
legend_txt = {};

for i=1:n
    poles = get_equivalent_poles(hkl_list(i,:), ops, uvw);

    h = scatter(poles(:,1),poles(:,2),120,...
        'MarkerFaceColor',colors(i,:),...
        'MarkerEdgeColor','k');

    legend_h(end+1)=h;
    legend_txt{end+1}=sprintf('{%d%d%d}',hkl_list(i,:));
end

legend(legend_h,legend_txt,'Location','bestoutside');
title('2D 极射投影');
hold off;

%% ================= 3D =================
figure; hold on; axis equal; grid on; view(3);

R = sqrt(3)*1.05;

% 球
[X,Y,Z]=sphere(80);
surf(R*X,R*Y,R*Z,'FaceAlpha',0.08,'EdgeColor','none');

% 赤道面（加深）
[xp,yp]=meshgrid(linspace(-R,R,60));
surf(xp,yp,zeros(size(xp)),...
    'FaceColor',[0.7 0.85 1],...
    'FaceAlpha',0.4,...
    'EdgeColor','none');

% 赤道圆
theta = linspace(0,2*pi,200);
plot3(R*cos(theta),R*sin(theta),zeros(size(theta)),'k','LineWidth',2);

% 南北极
plot3(0,0,R,'ro','MarkerFaceColor','r'); text(0,0,R,'N');
plot3(0,0,-R,'bo','MarkerFaceColor','b'); text(0,0,-R,'S');

south = [0 0 -R];

legend_h3 = [];
legend_txt3 = {};

%% ===== 主循环 =====
for i=1:n

    hkl = hkl_list(i,:);

    % ===== 所有法向 =====
    normals = get_equivalent_normals(hkl, ops);

    % ===== 所有投影（未去重）=====
    poles_all = [];
    valid_normals = [];

    for j=1:size(normals,1)
        nrm = normals(j,:);
        if nrm(3)<=0, continue; end

        x = nrm(1)/(1+nrm(3));
        y = nrm(2)/(1+nrm(3));

        poles_all = [poles_all; x y];
        valid_normals = [valid_normals; nrm];
    end

    % ===== 唯一投影 =====
    poles_unique = unique(round(poles_all*1e6)/1e6,'rows');

    % legend
    h_leg = plot3(valid_normals(1,1),valid_normals(1,2),valid_normals(1,3),'o',...
        'MarkerFaceColor',colors(i,:));
    legend_h3(end+1)=h_leg;
    legend_txt3{end+1}=sprintf('{%d%d%d}',hkl);

    %% ===== 判定删除 or 保留 =====
    for j=1:size(valid_normals,1)

        P = valid_normals(j,:);
        x = poles_all(j,1);
        y = poles_all(j,2);

        key = round([x y]*1e6)/1e6;

        is_keep = ismember(key, poles_unique, 'rows');

        % ===== 球面点 =====
        if is_keep
            % 保留点 ●
            plot3(P(1),P(2),P(3),'o',...
                'MarkerFaceColor',colors(i,:),...
                'MarkerEdgeColor','k');
        else
            % 删除点 ×
            plot3(P(1),P(2),P(3),'x',...
                'Color',colors(i,:),...
                'LineWidth',2,...
                'MarkerSize',10);
        end

        % ===== 投影线 =====
        plot3([south(1) P(1)],...
              [south(2) P(2)],...
              [south(3) P(3)],...
              '--','Color',colors(i,:));

        % ===== 投影点（空心）=====
        plot3(x,y,0,'o',...
            'MarkerFaceColor','none',...
            'MarkerEdgeColor',colors(i,:),...
            'LineWidth',2,...
            'MarkerSize',10);
    end
end

legend(legend_h3,legend_txt3,'Location','bestoutside');
title('3D 极射投影（删除机制可视化）');

axis([-R R -R R -R R]);

hold off;

%% ===== 函数 =====

function ops = cubic_symmetry_ops()
    ops = {};
    idx = 1;
    vals = [-1 0 1];

    for a1=vals, for a2=vals, for a3=vals
    for b1=vals, for b2=vals, for b3=vals
    for c1=vals, for c2=vals, for c3=vals

        M = [a1 a2 a3; b1 b2 b3; c1 c2 c3];

        if abs(abs(det(M))-1)>1e-10, continue; end
        if norm(M*M'-eye(3),'fro')>1e-10, continue; end

        ops{idx}=M; idx=idx+1;

    end,end,end,end,end,end,end,end,end
end

function poles = get_equivalent_poles(hkl, ops, uvw)

    normals = get_equivalent_normals(hkl, ops);

    z=[0;0;1];
    if norm(uvw-z)<1e-10
        R=eye(3);
    else
        axis=cross(uvw,z); axis=axis/norm(axis);
        angle=acos(dot(uvw,z));
        K=[0 -axis(3) axis(2);
           axis(3) 0 -axis(1);
          -axis(2) axis(1) 0];
        R=eye(3)+sin(angle)*K+(1-cos(angle))*K^2;
    end

    poles=[];
    for i=1:size(normals,1)
        nr=R*normals(i,:)';
        nr=nr/norm(nr);
        if nr(3)<=0, continue; end
        poles=[poles; nr(1)/(1+nr(3)) nr(2)/(1+nr(3))];
    end

    poles=unique(round(poles*1e6)/1e6,'rows');
end

function normals = get_equivalent_normals(hkl, ops)

    hkl=hkl(:);
    normals=[];

    for i=1:length(ops)
        n=ops{i}*hkl;
        n=n/norm(n);
        if n(3)<0, n=-n; end
        normals=[normals; n'];
    end

    normals=unique(round(normals*1e6)/1e6,'rows');
end
