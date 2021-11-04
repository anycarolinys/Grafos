#include "primMST.h"

Grafo :: Grafo(int V) {
    this->V = V;
    this->listaAdjacencias = new list<iPair>[V];
}

void Grafo :: addAresta(int vertice1, int vertice2, int peso) {
    listaAdjacencias[vertice1].push_back(make_pair(vertice2, peso));
    listaAdjacencias[vertice2].push_back(make_pair(vertice1, peso));
}

void Grafo :: primMST(int origem) {

    priority_queue<iPair, vector<iPair>, greater<iPair>> filaPrioridade;

    vector <int> preco(V, MAXIMO);

    vector<int> pai(V, -1);

    vector<bool> naMST(V, false);

    filaPrioridade.push(make_pair(0, origem));
    preco[origem] = 0;

    while (!filaPrioridade.empty()) {
        int v = filaPrioridade.top().second;
        filaPrioridade.pop();

        if (naMST[v] == true) {
            continue;
        }

        naMST[v] = true;

        list<pair<int, int>> :: iterator i;

        for (i = listaAdjacencias[v].begin(); i != listaAdjacencias[v].end(); i++) {
            
            int u = (*i).first;
            int peso = (*i).second;
            
            if (naMST[u] == false && preco[u] > peso) {
                preco[u] = peso;
                filaPrioridade.push(make_pair(preco[u], u));
                pai[u] = v;
            }
        }
    }

    for (int i = 1; i < V; ++i) {
        printf("Pai: %d - %d\n", pai[i], i);
        printf("Preco: %d - %d\n", preco[i], i);
    }
}