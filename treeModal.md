|--- feature_0 <= 0.50
| |--- feature_1 <= 1.50
| | |--- feature_3 <= 0.50
| | | |--- feature_1 <= 0.50
| | | | |--- class: 0
| | | |--- feature_1 > 0.50
| | | | |--- feature_2 <= 0.50
| | | | | |--- class: 0
| | | | |--- feature_2 > 0.50
| | | | | |--- class: 0
| | |--- feature_3 > 0.50
| | | |--- feature_2 <= 0.50
| | | | |--- class: 0
| | | |--- feature_2 > 0.50
| | | | |--- feature_1 <= 0.50
| | | | | |--- class: 0
| | | | |--- feature_1 > 0.50
| | | | | |--- class: 0
| |--- feature_1 > 1.50
| | |--- class: 0
|--- feature_0 > 0.50
| |--- feature_1 <= 0.50
| | |--- feature_2 <= 0.50
| | | |--- feature_3 <= 0.50
| | | | |--- class: 0
| | | |--- feature_3 > 0.50
| | | | |--- class: 0
| | |--- feature_2 > 0.50
| | | |--- feature_3 <= 0.50
| | | | |--- class: 1
| | | |--- feature_3 > 0.50
| | | | |--- class: 1
| |--- feature_1 > 0.50
| | |--- feature_3 <= 0.50
| | | |--- feature_2 <= 0.50
| | | | |--- feature_1 <= 1.50
| | | | | |--- class: 1
| | | | |--- feature_1 > 1.50
| | | | | |--- class: 1
| | | |--- feature_2 > 0.50
| | | | |--- feature_1 <= 1.50
| | | | | |--- class: 1
| | | | |--- feature_1 > 1.50
| | | | | |--- class: 1
| | |--- feature_3 > 0.50
| | | |--- feature_1 <= 1.50
| | | | |--- feature_2 <= 0.50
| | | | | |--- class: 1
| | | | |--- feature_2 > 0.50
| | | | | |--- class: 1
| | | |--- feature_1 > 1.50
| | | | |--- feature_2 <= 0.50
| | | | | |--- class: 0
| | | | |--- feature_2 > 0.50
| | | | | |--- class: 1
