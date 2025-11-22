% Planets Database
% Format: planet(Name, DistanceFromSun_km, Diameter_km, Moons).

planet(mercury, 57900000, 4879, 0).
planet(venus, 108200000, 12104, 0).
planet(earth, 149600000, 12742, 1).
planet(mars, 227900000, 6779, 2).
planet(jupiter, 778500000, 139820, 79).
planet(saturn, 1434000000, 116460, 83).
planet(uranus, 2871000000, 50724, 27).
planet(neptune, 4495000000, 49244, 14).

% Rules
has_moons(Name) :-
    planet(Name, _, _, Moons),
    Moons > 0.

closer_than(Name1, Name2) :-
    planet(Name1, Dist1, _, _),
    planet(Name2, Dist2, _, _),
    Dist1 < Dist2.

% Sample Queries:
% ?- planet(Name, _, _, _).                % List all planets
% ?- has_moons(Name).                      % Planets with moons
% ?- closer_than(earth, mars).             % Is Earth closer to the Sun than Mars?
% ?- planet(Name, _, _, Moons), Moons > 10.% Planets with more than 10 moons