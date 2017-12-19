%%
data = importdata('SchoolKids.txt');
Kids = data.textdata(2:end,1);
Goals = data.textdata(2:end,7);


counts = zeros(3,1);
for i = 1:numel(Goals)
if strcmp(Goals{i}, 'Sports'); counts(1) = counts(1) + 1; end
if strcmp(Goals{i}, 'Grades'); counts(2) = counts(2) + 1; end
if strcmp(Goals{i}, 'Popular'); counts(3) = counts(3) + 1; end
end

counts_boys = zeros(3,1);
for i = 1:numel(Goals)
if strcmp(Kids{i}, 'boy') && strcmp(Goals{i}, 'Sports'); counts_boys(1) = counts_boys(1) + 1; end
if strcmp(Kids{i}, 'boy') && strcmp(Goals{i}, 'Grades'); counts_boys(2) = counts_boys(2) + 1; end
if strcmp(Kids{i}, 'boy') && strcmp(Goals{i}, 'Popular'); counts_boys(3) = counts_boys(3) + 1; end
end

counts_girls = zeros(3,1);
for i = 1:numel(Goals)
if strcmp(Kids{i}, 'girl') && strcmp(Goals{i}, 'Sports'); counts_girls(1) = counts_girls(1) + 1; end
if strcmp(Kids{i}, 'girl') && strcmp(Goals{i}, 'Grades'); counts_girls(2) = counts_girls(2) + 1; end
if strcmp(Kids{i}, 'girl') && strcmp(Goals{i}, 'Popular'); counts_girls(3) = counts_girls(3) + 1; end
end

%%
figure(1);
bar(counts);
set(gca, 'XTickLabel',  {'Sports','Grades','Popular'})
title('Number of school childen choosing each goal');

figure(2);
bar([counts_boys counts_girls]);
set(gca, 'XTickLabel',  {'Sports','Grades','Popular'})
legend({'boys', 'girls'})
title('Number of school childen choosing each goal');

%% pie chart
all_counts = [counts_boys; counts_girls];
pie(all_counts, {'boy-Sports', 'boy-Grades', 'boy-Popular','girl-Sports', 'girl-Grades', 'girl-Popular'});

%%
HeatMap([counts_boys counts_girls], 'ColumnLabels', {'boy', 'girl'}, 'RowLabels', {'Sports','Grades','Popular'}, 'colormap', bone);
