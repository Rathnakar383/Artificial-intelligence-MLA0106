% --- Facts: Graph representation ---
% edge(Start, End, Cost)
edge(a, b, 4).
edge(a, c, 3).
edge(b, d, 5).
edge(b, e, 12).
edge(c, f, 7).
edge(c, g, 8).
edge(d, h, 6).
edge(e, h, 2).
edge(f, h, 1).
edge(g, h, 4).

% heuristic(Node, Value)
heuristic(a, 14).
heuristic(b, 12).
heuristic(c, 11).
heuristic(d, 6).
heuristic(e, 4).
heuristic(f, 11).
heuristic(g, 9).
heuristic(h, 0).  % Goal node

% --- Best First Search ---
best_first_search(Start, Goal, Path) :-
    bfs([[Start]], Goal, Path).

% BFS helper
bfs([[Goal|Rest]|_], Goal, Path) :-
    reverse([Goal|Rest], Path).

bfs([Path|Paths], Goal, FinalPath) :-
    extend(Path, NewPaths),
    append(Paths, NewPaths, TempPaths),
    sort_paths(TempPaths, SortedPaths),
    bfs(SortedPaths, Goal, FinalPath).

% Extend path with neighbors
extend([Node|Rest], NewPaths) :-
    findall([NewNode, Node|Rest],
            (edge(Node, NewNode, _), \+ member(NewNode, [Node|Rest])),
            NewPaths).

% Sort paths by heuristic value of the head node
sort_paths(Paths, SortedPaths) :-
    map_list_to_pairs(path_heuristic, Paths, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, SortedPaths).

% Get heuristic value for a path
path_heuristic([Node|_], H) :-
    heuristic(Node, H).

% --- Sample Query ---
% ?- best_first_search(a, h, Path).
% Expected Output: Path = [a, c, f, h] OR similar depending on graph.
