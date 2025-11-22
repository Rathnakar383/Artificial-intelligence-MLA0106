% Facts: diet recommendations based on diseases
diet(diabetes, 'Low sugar diet with high fiber foods, avoid sweets and sugary drinks.').
diet(hypertension, 'Low salt diet, eat more fruits and vegetables, avoid processed foods.').
diet(obesity, 'Low calorie diet, high in protein and fiber, avoid junk food.').
diet(anemia, 'Iron-rich diet, include spinach, red meat, and legumes.').
diet(heart_disease, 'Low fat diet, avoid fried foods, eat more fish and whole grains.').
diet(kidney_disease, 'Low protein and low salt diet, avoid red meat and processed foods.').
diet(gastritis, 'Soft, non-spicy food, avoid alcohol and caffeine.').
diet(liver_disease, 'Low fat diet, avoid alcohol, eat plenty of fruits and vegetables.').

% Rule to suggest diet based on disease
suggest_diet(Disease) :-
    diet(Disease, DietPlan),
    write('Recommended Diet for '), write(Disease), write(': '), nl,
    write(DietPlan).

