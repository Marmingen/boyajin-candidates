% Approximate positions of slow dippers around 
% Boyajin's star using data from Schmidt 2021
% ###############################################
% Marminge

%% Clump Data

star_labels_clump = ["2913753" "3037513" "3093586"... 
    "5334181" "5436225" "5482005" "7971210"...
    "8046240"];
x_clump = [210 579 313 574 262 623 580 394];
y_clump = [56 125 101 -31 16 -1 -182 -49];
z_clump = [39 -10 -55 98 -3 -33 130 36];

%% Non-Clump Data

star_labels_nclump = ["2958269" "8128754" "8233191"...
    "8491743" "8935719" "8942941" "8987978"];

x_nclump = [2180 1507 7658 1025 1154 687 829];
y_nclump = [836 -418 -876 21 507 344 757];
z_nclump = [332 -56 -1142 -508 -1444 -863 -1530];

%% Boyajin's Star Data
x_boy = 415;
y_boy = 77;
z_boy = -137;

%% New Candidate Data

star_labels_new = ["1933490" "2354429" "2506699"...
    "2560138" "3781455" "4111136" "4754014"...
    "4989822" "5190574" "6757658" "6804071"...
    "6814519" "7255468" "7575062" "7642696"];

x_new = [183 228 105 461 394 314 46 144 699 -226 ...
    -398 -119 -265 68 72];
y_new = [650 758 321 668 711 1527 341 143 46 749 ...
    1902 669 651 99 25];
z_new = [-151 299 237 650 -563 -314 196 278 352 ...
    -171 -225 -45 349 278 137];

%% Plotting

clump = plot3(x_clump, y_clump, z_clump, '.');
grid on
set(clump, 'MarkerSize', 20)
set(clump, 'Color','black')
hold on

boy = plot3(x_boy, y_boy, z_boy, 'pentagram');
set(boy, 'MarkerSize', 10)
set(boy, 'Color', 'red')

nclump = plot3(x_nclump, y_nclump, z_nclump, 'o');
set(nclump, 'MarkerSize', 5)
set(nclump, 'Color', 'black')

new_stars = plot3(x_new, y_new, z_new, '.');
set(new_stars, 'MarkerSize', 20)
set(new_stars, 'Color','blue')

sun = plot3(0,0,0,'.yellow');
set(sun, 'MarkerSize', 20)
set(sun, 'Color','yellow')
hold off
